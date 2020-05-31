import csv
import re

DATA_FILE_PATH='data/train.csv'
INPUT_FILE_PATH='data/predict.csv'
OUTPUT_FILE_PATH='data/output.csv'

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

# Reads all rows from input.
result_list = []
with open(INPUT_FILE_PATH) as f:
	csv_file = csv.reader(f, delimiter=',', quotechar='"')
	next(csv_file, None)

	# Processes row by row.
	for row in csv_file:
		index = int(row[0])
		name = row[1]

		result = check(name)
		result_str = str(result)
		result_list.append([index, result_str])

# Writes back to output file.
# writing to csv file
with open(OUTPUT_FILE_PATH, 'w') as csv_file:
    # creating a csv writer object
    csv_writer = csv.writer(csv_file)

    # writing the fields
    csv_writer.writerow(['index', 'groups_found'])

    # writing the data rows
    csv_writer.writerows(result_list)
