import pickle
import pyperclip

user_id = input("Enter your user ID (Press 1 to create account) : ")

dictionary = {}

with open(r"C:\Users\Caiseyann\Documents\passwords\pass_man.txt", "br") as filewrite:
    dictionary = pickle.load(filewrite)

if "1" in user_id:

     email = input("Enter your user ID : ")

     with open(r"C:\\Users\\Caiseyann\\Documents\\passwords\\email.txt", "w") as f:
        f.write(email)

     password = input("Enter your user passwords : ")

     with open(r"C:\\Users\\Caiseyann\\Documents\\passwords\\pass.txt", "w") as a:
         a.write(password)

with open(r"C:\\Users\\Caiseyann\\Documents\\passwords\\email.txt", "r") as fr:
         store_email = fr.read()

if user_id == store_email:
    password2 = input("Enter your password : ")
    with open(r"C:\\Users\\Caiseyann\\Documents\\passwords\\pass.txt", "r") as ar:
        store_pass = ar.read()

    if password2 == store_pass:
       conf = input("To know your password select '1', to save your password select '2' :")

       if "2" in conf:
           account = input("Enter your account name : ")
           acc_pass = input("Enter your account password : ")

           confirmation = input("Would you like to save it (y/n) : ")

           if "y" in confirmation:
               dictionary[account] = acc_pass

               with open(r"C:\\Users\\Caiseyann\\Documents\\passwords\\pass_man.txt", "bw") as readfile:
                   dictionary = pickle.dump(dictionary, readfile, protocal=2)
               print(f"Done! Your {account}'s password has been saved")

           else:
               print("your data has not been saved")

       if "1" in conf:
           email1 = input("Which account's password would you want to know: ")

           with open(r"C:\\Users\\Caiseyann\\Documents\\passwords\\pass_man.txt", "br") as file:
               dictionary = pickle.load(file)

           if email1 in dictionary:
               print(f"Your {email1}'s password is {dictionary[email1]}")
               print("Your password has been saved to your clipboard")
               pyperclip.copy(dictionary[email1])
       else:
           print("This password is not saved")




