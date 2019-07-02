#		Byte Adder created as part of a coursework for university. 
#		AUTHOR: JAMES LEGGE - https://github.com/HydroZA/


print ("Welcome to the Byte Calculator!\n")

# define if INT convert to BIN
def intToBin(x, bits):
	x = int(x)
	binary = bin(x)[2:].zfill(bits)[0:bits]
	return binary

# define if BIN convert to INT to check if larger than 255
def binToInt(y):
	dec = int(y, 2)
	return dec

#   define get input
def getInput():     #Returns an array of the inputs and the type
	inputType = input ("Do you want to enter INT or BIN? ")

	if(inputType.upper() != "INT" and inputType.upper() != "BIN"):
		return ("ERROR:	Your input type is invalid. Try again")
		getInput()

	inputA = input ("Enter the first byte or integer ")
	inputB = input ("Enter the second byte or integer ")

	return inputA, inputB, inputType

# Function to check if the input is a number and not a letter
def checkNum(num):
	isNumber = False
	try:
		num = int(num)
		isNumber = True
		return isNumber
	except ValueError:
		isNumber = False
		return isNumber

#   define method check input is valid
def checkInputValid(inputA, inputB, inputType):
	AValid = False
	BValid = False
	ANeg = False
	BNeg = False
	lenAValid = False
	lenBValid = False
	sizeAValid = False
	sizeBValid = False
	inputType = inputType.upper()
	
	if (inputType == "BIN"):
		#   ============================================= FIRST INPUT VALIDITY CHECK FOR BINARY =============================================
		#Length Checks
		if (len(inputA) > 8):
			# Input is too long
			lenAValid = False

		elif (len(inputA) < 8):
			# Input is too short
			lenAValid = False

		elif (len(inputA) == 8):
			lenAValid = True

		#Size Checks
		#Convert BIN to INT and check size
		tempA = binToInt(inputA)
		if (tempA > 127):
			# Input is too large
			sizeAValid = False

		elif(tempA < 0):
			#Binary can not be negative
			sizeAValid = False

		elif(tempA < 127 and tempA > 0):
			# Input is valid and postive
			sizeAValid = True

		#Final validity confirmation for input A (Size and length)
		if(lenAValid == True and sizeAValid == True):
			AValid = True
		else:
			AValid = False

		#   =============================================SECOND INPUT VALIDITY CHECK FOR BINARY =============================================
		#Length Checks
		if (len(inputB) > 8):
			# Input is too long
			lenBValid = False

		elif (len(inputB) < 8):
			# Input is too short
			lenBValid = False
	

		elif (len(inputB) == 8):
			lenBValid = True

		#Size checks
		#Convert BIN to INT
		tempB = binToInt(inputB)
		if (tempB > 127):
			# Input is too large
			sizeBValid = False

		elif(tempB < 0):
			sizeBValid = False

		elif(tempB < 127 and tempB > 0):
			# Input is valid and postive
			sizeBValid = True

		#Final validity confirmation for input B (Size and length)
		if(lenBValid == True and sizeBValid == True):
			BValid = True
		else:
			BValid = False

	elif (inputType == "INT"):
		#   ============================================= FIRST INPUT VALIDITY CHECK FOR INT =============================================
			#quickly check if input is a valid number
			if (checkNum(inputA) == True):
				intInputA = int(inputA)

				# Size checks
				if (intInputA > 127):
					# Input is too large
					AValid = False

				elif(intInputA < 0):
					# Input is negative THROW TO NEGATIVE HANDLER
					ANeg = True
					AValid = True

				elif(intInputA < 127 and intInputA > 0):
					# Input is valid and postive
					AValid = True
			else:
				# Program exits with error when user enters anything other than an integer
				BValid = False
		#  ============================================= SECOND INPUT VALIDITY CHECK FOR INT =============================================
			if (checkNum(inputB) == True):
				intInputB = int(inputB)
				if (intInputB > 127):
					# Input is too large
					BValid = False

				elif(intInputB < 0):
					# Input is negative THROW TO NEGATIVE HANDLER
					BValid = True
					BNeg = True
					
				elif(intInputB < 127 and intInputB > 0):
					# Input is valid and postive
					BValid = True
			else:
				# Program exits with error when user enters anything other than an integer
				BValid = False
		# ============================================= END OF INPUT CHECKS =============================================

	return AValid, BValid, ANeg, BNeg


