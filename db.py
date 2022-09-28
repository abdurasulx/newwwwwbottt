import sqlite3

class Database:
    def __init__(self,db_file):
        self.connection=sqlite3.connect(db_file)
        #self.cursor=self.connection.cursor()
    def exists(self,user_id):
        with self.connection:
            result=self.connection.execute("SELECT * FROM `information` WHERE `User_id` = ?", (user_id,)).fetchall()
        return bool(len(result))
    def add_user(self,user_id):
        with self.connection:
            reurn =self.connection.execute("INSERT INTO `information` (`User_id`) VALUES (?)",(user_id,))[0]
            return reurn
    def get_lang(self,user_id):
        with self.connection:
            return self.connection.execute('select lang from "information" where "user_id" = ?"',(user_id,))[0]

    def set_lang(self,user_id,index):
        with self.connection:
               return self.connection.execute("UPDATE `information` set lang= (?) WHERE user_id= (  ?)",(index,user_id, ))


class mahsulotlar:
    def __init__(self,db_file):
        self.connection=sqlite3.connect(db_file)
        self.cursor=self.connection.cursor()
    def get_count(self,name):
        with self.connection:
            return self.cursor.connection.execute('SELECT count(*) FROM '+name+' where 1=1').fetchone()[0]
    def get_name(self,usid,dbname):
        with self.connection:
            return (self.connection.execute('select name from '+dbname+' where id=(?)',(usid,)).fetchone())[0]
    def get_price(self,usid,dbname):
        with self.connection:
            return (self.connection.execute('select narx from '+dbname+' where id=(?)',(usid,)).fetchone())[0]