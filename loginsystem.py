import re
def home_page():

    print("Welcome, if you are new user please register or Login")
    option = input("register-R | login-L | forgot password-F : ")

    if option == 'R':
        return registration()
    elif option == 'L':
        return login()
    elif option == 'F':
        return forgot_password()
    elif len(option)<1:
        print("select an option !!!")
        home_page()
    else:
        print("select a valid option !!! ")
        home_page()

def registration():
    db = open("C:\\Users\\aswin\\Desktop\\register.txt", "r")
    pattern = "^\D[a-zA-Z0-9]+@[a-zA-z]+\.(com|in)$"
    password_pattern = "^.*(?=.{6,15})(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_';:<>?/]).*$"

    email_id = input("enter your email_id : ")
    password = input("enter your password : ")
    list_U = []
    list_P = []

    for i in db:
        U, P = i.split(", ")
        P = P.strip()
        list_U.append(U)
        list_P.append(P)
    data = dict(zip(list_U, list_P))

    res_email = re.search(pattern, email_id)
    res_pass = re.search(password_pattern, password)

    if len(email_id)<1  or len(password)<1 :
        print("email_id or password is invalid")
        print("please enter the valid credentials to register")
        registration()

    elif email_id in list_U:
            print("username already exists")
            print("register or login to continue")
            home_page()

    elif (res_email) and (res_pass):
        db = open("C:\\Users\\aswin\\Desktop\\register.txt", "a")
        db.write(email_id + ", " + password + "\n")
        db.close()
        print("registration successful ! ")
        print("login to continue")
        login()
    else:
        print("invalid username or password")
        print("please enter valid credentials")
        registration()

def login():

    db = open("C:\\Users\\aswin\\Desktop\\register.txt", "r")
    pattern = "^\D[a-zA-Z0-9]+@[a-zA-z]+\.(com|in)$"
    password_pattern = "^.*(?=.{6,15})(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_';:<>?/]).*$"
    email_id = input("enter your email_id : ")
    password = input("enter your password : ")

    if not len(email_id or password)<1:
        list_U = []
        list_P = []

        for i in db:
            U, P = i.split(", ")
            P = P.strip()
            list_U.append(U)
            list_P.append(P)
        data = dict(zip(list_U, list_P))

        if email_id in list_U:
            if password == data[email_id]:
                print("Login success !! ")
                print("Welcome, ",email_id)
                db.close()
            else:
                print("email_id or password incorrect")
                login()
        else:
            print("user doesn't exits!")
            print("try registering")
            registration()
    else:
        print("invalid email_id or password")

def forgot_password():
    db = open("C:\\Users\\aswin\\Desktop\\register.txt", "r")
    pattern = "^\D[a-zA-Z0-9]+@[a-zA-z]+\.(com|in)$"
    email_id=input("enter your email_id : ")

    list_U = []
    list_P = []
    for i in db:
        U, P = i.split(", ")
        P = P.strip()
        list_U.append(U)
        list_P.append(P)
    data = dict(zip(list_U, list_P))

    if email_id in list_U:
        print("here is your password : ")
        print(data[email_id])
    elif email_id not in list_U:
        print("user doesn't exists")
        print("please register before trying")
        registration()
    else:
        print("invalid email_id : ")

home_page()
