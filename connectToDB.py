import pymysql
import sys
import config
class connectTodb():

    def get(self):
        print(1)
        conn = pymysql.Connect(host=config.host,
                                user=config.user,
                                passwd=config.password,
                                port=config.port,
                                db=config.database,
                                charset=config.charset)
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM toutiao.news")
            result = cursor.fetchall()
            print(result)
            return(result)
        except IOError:
            print("failed to connect to db")
            result = "error"

        finally:
            cursor.close()
            conn.close()
            #print(result)
            #return result

