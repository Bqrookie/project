import MySQLdb


def init_config():
    config = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'passwd': 'root',
        'db': 'wps',
        'charset': 'utf8',
    }

    db = MySQLdb.connect(host=config['host'],
                         port=config['port'],
                         user=config['user'],
                         passwd=config['passwd'],
                         db=config['db'],
                         charset=config['charset']
                         )

    return db


def get_data():

    data = list()

    db = init_config()

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT * FROM wifi"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            "id mac router routerPwd pin pwd ssid remark"

            data.append("%s %s %s %s %s %s %s %s" % (row[0], row[1], row[
                        6], row[5], row[2], row[3], row[4], row[7]))

    except Exception as ret:
        print('db_select[%s]' % (ret,))
    finally:
        return data

    # 关闭数据库连接
    db.close()


def insert_data(wifi_obj):

    db = init_config()

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 插入语句
    sql = "INSERT INTO `wifi` (`mac`, `router`, `routerPwd`, `pin`, `pwd`, `ssid`, `remarks`) VALUES ('%s', '%s', '%s'\
, '%s', '%s', '%s', '%s')" % (
        wifi_obj['mac'], wifi_obj['router'], wifi_obj['routerPwd'], wifi_obj['pin'], wifi_obj['pwd'], wifi_obj['ssid'],
        wifi_obj['remarks'])
    try:
        # 执行sql语句
        result = cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except Exception as ret:
        # Rollback in case there is any error
        print('db_add[%s]' % (ret,))
        db.rollback()

    # 关闭数据库连接
    db.close()
    return result


def del_data(obj_id):
    db = init_config()

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 删除语
    sql = "DELETE FROM wifi WHERE id = %d" % obj_id

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交修改
        db.commit()
    except Exception as ret:
        # Rollback in case there is any error
        print('db_del[%s]' % (ret,))
        db.rollback()

    # 关闭连接
    db.close()


def edit_data(wifi_obj, id_obj):
    db = init_config()

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 更新语句
    sql = "update wifi set mac='%s', router='%s', routerPwd='%s', pin='%s', pwd='%s', ssid='%s', remarks='%s' where id \
= %d" % (
        wifi_obj['mac'],  wifi_obj['router'],  wifi_obj['routerPwd'],  wifi_obj['pin'],  wifi_obj['pwd'],  wifi_obj['ssid'],  wifi_obj['remarks'], id_obj)


    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except Exception as ret:
        # Rollback in case there is any error
        print('db_edit[%s]' % (ret,))
        db.rollback()

    # 关闭数据库连接
    db.close()


def main():
    pass


if __name__ == '__main__':
    main()
