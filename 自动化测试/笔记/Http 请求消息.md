### Http 请求消息

#### 示例

```get
GET /mgr/login.html HTTP/1.1
Host: www.baiyueheiyu.com
User-Agent: Mozilla/6.0 (compatible; MSIE5.01; Windows NT)
Accept-Language: zh-cn
Accept-Encoding: gzip, deflate
```

```
POST /api/medicine HTTP/1.1
Host: www.baiyueheiyu.com
User-Agent: Mozilla/6.0 (compatible; MSIE5.01; Windows NT)
Content-Type: application/x-www-form-urlencoded
Content-Length: 51
Accept-Language: zh-cn
Accept-Encoding: gzip, deflate

name=qingmeisu&sn=099877883837&desc=qingmeisuyaopin
```



#### 1.请求行request line

是http请求的第一行的内容，表示要操作什么资源，使用的 http协议版本是什么。

里面包含了3部分信息： 请求的方法，操作资源的地址， 协议的版本号

``` python
GET /mgr/login.html HTTP/1.1
```

常见的HTTP 请求方法包括：

- GET

  从服务器 `获取` 资源信息，这是一种最常见的请求。

  比如 要 从服务器 获取 网页资源、获取图片资源、获取用户信息数据等等。

- POST，请求方法就应该是

  `添加` 资源信息 到 服务器进行处理（例如提交表单或者上传文件）。

  比如 要 添加用户信息、上传图片数据 到服务器 等等

  具体的数据信息，通常在 HTTP消息体中， 后面会讲到

- PUT

  请求服务器 `更新` 资源信息 。

  比如 要 更新 用户姓名、地址 等等

  具体的更新数据信息，通常在 HTTP消息体中， 后面会讲到

- DELETE

  请求服务器 `删除` 资源信息 。

  比如 要 删除 某个用户、某个药品 等等

#### 2.请求头 Request headers

请求头是http请求行下面的 的内容，里面存放 一些 信息。

比如，请求发送的服务端域名是什么， 希望接收的响应消息使用什么语言，请求消息体的长度等等。

通常请求头 都有好多个，一个请求头 占据一行

单个请求头的 格式是： `名字: 值`

HTTP协议规定了一些标准的请求头，[点击查看MDN的描述](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)

开发者，也可以在HTTP消息中 添加自己定义的请求头

#### 3.消息体 message body

  请求的url、请求头中 可以存放 一些数据信息， 但是 有些数据信息，往往需要 存放在消息体中。

特别是 POST、PUT等请求，添加、修改的数据信息 通常都是 存放在 请求消息体 中的。

如果 HTTP 请求 有 消息体， 协议规定 需要在 消息头和消息体 之间 插入一个空行， 隔开 它们。

请求消息体中保存了要提交给服务端的数据信息。

比如：客户端要上传一个文件给服务端，就可以通过HTTP请求发送文件数据给服务端。

文件的数据 就应该在请求的消息体中。





 