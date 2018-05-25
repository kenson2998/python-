### 簡單import 其他py檔的方法

現在有兩個py檔<br>
1.原目錄下的funt1.py<br>
2./fun_dir/funt2.py<br>
import sys 將路徑加入即可。欲了解系統的路徑可以另外print(sys.path)<br>

import_ex.py的內容:
```python
# -*- coding: utf-8 -*-
import sys 
import funt1
funt1.fun_a()

sys.path.append('/fun_dir/')
import funt2
funt2.fun_b()
```
<hr>
如果是import上一層的話就是:<br>

```python
import sys 
sys.path.append('../fun_dir/')

```
