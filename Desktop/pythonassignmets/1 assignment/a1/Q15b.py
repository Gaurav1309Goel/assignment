a=input("What is your age?")
if(a<5 and a>0):
	print("INFANT")
elif(a>=5 and a<18):
	print("CHILD")
elif(a>=18):
	print("ADULT")
else:
	print("INVALID AGE")
