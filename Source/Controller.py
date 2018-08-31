import sys
import os
import time
from Model import Model
from msvcrt import getch



class Controller:
    flag = None
    a = None
    b = None

    username = "Hello"
   


    def SignUp(self):
        model = Model()
     
        print("Nhap cac thong tin dang ki")
        username = input("Username: ")
        b = model.Check(username)
        if(b != None):
            print("Tai khoan da ton tai, vui long chon ten khac")
            return self.SignUp()
        else:
            password = input("Password: ")
            name = input ("Ho va ten: ")
            idcity = input("Ma so thanh pho: \n *Luu y ma so thanh pho la so nguyen tu 1 den 10 !\n")
           
            sex = input("Gioi tinh: ")
            birthday = input("Ngay sinh: ")

            model.SignUp(username, password, name, idcity, sex, birthday)  
            print("Dang ki thanh cong !")
         


    def SignIn(self):
        model = Model()

        self.username = input("Username: ")
        password = input("Password: ")
        self.flag = model.SignIn(self.username, password)
        if ( self.flag != None ):
            os.system('cls')
            print("\nDang nhap thanh cong !")
        else:
            print("\nDang nhap that bai, yeu cau kiem tra lai tai khoan va mat khau !")

       

    def SignOut(self):
        self.flag = None
        print("\nDang xuat thanh cong !")

   
#Tin nhan



    def SendMess(self, name1):
        model = Model()
        userrec = input("Nhap ten nguoi gui: ")
        b = model.Check(userrec)
        if( b != None):
            a = model.CheckBlock(userrec, name1)
            if ( a == None):
                messdata = input ("Nhap noi dung tin nhan: ")
                model.SendMess(name1, userrec, messdata)
                print("Gui tin nhan thanh cong !")
            else:
                print("Gui tin nhan that bai !\nBan da bi nguoi dung block")
        else:
            print("Gui tin nhan that bai !\nTai khoan nhan khong ton tai")

 
         
    def ListMessSend(self, name1):
        model = Model()
        model.ShowMessSend(name1)
        chose = input("Nhap id tin nhan muon xem chi tiet: ")
        int(chose,36)
        model.ShowMessSendWithIdMess(chose)
        z = model.ShowMessSendWithIdMess(chose)
        print("Nhan ctrl+R de gui tiep")
        input_key = ord(getch()) 
        if(input_key==18):
            self.Reply(name1, z)



    def ListMessRec(self,name1):
        model = Model()
        model.ShowMessRec(name1)
        chose = input("Nhap id tin nhan muon xem chi tiet: ")
        int(chose,36)
        model.ShowMessRecWithIdMess(chose)
        z = model.ShowMessRecWithIdMess(chose)
        print("Nhan ctrl+R de tra loi")
        input_key = ord(getch()) 
        if(input_key == 18):
            self.Reply(name1, z)
    def Reply(self,name1,username2):
        model = Model()
        mess = input("Nhap noi dung tin nhan: ")
        model.ReplyMess(name1, username2, mess)

#Ban be


    def AddFriend(self,name1):
        model = Model()
        useradd = input("Nhap ten tai khoan ban muon ket ban: ")
        b = model.Check(useradd)
        a = model.CheckFriend(name1,useradd)
        if (b != None):
           if(a == None):
                model.InsertFriend(name1,useradd)
                print("Ket ban thanh cong !")
           else: 
                print("Tai khoan nay da nam trong danh sach ban be !")
        else:
            print("Tai khoan khong ton tai")
            
    
    def ListFriend(self,name1):
        model = Model()
        model.ListFriend(name1)
        print("Nhan ctrl + C de hien thi danh sach ban be theo thanh pho")
        input_key = ord(getch()) 
        if(input_key==3):
             model.ListFriendForCity(name1)        


    def ListFriendForCity(self,name1):
        model = Model()
        model.ListFriendForCity(name1)


    def RemoveFriend(self, name1):
        model = Model()
        userremove = input("Nhap ten tai khoan muon xoa ban be: ")
        b = model.Check(userremove)
        a = model.CheckFriend(name1,userremove)
        if (b != None):
           if(a != None):
                model.RemoveFriend(name1,userremove)
                print("Xoa ban be thanh cong !")
           else: 
                print("Tai khoan nay khong nam trong danh sach ban be")
        else:
            print("Tai khoan khong ton tai")


#Block
    
    def Block(self,name1):
        model = Model()
        userblock = input("Nhap ten tai khoan ban muon block: ")
        b = model.Check(userblock)
        a = model.CheckBlock(name1,userblock)
        if (b != None):
           if(a == None):
                model.Block(name1,userblock)
                print("Block thanh cong !\n Tai khoan se khong the gui tin nhan cho ban")
           else: 
                print("Tai khoan nay da nam trong danh sach block")
        else:
            print("Tai khoan khong ton tai")


    def RemoveBlock(self, name1):
        model = Model()
        userremove = input("Nhap ten tai khoan muon bo block: ")
        b = model.Check(userremove)
        a = model.CheckBlock(name1,userremove)
        if (id2 > 0):
           if(a != None):
                model.RemoveBlock(name1,userremove)
           else: 
                print("Tai khoan nay da nam trong danh sach block")
        else:
            print("Tai khoan khong ton tai")

