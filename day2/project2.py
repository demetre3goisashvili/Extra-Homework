#პირველი დავალება


for i in range(1, 101):
    if i % 2 == 0:
        print("ლუწი")
        print(i)
    elif i % 2 == 1:
        print("კენტი")
        print(i)

#მეორე დავალება

while True:
    print("Selection")
    print("Type 1 to sign up")
    print("Type 2 to log in")
    print("Type 3 to exit the page")


    Selection = int(input("Please select the operation 1, 2 or 3: "))

    if Selection == 1:
        print("Sign up")
        password = input("Please create a password: ")
        email = input("Please enter your email: ")
        print("Congratulations you have registered")
        break


    elif Selection == 2:
      password1 = "demetredeme"
    user_password = input("Please enter your password: ")
    if user_password == password1:
        print("Succesfull login")
        break
    else:
        print("Incorrect try again")
        retype = input("Please retype your password: ")
        if retype == password1:
            print("Succesfull log in")

    if Selection == 3:
        print("Bye Bye Get Mogged")

         
    
                              

    

              

              
          
         
     


    
       

        

    


    

   

    






    
