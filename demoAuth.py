import re
import pyrebase

firebaseConfig = { 
    "apiKey": "AIzaSyBfKEThYdJTtEh2V8o1hcwcBSDk_TMYlOI",
    "authDomain": "demoauth-50202.firebaseapp.com",
    "databaseURL": "https://demoauth-50202-default-rtdb.firebaseio.com/",
    "projectId": "demoauth-50202",
    "storageBucket": "demoauth-50202.appspot.com",
    "messagingSenderId": "873707163912",
    "appId": "1:873707163912:web:e569eba9f5212c48831cbd",
    "measurementId": "G-NNCWZPREMZ"
}

regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()

def signUp():
    print("\nSIGNUP - FIREBASE")
    email = input("EMAIL: ")
    password = input("PASSWORD: ")

    if(re.search(regex, email)):
        print("Please Wait ...")
        try:
            user = auth.create_user_with_email_and_password(email, password)
            
            print("Successful Signup!")
            print("\nDo you want to login? [Y/n]")
            a = input("-> ")

            if a == 'y' or a == 'Y':
                login()
        except:
            print("Email Already Exists!")
    else:
        print("Error: Enter a valid email")
        signUp()   

def login():
    print("\nLOGIN - FIREBASE")
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    print("Please Wait ...")

    try:
        login = auth.sign_in_with_email_and_password(email, password)
        print("\nLogin Success!")
    except:
        print("\nError: Either email or password is wrong!")

print("Login Demo - Firebase\n")

a = int(input("[1] For Sign Up\n[2] For Login\n-> "))

if a == 1:
    signUp()
elif a == 2:
    login() 

