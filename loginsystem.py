import ast
import hashlib

isLogin = False
user = None


def login():
    print("You want to login")
    try:
        with open("database.txt", "r") as f:
            username = input("Enter a username: ")
            r = f.read()
            if r != "":
                database = ast.literal_eval(r)
                used = False
                for i in database:
                    if database[i]["username"] == username:
                        used = True
                        userid = i
                        break
                if used:
                    password1 = "one"
                    password2 = "two"
                    while password1 != password2:
                        passinp = input("Enter a password: ")
                        password1 = hashlib.sha256(str(passinp).encode("utf-8")).hexdigest()
                        password2 = database[userid]["password"]
                        if password1 != password2:
                            print("Password not correct!")
                        elif password1 == password2:
                            print("You logged in")
                            global isLogin
                            isLogin = True
                            global user
                            user = database[userid]

            else:
                print("No user found!")
                register()
    except FileNotFoundError:
        print("No user found! You have to register first.")


def register():
    print("You want to register")
    try:
        with open("database.txt", "r") as f:
            username = input("Enter a username: ")
            r = f.read()
            if r != "":
                database = ast.literal_eval(r)
                used = False
                for i in database:
                    if database[i]["username"] == username:
                        print("Username already in use")
                        used = True
                        break
                if not used:
                    passinp = "one"
                    password2 = "two"
                    while passinp != password2:
                        passinp = input("Enter a password: ")
                        password2 = input("Enter password again: ")
                        if passinp != password2:
                            print("Passwords must be identical!")
                    password1 = hashlib.sha256(str(passinp).encode("utf-8")).hexdigest()
                    with open("database.txt", "w") as fa:
                        nextid = len(database) + 1
                        database[nextid] = {"username": username, "password": password1}
                        fa.write(str(database))
                        print("Register complete. You are User number", nextid)
    except FileNotFoundError:
        print("You are the first User!")
        username = input("Enter a username: ")
        database = {}
        passinp = "one"
        password2 = "two"
        while passinp != password2:
            passinp = input("Enter a password: ")
            password2 = input("Enter password again: ")
            if passinp != password2:
                print("Passwords must be identical!")
        password1 = hashlib.sha256(str(passinp).encode("utf-8")).hexdigest()
        with open("database.txt", "w") as fa:
            nextid = len(database) + 1
            database[nextid] = {"username": username, "password": password1}
            fa.write(str(database))
            print("Register complete. You are User number", nextid)


def menu(isLogin, user=None):
    if not isLogin:
        print("Press 1 to login\nPress 2 to register")
        m = int(input("Choose a number: "))
        if m == 1:
            login()
        elif m == 2:
            register()
        else:
            print("Invalid number")
    elif user:
        print("This is the menu for", user.get("username"))
    else:
        print("Something went wrong")


def welcome(isLogin, user=None):
    if user is None:
        user = {"username": "Guest"}
    print("Welcome", user.get("username"), "!")
    if not isLogin:
        print("Please login or register to continue.")
    menu(isLogin, user)


if __name__ == '__main__':
    running = True
    while running:
        welcome(isLogin, user)
