import sys

if len(sys.argv) - 1 and sys.argv[1] == "-d":
	debug = True
else:
	debug = False

ap = raw_input("Area or perimeter (a / p): ")

while True:
	num = raw_input("Insert a number: ")
	try:
		num = int(num)
		break
	except TypeError:
		print "Invalid input ({})".format(num)

if not debug and raw_input("Find maximum or minimum (max / min)?: ").lower() == "max":
	mini = False
else:
	mini = True

if not debug and mini:
	compVal = float("inf")
	prefix = "Lowest"
else:
	compVal = float("-inf")
	prefix = "Highest"

lo1 = 0
lo2 = 0

def compareVals(num1, num2):
	global mini
	if mini:
		return num1 < num2
	else:
		return num1 > num2


if ap.lower() == "a":
	print "\n{} Perimeter (A = {}):".format(prefix, num)
	for i in range(1, num // 2 + 1):
		if not num % i:
			if debug: print "{} * {} = {} (P = {})".format(i, num / i, i * (num / i), 2 * i + 2 * (num / i))
			if compareVals(2 * i + 2 * (num / i), compVal):
				compVal = 2 * i + 2 * (num / i)
				lo1 = i
				lo2 = num / i
	if not debug: print "2({}) + 2({}) = {}".format(lo1, lo2, compVal)
elif ap.lower() == "p":
	print "\n{} Area (P = {}):".format(prefix, num)
	for i in range(1, num // 2 + 1):
		for j in reversed(range(1, num // 2 + 1)):
			if not j % i and 2 * i + 2 * j == num:
				if debug: print "2({}) + 2({}) = {} (A = {})".format(i, j, 2 * i + 2 * j, i * j)
				if compareVals(i * j, compVal):
					compVal = i * j
					lo1 = i
					lo2 = j
	if not debug: print "{} * {} = {}".format(lo1, lo2, compVal)
else:
	print "Invalid input ({})".format(num)