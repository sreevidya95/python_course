temperature = int(input("Enter Temperature"))
raining = True
if temperature >30 or raining == False :
    print("Stay Inside")
elif temperature <30 and raining == True :
    print("stay Inside")
else:
    print("Enjoy outdoors")
