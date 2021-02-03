
##################################################################################################
### CHARACTER / BYTE STUFFING ###
##################################################################################################

print("##################################################################################################")
print("                                SENDER SIDE - BYTE STUFFING ")
print("##################################################################################################")

def applyByteStuffing(f, e, p, n):
    x = p.replace (e, e*2, n)
    y = x.replace (f, e+f, n)
    return f + y + f

flagbyte = input("Enter Flag character: ")
escapebyte = input("Enter Escape character: ")
payload = input("Enter payload / frame: ")
n = len(payload)

print ( "The frame after Byte Stuffing is :", applyByteStuffing(flagbyte,escapebyte,payload,n))


##################################################################################################
### REVERSING CHARACTER / BYTE STUFFING ###
##################################################################################################

print("##################################################################################################")
print("                                RECEIVER SIDE - BYTE UNSTUFFING ")
print("##################################################################################################")

payload = input("Enter recieved byte stuffed frame: ")
n = len(payload)
flagbyte = input("Enter Flag character: ")
escapebyte = input("Enter Escape character: ")

def revByteStuffing(f, e, p, n):
	x = p [1:n-1]
	y = x.replace (e*2, e, n )
	z = y.replace (e+f , f, n)
	return z

print("The frame after unstuffing the Byte stuffed frame is: ",revByteStuffing(flagbyte,escapebyte,payload,n))

##################################################################################################


