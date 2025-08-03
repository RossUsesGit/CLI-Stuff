"""
code for handling account making
"""


from gamblers import Gambler, user_list

print("Make an account")

n = str(input("Name: "))
ab = float(input("Account Balance: "))
aid = int(input("Account ID: "))
astat = str(input("Account Status: "))

user2 = Gambler(n,ab,aid,astat) 

user_list.append(user2)

