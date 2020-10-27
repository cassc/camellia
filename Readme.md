# A company webstie with Go

## Requirements

You will need to install Go, Python 3 and Node.js.

## Build

* Edit company information in `gen-site.py`,

```python
# Edit this for new company 
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
           ]
```

* Run the following command in project directory, use the files in the `target` directory for deployment.

``` bash
make build
```

To run in Docker after building:

``` bash
cd target ; docker-compose up -d
```

## Run in dev mode

``` bash
cd be 
make dev
```

## Test the target build without Docker


``` bash
cd target/be 
./main
```


