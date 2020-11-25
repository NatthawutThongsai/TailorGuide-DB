import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode


class Customer() :
    def __init__(self, data) :
        self.custDataObj = CustomerDB(data)
    def write(self) :
        return self.custDataObj.writeDB("tg","stylist")   
    def search(self) :
        return self.custDataObj.searchDB("tg","stylist")
    
################################################################################    
    def delete(self):
        return self.custDataObj.deleteDB("tg", "stylist")
    
    def conSent(self):
        return self.custDataObj.conRequestDB("tg","")
    def canSent(self):
        return self.custDataObj.canRequestDB("tg", "")
        
    def allstyle(self) :
        return self.custDataObj.searchStyleDB("tg","stylist")
    def addStylist(self) :
        return self.custDataObj.addStylistDB("tg","stylist")
    
    def sentingRequest(self) :
        return self.custDataObj.sendRequestDB("tg","stylist")
################################################################################    

    def searchName(self) :
        return self.custDataObj.searchNameDB("tg","stylist")
    def searchRequest(self) :
        return self.custDataObj.searchReDB("tg","stylist")
    def acceptRe(self) :
        return self.custDataObj.acceptReDB("tg","stylist")
    def declineRe(self) :
        return self.custDataObj.declineReDB("tg","stylist")
    def getInfo(self) :
        return self.custDataObj.data
    
pw='0906585620'
class CustomerDB() :

    def __init__(self, data) :
        self.data = data


    def writeDB(self, databasename, table) :
        wdata=self.data

        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database=databasename,
                                                 user='root',
                                                 password=pw)
       
            objdata = (wdata[0], wdata[1])
            
            sqlQuery = "insert into "+table+" (id, name) " \
                               "values (%s,%s)"
            
            cursor = connection.cursor()
            cursor.execute(sqlQuery, objdata)
            
            connection.commit()
            

        except:
            retmsg = ["1", "writing error"]
        else :
            retmsg = ["0", "writing done"]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg


   
    def searchNameDB(self, databasename, table) :
        wkey = str(self.data[0]) #correct here

        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database=databasename,
                                                 user='root',
                                                 password=pw)

            cursor = connection.cursor()
            cursor.callproc('searchStyle', (self.data[0],))

            for result in cursor.stored_results():
                records = result.fetchall()               
            self.data = records
      
        except:
            retmsg = ["1", "Error"]
        else :
            retmsg = ["1", "Not Found"]
            if records[0] != "" :
                retmsg = ["0", "Found"]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg
    ##########################################################################

   
    def searchReDB(self, databasename, table) : #Search request id 
        wkey = str(self.data[0]) #correct here
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database=databasename,
                                                 user='root',
                                                 password=pw)

            cursor = connection.cursor()
            cursor.callproc('searchRe', (self.data[0],))
            for result in cursor.stored_results():
                records = result.fetchall()
            self.data = records
                    
        except:
            retmsg = ["1", "Error"]
        else :
            retmsg = ["1", "Not Found"]
            if records[0] != "" :
                retmsg = ["0", "Found"]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg


##########################################################################
        
    def acceptReDB(self, databasename, table) : 
        wkey = str(self.data[0]) #correct here

        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database=databasename,
                                                 user='root',
                                                 password=pw)
            objdata = (wkey,)
            sqlQuery = "call acceptRequest(%s)" 
            cursor = connection.cursor() 
            cursor.execute(sqlQuery, objdata)
            connection.commit()
                    
        except:
            retmsg = ["1", "Error"]
        else :
            retmsg = ["1", "Done"]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg


##########################################################################
        
    def declineReDB(self, databasename, table) :
        wkey = str(self.data[0]) #correct here

        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database=databasename,
                                                 user='root',
                                                 password=pw)
            objdata = (wkey,)
            sqlQuery = "call rejectRequest(%s)"
            cursor = connection.cursor()   
            cursor.execute(sqlQuery, objdata)
            connection.commit()       
        except:
            retmsg = ["1", "Error"]
        else :
            retmsg = ["1", "Done"]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg


