from db import *

class YoungerProfile():
    def __init__(self, email, password):
        self.email = email
        self.password = password
        sql = f'SELECT PK_user_id, name FROM users WHERE email = "{self.email}" '
        mycursor.execute(sql)
        user_id = mycursor.fetchone()
        self.user_id = user_id[0]
        self.younger_name = user_id[1]

    def sign_up(self, user_id):
        self.user_id = user_id
        sql = "INSERT INTO youngers (FK_user_ID) VALUES (%s)"
        val = (self.user_id)
        mycursor.execute(sql, val)
        print("inserted")
        mydb.commit()

        sql = f'SELECT PK_younger_id FROM youngers WHERE FK_user_id={self.user_id}'
        mycursor.execute(sql)
        younger_id = mycursor.fetchone()
        self.younger_id=younger_id[0]

    def log_in(self):
        #retrieving passwords for registered mobile no from both table
        sql = f'SELECT password FROM users WHERE email= "{self.email}" '
        mycursor.execute(sql)
        user_info = mycursor.fetchone()     # fetchall provides empty list if record does not exists
        if user_info==[]:
            print(f'{self.email} ot registered. Please try to register first')
            import index      # due to mutual importing we are importing here just before method calling
        elif self.password==user_info[0]:
            print("Logged IN")
            self.dashboard_younger()
        else:
            print("Wrong email and password")
            import index

    def dashboard_younger(self):
        print(f'Currentlty you are taking care of Elders\nYou can request for more elders to take care of.\n1.View list of Available elders to take care of.\n2.Give review and rating for a elder\n3.LogOut')
        choice = int(input())
        if choice==1:
            self.request_elder()
        elif choice==2:
            self.review()
        elif choice==3:
            self.log_out()

    # user should be able to see list of available elder and sent them request. NOTE:- 1 user can't sent request to same elder twice
    def request_elder(self):
        sql = 'select u.name from users as u inner join elders as e where e.available=1 and e.fk_user_id=u.pk_user_id'
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print('Showing list of available needing care')
        print('--------------------------------')
        for elder in result:
            print(elder[0])
        print('--------------------------------')
        import index

    # younger can give review and rating to elders
    def review(self):
        elder_name = input("Enter name whom do you want to rate and review") #taking name of elder
        elderid = self.get_elder_id(elder_name) #getting elderid corresponds to elder_name
        review = input("Please give your review in text:")
        rating = float(input("your rating"))
        #younger_name = self.younger_name
        sql = 'insert into reviews(fk_user_id,review,rating,review_by) values(%s,%s,%s,%s)'
        val = (elderid,review,rating,self.younger_name)
        mycursor.execute(sql,val)
        mydb.commit()
        #updating the elders data after the review
        sql = f'update elders set rating={rating} where fk_user_id={elderid}' 
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