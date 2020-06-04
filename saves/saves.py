# coding:utf-8
import sqlite3
import ast
import os


table_name = 'saTable'
types = (int,str,bool,list,dict,tuple)


class Saves():
    current_dbname = 'database.db'

    def __init__(self, table=table_name):
        self.__conn = sqlite3.connect(self.__modify_dbname(Saves.current_dbname))
        self.__c = self.__conn.cursor()
        self.__table = table
        r = self.__is_exist(self.__table)

        if r:
            return
        self.__createTable(self.__table)

    def __del__(self):
        self.__conn.close()

    def save(self, key: str, value: object):
        """save data"""
        v = str(value)
        t = type(value)
        self.__upsert(key, v, t)

    def load(self, key: str) -> object:
        """get data"""
        r = self.__select(key)
        if len(r) < 1:
            return r
        VALUE = 1
        TYPE = 2
        v = [row[VALUE] for row in r].pop()
        t = [row[TYPE] for row in r].pop()
        return self.__trance(v,t)

    def delete(self, key: str):
        """delete record from key"""
        self.__delete(key)

    def clean(self):
        """delete all records"""
        self.__delete('hoge',all=True)

    def keys(self) -> [str]:
        """get all keys"""
        r = self.__select('')
        if len(r) < 1:
            return r
        KEYS = 0
        return [row[KEYS] for row in r]

    def drop(self, table=table_name):
        """drop table"""
        sql = 'drop table ' + table
        self.__c.execute(sql)
        self.__conn.commit()

    def set_db_name(self, dbname: str):
        """ """
        dbname = self.__modify_dbname(dbname)
        self.__update_db_name(dbname)
        Saves.current_dbname = dbname
        self.__reconnect(dbname)

    def __modify_dbname(self, dbname: str):
        return dbname.replace('.db', '') + '.db'

    def __reconnect(self, dbname: str):
        self.__conn = sqlite3.connect(dbname)
        self.__c = self.__conn.cursor()

    def __update_db_name(self, dbname: str):
        """データベース名を更新する"""
        current_dbname = self.__modify_dbname(self.current_dbname)
        if os.path.exists('./' + current_dbname):
            os.rename('./' + current_dbname, dbname)
            return
        os.rename('./' + current_dbname, dbname)

    def __createTable(self, table: str):
        """テーブルを作成する"""
        sql = 'create table ' + table +  '(key varchar(64) primary key, value none, type varchar(16))'
        self.__c.execute(sql)
        self.__conn.commit()

    def __is_exist(self,table: str):
        """Check is table exist."""
        sql = 'SELECT name FROM sqlite_master WHERE name = ?'
        r = self.__c.execute(sql,(table,))
        for h in r:
            return True
        return False

    def __upsert(self, key: str, value: object, type: type):
        """write to table"""
        if key == '':
            key = str(value)
        type = self.__get_type(type)
        sql = 'replace into ' + self.__table + ' (key, value, type) values (?,?,?)'
        record = (key, value, type)
        self.__c.execute(sql, record)
        self.__conn.commit()

    def __delete(self, key: str, all = False):
        """delete from table"""
        if all:
            sql = 'delete from ' + self.__table
        else:
            sql = 'delete from ' + self.__table + ' WHERE key = {0}'.format(key)

        self.__c.execute(sql)
        self.__conn.commit()

    def __select(self,key= ''):
        """select"""
        if key != '':
            sql = "select * from {0} where key = '{1}'".format(self.__table, key)
        else:
            sql = "select * from {0}".format(self.__table)
        r = self.__c.execute(sql)
        return r.fetchall()

    def __get_type(self, t: type) -> str:
        """check value type"""
        for v in types:
            if v == t:
                return str(v)
        return 'unknown'

    def __trance(self,v: object,t: str) -> object:
        """transform value based on type"""
        if t == str(str):
            return str(v)
        elif t == str(int):
            return int(v)
        else:
            return ast.literal_eval(v)