#   define XOR gate
def XORGate(a, b):
	a = int(a)
	b = int(b)
	res = 0

	if (a == 0 and b == 0):
		res = 0
		return res
	elif (a == 0 and b == 1):
		res = 1
		return res
	elif (a == 1 and b == 0):
		res = 1
		return res
	elif (a == 1 and b == 1):
		res = 0
		return res

#   define AND gate
def ANDGate (a, b):
	a = int(a)
	b = int(b)
	res = 0
	if (a == 0 and b == 0):
		res = 0
		return res
	elif (a == 0 and b == 1):
		res = 0
		return res
	elif (a == 1 and b == 0):
		res = 0
		return res
	elif (a == 1 and b == 1):
		res = 1
		return res

# Define OR gate
def ORGate (a, b):
	res = 0
	if (a == 0 and b == 0):
		res = 0
		return res
	elif (a == 0 and b == 1):
		res = 1
		return res
	elif (a == 1 and b == 0):
		res = 1
		return res
	elif (a == 1 and b == 1):
		res = 1
		return res

# Define NOT gate 
def NOTGate (a):
	b = int(a)
	res = 0
	if (b == 1):
		res = 0
		return res
	elif(b == 0):
		res = 1
		return res

def addition(a, b):
	# Reverse input bin
	binrevA = ""
	for q in reversed(a):
		binrevA += q

	binrevB = ""
	for c in reversed(b):
		binrevB += c

	finalAns = ""
	# Half adder
	xorinit = XORGate(binrevA[0], binrevB[0])
	cout = ANDGate(binrevA[0], binrevB[0])
	finalAns += str(xorinit)
	
	# Full adder
	for g in range (7):
		xor1 = XORGate(binrevA[g+1], binrevB[g+1])
		xor2 = XORGate(xor1, cout)
		finalAns += str(xor2)
		and1 = ANDGate(xor1, cout)
		and2 = ANDGate(binrevA[g+1], binrevB[g+1])
		or1 = ORGate(and1, and2)
		cout = or1

	addAns =""
	for q in reversed(finalAns):
		addAns += q
	return addAns

def subtract (a, b):
	finalSubAns = ""
	# a and b are expected to be 8 bit binary strings therefore conversion is needed BEFORE feeding to subtract function
	# Reverse input 
	revA = ""
	for q in reversed(a):
		revA += q

	revB = ""
	for c in reversed(b):
		revB += c

	# START OF HALF SUBTRACTOR
	# we need to first isolate the first bit of each string and use a half subtractor on them

	# diff = first 2 bits subtracted
	diff = XORGate(a[0], b[0])
	# now be need to get the borrow (basically the Carry from the adder)
	# a put through a NOT gate
	not1 = NOTGate(a[0])
	# not1 AND b
	borrow = ANDGate(not1, b[0])
	finalSubAns += str(diff)
	# END OF HALF SUBTRACTOR

	# START OF FULL SUBTRACTOR
	for i in range(7):
		# Difference
		xor1 = XORGate(revA[i+1], revB[i+1])
		ans = XORGate(borrow, xor1)
		finalSubAns += str(ans)

		# Borrow
		not2 = NOTGate(revA[i+1])
		and1 = ANDGate(not2, revB[i+1])
		not3 = NOTGate(xor1)
		and2 = ANDGate(not3, borrow)
		borrow = ORGate(and1, and2)
	# END OF FULL SUBTRACTOR

	# Reverse answer back to correct form and return answer
	subAns = ""
	for g in reversed(finalSubAns):
		subAns += g

	return subAns

def multiplication(a, b):
	mulAns = "00000000"
	tempAns = ""
	intAns = 0
	loops = (binToInt(b))

	for i in range (loops):
			tempAns = addition(a, a)
			mulAns = addition(tempAns, mulAns)

	return mulAns

