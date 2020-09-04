user_id = input("Enter your user ID (Press 1 to create account) :")

if "1" in user_id:

     email = input("Enter your user ID :")

     with open("passwords\\email.txt","w") as f:
         store_email = f.write(email)

     password = input("Enter your user passwords :")

     with open("passwords\\password.txt","w") as f:
         store_password = f.write(password)

