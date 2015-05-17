password = "password"
for i in range(3):
    j = 2
    pwd = input("Enter the password: ")
    if (pwd==password):
        print("Correct, please come in")
        break
    else: 
        print("Oh no, that\'s incorrect, please try again.  You have ",j-i, "attempts left.")
        continue
