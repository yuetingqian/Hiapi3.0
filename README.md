Hiapi3.0
========

Hiapi version 3.0

###环境要求
* Python2.7
* web.py (`easy_install web.py`)
* MySQLdb (`easy_install MySQL-python`)
  Mako (`cd Mako-0.8.0 && python setup.py install`)


###Database
```
cd dao
mysql -u hiapi -pmobileqa654321 Hiapi3 < create.sql
```


如果本地没有Hiapi3数据库先自己建一个

```
create database Hiapi3
```



###结构
```text
$project_root
| - config/        # 配置文件
| - controllers/   # MVC-C
| - dao/           # db操作
| - static/        # 资源文件 
| - templates/     # MVC-V
| - server.py      # 启动服务
```


以下代码规范抄袭gitcorp ^ ^
## Python

原则上遵守[PEP8](http://www.python.org/dev/peps/pep-0008/)。

### 换行

采用`\n`换行符

### 缩进
采用 **4个空格** 的缩进

### 行宽
尽量不超过 **80列** 的行宽。

理由:
  * 这在查看side-by-side的diff时很有帮助
  * 方便在控制台下查看代码
  * 太长可能是设计有缺陷

### UTF-8
代码采用UTF-8编码，在代码文件的行首加上`# -*- coding: utf-8 -*-`

### Imports

使用 **absolute** import

```
# yes
from gitcorp.biz import create_user

# no
from ..biz import create_user
```

能够在模块开头进行的import就应该放在模块前部

每行import只引入一个对象，并且按照字母顺序排序

```
# yes
from gitcorp.biz import create_user
from gitcorp.biz import delete_user

# yes
from gitcorp.biz import (
    create_user,
    delete_user
)

# no
from gitcorp.biz import create_user, delete_user

# no
from gitcorp.biz import (
    delete_user,
    create_user
)
```

Imports should be grouped in the following order:
* standard library imports
* related third party imports
* local application/library specific imports

`__all__` 跟在import声明之后

### DocString

参考[Google Style Guide](http://google-styleguide.googlecode.com/svn/trunk/pyguide.html?showone=Comments#Comments)

例如

```python
def create_user(username, display_name='', email=''):
    """Create a user with given username
    Args:
        username (string):
    Returns:
        The User model just created
    """
```

### 引号

简单说，自然语言使用双引号，机器标识使用单引号，因此 **代码里** 多数应该使用 **单引号** 

 * ***自然语言*** **使用双引号** `"..."`  
   例如错误信息；很多情况还是unicode，使用`u"你好世界"`
 * ***机器标识*** **使用单引号** `'...'` 
   例如dict里的key
 * ***正则表达式*** **使用原生的双引号** `r"..."`
 * ***文档字符*** **使用三个双引号** `"""......"""`

## JavaScript

### 缩进

采用 **2个空格** 的缩进

## HTML

### 缩进

采用 **2个空格** 的缩进

## CSS

### 缩进

采用 **2个空格** 的缩进

