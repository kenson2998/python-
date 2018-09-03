
# 使用sys.argv 取值

<h3>說明:</h3><br>
<font style=color:blue>sys.argv </font>用來撈取值給code使用,偶爾需要更改一些變數但又不想寫死code的時候可以用到。

<h3>例子說明:</h3><br>
我想寫一段指令去運算兩數相加，兩個數字可以自己修改<br>
指令是: <font style=color:blue> python sysargv.py </font><font style=color:red>8 8</font><br>
建立一個叫做 <font style=color:blue>sysargv.py</font>的檔案，類似bat檔的概念去做那些指令。

sysargv.py 裡面的code

```python
# -*- coding: utf-8 -*-
import sys
print ('sys.argv[1]: '+sys.argv[1])
print ('sys.argv[2]: '+sys.argv[2])
print (sys.argv[1]+'+'+ sys.argv[2] + '='+ str(int(sys.argv[1])+int(sys.argv[2])))

```

輸入 python sysargv.py 8 8
```python
sys.argv[1]: 8
sys.argv[2]: 8
8+8=16
```
