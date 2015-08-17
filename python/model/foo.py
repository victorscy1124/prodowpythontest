# -*- coding: utf-8 -*-
import pymysql

class Foo(object):
    def save_and_find_all(self, parms):
        connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='prodowpythontest',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                sql = """
                    INSERT INTO foo (`name`) VALUES (%s)
                    """
                cursor.execute(sql, (parms['name'],))
                connection.commit()
                
            with connection.cursor() as cursor:
                sql = "SELECT * from foo"
                cursor.execute(sql)
            result = cursor.fetchall()
        finally:
            connection.close()
        return result