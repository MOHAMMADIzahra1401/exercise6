import random
pc_number=random.randint(0,20)
count=1
for i in range(10):
    
    user_number=int(input("Enter a number:"))

    if user_number<20 and user_number<0:
        print("Enter a number in range 0 ta 20")

    elif user_number==pc_number :
        print("you have won")
        print("tedad hads to hast :",count)
        break

    elif user_number<pc_number :
        print("adad bozorgtari entekhab kon")
        
    elif user_number>pc_number :
        print("adad kochaktari entekhab kon")
    count+=1