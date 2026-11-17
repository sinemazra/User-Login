print("""
*********************************

            USER LOGIN      
        
*********************************
""")

sys_username = "sinem_azra"
sys_password = "password123"

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == sys_username and password != sys_password:
    print("Error: Incorrect Password")

elif username != sys_username and password == sys_password:
    print("Error: Invalid Username")

elif username != sys_username and password != sys_password:
    print("Error: Invalid Username and Password")

else:
    print("Login Successful")
