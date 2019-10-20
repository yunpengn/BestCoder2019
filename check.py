import csv
import re

DATA_FILE_PATH='data/train.csv'

# Stores mapping from keyword to group_id.
mapping = {}

def remove_bad_char(str):
	return re.sub(r'[^0-9a-zA-Z]', "", str)

# Reads the CSV file.
with open(DATA_FILE_PATH) as f:
	csv_file = csv.reader(f, delimiter=',', quotechar='"')
	next(csv_file, None)

	# Processes line by line.
	for row in csv_file:
		group_id = int(row[0])
		keywords = row[1]

		# First split by comma.
		for part in keywords.split(','):
			# Strip first.
			cano = part.strip()
			if cano == '':
				continue

			# Then split by white space.
			for mini_part in cano.split(' '):
				# Removes empty ones.
				cano2 = remove_bad_char(mini_part.strip().lower())
				if cano2 == '':
					continue

				# Adds to mapping.
				if cano2 not in mapping:
					mapping[cano2] = set()
				mapping[cano2].add(group_id)

# Checks the product name.
def check(name):
	# Splits into unit of words.
	result = set()
	for word in name.split(' '):
		cano = remove_bad_char(word.strip().lower())
		if cano == '':
			continue

		# Adds the mapping if exist.
		if cano in mapping:
			for group_id in mapping[cano]:
				result.add(group_id)

	return list(result)
