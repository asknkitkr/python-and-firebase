import pyrebase
from prettytable import PrettyTable

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

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

t = PrettyTable()
f = PrettyTable()

def menu():
    print("::::: REAL-TIME DATABASE :::::")
    f.field_names = ["Command", "Task"]
    f.add_row(["C", "Store Information"])
    f.add_row(["R", "Print Information"])
    f.add_row(["U", "Update Information"])
    f.add_row(["D", "Delete Information"])
    f.add_row(["E", "Exit Program"])
    print(f)

def create():
    username = input("Enter Username: ")
    name = input("Enter Name: ")
    
    while True:
        gender = input("Enter Gender [M/F/O]: ")
        if gender in ['M', 'F', 'O', 'm', 'f', 'o']:
            break
        else:
            print("\nError: Enter a valid gender.\n")

    country = input("Enter Country: ")

    data = {
        "username": username,
        "name": name.capitalize(),
        "gender": gender.upper(),
        "country": country.capitalize()
    }

    print("\nPlease Wait ...\n")

    db.child("Users").child(username).set(data)
    print("Success: Information Stored\n")

def retrieve():

    s = int(input("[1] Get information of the user.\n[2] Get All Data.\n-> "))

    if s == 1:
        user = input("\nEnter Username: ")

        users = db.child("Users").order_by_child("username").equal_to(user).get()
         
        t.field_names = ["Name", "Gender", "Country"]
        for user in users:
            name = user.val()['name']
            gender = user.val()['gender']
            country = user.val()['country']
            t.add_rows(
                [
                    [name, gender, country]
                ]
            ) 
        print(t)
        print("\n")
    elif s == 2:
        users = db.child("Users").get()
        t.field_names = ["Username","Name", "Gender", "Country"]
        for user in users.each():     
            username = user.val()['username']
            name = user.val()['name']
            gender = user.val()['gender']
            country = user.val()['country']     
            t.add_rows(
               [
                   [username,name, gender, country]
               ]
            )
        print(t)
        print("\n")

def update():
    s = input("Enter username: ")

    m = int(input("[1] Update Name\n[2] Update Gender\n[3] Update Country\n-> "))

    if m == 1:
        n = input("Enter New Name: ")
        try:
            db.child("Users").child(s).update({"name": n.capitalize()})
            print("Success: Name updated")
        except:
            print("Error: Unable to update the name")
    elif m == 2:
        n = input("Enter New Gender [M/F/O]: ")
        try:
            db.child("Users").child(s).update({"gender": n.upper()})
            print("Success: Gender updated")
        except:
            print("Error: Unable to update gender")
    elif m == 3:
        n = input("Enter New Country: ")
        try:
            db.child("Users").child(s).update({"country": n.capitalize()})
            print("Success: Country updated")
        except:
            print("Error: Unable to update the countryui hjvb ")

def delete():
    s = input("Enter username: ")

    db.child("Users").child(s).remove()
    print(s + " is removed from the database.")

menu()
s = input("Select Option -> ")

if s in ['c', 'C', '1']:
    print("\n::::: STORE INFORMATION :::::")
    create()    
    while True:
        a = input("Add More? (Y/N) -> ")
        if a == 'y' or a == 'Y':
            create()
        else:
            break
elif s in ['r', 'R', '2']:
    print("\n::::: PRINT INFORMATION :::::")
    retrieve()

elif s in ['u', 'U', '3']:
    print("\n::::: UPDATE INFORMATION :::::")
    update()
        
elif s in ['d', 'D', '4']:
    print("\n::::: DELETE INFORMATION :::::")
    delete()

elif s in ['e', 'E', '5']:
    print("\nBye...\n")
else:
    print("\nInvalid Choice!")