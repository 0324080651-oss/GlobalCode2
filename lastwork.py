


users = {
      "user1": "password1",  
      "user2": "password2",
      "user3": "pasword3"       
}


print(users["user1"])

username = input("Enter your username")
password = input("Enter your password")
if username in users and users[username] == password:
    print("login successful")
else:
    print("login failed")