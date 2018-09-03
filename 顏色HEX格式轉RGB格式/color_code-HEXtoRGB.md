
# HEX轉RGB碼
當選擇顏色格式不同時，將HEX格式轉為比較熟悉的RGB時，可以用這個方法轉為RGB。



```python
h='#00b33c'
h=h.replace('#','')
h1, h2, h3 = h[0:2], '0x' + h[2:4], '0x' + h[4:6]
h1, h2, h3 = int(h1, 16),int(h2, 16),int(h3, 16)
abc= str(h1)+','+str(h2)+','+str(h3)
print(abc)
```

    0,179,60

