# Hawkeye
数据库自动化运维系统
#### 配置地址
app/inception.py

``` python
def table_structure(sqlcode):
    """
    sql1 指定验证库的连接地址,具体对号入座就好
    """
    sql1='/*--user=root;--password=123456;--host=127.0.0.1;--execute=1;--port=3306;*/\
            inception_magic_start;'
    sql2='inception_magic_commit;'
    sql = sql1 + sqlcode + sql2
    try:
        """
        conn 这里指定inception的服务地址,用户名,密码,端口
        """
        conn=MySQLdb.connect(host='192.168.10.130',user='root',passwd='',db='',port=6669,use_unicode=True, charset="utf8")
        cur=conn.cursor()
        ret=cur.execute(sql)
        result=cur.fetchall()
        num_fields = len(cur.description)
        field_names = [i[0] for i in cur.description]
        print field_names
        for row in result:
            print row[0], "|",row[1],"|",row[2],"|",row[3],"|",row[4],"|",row[5],"|",row[6],"|",row[7],"|",row[8],"|",row[9],"|",row[10]
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    return result[1][4].split("\n")
```
#### 运行 与 部分实现
环境:   python2.7+flask  ， inception默认配置，  mysql
直接输入rtquery，测试一个基本验证流程

http://127.0.0.1:5000/rtquery

该界面下，实现了一个基本的验证流程

验证方法：

1，只需在语句框中输入相应代码，如

    use db1;
    create table t1(id int(10));
2，点击提交审核，会在初审结果下面反馈审核结果，如
    我这里t1表已经存在，则反馈
```    
Table 't1' already exists.
Set engine to innodb for table 't1'.
Set charset to one of 'utf8mb4' for table 't1'.
Set comments for table 't1'.
Column 'id2' in table 't1' have no comments.
Column 'id2' in table 't1' is not allowed to been nullable.
Set Default value for column 'id2' in table 't1'
Set a primary key for table 't1'.
```
