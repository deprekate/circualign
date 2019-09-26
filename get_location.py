import sys

for line in sys.stdin:
	fields = line.split()
	if fields[8] < fields[9]:
		if fields[6] < fields[7]: 
			sys.stdout.write(fields[0])
			sys.stdout.write("\t")
			sys.stdout.write(fields[6])
			sys.stdout.write("\n")
		else:
			sys.stdout.write(fields[0])
			sys.stdout.write("\t")
			sys.stdout.write("-")
			sys.stdout.write(fields[6])
			sys.stdout.write("\n")
	else:
		sys.stdout.write(fields[0])
		sys.stdout.write("\t")
		sys.stdout.write("-")
		sys.stdout.write(fields[7])
		sys.stdout.write("\n")
