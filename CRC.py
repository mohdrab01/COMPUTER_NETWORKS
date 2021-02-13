
##################################################################################################
### CRC CODE GENERATION - SENDER SIDE ###
##################################################################################################

print("##################################################################################################")
print("                                CRC CODE GENERATION - SENDER SIDE ")
print("##################################################################################################")

def Xor(a,b):
	res = []
	for i in range(1,len(b)):
		if a[i]==b[i]:
			res.append('0')
		else:
			res.append('1')

	return ''.join(res)

def CRC_codeGeneration(D,d):
	# D = Dividend and d = Divisor
	print('Dividend: ',D,'\nDivisor: ',d)
	n = len(d)
	t = D[0:n] 
	while n < len(D):
		if t[0] == '1':
			t = Xor(d,t) + D[n]
		else:
			t = Xor('0'*(n), t) + D[n]
		n+=1 

	if t[0] == '1':
		t = Xor(d,t)
	else:
		t = Xor('0'*n,t)

	word = t 
	return word

def encodeFrame(nf,ng,frame,gen):
	code = frame + '0'*(ng-1)
	CRC_code = CRC_codeGeneration(code, gen)
	print("CRC Code generated (remainder): ",CRC_code)
	newcode = frame + CRC_code 
	return newcode


nf = int(input("Enter Frame size: "))
frame = input("Enter Frame: ")
ng = int(input("Enter CRC Generator size: "))
gen = input("Enter CRC Generator: ")


msg2send = encodeFrame(nf,ng,frame,gen)
print("The New Generated CRC Sending Code: ",msg2send)



##################################################################################################
### CRC CODE CHECKING - RECIEVER SIDE ###
##################################################################################################

print("##################################################################################################")
print("                                CRC CODE CHECKING - RECIEVER SIDE ")
print("##################################################################################################")

# Here we get the message from sender, we have to check if its error free 
def checkCRC(CRC_code):
	for bit in CRC_code:
		if bit == '1':
			return 0
	return 1


def decodeFrame(frame,gen):
	n = len(gen)
	m = len(frame)
	newcode = frame[:m-n]
	return newcode

msgrecieved = msg2send
print("The Recieved Code: ",msgrecieved)

CRC_code = CRC_codeGeneration(msgrecieved,gen)
print("CRC_code generated at Reciever end: ",CRC_code)
if checkCRC(CRC_code)==0:
	print("Some ERROR Occured while Tranmission!")
else:
	print("No ERROR Detected!")
	print("Actual Code Recieved was: ",decodeFrame(msgrecieved,CRC_code))
