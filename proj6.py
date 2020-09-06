import pickle

user_id = input("Enter your user ID (Press 1 to create account) :")

dictionary = {}

# with open(r"C:\Users\Caiseyann\Documents\passwords\pass_man.txt", "br") as filewrite:
#     dictionary = pickle.load(filewrite)

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

       if "2" in conf:
           account = input("Enter your account name : ")
           acc_pass = input("Enter your account password : ")

           confirmation = input("Would you like to save this input (y/n) : ")

           if "y" in confirmation:
               dictionary[account] = password

               with open(r"C:\Users\Caiseyann\Documents\passwords\pass_man.txt", "bw") as readfile:
                   dictionary = pickle.dump.load()


