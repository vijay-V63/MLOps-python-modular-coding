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
                    3. press 3 To know about company \n
                    4. press any key to exit \n
                    
                    Enter here: """)
        
        if choice=='1':
            self.register()
        elif choice=='2':
            self.signin()
        elif choice=='3':
            self
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

        else:
            print("user doesn't exists or data has been breached sorry oops...")
            self.menu()




obj=chatmap()