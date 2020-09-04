user_id = input("Enter your user ID (Press 1 to create account) :")

if "1" in user_id:

     email = input("Enter your user ID :")

     with open(r"C:\Users\Caiseyann\Documents\passwords\email.txt", "w") as f:
         store_email = f.write(email)

     password = input("Enter your user passwords :")

     with open(r"C:\Users\Caiseyann\Documents\passwords\password.txt", "w") as a:
         store_password = a.write(password)

