### 可以簡體字轉繁體字的小工具

下載以下兩個文件<br>
zh_wiki.py: https://github.com/skydark/nstools/blob/master/zhtools/zh_wiki.py<br>
langconv.py: https://github.com/skydark/nstools/blob/master/zhtools/langconv.py<br>

```python
def cn2zh (line) :
    from langconv import Converter
    # 簡體轉繁體
    line = line.encode('utf-8')
    line = Converter('zh-hant').convert(line.decode('utf-8'))
    return line

word='网站里面有什么繁体价格异常'

print('轉成繁體:',cn2zh(word))
```
<hr>
執行後轉成繁體<br>
python conver-word.py

```python

轉成繁體: 網站裡面有什麼繁體價格異常
```