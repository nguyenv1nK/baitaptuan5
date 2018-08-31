import sys
import os
from Controller import Controller
from msvcrt import getch


class View():

    username = None
    def MainMenu(self):
        controller = Controller()
        print("\n========Menu========\n")
        print("1.Tin nhan")
        print("2.Ban be")
        print("3.Block")
        print("4.Dang xuat")
        chose = input("\nMoi nhap lua chon: ")

        if(chose == "1"):
            os.system('cls')
            return self.MenuMess()

        elif(chose == "2"):
            os.system('cls')
            return self.MenuFriend()

        elif(chose == "3"):
            os.system('cls')
            return self.MenuBlock()

        elif(chose == "4"):
            os.system('cls')
            controller.SignOut()
            self.username = None
            return self.Menu()

        else:
            os.system('cls')
            print("\nKhong co lua chon nay, yeu cau nhap lai !")
            return self.MainMenu()
       


    def Menu(self):

        controller = Controller()
        print("\n========Login Screen========\n")
        print("1.Dang nhap")
        print("2.Dang ki")
        print("\n\n")
        chose = input("Moi nhap lua chon: ")
        
        if(chose == "1"):
            os.system('cls')
            controller.SignIn()

        elif(chose == "2"):
            os.system('cls')
            controller.SignUp()

        else:
            os.system('cls')
            print("\nKhong co lua chon nay, yeu cau nhap lai !")

        
        if( controller.flag != None ):
            self.username = controller.username
            return  self.MainMenu()
            
        else:
            return self.Menu()
     
        

  
    def MenuMess(self):

        controller = Controller()
        print("\n========Tin nhan========\n")
        print("1.Gui tin nhan")
        print("2.Danh sach tin nhan da gui")
        print("3.Danh sach tin nhan da nhan")

        chose = input("\nMoi nhap lua chon: ")
        
        if(chose =="1"):
            os.system('cls')
            controller.SendMess(self.username)
        elif(chose == "2"):
            os.system('cls')
            controller.ListMessSend(self.username)
        elif(chose == "3"):
            os.system('cls')
            controller.ListMessRec(self.username)
        else:
            os.system('cls')
            print("\nKhong co lua chon nay, yeu cau nhap lai !")
            return self.MenuMess()
        print("Nhan ctrl + B de quay lai Tin nhan")
        print("Nhan ctrl + M de quay lai Menu")
        print("Nhan ctrl + X de thoat chuong trinh")
        input_key = ord(getch()) 
        if(input_key==2):
            os.system('cls')
            return self.MenuMess()
        if(input_key==13):
            os.system('cls')
            return self.MainMenu()
        if(input_key==24):
            return 0

    def MenuFriend(self):
        controller = Controller()
        print("========Ban be========\n")
        print("1.Them ban")
        print("2.Danh sach ban")
        print("3.Xoa ban be")

        chose = input("\nMoi nhap lua chon: ")

        if(chose =="1"):
           os.system('cls')
           controller.AddFriend(self.username) 

        elif(chose == "2"):
            os.system('cls')
            controller.ListFriend(self.username)

        elif(chose == "3"):
            os.system('cls')
            controller.RemoveFriend(self.username)

        else:
            print("\nKhong co lua chon nay, yeu cau nhap lai !")
            return self.MenuFriend()
        print("Nhan ctrl + B de quay lai Ban be")
        print("Nhan ctrl + M de quay lai Menu")
        print("Nhan ctrl + X de thoat chuong trinh")
        if(input_key==2):
            os.system('cls')
            return self.MenuFriend()
        if(input_key==13):
            os.system('cls')
            return self.MainMenu()
        if(input_key==24):
            return 0

    def MenuBlock(self):
        controller = Controller()
        print("========Block========\n")
        print("1.Block")
        print("2.Go block")
        chose = input("\nMoi nhap lua chon: ")

        if(chose =="1"):
            os.system('cls')
            controller.Block(self.username)
        elif(chose =="2"):
            os.system('cls')
            controller.RemoveBlock(self.username)
        else:
            print("\nKhong co lua chon nay, yeu cau nhap lai !")
            return self.MenuBlock()
        print("Nhan ctrl + B de quay lai Block")
        print("Nhan ctrl + M de quay lai Menu")
        print("Nhan ctrl + X de thoat chuong trinh")
        if(input_key==2):
            os.system('cls')
            return self.MenuBlock()
        if(input_key==13):
            os.system('cls')
            return self.MainMenu()
        if(input_key==24):
            return 0
