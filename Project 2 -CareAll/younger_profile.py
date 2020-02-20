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
        pass

    def log_out(self):
        import index