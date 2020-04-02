from db import *

class ElderProfile():
    def __init__(self, email, password):
        self.email = email
        self.password = password
        sql = f'SELECT PK_user_id, name FROM users WHERE email = "{self.email}"'
        mycursor.execute(sql)
        user_id = mycursor.fetchone()
        self.user_id = user_id[0]
        self.elder_id = self.user_id
        self.elder_name = user_id[1]
        

    def sign_up(self, user_id):
        self.user_id = user_id
        sql = "INSERT INTO elders (FK_user_ID) VALUES (%s)"
        val = (self.user_id)
        mycursor.execute(sql, val)
        print('inserted')
        mydb.commit()
        sql = f'SELECT PK_elder_id FROM elders WHERE FK_user_id={self.user_id}'
        mycursor.execute(sql)
        elder_id = mycursor.fetchone()
        self.elder_id=elder_id[0]

    def log_in(self):
        #retrieving passwords for registered mobile no from both table
        sql = f'SELECT password FROM users WHERE email= "{self.email}" '
        mycursor.execute(sql)
        user_info = mycursor.fetchone()     # fetchall provides empty list if record does not exists
        if user_info==[]:
            print(f'{self.email} not registered. Please try to register first')
            import index      # due to mutual importing we are importing here just before method calling
        elif self.password==user_info[0]:
            print("Logged IN")
            self.dashboard_elder()
        else:
            print("Wrong email and password")
            import index

    def dashboard_elder(self):
        sql = f'SELECT available FROM elders where fK_user_id = {self.elder_id}'
        mycursor.execute(sql)
        user_info = mycursor.fetchone()
        if user_info[0]==1:
            print(f"Hello {self.elder_name},You are currently Available to take care of.\n1.Make Unavailable\n2.Fund\n3.Request\n4.Take Care Name\n5.Give review and rating for a younger\n6.LogOut")
            choice = int(input(":"))
            if choice==1:
                self.change_status()
                self.dashboard_elder()
            elif choice==2:
                self.allocate_fund()
            elif choice==3:
                self.show_request()
            elif choice==4:
                self.take_care_name()
            elif choice==5:
                self.review()
            elif choice==6:
                self.log_out()

        else:
            print("You are currently Unavailable to take care of.\n1.Make Available\n2.Log Out")
            choice = int(input())
            if choice==1:
                self.change_status()
                self.dashboard_elder()
            elif choice==2:
                self.log_out()

    # elder should be able to allocate fund
    def allocate_fund(self):
        pass

    # elder can change their status from available to unavailable and vice-versa
    def change_status(self):
        #elder who is logged in can change their respective avialabiliy
        id = self.get_elder_id(self.elder_name)
        sql = f'select pk_elder_id,available from elders where fk_user_id={id}'
        mycursor.execute(sql)
        result = mycursor.fetchone()
        if result[1]:
            sql = f'update elders set available={0} where pk_elder_id={result[0]}'
            mycursor.execute(sql)
            mydb.commit()
        else:
            sql = f'update elders set available={1} where pk_elder_id={result[0]}'
            mycursor.execute(sql)
            mydb.commit()


    # elder can see requests and accept whome they trust only 1 request can be accepted by elder      
    def show_request(self):
        pass

    # elder can see name of younger who is taking care of them
    def take_care_name(self):
        pass

    # elder can give review and rating to youngers
    def review(self):
        younger_name = input("Enter name whom do you want to rate and review") #taking name of younger
        youngerid = self.get_younger_id(younger_name) #getting youngerid corresponds to younger_name
        review = input("Please give your review in text:")
        rating = float(input("your rating"))
        #younger_name = self.younger_name
        sql = 'insert into reviews(fk_user_id,review,rating,review_by) values(%s,%s,%s,%s)'
        val = (youngerid,review,rating,self.elder_name)
        mycursor.execute(sql,val)
        mydb.commit()
        #updating the elders data after the review
        sql = f'update youngers set rating={rating} where fk_user_id={youngerid}' 
        mycursor.execute(sql)
        mydb.commit()

    def log_out(self):
        import index

    
    def get_elder_id(self,elder_name):
        elder_name = elder_name.split(" ")
        fname =  elder_name[0]
        lname = elder_name[1]   #fetching first and last name because two person may have same fname
        sql = 'select pk_user_id,name from users'
        mycursor.execute(sql)
        result = mycursor.fetchall()
        elderid = 0
        for info in result:
            fullname = info[1].split(" ")
            if fname.lower() == fullname[0].lower() and lname.lower() == fullname[1].lower():
                elderid = info[0]
        return elderid


    def get_younger_id(self,younger_name):
        younger_name = younger_name.split(" ")
        fname =  younger_name[0]
        lname = younger_name[1]   #fetching first and last name because two person may have same fname
        sql = 'select pk_user_id,name from users'
        mycursor.execute(sql)
        result = mycursor.fetchall()
        elderid = 0
        for info in result:
            fullname = info[1].split(" ")
            if fname.lower() == fullname[0].lower() and lname.lower() == fullname[1].lower():
                elderid = info[0]
        return elderid
