user_id = input("Enter your user ID (Press 1 to create account) :")

if "1" in user_id:

     email = input("Enter your user ID :")

     with open(r"C:\Users\Caiseyann\Documents\passwords\email.txt", "w") as f:
         store_email = f.write(email)

     password = input("Enter your user passwords :")

     with open(r"C:\Users\Caiseyann\Documents\passwords\pass.txt", "w") as a:
         store_pass = a.write(password)

with open(r"C:\Users\Caiseyann\Documents\passwords\email.txt", "r") as fr:
         store_email = fr.read()

if user_id == store_email:
    password2 = input("Enter your password : ")
    with open(r"C:\Users\Caiseyann\Documents\passwords\pass.txt", "r") as ar:
        store_pass = ar.read()

    if password2 == store_pass:
       conf = input("To know your password select '1', to save your password select '2' :")