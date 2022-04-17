#### Unittest 框架

#### 基本应用

1.环境搭建：python3.7以上的版本内直接加载了unittest框架

2.四大组件

①test fixture：setup（前置条件） teardown（后置条件），用来初始化用例以及清理和释放资源

②test case：测试用例，通过集成unittest.TestCase，来实现用例的继承，在Unittest,所有用例都是通过test来识别的

③test suite:测试套件，测试集

list[case1,case2,case3]

④test runner：运行器，一般通过runner来调用suite去执行测试



3.运行机制：通过在main函数中，调用unittest.main()运行所有





自动化测试框架：

采用python+selenium+unittest+ddt等技术去实现的，数据驱动是使用ddt+excel实现的，测试代码分为公共模块，http请求，断言，发送邮件，读取excel内容等，数据区，用例模块，测试项目的逻辑代码大部分放在这里，用例收集



接口关联：

多个用例需要用到同一个参数token，并且测试用例跨python脚本。

一般token 只需要获取一次就好了。

解决思路：

1.首先把公共数据单独抽出来，用yaml文件去管理

2.封装读取yaml文件，获取其中的token的值

3.其他脚本全部调用a.py()里面的get_token()函数

4.token动态获取写个登录函数放到run.py









