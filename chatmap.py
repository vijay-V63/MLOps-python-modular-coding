class chatmap:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin='false'
        self.menu()


    def menu(self):
        choice=input("""enter the users choice & menu is here \n
                    1. press 1 To Register \n
                    2. press 2 To signup \n
                    3. press 3 To know about company \n
                    4. press any key to exit \n
                    
                    Enter here: """)
        
        if choice=='1':
            self.register()
        elif choice=='2':
            self
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
            print("User succesfully registered")

        else:
            print("There is a network glitch or password not matches")
            print("Thank you and try again...")




obj=chatmap()