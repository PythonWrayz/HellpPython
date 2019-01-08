Modules 可看做是 Files，一個 Module 就是一份檔案，裡頭有定義的 variables, functions, class, script

## 匯入 module

匯入 module 名稱就是檔案名稱，
在執行程式可用幾個方式 import

- import module
- import module as nickname
  > 上面方式前提要 module 檔案在同一層
- from folder import module1, module2
- from . import module
- from ..folder import module1, module2
- from ..forlder.subforder import module
  > 建議使用相對路徑
- from mudule import function1, function2
- from module import \*
  > 不推薦

## 匯入 module 的 class

- import folder.module import class

一樣可用相對路徑

**Ray 習慣**

以後專案還是將 class 統一放在資料夾 Modles 比較方便。

```txt
import 陷阱

moduleA 匯入 moduleB
moduleB 也匯入 moduleA

匯入方式：
from module import function

這個方式會先執行 module 再匯入 function

就會變成 moduleA -> moduleB -> moduleA -> moduleB -> ...

[解決方法]
把匯入方式改成匯入整個 module 而不是 functionname 就可解決，因為這樣不會先執行 module，而是到了程式要使用 module.function 的時候執行另外被建立的 module instance
```

## `__main__`

在 module 加上這段判斷，當  module  是主要程式入口點時才執行 something，匯入的時候，因為 name 不是 main，所以 something 不會執行。

```python
# 當此 module 為主要入口點
if __name__ == "__main__":
    # do something
```

## Packages

建立資料夾/子資料夾：
一般我們會把相關的類別歸納在一個資料夾，或是先開資料夾然後放相關的類別。

**Python** 專用
要讓程式可以匯入 package，在資料夾內就要新增一份檔案 `__init__.py`，宣稱此資料夾是一個 package

這份檔案裡面可以寫東西，當匯入 package 執行時，`__init__.py` 每次都會被優先執行

### 好用的 dir

dir 可以列出指定 object 包含哪些屬性、方法

```python
print(dir(object))
```

## Python Complie

指令：python3 執行檔案名稱

下完指令就會產生一份資料夾 `__pycache__`，裡面將使用的 `.py` 檔案用編譯成 CPython 37 版可讀取的 code `xxx.cpython-37.pyc`