#   Main loop
def mainLoop():
	proceed = False
	exit = ""
	while (exit.upper() != "EXT"):
		# START GET INPUT
		inputs = getInput()
		inputA = inputs[0]
		inputB = inputs[1]
		inputType = inputs[2]

		if (inputType.upper() == "INT" or inputType.upper() == "BIN"):
			# Check the inputs are valid
			validity = checkInputValid(*inputs)
			AValid = validity[0]
			BValid = validity[1]
			ANeg = validity[2]
			BNeg = validity[3]

			# Start validity checks
			print("\n**************************VALIDITY SUMMARY**************************")
			print("First input valid? " + (str(AValid)))				
			print("Second input valid? " + (str(BValid)))
			print("Is the first input negative? " + (str(ANeg)))
			print("Is the second input negative? " + (str(BNeg)))
			print("***********************END OF VALIDITY SUMMARY***********************")


			if (AValid == True and BValid == True):
				proceed = True

			if (proceed == True and ANeg == False and BNeg == False):
				if (inputType.upper() == "INT"):
					print("\n************INPUT SUMMARY**********")
					print("First Input: " + inputA)
					print("First input in binary: " + intToBin(inputA, 8))
					print("Second Input: " + inputB)
					print("Second input as binary: " + intToBin(inputB, 8))
					print("Type of Inputs: " + inputType.upper())
					print("*******END OF INPUT SUMMARY******")

				elif(inputType.upper() == "BIN"):
					print("\n************INPUT SUMMARY**********")
					print("First Input: " + inputA)
					print("First input as an integer: " + str(binToInt(inputA)))
					print("Second Input: " + inputB)
					print("Second input as an integer: " + str(binToInt(inputB)))
					print("Type of Inputs: " + inputType.upper())
					print("*********END OF INPUT SUMMARY**********")
				# END GET INPUT
				# END VALIDITY CHECKS
				operator = input("\nWhat operation would you like to perform on these numbers?\nAddition = ADD\t\tSubtraction = SUB\tMultiplication = MUL\n")
				if (operator.upper() == "ADD"):
					# BYTE ADDITION STARTS HERE
					# If input is integer convert to binary
					if (inputType.upper() == "INT"):
						binInputA = intToBin(inputA, 8)
						binInputB = intToBin(inputB, 8)
					
						finalAns = addition(binInputA, binInputB)

						print ("\n************************************")
						print ("THE FINAL ANSWER: " + inputA + " + " + inputB + " = " + str(binToInt(finalAns)))
						print ("************************************\n")

					elif (inputType.upper() == "BIN"):
						#Do the math with binary
						finalAns = addition(inputA, inputB)

						# Print ans
						print ("\n************************************")
						print ("THE FINAL ANSWER: " + inputA + " + " + inputB + " = " + finalAns)
						print ("INTEGER FORM: " + str(binToInt(inputA)) + " + " + str(binToInt(inputB)) + " = " + str(binToInt(finalAns)))
						print ("************************************\n")

				elif (operator.upper() == "SUB"):
					if (inputType.upper() == "INT"):
						# Conver the integers to binary
						binInputA = intToBin(inputA, 8)
						binInputB = intToBin(inputB, 8)

						# Do the math
						subAns = subtract(binInputA, binInputB)

						# Print the answer
						print ("\n************************************")
						print ("THE FINAL ANSWER: " + inputA + " - " + inputB + " = " + str(binToInt(subAns)))
						print ("************************************\n")

					elif(inputType.upper() == "BIN"):
						subAns = subtract(inputA, inputB)

						print ("\n************************************")
						print ("THE FINAL ANSWER: " + inputA + " - " + inputB + " = " + str(binToInt(subAns)))
						print ("************************************\n")
				
				elif(operator.upper() == "MUL"):
					if(inputType.upper() == "INT"):
						binInputA = intToBin(inputA, 8)
						binInputB = intToBin(inputB, 8)

						mulAns = multiplication(binInputA, binInputB)

						print ("\n************************************")
						print ("THE FINAL ANSWER: " + inputA + " x " + inputB + " = " + str(binToInt(mulAns)/2))
						print ("************************************\n")

					elif(inputType.upper() == "BIN"):
						mulAnsTemp = multiplication(inputA, inputB)
						mulAns = (binToInt(mulAnsTemp)/2)
						print ("\n************************************")
						print ("THE FINAL ANSWER: " + inputA + " x " + inputB + " = " + str(mulAns))
						print ("THE FINAL ANSWER IN BINARY: " + inputA + " x " + inputB + " = " + intToBin(mulAns, 8))
						print ("************************************\n")
				else:
					print ("Operator Selection Invalid")
			# Throw errors when the user doesnt enter valid inputs 
			elif (proceed == False):
				if (AValid == False and BValid == True):
					print ("ERROR:	There was a problem with your first entry. You entered: " + inputA)
				elif (AValid == True and BValid == False):
					print ("ERROR:	There was a problem with your second entry. You entered: " + inputB)
				elif(AValid == False and BValid == False):
					print ("ERROR:	There was a problem with both of your inputs. You entered " + inputA + " and " + inputB)
		else:
			print ("Error with your input type. Try again")

		exit = input("Enter any key to try again or type EXT to exit the program ")  

mainLoop()