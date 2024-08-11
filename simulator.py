import time
import csv
import threading

def parse_input_file():
	with open('input.csv', 'r') as file:
		csv_reader = csv.DictReader(file)
		active = 0
		line = 0
		for row in csv_reader:
			if active == 0:
				active = int(row['Active'])
			line += 1
			if active == line:
				return row
			else:
				continue

sensor_values = None
class SensorThread (threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		while True:
			sensor_values = parse_input_file()
			time.sleep(0.2)


def get_sensor_value(id):
	global sensor_values
	# print(id)
	key = 'gray_' + str(id)
	sensor_values = parse_input_file()
	return int (sensor_values[key]) * 3000
