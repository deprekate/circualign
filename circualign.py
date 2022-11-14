import os
import sys
import csv

old_chars = "ACGTacgt"
replace_chars = "TGCAtgca"

if len(sys.argv) < 3:
	raise ValueError("usage: python circulaline.py FOLDER LOCATION_FILE")

folder_path = sys.argv[1]
nucleotide_dict = dict()

for filename in os.listdir(folder_path):
	if filename.endswith(tuple(['fasta', 'fna'])):
		nucleotides = ''
		with open(os.path.join(folder_path, filename)) as file_contents:
			for line in file_contents:
				if line.startswith('>'):
					header = line[1:].rstrip()
				else:
					nucleotides += line.rstrip()
		nucleotide_dict[header] = nucleotides

reader = csv.reader(open(sys.argv[2], 'r'), delimiter='\t')
coords = {}
for row in reader:
	k, v = row
	coords[k] = int(v)

for name in nucleotide_dict:
	start = coords[name] #.get(name, 0)
	nucleotides = nucleotide_dict[name]
	if start < 0:
		tab = str.maketrans(old_chars,replace_chars)
		nucleotides = nucleotides.translate(tab)[::-1]
		start += 1
	print(">", name, sep="")
	print(nucleotides[start:] + nucleotides[:start])

