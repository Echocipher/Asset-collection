# Asset-collection

[![Python 3.6](https://img.shields.io/badge/python-3.6-yellow.svg)](https://www.python.org/)

## 版权 ##

author：Echocipher

mail：echocipher@163.com

blog：https://www.jianshu.com/u/1f2643f05298

## 关于 ##

资产信息收集脚本

## 使用说明 ##

1. 查看帮助

> main.py -h

![help](https://raw.githubusercontent.com/Echocipher/picture/master/asset-collection/help.png)

2. 指定单个目标地址

> main.py -u www.test.com

3. 指定目标文件

> main.py -r url.txt

4. 选择功能模块

> main.py -s port|subdomain|catalog|all

分别为全端口探测，子域名挖掘，敏感文件/地址探测，全选。

5. 指定线程

> main.py -t 50

### 使用示例 ###

1. 指定网址进行全端口扫描

> main.py -u www.33s98k.cn -t 50

![url](https://raw.githubusercontent.com/Echocipher/picture/master/asset-collection/%E5%8D%95%E4%B8%AA%E6%96%87%E4%BB%B6.png)

2. 选择文件进行全端口扫描

> main.py -r url.txt -t 50

![file](https://raw.githubusercontent.com/Echocipher/picture/master/asset-collection/%E7%AB%AF%E5%8F%A3%E6%89%AB%E6%8F%8F.png)

3. 查看结果

结果会按照日期和目标保存在output/Port目录下：

![result](https://raw.githubusercontent.com/Echocipher/picture/master/asset-collection/%E7%BB%93%E6%9E%9C.png)


## 说明 ##


本项目仅进行漏洞探测工作，无漏洞利用、攻击性行为，开发初衷仅为方便安全人员对授权项目完成测试工作和学习交流使用，**请使用者遵守当地相关法律，勿用于非授权测试，如作他用所承受的法律责任一概与作者无关，下载使用即代表使用者同意上述观点**。

附《[中华人民共和国网络安全法](http://www.npc.gov.cn/npc/xinwen/2016-11/07/content_2001605.htm)》。


