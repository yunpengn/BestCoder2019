import csv

DATA_FILE_PATH='data/train.csv'

# Stores mapping from keyword to group_id.
mapping = {}

# Reads the CSV file.
with open(DATA_FILE_PATH) as f:
	csv_file = csv.reader(f, delimiter=',', quotechar='"')
	next(csv_file, None)

	# Processes line by line.
	for row in csv_file:
		group_id = row[0]
		keywords = row[1]

		# First split by comma.
		for part in keywords.split(','):
			# Strip first.
			cano = part.strip()

			# Then split by white space.
			for mini_part in cano.split(' '):
				# Removes empty ones.
				cano2 = mini_part.strip().lower()
				if cano2 == '':
					continue

				# Adds to mapping.
				if cano2 not in mapping:
					mapping[cano2] = set()
				mapping[cano2].add(group_id)

	# Prints to ack completeness.
	print("Finished loading data")

# Checks the product name.
def check(name):
	print("Predict for: " + name)
