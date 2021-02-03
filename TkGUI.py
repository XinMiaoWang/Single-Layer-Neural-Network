import tkinter as tk
from tkinter.filedialog import askopenfilename
import globalVar
import perceptron


# 讀檔
def load_file():
    globalVar.path_ = tk.filedialog.askopenfilename()
    path.set(globalVar.path_.split('/')[-1])

# 取得輸入值
def get_value():
    learning_rate = float(entry_2.get())
    iteration = int(entry_3.get())
    begin(learning_rate,iteration)

# 清空欄位
def clear():
    text_1.delete(0.0, tk.END)
    text_2.delete(0.0, tk.END)
    text_3.delete(0.0, tk.END)
# 顯示結果
def show_result(train_accuracy,test_accuracy,final_weight):
    clear()
    text_1.insert('insert', str(train_accuracy))
    text_2.insert('insert', str(test_accuracy))
    text_3.insert('insert', str(final_weight))

# 建立介面
def createWidgets():
    global path, entry_2, entry_3, text_1, text_2, text_3

    # Load File ---Start
    path = tk.StringVar()
    # 标签的文字、字体和字体大小、标签长宽
    label_1 = tk.Label( window, text="檔案路徑:", font=('Arial', 14), width=15, height=2 ).place(x=0, y=25, anchor='nw')
    entry_1 = tk.Entry(window, textvariable=path)
    entry_1.place(x=150, y=40, anchor='nw')
    button_1 = tk.Button(window, text="選擇檔案", font=('Arial', 14), command=load_file).place(x=300, y=30, anchor='nw')
    # Load File ---End

    # 學習率設定 ---Start
    label_2 = tk.Label( window, text='學習率設定:', font=('Arial', 14), width=15, height=2 ).place(x=0, y=85, anchor='nw')
    entry_2 = tk.Entry(window)
    entry_2.place(x=150, y=100, anchor='nw')
    # 學習率設定 ---End

    # 收斂條件設定 ---Start
    label_3 = tk.Label( window, text='收斂條件設定:', font=('Arial', 14), width=15, height=2 ).place(x=0, y=150, anchor='nw')
    entry_3 = tk.Entry(window)
    entry_3.place(x=150, y=165, anchor='nw')
    # 收斂條件設定 ---End


    # 顯示訓練準確率 ---Start
    label_4 = tk.Label( window, text='訓練準確率:', font=('Arial', 14), width=15, height=2 ).place(x=0, y=275, anchor='nw')
    text_1 = tk.Text(window, width=20, height=1.3)
    text_1.place(x=150, y=290, anchor='nw')
    # 顯示訓練準確率 ---End

    # 顯示測試準確率 ---Start
    label_5 = tk.Label( window, text='測試準確率:', font=('Arial', 14), width=15, height=2 ).place(x=0, y=330, anchor='nw')
    text_2 = tk.Text(window, width=20, height=1.3)
    text_2.place(x=150, y=350, anchor='nw')
    # 顯示測試準確率 ---End

    # 顯示鍵結值 ---Start
    label_6 = tk.Label(window, text='鍵結值:', font=('Arial', 14), width=15, height=2).place(x=0, y=385, anchor='nw')
    text_3 = tk.Text(window, width=25, height=1.3)
    text_3.place(x=150, y=410, anchor='nw')
    # 顯示鍵結值 ---End

    # 執行 ---Start
    button_2 = tk.Button( window, text="執行", width=15, height=2, command=get_value ).place(x=150, y=450, anchor='nw')
    # 執行 ---End

# 程式開始執行
def begin(learning_rate,iteration):
    data = perceptron.readfile() # 讀檔
    train, test, noiseData = perceptron.preprocess(data) # 前處理
    train_accuracy,test_accuracy,final_weight = perceptron.perceptron(train, test, learning_rate, iteration) # 感知機

    perceptron.plotData(train, final_weight, window, 'Training', noiseData) # 畫訓練資料
    perceptron.plotData(test, final_weight, window, 'Testing', noiseData) # 畫測試資料
    show_result(train_accuracy,test_accuracy,final_weight) # 顯示準確率、鍵結值

if __name__ == '__main__':
    globalVar.initialize()
    # global window
    window = tk.Tk()
    window.title('Hw1')
    window.geometry('1300x600') # 視窗大小
    createWidgets() # 建立介面
    window.mainloop()
