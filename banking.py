#%%
import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="abidi@110$",
    database="Banking"
)
class user():
    '''
    This the parent class which define all basic details related to the customer
    '''    
    def __init__(self,name,age,gender,National_id,E_mail,account_no):
        self.name=name
        self.age=age
        self.gender=gender
        self.National_id=National_id
        self.E_mail=E_mail
        self.account_no=account_no 

    def user_records(self):
        '''
        Create the tuple of user_info table
        '''
        record=(self.name,self.age,self.gender,self.National_id)
        return record
    def user_details(self):
        '''
        Print out Name age Gender of customer
        '''
        print("(Name,Age,Gender) =",(self.name,self.age,self.gender))
class Registration(user):
    def __init__(self,name,age,gender,National_id,E_mail,account_no):
        super().__init__(name,age,gender,National_id,E_mail,account_no)
        self.name=name
        self.age=age
        self.gender=gender
        self.National_id=National_id
        self.E_mail=E_mail
        self.account_no=account_no 
        
    def new_user_info(self):
        '''
        Add new row of record in user_info table
        '''
        userinfo=customer.user_records()
        mycursor=db.cursor()
        sql="Insert into user_info(name,age,gender,National_id) VALUES(%s,%s,%s,%s)"
        values=userinfo
        mycursor.execute(sql,values)
        db.commit()
        print(mycursor.rowcount,"Record inserted")

    def new_login_info(self,__pas):
        '''
        Add new row of record in login_info table
        '''
        self.pas=__pas
        pas=input("Create password") 
        value=(self.pas,self.E_mail)
        mycursor=db.cursor()
        sql="Insert into login_info(password,E_mail_id) Values(%s,%s)"
        mycursor.execute(sql,value)
        db.commit()
        print(mycursor.rowcount,"Record inserted")

    def new_account_info(self):  
        '''
        Add new row of record in account_info table
        '''        
        value=(self.account_no,0)
        mycursor=db.cursor()
        sql="Insert into account_info(Account_no,Balance) Values(%s,%s)"
        mycursor.execute(sql,value)
        db.commit()
        print(mycursor.rowcount,"Record inserted")
    def new_user_details(self):
        '''
        Add new row of record in user_details table
        '''
        value=(self.name[:2]+"_"+str(self.account_no)[-5:],self.account_no,self.National_id,self.E_mail)
        mycursor=db.cursor()
        sql="Insert into user_details(user_id,Account_no,National_id,E_mail_id) values(%s,%s,%s,%s)"
        mycursor.execute(sql,value)
        db.commit()
        print(mycursor.rowcount,"Rows inserted")

class banking():
    def __init__(self,account_no,balance):
        self.account_no=account_no
        self.balance=balance

    def deposite(self,ammount):
        '''
        This function is used to deposite ammount in your existing account
        '''
        self.ammount=ammount
        self.balance+=ammount
        sql="update account_info set Balance = %s where Account_no = %s"
        data=(self.balance,self.account_no)
        mycursor=db.cursor()
        mycursor.execute(sql,data)
        db.commit()
        print("$",ammount,"credited in your account")

    def withdraw(self,ammount):
        '''
        This funtion is used to withraw ammount from your existing acccount
        '''
        self.ammount=ammount
        if ammount>self.balance:
            print("Insufficient ammount")
        else:
            self.balance-=ammount
            sql="update account_info set Balance = %s where Account_no = %s "
            data=(self.balance,self.account_no)
            mycursor=db.cursor()
            mycursor.execute(sql,data)
            db.commit()
            print("$",self.ammount,"withdrawn from your account")



class verify():
    def __init__(self,input_E_mail,input_pas):
        self.input_E_mail=input_E_mail
        self.input_pas=input_pas
    def verify_login(self):
        '''
        This function verify the user credentials 
        '''    
        mycursor=db.cursor()
        sql="select password,E_mail_id from login_info"
        mycursor.execute(sql)
        result=mycursor.fetchall()
        inspect=(self.input_pas,self.input_E_mail)
        if inspect in result:
            return True
        else:
            return False

    def querry_user_details(self,E_mail_id):
        '''
        This function retrieve the tuple from user_details where input email id is attached
        '''
        self.E_mail_id=E_mail_id
        mycursor=db.cursor()
        sql="select * from user_details where E_mail_id=%s"
        data=(self.E_mail_id,)
        mycursor.execute(sql,data)
        result=mycursor.fetchone()
        return result  
    def querry_name(self,National_id):
        '''
        This function queery the name of customer from user_info table takes one positional argumment National id 
        '''
        mycursor=db.cursor()
        sql="select name from user_info where National_id=%s"
        data=(National_id,)
        mycursor.execute(sql,data)
        result=mycursor.fetchone()
        return list(result) 
    def querry_balance(self,Account_no):
        '''
        This function queery balance of customer, takes one positional argument Account number
        '''
        mycursor=db.cursor()
        sql="select Balance from account_info where Account_no=%s"
        data=(Account_no,)
        mycursor.execute(sql,data)
        result=mycursor.fetchone()
        return list(result)                          
           

if __name__=="__main__":

    print("Welcom to our project")
    ans=input("Are you already registered with us? if no type 1 else anykey ")
    if ans=="1":
        name=input("Enter your name ")
        age=int(input("Enter your age"))
        gender=input("Enter your gender")
        National_id=int(input("Enter Id number"))
        E_mail=input("Enter your E_mail address")
        account_no=int(input("Enter your account number"))
        pas=input("Create password") 
        customer=Registration(name,age,gender,National_id,E_mail,account_no)
        customer.new_user_info()
        customer.new_login_info(pas)
        customer.new_account_info()
        customer.new_user_details()
        print("You have been successfully registered")
    else:
        input_e_mail=input("Enter e_mail id")
        input_password=input("Enter your password")
        holder=verify(input_e_mail,input_password)
        if holder.verify_login():
            nav=input("Enter 1 for printing user details, 2 for Depositing ammount,3 to withdraw")
            if nav=="1" :
               Acct_no= holder.querry_user_details(input_e_mail)[1]
               Nat_id=holder.querry_user_details(input_e_mail)[2]
               print("user name :",holder.querry_name(Nat_id)[0])
               print("user id :",holder.querry_user_details(input_e_mail)[0])
               print("Account_no :",holder.querry_user_details(input_e_mail)[1])
               print("National_id :",holder.querry_user_details(input_e_mail)[2])
               print("E_mail_id :",holder.querry_user_details(input_e_mail)[3])
               print("Balance : $",holder.querry_balance(Acct_no)[0])
            elif nav=="2":
                Acct_no= holder.querry_user_details(input_e_mail)[1]
                balance=holder.querry_balance(Acct_no)[0]
                ammount=int(input("Enter the ammount you want to credited"))
                holder_deposite=banking(Acct_no,balance)
                holder_deposite.deposite(ammount)
            elif nav=="3":
                Acct_no= holder.querry_user_details(input_e_mail)[1]
                balance=holder.querry_balance(Acct_no)[0]  
                ammount=int(input("Enter ammount to withdraw"))
                holder_withdraw=banking(Acct_no,balance)
                holder_withdraw.withdraw(ammount)
            else:
                pass    
        else:
            print("Incorrect Email ID or password")        
print("Thank you")            

# %%
