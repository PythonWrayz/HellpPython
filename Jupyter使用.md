# Jupyter notebook

Jupyter notebook 是 Python 開發利器，用來即時紀錄/呈現程式結果相當方便！notebook 可以寫 python 也可以寫 markdown、文字...還可以即時顯示圖表結果，強大...

這裡只有列出部分指令

## 啟動流程

1. 使用 conda 建立開發環境以後，安裝 jupyter notebook
2. 建立一個專案資料夾，名稱跟上一步建立的開發環境名稱相同
3. terminal 移動路徑到專案資料夾
4. 啟動: jupyter notebook
5. 建立的檔案、資料夾都會在專案資料夾中

## 好用的指令

- jupyter 快捷鍵 cheetsheet，按 h
- markdown 下 \$\$ 用來寫數學公式

$$
x = y
$$

- jupyter 裡面直接用 python 指令透過 %
  1. 用來開啟 Debug 模式，執行完 code 要結束就下 q
     `%pdb`
  2. 顯示統計圖表，再加高畫質
  ```python
  %matplotlib
  %config InlineBackend.figure_format='retina'
  ```
  3. 計算執行效率，使用 call funtion 的話，就先下 `%timeit`
  4. 計算執行效率，直接執行 code，下 `%%timeit`
