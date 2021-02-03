
##################################################################################################
### CHARACTER STREAM TO FRAMES ###
##################################################################################################
print("##################################################################################################")
print("                                SENDER SIDE - CHARACTER COUNT ")
print("##################################################################################################")

stream = input("Enter the character Stream with frame count: ")

### FRAME COUNT ###

frames = []

def countNoOfFrames(s, f):
	if len(s) > 1:
		cnt = 0
		i = 0
		while i < len(s):
			k = i
			cnt += 1
			try:
				i += int(s[i])
				f.append(s[k+1:i])
			except:
				print("Invalid character stream!")
				break
		return cnt
	return -1

def printFrames(f):
	cnt = 0
	for frame in f:
		print("Frame ",cnt+1," : ",frame)
		cnt += 1
	return f

print("No of Frames in character stream: ",countNoOfFrames(stream,frames))
print("Frames : ",printFrames(frames))

##################################################################################################
### FRAMES TO CHARACTER STREAM ###
##################################################################################################

print("##################################################################################################")
print("                                RECEIVER SIDE - CHARACTER COUNT ")
print("##################################################################################################")

n = int(input("Enter no of Frames: "))
frames = list(map(str,input("Enter the Frames (seperated by a space): ").split(" ")))

def convertFramesToStream(f):
	stream = ""

	for frame in frames:
		stream += str(len(frame) + 1)
		stream += frame

	return stream

print("The character stream is : ",convertFramesToStream(frames))

##################################################################################################