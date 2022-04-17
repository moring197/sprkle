pytest用例发现机制

1.文件夹规则:递归形式查找

2.文件形式:在文件夹形式的基础上,test_*.py,test开头或test结尾的文件

3.用例形式: 以Test开头的类

​                   test开头的函数或方法



#### 1.作用

①发现测试用例：从多个py文件中通过默认的规则去找测试用例

②执行测试用例:顺序和条件

③判断测试结果：断言

④生成测试报告：html,allure

全局观

1.web ui自动化和接口自动化

2.跳过用例以及失败用例重跑

3.结合allure生成美观的测试报告

4.和jekins持续集成

pytest-html 生成html测试报告

pyest-xdist 多线程运行

pytest-ordering 改变测试用例的执行顺序

pytest-rerunfailures 失败用例重跑

allure-pytest 生成allure测试报告