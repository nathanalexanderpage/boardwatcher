import csv
import os

import psycopg2 as db
from dotenv import load_dotenv, find_dotenv

colors = {}

company_roles = list()
with open('company_roles.tsv', newline='') as csv_company_roles:
	company_roles_reader = csv.reader(csv_company_roles, delimiter='\t')
	row_no = 0
	columns = []
	for row in company_roles_reader:
		if row_no == 0:
			for column in row:
				columns.append(column)
		else:
			row_data = {}
			column_no = 0
			for cell in row:
				current_column = columns[column_no]
				if cell != '':
					row_data[current_column] = cell
				else:
					row_data[current_column] = None
				column_no += 1
			company_roles.append(row_data)
		row_no += 1

companies = list()
with open('companies.tsv', newline='') as csv_companies:
	companies_reader = csv.reader(csv_companies, delimiter='\t')
	row_no = 0
	columns = []
	for row in companies_reader:
		if row_no == 0:
			for column in row:
				columns.append(column)
		else:
			row_data = {}
			column_no = 0
			for cell in row:
				current_column = columns[column_no]
				if cell != '':
					row_data[current_column] = cell
				else:
					row_data[current_column] = None
				column_no += 1
			companies.append(row_data)
		row_no += 1

generations = list()
with open('generations.tsv', newline='') as csv_generations:
	generations_reader = csv.reader(csv_generations, delimiter='\t')
	row_no = 0
	columns = []
	for row in generations_reader:
		if row_no == 0:
			for column in row:
				columns.append(column)
		else:
			row_data = {}
			column_no = 0
			for cell in row:
				current_column = columns[column_no]
				if cell != '':
					row_data[current_column] = int(cell)
				else:
					row_data[current_column] = None
				column_no += 1
			generations.append(row_data)
		row_no += 1

console_families = list()
with open('console_families.tsv', newline='') as csv_platform_families:
	platform_families_reader = csv.reader(csv_platform_families, delimiter='\t')
	row_no = 0
	columns = []
	for row in platform_families_reader:
		if row_no == 0:
			for column in row:
				columns.append(column)
		else:
			row_data = {}
			column_no = 0
			for cell in row:
				current_column = columns[column_no]
				if cell != '':
					if current_column in ['developer']:
						row_data[current_column] = cell.title()
					elif current_column in ['generation']:
						row_data[current_column] = int(cell)
					else:
						row_data[current_column] = cell
				else:
					row_data[current_column] = None
				column_no += 1
			console_families.append(row_data)
		row_no += 1

name_groups = list()
with open('name_groups.tsv', newline='') as csv_name_groups:
	name_groups_reader = csv.reader(csv_name_groups, delimiter='\t')
	row_no = 0
	columns = []
	for row in name_groups_reader:
		if row_no == 0:
			for column in row:
				columns.append(column)
		else:
			row_data = {}
			column_no = 0
			for cell in row:
				current_column = columns[column_no]
				if cell != '':
					row_data[current_column] = cell
				else:
					row_data[current_column] = None
				column_no += 1
			name_groups.append(row_data)
		row_no += 1

consoles = list()
with open('consoles.tsv', newline='') as csv_platforms:
	platforms_reader = csv.reader(csv_platforms, delimiter='\t')
	row_no = 0
	columns = []
	for row in platforms_reader:
		if row_no == 0:
			for column in row:
				columns.append(column)
		else:
			row_data = {}
			column_no = 0
			for cell in row:
				current_column = columns[column_no]
				if cell != '':
					if cell == 'y' and current_column in ['is_brand_missing']:
						row_data[current_column] = True
					elif cell == 'n' and current_column in ['is_brand_missing']:
						row_data[current_column] = False
					else:
						row_data[current_column] = cell
				else:
					row_data[current_column] = None
				column_no += 1
			consoles.append(row_data)
		row_no += 1

