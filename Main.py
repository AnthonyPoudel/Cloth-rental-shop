# importing function
import Functions
Functions.welcome()
continue_loop=True
while continue_loop:
    Functions.option()
    
    try:
     option = int(input("Please! Enter Your Option"))
    except:
        print("Option You Have Entered Is Invalied! Please Enter The Correct One")
        continue
    if option == 1:
       
    #    calling function custome_rent for renting costume
        Functions.custome_rent()

    elif option == 2:
        Functions.costume_return()
        # calling function costume_return for returning costume
        
    elif option == 3:
        
        continue_loop = False
        print("Successfully Exited!!!")
    #    Above message will be displayed is option 3 is entered
    else:
        print("ID You Have Entered Is Invalid")
        continue