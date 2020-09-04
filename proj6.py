user_id = input("Enter your user ID (Press 1 to create account) :")

if "1" in user_id:

     email = input("Enter your user ID :")

     with open("passwords\\email.txt","w") as f:
         