console_editions = list()
with open('console_editions.tsv', newline='') as csv_editions:
	editions_reader = csv.reader(csv_editions, delimiter='\t')
	row_no = 0
	columns = []
	for row in editions_reader:
		if row_no == 0:
			for column in row:
				columns.append(column)
		else:
			row_data = {}
			column_no = 0
			for cell in row:
				current_column = columns[column_no]
				if cell != '':
					if cell == 'y' and current_column in ['gloss', 'matte', 'transparency']:
						row_data[current_column] = True
					elif cell == 'n' and current_column in ['gloss', 'matte', 'transparency']:
						row_data[current_column] = False
					elif current_column == 'color':
						row_data[current_column] = cell.title()
					elif current_column == 'colors':
						cell_colors = cell.split(', ')
						for color in cell_colors:
							if color not in colors.keys():
								colors[color] = None
						row_data[current_column] = cell_colors
					elif current_column == 'name':
						row_data[current_column] = cell.replace('Pokemon', 'Pokémon')
					elif current_column == 'design note':
						row_data[current_column] = cell.replace('pokemon', 'Pokémon')
					else:
						row_data[current_column] = cell
				else:
					row_data[current_column] = None
				column_no += 1
			console_editions.append(row_data)
		row_no += 1

addon_platforms = list()
with open('addon_platforms.tsv', newline='') as csv_addon_platforms:
	addon_platforms_reader = csv.reader(csv_addon_platforms, delimiter='\t')
	row_no = 0
	columns = []
	for row in addon_platforms_reader:
		if row_no == 0:
			for column in row:
				columns.append(column)
		else:
			row_data = {}
			column_no = 0
			for cell in row:
				current_column = columns[column_no]
				if cell != '':
					row_data[current_column] = cell
				else:
					row_data[current_column] = None
				column_no += 1
			addon_platforms.append(row_data)
		row_no += 1

accessory_types = list()
with open('accessory_types.tsv', newline='') as csv_accessory_types:
	accessory_types_reader = csv.reader(csv_accessory_types, delimiter='\t')
	row_no = 0
	columns = []
	for row in accessory_types_reader:
		if row_no == 0:
			for column in row:
				columns.append(column)
		else:
			row_data = {}
			column_no = 0
			for cell in row:
				current_column = columns[column_no]
				if cell != '':
					row_data[current_column] = cell
				else:
					row_data[current_column] = None
				column_no += 1
			accessory_types.append(row_data)
		row_no += 1

game_families = list()
with open('game_families.tsv', newline='') as csv_game_families:
	game_families_reader = csv.reader(csv_game_families, delimiter='\t')
	row_no = 0
	columns = []
	for row in game_families_reader:
		if row_no == 0:
			for column in row:
				columns.append(column)
		else:
			row_data = {}
			column_no = 0
			for cell in row:
				current_column = columns[column_no]
				if cell != '':
					row_data[current_column] = cell
				else:
					row_data[current_column] = None
				column_no += 1
			game_families.append(row_data)
		row_no += 1

games = list()
with open('games.tsv', newline='') as csv_games:
	games_reader = csv.reader(csv_games, delimiter='\t')
	row_no = 0
	columns = []
	for row in games_reader:
		if row_no == 0:
			for column in row:
				columns.append(column)
		else:
			row_data = {}
			column_no = 0
			for cell in row:
				current_column = columns[column_no]
				if cell != '':
					if current_column in ['year_release']:
						row_data[current_column] = int(cell)
					elif cell == 'y' and current_column in ['is_bootleg']:
						row_data[current_column] = True
					elif cell == 'n' and current_column in ['is_bootleg']:
						row_data[current_column] = False
					else:
						row_data[current_column] = cell
				else:
					row_data[current_column] = None
				column_no += 1
			games.append(row_data)
		row_no += 1

# visual confirmation of data to be inserted
for family in console_families:
	for console in consoles:
		if console['console'] == family['console']:
			for edition in console_editions:
				if edition['console'] == console['console'] and edition['variation ref'] == console['desc']:
					printable = '\t\t'
					if edition['name'] is not None:
						printable += edition['name'] + ' - '
					if edition['color'] is not None:
						printable += edition['color'] + ' - '
					if edition['colors'] is not None:
						printable += ', '.join(edition['colors'])

# execute SQL seed statements
print('-------------------- enter SQL section --------------------')

load_dotenv(dotenv_path=find_dotenv())
POSTGRESQL_USERNAME = os.getenv('POSTGRESQL_USERNAME')
POSTGRESQL_PASSWORD = os.getenv('POSTGRESQL_PASSWORD')
POSTGRESQL_PORT = os.getenv('POSTGRESQL_PORT')
POSTGRESQL_HOST = os.getenv('POSTGRESQL_HOST')
POSTGRESQL_DBNAME = os.getenv('POSTGRESQL_DBNAME')

