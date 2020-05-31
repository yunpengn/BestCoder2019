import csv
import re

def replace_data(old_file_name, new_file_name):
	f = open(old_file_name, 'r')
	data = f.read()
	new_data = data.replace(',', ' ')
	new_f = open(new_file_name, 'w')
	new_f.write(new_data)

replace_data('data/bank_accounts.csv', 'data/bank_accounts_new.csv')
replace_data('data/credit_cards.csv', 'data/credit_cards_new.csv')
replace_data('data/devices.csv', 'data/devices_new.csv')
replace_data('data/orders.csv', 'data/orders_new.csv')
