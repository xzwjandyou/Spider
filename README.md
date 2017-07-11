# Spider
Spider



<!-- Scrapy，virtualenvwrapper需要依赖six，在安装six的时候发现系统已经有一个six-1.4.1，但是virtualenvwrapper需要six-1.9.0，于是想先卸载老版本的six，此时问题来了，发现没有权限卸载，此时我就纳闷，加上sudo，还是没权限。于是Google之，最终还是在万能的GitHub找到答案。six-1.4.1是系统内置的packages，因 系统集成保护 你是没有权限去修改/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/six-1.4.1-py2.7.egg-info目录的。因此在安装virtualenvwrapper的时候需要选择忽略six的安装：



sudo brew install wget/sudo port install wget

sudo pip install --upgrade pip

 

sudo pip install virtualenvwrapper --upgrade --ignore-installed six

 

sudo pip install Scrapy --upgrade --ignore-installed six





wget http://pypi.python.org/packages/source/z/zope.interface/zope.interface-4.0.1.tar.gz




source ~/.bash_profile 
mysqld_safe --skip-grant-tables
mysql -u root -p
SET PASSWORD FOR 'root'@'localhost' = PASSWORD('newpass’);
flush privileges;
show global variables like 'port’;
3. MAC OX命令行启动/停止/重启MySQL命令:

sudo /usr/local/mysql/support-files/mysql.server start

sudo /usr/local/mysql/support-files/mysql.server stop

sudo /usr/local/mysql/support-files/mysql.server restart





1、停止MySQL

sudo /usr/local/mysql/support-files/mysql.server stop

2、切换到MySQL的安装目录下的bin目录

cd  /usr/local/mysql/bin

3、安全模式启动MySQL

sudo ./mysqld_safe --skip-grant-tables

该命令执行后会得到完整的MySQL数据库，如下


mysql> show databases;

+-----------------------------+

| Database                    |

+-----------------------------+

| information_schema   |

| mysql                          |

| performance_schema |

| test                              |

+-----------------------------+


4、使用root用户启动mysql

mysql -u root

5、为root用户设置新的密码

mysql > UPDATE mysql.user SET Password=PASSWORD('password') WHERE User='root';

6、刷新

mysql > FLUSH PRIVILEGES;

7、退出MySQL后重启使用root登录，大功告成！！！！ -->