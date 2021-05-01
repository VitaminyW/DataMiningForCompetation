import pymysql


class MyDB:
    def __init__(self, host: str, user: str, password: str, db: str, port=3306):
        self.db = pymysql.connect(host=host, user=user, password=password, port=port, db=db)
        self.cursor = self.db.cursor()

    def execute(self, sql, flag: bool):
        self.cursor.execute(sql)
        if flag:
            self.db.commit()

    def insert_data(self, data_dic: dict, table: str):
        keys = ','.join(data_dic.keys())
        values = ','.join(['%s'] * len(data_dic))
        sql = 'INSERT INTO {table}({keys})VALUES({values})'.format(table=table, keys=keys, values=values)
        try:
            if self.cursor.execute(sql, tuple(data_dic.values())):
                # print('Successful!')
                self.db.commit()
        except Exception as e:
            print('Failed!', e)
            self.db.rollback()
            raise Exception('数据库储存错误', str(data_dic))

    def select_data(self, sql, flag: bool):
        try:
            if self.cursor.execute(sql):
                print('count', self.cursor.rowcount)
                results = self.cursor.fetchall()
                if flag:
                    for item in results:
                        print(item)
                return results
            else:
                print('Error')
                return None
        except Exception as e:
            print(e)
            return None

    def db_close(self):
        self.db.close()
