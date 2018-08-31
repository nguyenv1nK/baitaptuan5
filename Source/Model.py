
import sqlite3 as lite
import sys
import os
import time
con = None


class Model:
    #localtime = time.asctime( time.localtime(time.time()) )
    

    #Dang ki
    def SignUp( self,username, password, name, idcity, sex, birthday ):
        try:
            path = os.path.dirname(__file__) + "\\tuan41.db"
            con = lite.connect(path)
     
            cur = con.cursor()    
            cur.execute("insert into user(username, password, name, idcity, sex, birthday) values ( ?, ?, ?, ?, ?, ? )",(username, password, name, idcity, sex, birthday))
            con.commit()
        except lite.Error as e:
     
            print ("Error %s :" % e.args[0])
            sys.exit(1)
     
        finally:
     
            if con:
                con.close()


    #Dang nhap
    def SignIn(self,username, password):
        try:
            path = os.path.dirname(__file__) + "\\tuan41.db"
            con = lite.connect(path)
   
            cur = con.cursor()
            cur.execute("select id from user where username = ? and password = ?",(username, password))
            id = cur.fetchone()
            
        except lite.Error as e:
     
            print ("Error %s :" % e.args[0])
            sys.exit(1)
     
        finally:
     
            if con:
                con.close()
            return id


    #Check ton tai
    def Check(self,username):
        try:
            path = os.path.dirname(__file__) + "\\tuan41.db"
            con = lite.connect(path)
     
            cur = con.cursor()    
            cur.execute("select id from user where username = ?",(username,))
            id = cur.fetchone()
     
        except lite.Error as e:  
            print ("Error %s :" % e.args[0])
            sys.exit(1)
     
        finally:
            if con:
                con.close()
                return id
    #Them ban
    def InsertFriend( self,name1, name2):
        localtime = time.asctime( time.localtime(time.time()) )
        try:
            path = os.path.dirname(__file__) + "\\tuan41.db"
            con = lite.connect(path)
     
            cur = con.cursor()    
            cur.execute("insert into friend (name1, name2, intertime ) values ( ?, ?, ? )",( name1, name2, localtime ))
            con.commit()       
     
        except lite.Error as e:
            print ("Error %s :" % e.args[0])
            sys.exit(1)
     
        finally:
            if con:
                con.close()



    #Danh sach ban
    def ListFriend(self,name1):
        try:
            path = os.path.dirname(__file__) + "\\tuan41.db"
            con = lite.connect(path)
            cur = con.cursor()

            cur.execute("SELECT DISTINCT user.username FROM ((SELECT * FROM friend where (name1 = ? OR name2 = ?)) as A LEFT JOIN user ON (A.name2 = user.username OR A.name1 = user.username)) ORDER BY intertime desc",(name1,name1))
            rows = cur.fetchall()
            for row in rows:
                print(row)
           

        except lite.Error as e:
            print ("Error %s :" % e.args[0])
            sys.exit(1)
     
        finally:
            if con:
                con.close()

    #Danh sach ban theo thanh pho
    def ListFriendForCity(self,name1):
        try:
            path = os.path.dirname(__file__) + "\\tuan41.db"
            con = lite.connect(path)
            cur = con.cursor()

            cur.execute("select username,namecity from ((select * from friend where (name1 = ? or name2 =?)) as m left join user on (user.username = m.name2))as n left join city on (user.idcity = city.idcity)  ORDER BY user.idcity asc",(name1,name1))
            rows = cur.fetchall()
            for row in rows:
                print(" %s den tu %s " % (row[0],row[1]))
           

        except lite.Error as e:
            print ("Error %s :" % e.args[0])
            sys.exit(1)
     
        finally:
            if con:
                con.close()


    #Kiem tra ban
    def CheckFriend(self, name1, name2):
        try:
            path = os.path.dirname(__file__) + "\\tuan41.db"
            con = lite.connect(path)
            cur = con.cursor()

            cur.execute("select * from friend where (name1= ? and name2= ?) or (name1 =? and name2 = ?)",(name1,name2,name2,name1))
            row = cur.fetchone()
           

        except lite.Error as e:
            print ("Error %s :" % e.args[0])
            sys.exit(1)
     
        finally:
            if con:
                con.close()
                return row
    #Xoa ban
    def RemoveFriend(self,id1,id2):
       try:
            path = os.path.dirname(__file__) + "\\tuan41.db"
            con = lite.connect(path)
            cur = con.cursor()

            cur.execute(" delete from friend where (name1 = ?  and name2 = ?) ",(name1,name2))
            con.commit()

       except lite.Error as e:
            print ("Error %s :" % e.args[0])
            sys.exit(1)
     
       finally:
            if con:
                con.close()


    #Block
    def Block(self,name1,name2):
       try:
            path = os.path.dirname(__file__) + "\\tuan41.db"
            con = lite.connect(path)
            cur = con.cursor()

            cur.execute(" insert into block (name1,name2) values (?,?) ",(name1,name2))
            con.commit()

       except lite.Error as e:
            print ("Error %s :" % e.args[0])
            sys.exit(1)
     
       finally:
            if con:
                con.close()

    #Kiem tra block
    def CheckBlock(self,name1,name2):
        try:
            path = os.path.dirname(__file__) + "\\tuan41.db"
            con = lite.connect(path)
   
            cur = con.cursor()
            cur.execute("select * from block where name1 = ? and name2 = ?",(name1, name2))
            row = cur.fetchone()
            
        except lite.Error as e:
     
            print ("Error %s :" % e.args[0])
            sys.exit(1)
     
        finally:
     
            if con:
                con.close()
                return row
            
    #Xoa block
    def RemoveBlock(self,name1,name2):
       try:
            path = os.path.dirname(__file__) + "\\tuan41.db"
            con = lite.connect(path)
            cur = con.cursor()

            cur.execute(" delete from block where (name1 = ?  and name2 = ?) ",(name1,name2))
            con.commit()

       except lite.Error as e:
            print ("Error %s :" % e.args[0])
            sys.exit(1)
     
       finally:
            if con:
                con.close()



    #Gui thu

    def SendMess( self,name1, name2, mess):
        localtime = time.asctime( time.localtime(time.time()) )
        try:
            path = os.path.dirname(__file__) + "\\tuan41.db"
            con = lite.connect(path)
     
            cur = con.cursor()    
            cur.execute("insert into messeger (namesend, namerec, mess, time, status) values (?, ?, ?, ?,'chua xem')",(name1, name2, mess, localtime))
            cur.execute("update friend set intertime = ? where (name1 = ? and name2 = ?) or (name1 = ? and name2 = ?)",(localtime, name1, name2, name2, name1)) 
            con.commit()       
     
        except lite.Error as e:
            print ("Error %s :" % e.args[0])
            sys.exit(1)
     
        finally:
            if con:
                con.close()

    #Hien thi tin nhan gui
    def ShowMessSend( self, name1 ):

        try:
            path = os.path.dirname(__file__) + "\\tuan41.db"
            con = lite.connect(path)
            cur = con.cursor()

            cur.execute("select idmess,mess from messeger where namesend = ?",(name1,))
            rows = cur.fetchall()
            for row in rows:
                print(row)
           
        except lite.Error as e:
            print ("Error %s :" % e.args[0])
            sys.exit(1)
     
        finally:
            if con:
                con.close()


    #Hien thi tin nhan nhan
    def ShowMessRec( self,name1 ):
        try:
            path = os.path.dirname(__file__) + "\\tuan41.db"
            con = lite.connect(path)
            cur = con.cursor()

            cur.execute("select idmess,mess from messeger where namerec = ?",(name1,))
            rows = cur.fetchall()
            for row in rows:
                print(row)

        except lite.Error as e:
            print ("Error %s :" % e.args[0])
            sys.exit(1)

        finally:
            if con:
                con.close()

    #Reply tin nhan
    def ReplyMess(self, name1, name2, mess):
        localtime = time.asctime( time.localtime(time.time()) )
        try:
            path = os.path.dirname(__file__) + "\\tuan41.db"
            con = lite.connect(path)
     
            cur = con.cursor()    
            cur.execute("insert into messeger (namesend, namerec, mess, time, status) values (?, ?, ?, ?,'chua xem')",(name1, name2, mess, localtime))
            cur.execute("update friend set intertime = ? where (name1 = ? and name2 = ?) or (name1 = ? and name2 = ?)",(localtime, name1, name2, name2, name1)) 
            con.commit()       
     
        except lite.Error as e:
            print ("Error %s :" % e.args[0])
            sys.exit(1)
     
        finally:
            if con:
                con.close()



    #Hien thi chi tiet tin nhan da nhan theo id
    def ShowMessRecWithIdMess(self,id):
        try:
            path = os.path.dirname(__file__) + "\\tuan41.db"
            con = lite.connect(path)
            cur = con.cursor()

            cur.execute("select mess, time, username from ( select * from messeger as m left join user on (user.username = m.namerec)) where idmess = ?",(id,))
            rows = cur.fetchall()
            for row in rows:
                #print ("%s %s %s" % (row["Id"], row["Name"], row["Price"]))
                print ("Tin nhan tu %s " % (row[2]))
                print ("Voi noi dung %s " % (row[0]))
                print ("Vao luc %s" % (row[1]))
            cur.execute("update messeger set status = 'da xem' where idmess = ? ",(id,))
            con.commit()

        except lite.Error as e:
            print ("Error %s :" % e.args[0])
            sys.exit(1)
     
        finally:
            if con:
                con.close()
                return row[2]

    #Hien thi chi tiet tin nhan da gui theo id
    def ShowMessSendWithIdMess(self,id):
        try:
            path = os.path.dirname(__file__) + "\\tuan41.db"
            con = lite.connect(path)
            cur = con.cursor()

            cur.execute("select mess, time, username, status from ( select * from messeger as m left join user on (user.username = m.namesend)) where idmess = ?",(id,))
            rows = cur.fetchall()
            for row in rows:
                print("Da gui tin nhan den: %s " % (row[2]))
                print("Voi noi dung: %s " % (row[0]))
                print("Vao luc: %s " % (row[1]))
                print("Tinh trang: %s " % (row[3]))

        except lite.Error as e:
            print("Error %s : " %e.args[0])
            sys.exit(1)

        finally:
            if con:
                con.close()
                return row[2]