首先不得不先誇獎自己，anaconda 在 mac 的 path 設定終於搞定了！

Mac 安裝 Anaconda 有些眉角，花了不少時間搞定它。

## 安裝

1. 上 Anaconda 找到安裝檔

   - GUI 介面安裝
   - Command Line 安裝
     二選一就可以了。

2. 跟著安裝手冊跑

這份文件路徑不起眼，很容易被忽略掉！
[Anaconda 安裝文件](http://docs.anaconda.com/anaconda/install/mac-os/#macos-graphical-install)

3. 裝完以後上 Conda 網站跟著文件做設定

[Conda 文件](https://conda.io/docs/user-guide/install/macos.html#install-macos-silent)

**重點**
就只有一個 PATH 設定，才能在 terminal 直接下 `conda xxxxx`

在網路上查到很多範例都是要設定環境變數 PATH
`export PATH="$HOME/anaconda/bin:$PATH"`

但 Anaconda 在安裝的時候已經有設定好 PATH 在 `~/.bash_profile`，這是屬於個人帳號使用的環境變數，所以要自己記得啟動它 `source ~/.bash_profile`，之後才能直接下 `conda xxx`

就這個讓我搞了很久，又學到一件事了，設定文件要好好看，很容易 miss 掉...
