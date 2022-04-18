##### Postman界面

collections 项目集合

APis api文档

Environments 环境变量

Mock Server 虚拟服务器

Monitors 监听器

History 历史

##### Postman执行接口测试

请求页面

Params:get请求传参

authorization：鉴权

headers：请求头

Body：post 请求传参

​          none 没有参数

​		 form-data：既可以传键值对参数也可以传文件

​		 x-www-form-urlemcoded：只能够传键值对参数

​	    raw：json，text，xml，html，JavaScript

​        binary：把文件以二进制的方式传参

​        pre-request script：请求之前的脚本

​         tests：请求后的断言

​	     cookies：管理cookies信息

响应标签

Body:

​	Pretty:以Json，html,XML...不同的格式查看

Cookies:



##### 接口关联

1.使用json提取器实现接口关联

```javascript
console.log(responseBody);

var result=Json.parase(responBody)
console.log(result.token)

//resoponseBody.match();
```



