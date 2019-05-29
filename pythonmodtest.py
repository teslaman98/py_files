some = 0

def adding_report(text):
	global some
	while some == 0:
		if text.isdigit():
			#add to total
			if report == A:
				print ("report is diget and a")
			if report != A:
				print ("Return this to start loop")
		if text.startswith("q"):
			report = input("(A)ll or just (T)otal")
			if report == A:
				print ("report is a")
				#print (items & total)
				some += 1
			else:
				print ("Total")
				#print total
				some += 1
		else:
			print ("Invalid Input")
			#loop back to while

print adding_report(input("enter a diget or q"))