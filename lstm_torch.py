#!/usr/bin/env python
# encoding: utf-8
# @Author: franky
# @Date: 2022/4/14 下午1:05

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn as nn
from sklearn.preprocessing import MinMaxScaler


class LSTM(nn.Module):
    def __init__(self, input_size=1, hidden_layer_size=100, output_size=1):
        super().__init__()
        # 数据加载
        self.dataset_name = "flights"
        self.data_home = "/home/ybsun/github/seaborn-data"
        self.flight_data = sns.load_dataset(self.dataset_name, cache=True, data_home=self.data_home)
        self.test_data_size = 12
        self.scaler = MinMaxScaler(feature_range=(-1, 1))  # 数据归一化
        self.train_data_normalized = self.data_preprocess()

        # 模型参数
        self.hidden_layer_size = hidden_layer_size
        # 创建LSTM层和linear层，LSTM层提取特征，linear层用作最后的预测
        # LSTM算法接受三个输入：先前的隐藏状态，先前的单元状态和当前输入。
        self.lstm = nn.LSTM(input_size, hidden_layer_size)
        self.linear = nn.Linear(hidden_layer_size, output_size)
        # 初始化隐含状态及细胞状态C，hidden_cell变量包含先前的隐藏状态和单元状态
        self.hidden_cell = (torch.zeros(1, 1, self.hidden_layer_size),
                            torch.zeros(1, 1, self.hidden_layer_size))

        # 训练参数
        self.train_window = 12  # 设置训练输入的序列长度为12，类似于time_step = 12
        self.loss_function = nn.MSELoss()
        self.lr = 0.001
        self.epochs = 100

        # 模型验证参数
        self.fut_pred = 12

    def data_preprocess(self):
        """
        数据预处理
        :return:
        """
        all_data = self.flight_data['passengers'].values.astype(float)  # 将passengers列的数据类型改为float
        # 1.划分测试集和训练集
        train_data = all_data[:-self.test_data_size]  # 除了最后12个数据，其他全取
        test_data = all_data[-self.test_data_size:]  # 取最后12个数据
        # 2.数据归一化，减小误差，数据标准化只用于训练数据而不用于测试数据
        train_data_normalized = self.scaler.fit_transform(train_data.reshape(-1, 1))
        # 将数据集转换为tensor，因为PyTorch模型是使用tensor进行训练的，并将训练数据转换为输入序列和相应的标签
        # view相当于numpy中的resize,参数代表数组不同维的维度；
        # 参数为-1表示，这个维的维度由机器自行推断，如果没有-1，那么view中的所有参数就要和tensor中的元素总个数一致
        train_data_normalized = torch.FloatTensor(train_data_normalized).view(-1)

        return train_data_normalized

    # 定义create_inout_sequences函数，接收原始输入数据，并返回一个元组列表。
    def create_inout_sequences(self, input_data, tw):
        inout_seq = []
        L = len(input_data)
        for i in range(L - tw):
            train_seq = input_data[i:i + tw]
            train_label = input_data[i + tw:i + tw + 1]  # 预测time_step之后的第一个数值
            inout_seq.append((train_seq, train_label))  # inout_seq内的数据不断更新，但是总量只有tw+1个
        return inout_seq

    def forward(self, input_seq):
        lstm_out, self.hidden_cell = self.lstm(input_seq.view(len(input_seq), 1, -1), self.hidden_cell)
        # lstm的输出是当前时间步的隐藏状态ht和单元状态ct以及输出lstm_out
        # 按照lstm的格式修改input_seq的形状，作为linear层的输入
        predictions = self.linear(lstm_out.view(len(input_seq), -1))
        return predictions[-1]  # 返回predictions的最后一个元素

    def model_train(self, model):
        # model = LSTM()
        optimizer = torch.optim.Adam(model.parameters(), lr=self.lr)  # 建立优化器实例
        train_inout_seq = self.create_inout_sequences(self.data_preprocess(), self.train_window)
        for i in range(self.epochs):
            for seq, labels in train_inout_seq:
                # 清除网络先前的梯度值
                optimizer.zero_grad()  # 训练模型时需要使模型处于训练模式，即调用model.train(
                # )。缺省情况下梯度是累加的，需要手工把梯度初始化或者清零，调用optimizer.zero_grad()
                # 初始化隐藏层数据
                model.hidden_cell = (torch.zeros(1, 1, model.hidden_layer_size),
                                     torch.zeros(1, 1, model.hidden_layer_size))
                # 实例化模型
                y_pred = model(seq)
                # 计算损失，反向传播梯度以及更新模型参数
                single_loss = self.loss_function(y_pred, labels)  # 训练过程中，正向传播生成网络的输出，计算输出和实际值之间的损失值
                single_loss.backward()  # 调用loss.backward()自动生成梯度，
                optimizer.step()  # 使用optimizer.step()执行优化器，把梯度传播回每个网络

            # 查看模型训练的结果
            if i % 25 == 1:
                print(f'epoch:{i:3} loss:{single_loss.item():10.8f}')
        return model

    def _draw(self, actual_predictions):
        x = np.arange(132, 132 + self.fut_pred, 1)
        plt.title('Month vs Passenger')
        plt.ylabel('Total Passengers')
        plt.xlabel('Months')
        plt.grid(True)
        plt.autoscale(axis='x', tight=True)
        plt.plot(self.flight_data['passengers'])
        plt.plot(x, actual_predictions)
        plt.show()
        # 绘制最近12个月的实际和预测乘客数量,以更大的尺度观测数据
        plt.title('Month vs Passenger')
        plt.ylabel('Total Passengers')
        plt.xlabel('Months')
        plt.grid(True)
        plt.autoscale(axis='x', tight=True)
        plt.plot(self.flight_data['passengers'][-self.train_window:], label='业绩趋势走向')
        plt.plot(x, actual_predictions, label='预测值')
        plt.show()

    def model_test(self, model):
        test_inputs = self.train_data_normalized[-self.train_window:].tolist()  # 首先打印出数据列表的最后12个值
        # 更改模型为测试或者验证模式
        model.eval()  # 把training属性设置为false,使模型处于测试或验证状态
        for i in range(self.fut_pred):
            seq = torch.FloatTensor(test_inputs[-self.train_window:])
            with torch.no_grad():
                model.hidden = (torch.zeros(1, 1, model.hidden_layer_size),
                                torch.zeros(1, 1, model.hidden_layer_size))
                test_inputs.append(model(seq).item())
        # 由于对训练集数据进行了标准化，因此预测数据也是标准化了的
        # 需要将归一化的预测值转换为实际的预测值。通过inverse_transform实现
        actual_predictions = self.scaler.inverse_transform(np.array(test_inputs[self.train_window:]).reshape(-1, 1))
        self._draw(actual_predictions)


if __name__ == '__main__':
    model = LSTM()
    model.model_train(model)
    model.model_test(model)
