# Single-Layer-Perceptron
### 實作單層感知機  
* 程式執行說明：  
1、點擊選擇檔案，可選擇dataset。  
2、學習率設定可輸入大於0，小於等於1的小數。  
3、收斂條件設定，即輸入感知機疊代次數。  
4、完成1~3設定後，點擊「執行」即可顯示訓練準確率、測試準確率、鍵結值和訓練/測試資料分布圖。  
5、Toolbar可調整分布圖大小等等。  
  
![](https://github.com/XinMiaoWang/Single-Layer-Neural-Network/blob/main/demo/1.PNG)
  
* 程式碼簡介:  
  - GUI設計  
    createWidgets()函式會建立出使用者介面，包含文字、輸入框、按鈕等等。  
  - 資料前處理  
    因為單層感知機架構上的設計只能進行二分類，再加上每個dataset要分類的label都不相同，因此在資料前處理的時候統一了各個dataset的label，label數字較大的標為1代表正樣本，較小的標為0代表負樣本。 
      
    ![](https://github.com/XinMiaoWang/Single-Layer-Perceptron/blob/main/demo/2.png)  
      
    在2Circle2 dataset發現label數量有三個，但是第三個label的數量較少，因此我把它當作Noise，不加入Train和Test的過程。  
      
    ![](https://github.com/XinMiaoWang/Single-Layer-Perceptron/blob/main/demo/3.png)  
      
  - 感知機設計  
    步驟一：網路初始化  
        Weight的初始值為隨機產生，範圍在[0,1)之間。  
          
       ![](https://github.com/XinMiaoWang/Single-Layer-Perceptron/blob/main/demo/4.png)  
          
    步驟二：計算網路輸出值  
        根據計算公式將輸入值與鍵結值進行內積運算，再對計算結果進行分類，若為正，則將他分類為正樣本，反之則為負樣本。  
       -	計算公式為：  
        ![](https://github.com/XinMiaoWang/Single-Layer-Perceptron/blob/main/demo/5.png)  
          
       -	程式碼：  
        ![](https://github.com/XinMiaoWang/Single-Layer-Perceptron/blob/main/demo/6.png)  
        ![](https://github.com/XinMiaoWang/Single-Layer-Perceptron/blob/main/demo/7.png) 

    步驟三：調整鍵結值向量  
        判斷資料是否有正確分類，若誤判就對Weight進行更新，根據以下原則來計算新的Weight：  
        ![](https://github.com/XinMiaoWang/Single-Layer-Perceptron/blob/main/demo/8.png)  
        ![](https://github.com/XinMiaoWang/Single-Layer-Perceptron/blob/main/demo/9.png)  
  
    步驟二和步驟三反覆執行，直到達到我們所設的收斂條件(疊代次數)才停止(每一次疊代訓練一筆資料)。

  - 繪圖  
    使用matplotlib套件。圈圈為正樣本，叉叉為負樣本，藉由訓練完成的感知機可以得到最終的Weight，從Weight我們能夠得到分割正負樣本的直線方程式，並將之繪於圖上。
    - 畫正負樣本  
     ![](https://github.com/XinMiaoWang/Single-Layer-Perceptron/blob/main/demo/10.png)  
    - 畫Noise  
     ![](https://github.com/XinMiaoWang/Single-Layer-Perceptron/blob/main/demo/11.png)  
    - 畫分割線  
     ![](https://github.com/XinMiaoWang/Single-Layer-Perceptron/blob/main/demo/12.png)
