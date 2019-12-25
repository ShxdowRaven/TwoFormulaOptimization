import sys
import string

class Colors(object):
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

	RED = "\033[31m"
	GREEN = "\033[32m"
	YELLOW = "\033[33m"
	BLUE = "\033[34m"
	CYAN = "\033[36m"
	CYANL = "\033[96m"

lo1 = 0
lo2 = 0
ltrs1 = []
ltrs2 = []
count = 0
max_dec = 2

if len(sys.argv) - 1 and sys.argv[1] == "-d":
	debug = True
else:
	debug = False

while True:
	f1 = raw_input("Insert first formula (with =): ")
	if "=" not in f1:
		print "Invalid input"
		continue
	break

f1 = f1.replace("pi", "\xE3")
f1, num = f1.split("=")
num = int(num)
for i in range(len(f1)):
	#print f1, i, count, i + count, ",", temp_after_i, ","
	if f1[i + count] in (string.ascii_lowercase + "\xE3") and f1[i + count]:
		#print "Found\t{}\tat {}".format(f1[i + count], i + count)
		if f1[i + count] not in ltrs1:
			ltrs1.append(f1[i + count])
		if i + count != 0:
			#print "Added * to\t{}\tat {}".format(f1, i + count)
			f1 = f1[:i + count] + " * " + f1[i + count:]
			#print "...is now\t{}".format(f1)
			count += 3
f1 = f1.replace("\xE3", "3.14")
ltrs1.sort()
#print f1

while True:
	count = 0
	f2 = raw_input("Insert second formula: ")
	f2 = f2.replace("pi", "\xE3")
	for i in range(len(f2)):
		if f2[i + count] in string.ascii_lowercase + "\xE3" and f2[i + count] not in ltrs2:
			#print "Found\t{}\tat {}".format(f2[i + count], i + count)
			if f2[i + count] not in ltrs2:
				ltrs2.append(f2[i + count])
			if i + count != 0:
				#print "Added * to\t{}\tat {}".format(f2, i + count)
				f2 = f2[:i + count] + " * " + f2[i + count:]
				#print "...is now\t{}".format(f2)
				count += 3
	f2 = f2.replace("\xE3", "3.14")
	ltrs2.sort()
	#print ltrs1, "\t", ltrs2
	if ltrs1 != ltrs2:
		print "Invalid input"
		continue
	break
#print f2

minmax = ""
while True:
	minmax = raw_input("Find maximum or minimum (max / min)?: ").lower()
	if minmax == "max":
		mini = False
		break
	elif minmax == "min":
		mini = True
		break
	else:
		print "Invalid input"

#print "F1: {}\tF2: {}".format(f1, f2)

if mini:
	starting_compVal = compVal = float("inf")
	tPrefix = "Lowest"
else:
	starting_compVal = compVal = float("-inf")
	tPrefix = "Highest"

def compareVals(num1, num2):
	global mini
	if mini:
		return num1 < num2
	else:
		return num1 > num2

#print f1, f2
curr_dec = 1
#print "ltrs1", ltrs1, "\tltrs2", ltrs2
while True:
	mPrefix =  "{:." + str(curr_dec) + "f}"
	for i in range(1, num * 10 ** curr_dec // 2 + 1):
		dec_i = i / float(10) ** curr_dec
		for j in reversed(range(1, num * 10 ** curr_dec // 2 + 1)):
			dec_j = j / float(10) ** curr_dec

			curr_f1 = f1.replace(ltrs1[0], mPrefix.format(dec_i))
			curr_f1 = curr_f1.replace(ltrs1[1], mPrefix.format(dec_j))
			curr_f1_res = round(float(mPrefix.format(eval(curr_f1))), curr_dec)

			curr_f2 = f2.replace(ltrs2[0], mPrefix.format(dec_i))
			curr_f2 = curr_f2.replace(ltrs2[1], mPrefix.format(dec_j))
			curr_f2_res = round(float(mPrefix.format(eval(curr_f2))), curr_dec)
			if debug: print "i = {}\tj = {}\tF1 {} = {}\tF2 {} = {}".format(dec_i, dec_j, curr_f1, curr_f1_res, curr_f2, curr_f2_res)

			if curr_f1_res == num and compareVals(curr_f2_res, compVal):
				compVal = eval(curr_f2)
				lo1 = dec_i
				lo2 = dec_j
				if debug: print "{} = {}".format(f1.replace(ltrs1[0], Colors.CYANL + str(lo1) + Colors.ENDC).replace(ltrs1[1], Colors.CYANL + str(lo2) + Colors.ENDC), compVal)
	#print "{}: (compVal [{}] == starting_compVal [{}])".format(compVal == starting_compVal, compVal, starting_compVal)
	if compVal == starting_compVal:
		#print "{}: (curr_dec [{}] < max_dec [{}])".format(curr_dec < max_dec, curr_dec, max_dec)
		if curr_dec < max_dec:
			curr_dec += 1
			#print "curr_dec = {}".format(curr_dec)
		else:
			break
	else:
		break

if compVal != starting_compVal:
	print "\n{} {} where {} = {}".format(tPrefix, f2, f1, num)
	print "{} = {}".format(f2.replace(ltrs2[0], Colors.CYANL + str(lo1) + Colors.ENDC).replace(ltrs2[1], Colors.CYANL + str(lo2) + Colors.ENDC), compVal)
else:
	print "Impossible"

'''
l**2 * h = 16
2 * l**2 + 4 * l * h
1**2 * 8				17
1**2 + 4 * 1 * 8 		35

2pir = 2
pir**2
'''