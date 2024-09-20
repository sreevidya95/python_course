import time
n= int(time.strftime("%H"))
if (n<12) :
    print("Good Morning")
elif(n>=12 and n<16):
    print("Good Afternoon")
elif(n>=16 and n<=18):
    print("Good Evening")
else:
    print("Good Night")