import random
import string

#A while loop for the registratiion process  
signup=True
while signup==True:

    print ("HNG Board Signup:.../")
    print ()
    # Accepts users input 
    first_name=input(str("Enter your first name: "))
    last_name=input(str("Enter your last name: "))
    email=input(str("Email address:  "))
    user_info=[first_name, last_name, email]
   #Function to generate randpm string fot the password 
    def random_string( size=5,chars=string.ascii_letters+string.digits):
        return "".join([random.choice(chars) for n in range(size)])
        
    #Generated password from the function random_string defined above 
    genrtd_pwrd =(random_string())
    #New password to be generated 
    pwrd= first_name[0:2] + last_name[-2::] + genrtd_pwrd
    print("Loading..../n Generating your password")
    print (pwrd)

    #A while loop for the password process 
    loop = True
    while loop==True:
        #Confirm if the user prefers the generated passsword or would create their own
        req= input(str("Are you satisfied with the password Y/N: "))
        pwrd_req= req.upper()
        
        #If the user is satisfied then assign user_info to a dictionary 
            # with 1 as the key and the user_info as the value  
        if pwrd_req == "Y":
            user_info.append (pwrd)
            print("password accepted")
            
            loop=False
        #If the user prefers to create a new password, 
        #   user is prompted to enter a new password 
        elif pwrd_req=="N": 
            pwrd= input(str("Enter new password: "))
            #Check the length of the entered password and accept or ask for a new inpput
            if len(pwrd) >=9:
                user_info.append (pwrd)
                print ("Password set succefully")
                loop=False
            else:
                print("Enter a password not less than 9 characters ")
        #If the user enters a different input in the while loop above, user is prompted to try agin 
        else:
            print ("Incorrect input.... Choose Y/N")
    #A function to append the user_info to lgin_data(list)


        def store_login(user_info):
            lgin_data = []
            for item in user_info:
                if item not in lgin_data:
                    lgin_data.append(user_info)
                    return lgin_data
        
        
   

        print (store_login(user_info))

    print("Registration complete!")    
    print("Your login details")
    print("Fullname: " + first_name + " " + last_name, )
    print("Email: "+ email)
    print("Password: " + pwrd)
    #prompt if user wants to register another user account 
    req= input(str("Would you like to register another user?..(Y/N) "))
    req1= req.upper()
    if req1 == "Y":
        print ("Returning to signup page... ")
    else:
        print("Have a good day")
        break
    






