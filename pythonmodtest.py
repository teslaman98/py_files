some = 0

def adding_report(text):
	global some
	while some == 0:
		if str(text).isdigit():
			print ("test")
			#add to total
			if report == A:
				print ("report is diget and a")
			if report != A:
				print ("Return this to start loop")
		elif text.startswith("q"):
			report = input("(A)ll or just (T)otal")
			if report == "A":
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

repla = adding_report(input("enter a diget or q: "))

print (repla)

#$ wget https://download.jetbrains.com/python/pycharm-community-2017.3.2.tar.gz