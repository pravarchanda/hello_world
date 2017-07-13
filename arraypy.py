from pprint import pprint
#When a government employee bride and a businessman groom called off their wedding over their opposing views on Prime Minister Narendra Modi.
line = "When a government employee bride and a businessman groom called off their wedding over their opposing views on Prime Minister Narendra Modi."
n = 15
for i in range(0, len(line), n):
	#print line.strip()[:15]
	#print line.strip()[15:]
	chk = line.strip()[:n]
	val = line.strip()[n:]
	newt = chk + val.split(' ',1)[0]
	print newt
	#print "###########################"
	try : 
		val.split(' ',1)[1]
	 	line = val.split(' ',1)[1]
	except:
	 	break