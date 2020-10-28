# 使用SQLite数据库的网站引擎



## 编译环境

Linux系统并安装 Go, Python 3 及 Node.js.

## 编译

> 若不需要修改公司信息，编译只需要进行一次。

* 修改 `gen-site.py`的公司信息,

```python
company = [dict(val='北京xxx有限公司',    ky='title.full', desc='公司全名'),
           dict(val='xxx',                ky='title.simple', desc='公司简称'),
           dict(val='xxx',                ky='title.en', desc='公司英文简称'),
           
           dict(val='x先生',              ky='contact.name', desc='公司联系人姓名'),
           dict(val='xxx',                ky='contact.phone', desc='联系人手机号'),
           dict(val='xxx',                ky='contact.email', desc='联系人邮箱'),
           dict(val='北京xxx区xxx路xxxo', ky='contact.address', desc='公司地址'),

           # 经纬度用于在地图上标记公司位置
           dict(val='39.9042',            ky='location.lat', desc='地址纬度'),
           dict(val='116.4074',           ky='location.lon', desc='地址经度'),

           # 英文网站链接，没有就不修改
           dict(val='javascript:;',       ky='ensite', desc='公司全名'),

           # 备案号
           dict(val='粤ICP备88888888号',  ky='beianhao', desc='公司全名'),

           # 电商n链接
           dict(val='',  ky='shop.title', desc='电商名'),
           dict(val='',  ky='shop.link', desc='电商链接'),
           ]
```

* 使用`python3 gen-site.py`编译。编译成功后，使用生成的 `target` 目录部署。

* 运行

``` bash
cd target/be ; ./main
```

## 开发

``` bash
cd be 
make dev
```


# 编辑

* 对于SQLite数据库，可以使用[sqlitebrowser](https://sqlitebrowser.org/dl/)修改，修改前请先备份数据库文件。
* 对于tmpl模板文件，可以使用文本编辑器如vscode打开编辑。

## 编辑产品

* 添加、修改、删除产品： 编辑 `be/product.db` sqlite数据库 及 `be/templates/products/`文件夹里对应的模板文件。
* 修改主页展示的产品：修改 `be/templates/index.tmpl`


## 编辑方案

编辑方案与编辑产品类似，只是修改的数据库与模板文件夹位置不同。

* 添加、修改、删除方案： 编辑 `be/solution.db` sqlite数据库 及 `be/templates/solutions/`文件夹里对应的模板文件。
* 修改主页展示的方案：修改 `be/templates/index.tmpl`

## 编辑新闻


编辑新闻与编辑产品类似，只是修改的数据库与模板文件夹位置不同。

* 添加、修改、删除新闻： 编辑 `be/news.db` sqlite数据库 及 `be/news/`文件夹里对应的HTML文件。

## 编辑页面及部分页面元素

* 主页：修改 `be/templates/index.tmpl`
* 导航栏: 修改 `be/templates/nav.tmpl`
* 页脚: 修改 `be/templates/footer.tmpl` 
* 联系我们页面: 修改 `be/templates/contactus.tmpl`
* 关于我们页面: 修改 `be/templates/aboutus.tmpl`
* 产品中心页面边栏：修改 `be/templates/product-left.tmpl`
* 解决方案页面边栏：修改 `be/templates/solution-left.tmpl`

