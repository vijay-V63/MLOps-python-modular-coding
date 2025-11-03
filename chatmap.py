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
            self
        elif choice=='2':
            self
        elif choice=='3':
            self
        else:
            exit


obj=chatmap()