conn = db.connect(dbname=POSTGRESQL_DBNAME, user=POSTGRESQL_USERNAME, password=POSTGRESQL_PASSWORD, host=POSTGRESQL_HOST, port=POSTGRESQL_PORT)
cur = conn.cursor()

for role in company_roles:
	print(role)
	cur.execute('INSERT INTO company_roles (name, description) VALUES(%s, %s) RETURNING name, description;', (role['name'], role['description']))
	conn.commit()

	query_result = cur.fetchone()
	print(query_result)
	
for acc_type in accessory_types:
	print(acc_type)
	cur.execute('INSERT INTO accessory_types (name, description) VALUES(%s, %s) RETURNING name, description;', (acc_type['name'], acc_type['description']))
	conn.commit()

	query_result = cur.fetchone()
	print(query_result)

for company in companies:
	print(company)
	cur.execute('INSERT INTO companies (name, street_address, web_address, description) VALUES(%s, %s, %s, %s) RETURNING id, name, street_address, web_address, description;', (company['name'], company['street_address'], company['web_address'], company['description']))
	conn.commit()

	query_result = cur.fetchone()
	print(query_result)

for gen in generations:
	print(gen)
	cur.execute('INSERT INTO generations (id, year_begin, year_end) VALUES(%s, %s, %s) RETURNING id, year_begin, year_end;', (gen['number'], gen['year_begin'], gen['year_end']))
	conn.commit()

	query_result = cur.fetchone()
	print(query_result)

for family in console_families:
	print(family)
	cur.execute('INSERT INTO platform_families (name, generation) VALUES(%s, %s) RETURNING id, name, generation;', (family['name'], family['generation']))
	conn.commit()

	query_result = cur.fetchone()
	print(query_result)
	family['id'] = query_result[0]

for name_group in name_groups:
	print(name_group)
	cur.execute('INSERT INTO platform_name_groups (name, description) VALUES(%s, %s) RETURNING id, name, description;', (name_group['name'], name_group['description']))
	conn.commit()

	query_result = cur.fetchone()
	print(query_result)
	name_group['id'] = query_result[0]

for console in consoles:
	console['name_group_id'] = None
	for name_group in name_groups:
		if name_group['name'] in console['name']:
			console['name_group_id'] = name_group['id']

	console['platform_family_id'] = None
	for family in console_families:
		if family['console'] == console['console']:
			console['platform_family_id'] = family['id']

	values = (console['name'], console['platform_family_id'], console['name_group_id'], console['is_brand_missing'], console['model_no'], console['storage'], console['description'], console['notes'], console['relevance'])

	cur.execute('INSERT INTO platforms (name, platform_family_id, name_group_id, is_brand_missing, model_no, storage_capacity, description, disambiguation, relevance) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id, name, name_group_id, is_brand_missing, model_no, storage_capacity, description, disambiguation, relevance;', values)
	conn.commit()

	query_result = cur.fetchone()
	print(query_result)
	console['id'] = query_result[0]

for color in colors.keys():
	cur.execute('INSERT INTO colors (name) VALUES(%s) RETURNING id, name;', (color,))
	conn.commit()

	query_result = cur.fetchone()
	print(query_result)
	colors[color] = query_result[0]

for edition in console_editions:
	for console in consoles:
		if edition['console'] == console['console'] and edition['variation ref'] == console['desc']:
			edition['platform_id'] = console['id']

	values = (edition['name'], edition['platform_id'], edition['color'], edition['matte'], edition['transparency'], edition['gloss'], edition['design note'], edition['image_url'])

	cur.execute('INSERT INTO platform_editions (name, platform_id, official_color, has_matte, has_transparency, has_gloss, note, image_url) VALUES(%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id, name, platform_id, official_color, has_matte, has_transparency, has_gloss, note, image_url;', values)
	conn.commit()

	query_result = cur.fetchone()
	edition['id'] = query_result[0]

	for color in colors.keys():
		if color in edition['colors']:
			cur.execute('INSERT INTO colors_platform_editions (platform_edition_id, color_id) VALUES(%s, %s)', (edition['id'], colors[color]))
	conn.commit()

cur.close()
conn.close()
print('-------------------- exit SQL section --------------------')
print(console_editions)
