import json

print("********** WELOCOMEto Login and sign up page *********")
user=input("If you want to Login or sign up :-")
if user=="sign up":
    user_name=input("enter the user name :-")
    password1=input("enter the password :-")
    password2=input("enter the confirm password :-")
    if password1==password2:
        print("Both password are a same")
        if "#" in password1 or "@" in password1 :
            print("password is special charcter")
            if password1==password2:
                description=input("enter the description :- ")
                Birth_date=input("enter the birth date :-")
                Hobbies=input("enter the Hobbies :-")
                Gender=input("enter the gender :-")
                print("congrates",user_name,"your are signed up successfully")
                user_details={user:{"username":user_name,"password":password1},"profilo":{"description":description,"birth_date":Birth_date,"Hobbies":Hobbies,"Gender":Gender}}
                with open("user_details.json","w") as file:
                    data=json.dump(user_details,file,indent=4)
            else:
                print("your password is Incorrect")
        else:
            print("At least password should be contain one special charcter or number")
    else:
        print("Sign up is not succesfully")
elif user=="Login":
    user_name1=input("enter the user name :-")
    password3=input("enter the password :-")
    with open("user_details.json","r") as file:
        data=json.load(file)
        for keys, values in data.items():
            print("\nPerson ID:", keys)
            for key in values:
                print(key + ':', values[key])
        print("congrates",user_name1,"your are Login successfully")
else:
    print("It is not valid")
   
    