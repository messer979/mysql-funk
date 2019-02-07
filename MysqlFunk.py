#! python3.7

import mysql.connector
import traceback



class MysqlFunk:
    '''
    notes
    '''
    def __init__(self,host,database,user,password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        dbconfig = {
            'user': user,
            'password': password,
            'host': host,
            'database': database
                }
    def query_statement(self, statement):
        cnx = mysql.connector.connect(**dbconfig)
        dbcur = cnx.cursor()
        try:
            dbcur.execute(statement)
            cursorReadout = dbcur.fetchall()
        except :
            print("Problem executing statement: %s" % (statement))
            traceback.print_exc()
            cursorReadout = []
        dbcur.close()
        cnx.close()
        return cursorReadout
    def commit_statement(self, statement):
        cnx = mysql.connector.connect(**dbconfig)
        dbcur = cnx.cursor()
        try:
            dbcur.execute(statement)
            cnx.commit()        
        except :
            print("Problem executing statement: %s" % (statement))
            traceback.print_exc()
        return