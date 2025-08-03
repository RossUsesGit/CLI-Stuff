"""
gambler class and info storage
"""



class Gambler():
    
    def __init__(self,name,acc_bal,acc_id,acc_status):

        self.name = name
        self.acc_bal = acc_bal
        self.acc_id = acc_id
        self.acc_status = acc_status

    def __str__(self):
        
        return f"Name: {self.name} || Account Balance: {self.acc_bal} || Account ID: {self.acc_id} || Status: {self.acc_status}"
    
   







