### 如何運用pymongo和免費空間mlab
會用到的東西:<br>
1.mlab空間
<img src="https://mlab.com/base/img/mLab-logo-dark.svg" title='mlab' width="40" height="40">網址:<a href="https://mlab.com/">https://mlab.com/</a><br>
2.pymongo (ver3.6.0)
3.Robo 3T <img src='https://robomongo.org/static/robomongo-128x128-129df2f1.png' width="40" height="40">網址:<a href='https://robomongo.org/'>https://mlab.com/</a><br>
安裝pymongo插件
在系統或是requirements.txt下pip安裝pymongo ，這邊版本是3.6.0

```python
$pip install pymongo==3.6.0
```
<hr>

## 到<a src='https://mlab.com/'>mlab官網</a>申請一組帳號
點擊sign up 註冊按鈕。<br>
<img src ='https://raw.githubusercontent.com/kenson2998/python-/master/pymongo運用/img/1.png' ><br>
註冊後，進入自己的面板大廳按下右邊的Creat new ，創建一個資料庫。<br>
<img src ='https://raw.githubusercontent.com/kenson2998/python-/master/pymongo運用/img/2.png' ><br>
第一排隨便你選，第二排選最左邊免費的，可提供單一沙盒500MB的空間，再按CONTINUE。<br>
<img src ='https://raw.githubusercontent.com/kenson2998/python-/master/pymongo運用/img/3.png' ><br>
選擇地點一樣看你，再按CONTINUE。<br>
<img src ='https://raw.githubusercontent.com/kenson2998/python-/master/pymongo運用/img/4.png' ><br>
命名你的資料庫名稱，再按下一步。<br>
<img src ='https://raw.githubusercontent.com/kenson2998/python-/master/pymongo運用/img/5.png' ><br>
這時候可以看到你剛剛建立的資料庫，點擊他可以看到兩串代碼，第二串是給pymongo使用的，先複製起來。<br>
<img src ='https://raw.githubusercontent.com/kenson2998/python-/master/pymongo運用/img/6.png' ><br>
點擊Users分頁，建立一個使用者來連線使用。<br>
<img src ='https://raw.githubusercontent.com/kenson2998/python-/master/pymongo運用/img/7.png' ><br>
輸入好使用者帳號密碼後，再按Create。<br>
<img src ='https://raw.githubusercontent.com/kenson2998/python-/master/pymongo運用/img/8.png' ><br>
<hr>

## 到<a src='https://robomongo.org/'>Robo 3T官網</a>下載Robo 3T 管理工具
此工具是方便做查詢、新增、修改、刪除等等小功能，大項目的新增資料還是不太方便。<br>

安裝後開啟Robo 3T程式，點擊Create按鈕。<br>
<img src ='https://raw.githubusercontent.com/kenson2998/python-/master/pymongo運用/img/robo1.png' ><br>
將剛剛的複製來的那串其中:ds119930.mlab.com:19930 輸入到欄位上。<br>
<img src ='https://raw.githubusercontent.com/kenson2998/python-/master/pymongo運用/img/robo2.png' ><br>
第二分頁輸入資料庫名稱"leon-mlab",還有使用者帳號密碼，<br>
再點擊test進行測試是否兩個燈都是綠色，確認資料輸入無誤。<br>

<img src ='https://raw.githubusercontent.com/kenson2998/python-/master/pymongo運用/img/robo3.png' ><br>
連線後對Collection點擊右鍵，Creat Collection 創立一個資料表單。<br>
<img src ='https://raw.githubusercontent.com/kenson2998/python-/master/pymongo運用/img/robo4.png' ><br>
命名為test1。<br>
<img src ='https://raw.githubusercontent.com/kenson2998/python-/master/pymongo運用/img/robo5.png' ><br>
這時候點兩下可以看到右邊是一個空的查詢結果。<br>
<img src ='https://raw.githubusercontent.com/kenson2998/python-/master/pymongo運用/img/robo6.png' ><br>

<hr>

## python 連線 mlab資料庫

前面建置的差不多後，終於可以切入主題拉～<br>
先import pymongo模包<br>

```python
import pymongo
```
然後將剛剛複製的內容，貼到一個字串變數裡。<br>
```python
uri = "mongodb://user:password@ds000000.mlab.com:000000/leon-mlab"
```
接下來用語法進行連接<br>
```python

client = pymongo.MongoClient(uri)
db = client['leon-mlab']
collect = db['test1']

```
現在要新增一筆資料給test這個資料庫試試。<br>

```python
collect.insert({'_id':'firstdata','name':'Leon'})
```

>'firstdata'

<img src ='https://raw.githubusercontent.com/kenson2998/python-/master/pymongo運用/img/pymongo1.png' ><br>



或是不給id他會自動亂數生成id。<br>
```python
collect.insert({'name':'Leon'})
```

>ObjectId('5af609bb4423710c2c8df899')

<img src ='https://raw.githubusercontent.com/kenson2998/python-/master/pymongo運用/img/pymongo2.png' ><br>