from base import *


def do_correction():
	result = get_current_position(get_sensor_data())
	if not line_find(result):
		print("failed to find line before correction:", get_sensor_data())
		return
	if result[0] > 0:
		move(result[1] - pie / 2, 0, 10, 0, 0, 1)
	elif result[0] < 0:
		move(result[1] + pie / 2, 0, 10, 0, 0, 1)
	sleep_until(0, 2, 1, 0)
	stop_and_sleep()
	print("in central position")
	# # 旋转直到转正
	if (result[1] - pie / 2) > 0:  # 判断向左转还是向右转
		move(0, 50, 0, 0, 0, 1)
	elif (result[1] - pie / 2) < 0:
		move(0, -50, 0, 0, 0, 1)
	else:
		stop()
		return
	robot.reset_timer(2)
	while robot.get_timer_ms(2) < 3000:  # 三秒内如果转不正就退出
		result = get_current_position(get_sensor_data())
		if line_find(result):  # 每次识别到线对旋转方向进行一次更正
			if (result[1] - pie / 2) > 0:
				move(0, 50, 0, 0, 0, 0)
			elif (result[1] - pie / 2) < 0:
				move(0, -50, 0, 0, 0, 0)
			else:
				stop()
				return


def get_avg_sensor_data():
	value = []
	for i in range(5):
		value.append(get_sensor_data())
	result = []
	avg = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]
	for i in range(5):
		for j in range(5):
			avg[0][i] = avg[0][i] + value[j][0][i]
			avg[1][i] = avg[1][i] + value[j][1][i]
	for i in range(5):
		avg[0][i] = avg[0][i] / 5
		avg[1][i] = avg[1][i] / 5
	return avg


def tail_adjust():
	sensor_data = get_avg_sensor_data()
	# 检查后排是否在正中间
	max_diff = -400
	limit = 200
	if (sensor_data[1][1] - sensor_data[1][3]) > max_diff + limit:
		robot.set_motor(3, -15)
		while (sensor_data[1][1] - sensor_data[1][3]) > max_diff:
			sensor_data = get_avg_sensor_data()
	elif (sensor_data[1][1] - sensor_data[1][3]) < max_diff - limit:
		robot.set_motor(3, 15)
		while (sensor_data[1][1] - sensor_data[1][3]) < max_diff:
			sensor_data = get_avg_sensor_data()
	else:
		return
	robot.set_motor(3, 0)


def head_adjust():
	sensor_data = get_avg_sensor_data()
	# 检查前排是否在正中间
	max_diff = 50
	if (sensor_data[0][1] - sensor_data[0][3]) > max_diff:
		move(0, 20, 0, 0, 0, 0)
	elif (sensor_data[0][1] - sensor_data[0][3]) < -max_diff:
		move(0, -20, 0, 0, 0, 0)
	else:
		pass
	while abs(sensor_data[0][3] - sensor_data[0][1]) > max_diff:
		sensor_data = get_avg_sensor_data()
		continue
	stop_and_sleep()


def correction():
	turn_to_find_line()
	print("find line")
	do_correction()
	add_event("correction")
	tail_adjust()
	add_event("tail adjust")
	head_adjust()
	add_event("head adjust")

	# value = get_sensor_data()
	# if value[0][2] < 3000 or value[1][2] < 3000:
	# 	do_correction()
