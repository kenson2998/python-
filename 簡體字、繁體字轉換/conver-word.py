def cn2zh (line) :
    from langconv import Converter
    # 簡體轉繁體
    line = line.encode('utf-8')
    line = Converter('zh-hant').convert(line.decode('utf-8'))
    return line

word='网站里面有什么繁体咸价格异常'

print('轉成繁體:',cn2zh(word))