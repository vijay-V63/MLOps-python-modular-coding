class chatmap:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin=False
        self.menu()


    def menu(self):
        choice=input("""enter the users choice & menu is here \n
                    1. press 1 To Register \n
                    2. press 2 To signin \n
                    3. press 3 To write a post \n
                    4. press 4 To know about company \n
                    5. press any key to exit \n
                    
                    Enter here: """)
        
        if choice=='1':
            self.register()
        elif choice=='2':
            self.signin()
        elif choice=='3':
            self.post()
        elif choice=='4':
            self.company()
        else:
            exit

    def menu_2(self):
        choice2=input("""enter the users choice & menu is here \n
                    1. press 3 To write a post \n
                    2. press 4 To know about company \n
                    3. press 5 To send a message or to chat with a friend \n
                    4. press any key to logout \n
                    
                    Enter here: """)
        
        if choice2=='3':
            self.post()
        elif choice2=='4':
            self.company()
        elif choice2=='5':
            self.msg()
        else:
            exit
    
    def register(self):
        print("Welcome onboard new user great that your joining our chatmap")
        user_mail=input("Enter your Email:    ")
        user_name=input("Enter your Name:   ")
        in_pass=input("Enter your pasword:   ")
        co_pass=input("Confirm your password:   ")
        if in_pass==co_pass:
            print("User succesfully registered ✅")
            self.username=user_mail
            self.password=co_pass
            print("You are in a queue please wait or go back to menu a quick profile screening has to be completed...")

        else:
            print("There is a network glitch or password not matches")
            print("Thank you and try again...")

        back=input("press key / To back to menu:   ")
        if back=='/':
            self.menu()

    def signin(self):
        user_mail=input("Enter your Email:    ")
        in_pass=input("Enter your pasword:   ")
        if user_mail==self.username and in_pass==self.password:
            self.loggedin=True
            print("😁🫱🏼‍🫲🏼 Logged in Successfully...")
            self.menu_2()


        else:
            print("user doesn't exists or data has been breached sorry oops...")
            self.menu()


    def post(self):
        if self.loggedin==False:
            print("please first login to the chatmap")
            self.menu()
        
        else:
            post_data=input("Create your valuable post insight here:    ")
            print("posted successfully...")
            print(post_data)
            print("\n")
            self.menu_2()

    def company(self):
        print("Company name is ChatMap founded by vijay and raju to learn about python oops through an application...")
        if self.loggedin==True:
            self.menu_2()
        else:
            print("please first login to the chatmap")
            self.menu()


    def msg(self):
        if self.loggedin==True:
            receiver=input("enter the username you wanted to chat with:   ")
            msge=input("enter your message here:   ")
            print("\n \n")
            print(f"Notification: {self.username} sends msg to {receiver}")
            print(msge)
            print("\n")
            self.menu_2()

        else:
            self.menu()




#commenting object to check the modular coding concept
#obj=chatmap()