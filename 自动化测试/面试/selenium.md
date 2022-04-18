| 定位一个元素                      | 定位多个元素                       | 含义                  |
| :-------------------------------- | ---------------------------------- | --------------------- |
| find_element_by_id                | find_elements_by_id                | 通过元素id定位        |
| find_element_by_name              | find_elements_by_name              | 通过元素name定位      |
| find_element_by_xpath             | find_elements_by_xpath             | 通过xpath表达式定位   |
| find_element_by_link_text         | find_elements_by_link_tex          | 通过完整超链接定位    |
| find_element_by_partial_link_text | find_elements_by_partial_link_text | 通过部分链接定位      |
| find_element_by_tag_name          | find_elements_by_tag_name          | 通过标签定位‘’‘       |
| find_element_by_class_name        | find_elements_by_class_name        | 通过类名进行定位      |
| find_elements_by_css_selector     | find_elements_by_css_selector      | 通过css选择器进行定位 |

注意：

1、find_element_by_xxx找的是第一个符合条件的标签，find_elements_by_xxx找的是所有符合条件的标签。

2、根据ID、CSS选择器和XPath获取，它们返回的结果完全一致。

3、另外，Selenium还提供了通用方法`find_element()`，它需要传入两个参数：查找方式`By`和值。实际上，它就是`find_element_by_id()`这种方法的通用函数版本，比如`find_element_by_id(id)`就等价于`find_element(By.ID, id)`，二者得到的结果完全一致。

##### 控制浏览器

| set_window_size()   | 设置浏览器的大小       |
| ------------------- | ---------------------- |
| back()              | 控制浏览器后退         |
| forward()           | 控制浏览器前进         |
| refresh()           | 刷新当前页面           |
| clear()             | 清除文本               |
| send_keys (value)   | 模拟按键输入           |
| click()             | 单击元素               |
| submit()            | 用于提交表单           |
| get_attribute(name) | 获取元素属性值         |
| is_displayed()      | 设置该元素是否用户可见 |
| size                | 返回元素的尺寸         |
| text                | 获取元素的文本         |

##### **调用JavaScript代码**

虽然WebDriver提供了操作浏览器的前进和后退方法，但对于浏览器滚动条并没有提供相应的操作方法。在这种情况下，就可以借助JavaScript来控制浏览器的滚动条。WebDriver提供了execute_script()方法来执行JavaScript代码。

用于调整浏览器滚动条位置的JavaScript代码如下：

```
from selenium import webdriver
from time import sleep
```

 

```
# 1.访问百度
drive = webdriver.Chrome(executable_path=``'chromedriver.exe'``)
drive.get(``'https://www.baidu.com'``)
```

 

```
# 2.搜索
drive.find_element_by_id(``'kw'``).send_keys(``'python'``)
drive.find_element_by_id(``'su'``).click()
```

 

```
# 3.休眠2s,获取服务器的响应内容
sleep(2)
```

 

```
# 4.通过javascript设置浏览器窗口的滚动条位置
drive.execute_script(``'window.scrollTo(0, 500)'``)
# drive.execute_script('window.scrollTo(0, document.body.scrollHeight)') #滑到最底部
```

 

```python
sleep(2)
drive.close()
```

