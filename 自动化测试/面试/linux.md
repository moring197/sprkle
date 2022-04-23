##### 1.文件查找命令：

find -name /dir  filename

##### 2.文件权限修改：

chmod +x

temp 临时存放文件权限  777

1777 表示只有创建者和root可以删除

文件所有者（属主） 文件所属组（属主） 其他用户

r:4 w:2 x:1

##### 3.查看linux性能的命令

1.top命令   cpu负载、内存负载

2.free命令  查看内存占用情况

3.iostat  IO读写速度

4.vmstat 虚拟内存读写速度

5.查看端口命令 lsof（list open files） -i:端口号   

netstat -tunlp | grep 端口号 用于显示tcp、udp的端口和进程等相关情况

6.grep 用于查找文件里符合条件的字符串

7.xargs  将管道或标准输入（stdin）数据转换成命令行参数，也能够从文件的输出中读取数据

8.find 路径 -name "filename"