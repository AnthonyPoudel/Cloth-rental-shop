import datetime
file_name="Costume.txt"
# creating a function which welcomes user
def welcome():
    print("""Welcome To Custome Rental Shop""")
# creating a fuction which displays id of the task
def option():
    print("""
    Press ID Of The Task, You Want Us To Perform
    1:For Renting Costume!
    2:For Returning Costume!
    3:For Exiting from here!
    """)
#creating function which show value of costume
def custome_value():
    file=open(file_name,'r')
    list=[]
    id=1
    for i in file:
        oo=i.replace("\n"," ").split(",")
        list.append(oo)
        id=1
    return list
print(custome_value())
# creating a function which displays details of costume
def display():
    Id=1
    print("----------------------------------Details of Costume----------------------------------")
    list = custome_value()
    print(f"{'Id':<25} {'Name':<25} {'Brand':<30} {'Price':<10} {'Quantity':<25}")
    for i in list:
        name, brand, price, quantity=i
        information = "{:<25} {:<25} {:<30} {:<10} {:<25}".format(Id,name,brand,price,quantity)
        price = price.replace("\n","")
        Id=Id+1
        print(information)

# Creating a function which ask user do they want to continue shopping
def ask_again():
    ask=input("Do You Want To Shop More [yes|no]\n""Please!! enter in small letter")
    if ask.isalpha():
        if ask.lower() == "yes":
            option()
        elif ask.lower() == "no":
            print("Generate Invoice")
        
        else:
            print("Invalid Option!!!")
    else:
        print("Please enter option in words [yes or no]")
    #creating a function which is use for extracting current date from the system 
def current_date():
    date=datetime.datetime.now()
    hour=str(date.hour)
    minute=str(date.minute)
    second=str(date.second)
    year=str(date.year)
    month=str(date.month)
    day=str(date.day)
    currentDate= year + "-" + month + "-"+ day+"-"+ hour+"-"+minute+""+second
    return currentDate
# creating a function for rented date
def get_rented_date():
    again = True
    while again == True:
        try:
            get_rented_date=input("Please!! Enter Rented Date| In format [yyyy-mm-dd]:")
            date=datetime.datetime.strptime(get_rented_date,'%Y-%m-%d')
            fdate=str(date)
            a=fdate.split("-")
            extract_date=a[2]
            day=int(extract_date[0:2])
            again=False
        except:
            print("Entered date is invalid!!!|Please enter the correct one in correct format.")
        return day
        # creating a function used for getting return costume date
def rcostume():
    date = datetime.datetime.now()
    rday=int(date.day)
    return rday
