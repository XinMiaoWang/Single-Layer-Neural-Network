import numpy as np
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import globalVar
import TkGUI as gui
import matplotlib.pyplot as plt
import copy

from collections import Counter

# 讀檔
def readfile():
    data = []
    filename = globalVar.path_
    with open(filename) as file:
        line = file.readline()
        while line:
            eachline = line.split()
            read_data = [ float(x) for x in eachline[0:len(eachline)-1] ] # 轉float
            read_data.insert(0, -1) # 所有data前面都加上-1
            label = [ int(x) for x in eachline[-1] ] # label轉int
            read_data.append(label[0])
            data.append(read_data)
            line = file.readline()

    # print('Original: ',data)
    return data

def preprocess(data):
    data, noiseData = romoveNoise(np.array(data)) # 移除雜點
    data = changeLabel(np.array(data)) # 統一label
    np.random.shuffle(data) # 打亂data
    # print('Random: ',data)
    train, test = data[:int(len(data)*2/3)], data[int(len(data)*2/3):] # 分2/3 teaing data，1/3 testing data
    # train, test = np.array(data[:]), []
    # print('Train: ',train)
    # print('Test: ',test)

    if len(noiseData) == 0:
        return train, test, []

    return train, test, noiseData

# 移除雜點
def romoveNoise(data):
    originalData = copy.copy(data)
    countLabel = Counter(data[:, -1]) # 計算label種類
    # print('QQQQQQ', countLabel)
    # print('Len: ',len(countLabel))

    if len(countLabel) > 2:
        most_common_words = [word for word, word_count in Counter(countLabel).most_common()[:-2:-1]] # 找出數量最少的label
        # print(type(most_common_words)) # list
        float_lst = [int(float(x)) for x in most_common_words] # 要先轉float再轉int否則會報錯

        removeIdx = np.where(data[:, -1] == float_lst[0]) # 找出雜點index
        print('Idx: ',removeIdx)
        noiseData = originalData[removeIdx,:]
        # print('!!!!!!!!', noiseData)
        result = np.delete(data, removeIdx, 0) # 刪除雜點
        # print('/////////////////////////////')
        # print('After Remove: ',result)
        # print('/////////////////////////////')

        return result,noiseData

    return data, []


# 統一label，原始label大的標為1，小的標為0
def changeLabel(data):
    changedata = copy.copy(data)
    # countLabel = Counter(changedata[:,-1])
    # print('QQQQQQ',countLabel)
    # print(data[:,-1])
    bigLabel = np.max(data[:,-1])
    bigIdx = np.where(data[:, -1] == bigLabel)
    print('bigIdx : ',bigIdx)
    changedata[bigIdx,-1] = 1

    smallLabel = np.min(data[:, -1])
    smallIdx = np.where(data[:, -1] == smallLabel)
    print('smallIdx : ', smallIdx)
    changedata[smallIdx, -1] = 0

    return changedata


def sgn(value):
    if value>=0:
        return 1
    else:
        return 0


def perceptron(train, test, learning_rate, iteration):
    # learning_rate = 0.8
    # weight = np.array([-1, 0, 1])
    weight = np.round(np.random.rand(train.shape[1]-1),2) #隨機產生在[0,1)之間均勻分布的鍵結值
    print('Original Weight: ',weight)

    train_error_rate = 0
    test_error_rate = 0

    x_train = train[:, :train.shape[1]-1]
    y_train = train[:, -1]
    # print('X_Train: ', x_train)
    # print('Y_Train: ', y_train)

    x_test = test[:, :test.shape[1] - 1]
    y_test = test[:, -1]
    # print('X_Test: ', x_test)
    # print('Y_Test: ', y_test)

    for n in range(iteration):
        # print('\nRound: ',n)
        i = n % train.shape[0]
        v = np.dot(weight.T, x_train[i])
        predict = sgn(v)
        # print('\npredict: ',predict)
        # print('ans: ',y_train[i])

        if y_train[i]>predict:
            weight = weight + learning_rate * x_train[i]
            train_error_rate = train_error_rate + 1
        elif y_train[i]<predict:
            weight = weight - learning_rate * x_train[i]
            train_error_rate = train_error_rate + 1

        # print('Weight: ',weight)
    weight = np.round(weight,2)

    training_accuracy = np.round( 1-(train_error_rate / iteration), 3 )
    # print("======= Training =======")
    # print('\nError: ', train_error_rate)
    # print('Correct Rate: ', training_accuracy)
    # print("========================")

    for i in range(test.shape[0]):
        v = np.dot(weight.T, x_test[i])
        predict = sgn(v)
        # print('\npredict: ',predict)
        # print('ans: ',y_test[i])

        if y_test[i]!=predict:
            test_error_rate = test_error_rate + 1

    test_accuracy = np.round( 1 - (test_error_rate / test.shape[0]), 3 )
    # print("\n======= Testing =======")
    # print('Error: ', test_error_rate)
    # print('Correct Rate: ', test_accuracy)
    # print("========================")
    return training_accuracy,test_accuracy,weight

# 畫圖
def plotData(dataSet, w, window, DataType, NoiseData):
    fig = plt.figure(figsize=(4,4), dpi=100)
    ax = fig.add_subplot(111)
    ax.set_title(DataType + 'dataset')
    plt.xlabel('X')
    plt.ylabel('Y')
    # plt.axis('equal')
    # ax.set_aspect('equal', adjustable='box')

    # 畫training/testing data
    labels = dataSet[:, -1]
    idx_1 = np.where(dataSet[:, -1] == 1)
    p1 = ax.scatter(dataSet[idx_1, 1], dataSet[idx_1, 2], marker='o', color='g', label=1, s=20)
    idx_2 = np.where(dataSet[:, -1] == 0)
    p2 = ax.scatter(dataSet[idx_2, 1], dataSet[idx_2, 2], marker='x', color='r', label=0, s=20)

    # print(len(NoiseData))
    # 畫雜點
    if len(NoiseData) > 0:
        p3 = ax.scatter(NoiseData[:, :, 1], NoiseData[:, :, 2], marker='^', color='b', label='Noise', s=20) # NoiseData is 3d-array

    # 畫分割線
    x = np.arange(np.min(dataSet[:,1]), np.max(dataSet[:,2]), 0.1)
    if w[2]==0:
        y = 0
    else:
        y = (w[0] - w[1] * x) / w[2]
    ax.add_line(plt.Line2D(x, y))

    # 示意圖
    plt.legend(loc='upper right')
    # plt.show()

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    if DataType == 'Training':
        canvas.get_tk_widget().place(x=450, y=80)
    else:
        canvas.get_tk_widget().place(x=850, y=80)

    # toolbar
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    toolbar.place(x=725, y=10)


# if __name__ == '__main__':
    # data = readfile()
    # train, test = preprocess(data)
    # perceptron(train, test)
