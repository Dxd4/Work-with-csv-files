import csv

with open("Names_and_phones.csv", newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	file = list(spamreader)
	index = int(input(f'Write number of column: {", ".join(file[0])}'))-1
	with open("output.txt", "w") as output:
		for row in file:
			print(row[index])
			temp = f" {(row[index])}"
			output.write(row[index]+"\n")