##########################################################################
    def sendRequestDB(self, databasename, table) : 
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database=databasename,
                                                 user='root',
                                                 password=pw)
            cursor = connection.cursor()

            #connection.autocommit = False

            query = "start transaction"
            cursor.execute(query)
            objdata1 = (self.data[1],)
            sqlQuery = "SELECT SSN FROM usert WHERE username = %s"
            cursor.execute(sqlQuery, objdata1)
            result = cursor.fetchone()[0]

            objdata = (self.data[0],result)
            sqlQuery3 = "call sentRequest(%s,%s)" #correct here
            cursor.execute(sqlQuery3, objdata)
            print(1)
            connection.commit()
        except:
            retmsg = ["1", "Error"]
        else :
            retmsg = ["1", "Done"]
#         finally:
#             if (connection.is_connected()):
#                 connection.close()
#                 cursor.close()
#             return retmsg

##########################################################################
    def conRequestDB(self, databasename, table) : 
     

        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database=databasename,
                                                 user='root',
                                                 password=pw)
            cursor = connection.cursor()
            connection.commit()
            connection.autocommit = True   
        except:
            retmsg = ["1", "Error"]
        else :
            retmsg = ["1", "Done"]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg

##########################################################################
    def canRequestDB(self, databasename, table) : 
     

        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database=databasename,
                                                 user='root',
                                                 password=pw)
            cursor = connection.cursor()
            connection.rollback()
            connection.autocommit = True   
        except:
            retmsg = ["1", "Error"]
        else :
            retmsg = ["1", "Done"]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg

##########################################################################

    def deleteDB(self, databasename, table):
        wdata = self.data[0]
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database=databasename,
                                                 user='root',
                                                 password=pw)
            
            objdata = (wdata,)
            cursor = connection.cursor()

            checkQuery = "SELECT * FROM usert U, stylist S WHERE U.username = %s AND S.SSN = U.SSN"            
            cursor.execute(checkQuery, objdata)            
            myresult = cursor.fetchall()
            if myresult == []:
                retmsg = ["1","Stylist is not found"]
                return
            sqlQuery = "delete from usert where username = %s"
            cursor.execute(sqlQuery, objdata)
            connection.commit()

        except:
            retmsg = ["1", "Delete Error"]
        else:
            retmsg = ["0", "Delete Complete"]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg

    ##########################################################################
    def searchStyleDB(self, databasename, table) :
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database=databasename,
                                                 user='root',
                                                 password=pw)
            sqlQuery = "select distinct style from stylist_style"
            cursor = connection.cursor()
            cursor.execute(sqlQuery)
            records = cursor.fetchall()
            self.data = records
        except:
            retmsg = ["1", "Error"]
        else :
            retmsg = ["1", "Not Found"]
            if records[1] != "" :
                retmsg = ["0", "Found"]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg
    

    def addStylistDB(self, databasename, table) :
        wdata=self.data

        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database=databasename,
                                                 user='root',
                                                 password=pw)
            cursor = connection.cursor()
            state =1
            connection.autocommit = False
            objdata = (wdata[0],wdata[5])
            objdata1 = (wdata[0],wdata[6])
            objdata2 = (wdata[0],wdata[4])
            objdata3 = (wdata[0],wdata[1],wdata[2],wdata[3])
            sqlQuery3 = "insert into usert (SSN,username,first_name,last_name) values (%s,%s,%s,%s)"
            cursor.execute(sqlQuery3, objdata3)
            sqlQuery2 = "insert into user_phone_no (SSN,phone_no) values (%s,%s)"
            cursor.execute(sqlQuery2, objdata2)
            sqlQuery = "insert into stylist(SSN,profile_pic,bio,bio_image,avg_rating) values (%s,null,%s,null,3.00)"
            cursor.execute(sqlQuery, objdata)
            sqlQuery1 = "insert into stylist_style (SSN,style) values (%s,%s)"
            cursor.execute(sqlQuery1, objdata1)
            
            if(len(wdata[0])==13):
                connection.commit()
                state = 0
            connection.rollback()
        except:
            retmsg = ["1", "Add error"]
        else :
            if(state):
                retmsg = ["0","SSN is't correct"]
            else:
                retmsg = ["0", "Add done"]
        finally:
            if (connection.is_connected()):
                connection.close()
                cursor.close()
            return retmsg
    
