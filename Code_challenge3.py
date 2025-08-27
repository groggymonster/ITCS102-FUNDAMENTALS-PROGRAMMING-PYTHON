#username and password 
username ='groggymonk'
Password ='biggpapid'

#get input from user
#from getpass import getpass for hiding password
Input_user= input("Enter Username:")
Input_pass= input("Enter Password:")

#check Credentials 

if Input_user==username and Input_pass == Password:
	print("access granted")
else:
	print("access denied")