# creating a function which lets user to rent costume
def custome_rent():
    list = custome_value()
    T=True
    while T == True:
        c_name=input("Please! Provide us your name:")
        if c_name.isalpha()==True:
            T=False
            n=c_name+".txt"
            o=open(n,"w")
            o.write(current_date())
            o.write("---------------------------------INVOICE GENERATED---------------------------------------\n")
            o.write("=================================Information Of customer=================================\n")
            o.write(f"################################Customer Name: {c_name} ################################\n")
            o.write("*********************************** COSTUME RENTAL SHOP *********************************\n")
            o.write("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^Thank You for choosing us^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
            o.close()
            price=0
            s=True
            while s== True:
                try:
                    display()
                    h= True
                    while h==True:
                        try:
                            c_no=int(input("Please provide the ID of the costume you want to rent"))
                            if c_no<=len(list) and c_no>0:
                                s= False
                                a=True
                                while a == True:
                                    try:
                                        q=int(input("Enter the quantity of the costume you want to rent: "))
                                        for a in range(c_no):
                                            costume_name=list[a][0]
                                            c_b=list[a][1]
                                            c_p=list[a][2]
                                            c_s=int(list[a][3])
                                        price1=int(c_p[1::])
                                        
                                        if q<=c_s and q>0:
                                            after_stock=c_s-q
                                            
                                            for b in range (c_no):
                                                if b==c_no-1:
                                                    list[b][3]=after_stock
                                            
                                            
                                            daraz=open(file_name,"w")
                                            for c in range(len(list)):
                                                daraz.write(str(list[c][0])+","+str(list[c][1])+","+str(list[c][2])+","+str(list[c][3])+"\n")
                                            daraz.close()
                                            print("for 3")
                                            price_after=price1*q*5
                                            price=price+price_after
                                            d=open(n,"a")
                                            d.write(f"\n Costume Name: {c_name}\t Brand: {c_b}\tPrice:{c_p}\tQuantity:{q}\nTotal: ${price_after}")
                                            # d.write("\n\n〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣")
                                            a=False
                                            h=False
                                        else:
                                            print("Stock is not available right now")
                                    except :
                                        
                                        print("Invalid input for the costume")
                            else:
                                print("Costume ID did not matched")
                        except:
                            print("Please enter ID in integer")
                    q= True
                    while q== True:
                        again=input("DO you want to continue shopping [yes|no]").lower()
                        if again =="no":
                            s=False
                            q=False
                            print("Thanks for choosing us for your service")
                        elif again=="yes":
                            q=False
                            s=True
                        else:
                            print("Invalid input!!! Please enter input in yes|no")

                except:
                    print("Please enter valid costume Id")
            z=open(n,"a")
            z.write(f"\n\n Total Price: ${price}")
            z.write("\n\n The price for renting costume for 5 days")

        else:
            print("Plaease!!| Provide a valid name")

    #creating a function which lets user to return costume 
def costume_return():
    list =custome_value()
    T=True
    while T == True:
        c_name=input("Please! Provide us your name:")
        if c_name.isalpha()== True:
            T=False
            n=c_name+".txt"
            d= open(n,"w")
            d.write(current_date())
            d.write("---------------------------------INVOICE GENERATED---------------------------------------\n")
            d.write("=================================Information Of customer=================================\n")
            d.write(f"################################Customer Name: {c_name} ################################\n")
            d.write("*********************************** COSTUME RENTAL SHOP *********************************\n")
            d.write("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^Thank You for choosing us^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
            d.close()
            price=0
            Fine=0
            s=True
            while s== True:
                try:
                    display()
                    h= True
                    while h==True:
                        try:
                            c_no=int(input("Please provide the ID of the costume you want to return"))
                            if c_no<=len(list) and c_no>0:
                                s= False
                                a=True
                                while a == True:
                                    try:
                                        q=int(input("Enter the quantity of the costume you want to return: "))
                                        for a in range(c_no):
                                            costume_name=list[a][0]
                                            c_b=list[a][1]
                                            c_p=list[a][2]
                                            c_s=int(list[a][3])
                                        price1=int(c_p[1::])
                                        
                                        if q>0:
                                            after_stock=c_s+q
                                            
                                            for b in range (c_no):
                                                if b==c_no-1:
                                                    list[b][3]=after_stock

                                            date_loop=True
                                            while date_loop==True:
                                                rent_Date=get_rented_date()
                                                return_Date=rcostume()
                                                if return_Date>rent_Date:
                                                    Rented_Day=int(return_Date-rent_Date)
                                                    date_loop=False
                                                else:
                                                    print ("Entered date is invalid!!")
                                            
                                            if Rented_Day>5:
                                                FINE_DAYS=Rented_Day-5
                                                Fine=FINE_DAYS*5*q
                                                price_after=Rented_Day*price1*q
                                            
                                            else:
                                                price_after=price1*q*Rented_Day

                                            
                                            
                                            daraz=open(file_name,"w")
                                            for c in range(len(list)):
                                                daraz.write(str(list[c][0])+","+str(list[c][1])+","+str(list[c][2])+","+str(list[c][3])+"\n")
                                            daraz.close()
                                            print("for 3")
                                            price=price+price_after
                                            d=open(n,"a")
                                            d.write(f"\n Costume Name: {c_name}\t Brand: {c_b}\tPrice:{c_p}\tQuantity:{q}\nTotal: ${price_after}")
                                            # d.write("\n\n〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣〣")
                                            a=False
                                            h=False
                                        else:
                                            print("Stock is not valid")
                                    except :
                                    
                                        print("Invalid input for the costume")
                            else:
                                print("Costume ID did not matched")#costume no milena
                        except:
                            print("Please enter ID in integer")#string value halo vhaney
                    q= True
                    while q== True:
                        again=input("DO you want to continue shopping [yes|no]").lower()
                        if again =="no":
                            s=False
                            q=False
                            print("Thanks for choosing us for your service")
                        elif again=="yes":
                            q=False
                            s=True
                        else:
                            print("Invalid input!!! Please enter input in yes|no")

                except:
                    print("Please enter valid costume Id")#system error
            z=open(n,"a")
            z.write(f"\n\n Total Price: ${price}")
            z.write(f"\n\n Fine: ${Fine}")
            z.write(f"\n\n Total Price With Fine: ${price+Fine}")
        else:
            print("Plaease!!| Provide a valid name")
   



    
