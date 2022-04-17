### 构建HTTP请求

#### 构建请求URL参数

使用Requests发送HTTP请求，url里面的参数，通常可以直接写在url里面，比如

```  python
response = requests.get('https://www.baidu.com/s?wd=iphone&rsv_spt=1')
```

可以把这些参数放到一个字典里面，然后把字典对象传递给 Requests请求方法的 params 参数

``` python
urlpara = {
    'wd':'iphone&ipad',
    'rsv_spt':'1'
}

response = requests.get('https://www.baidu.com/s',params=urlpara)
```

#### 构建请求消息头

```python
headers = {
    'user-agent': 'my-app/0.0.1', 
    'auth-type': 'jwt-token'
}

r = requests.post("http://httpbin.org/post", headers=headers)
print(r.text)
```

#### 构建请求消息体

Web API接口中，消息体基本都是文本，文本的格式主要是这3种： urlencoded ，json ， XML。

<font color='red'>注意：消息体采用什么格式，是由 开发人员设计的决定的</font>

XML格式

```XML
payload = '''
<?xml version="1.0" encoding="UTF-8"?>
<WorkReport>
    <Overall>良好</Overall>
    <Progress>30%</Progress>
    <Problems>暂无</Problems>
</WorkReport>
'''

r = requests.post("http://httpbin.org/post",
                  data=payload.encode('utf8'))
print(r.text)
```

Requests库的post方法，参数data指明了，消息体中的数据是什么。

如果传入的是字符串类型，Requests 会使用缺省编码 `latin-1` 编码为字节串放到http消息体中，发送出去。而上面的例子里面包含中文，不能用缺省 `latin-1`编码.

所以我们将字符串对象，用 `utf8` 编码为字节串对象Bytes 传入给data参数，Requests就会直接把这个字符串放到 http消息体中，发送出去。

json格式

```json
payload = '''
 report 
 Overall：良好 
 Progress: 30% 
 Problems：暂无
'''
r = requests.post("http://httpbin.org/post", 
                  data=payload.encode('utf8'))
print(r.text)
```

#### urlencoded 格式消息体

key1=value1&key2=value2

```
payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)
```

### 检查HTTP响应

#### 检查响应状态码

要检查 HTTP 响应 的状态码，直接 通过 reponse对象的 `status_code` 属性获取

```python
import requests

response = requests.get('http://mirrors.sohu.com/')
print(response.status_code)
```

#### 检查响应消息头

要检查 HTTP 响应 的消息头，直接 通过 reponse对象的 `headers` 属性获取

```python
import requests,pprint

response = requests.get('http://mirrors.sohu.com/')

print(type(response.headers))

pprint.pprint(dict(response.headers))
```

#### 检查响应消息体

要获取响应的消息体的文本内容，直接通过response对象 的 `text` 属性即可获取

```python
import requests

response = requests.get('http://mirrors.sohu.com/')
print(response.text)
```

如果我们要直接获取消息体中的字节串内容，可以使用 `content` 属性，

```python
import requests

response = requests.get('http://mirrors.sohu.com/')
print(response.content)
```

当然，如果可以直接对 获取的字节串 bytes对象进行解码

```
print(response.content.decode('utf8'))
```

API 响应的消息体格式，通常以json居多。

为了 `方便处理 响应消息中json 格式的数据` ，我们通常应该把 json 格式的字符串 转化为 python 中的数据对象。

怎么转化？ 前面我们学习过 json库，可以直接使用 json库里面的 `loads` 函数， 把 json 格式的字符串 转化为 数据对象

```
import requests,json
response = requests.post("http://httpbin.org/post", data={1:1,2:2})

obj = json.loads(response.content.decode('utf8'))
print(obj)
```

