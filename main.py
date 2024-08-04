# *** Abilix Programme
# *** http://www.abilix.com

import robot
#  pid
p_dis = 0
i_dis = 0
d_dis = 0
k_p_dis = 0.15
k_i_dis = 0.001
k_d_dis = 0
p_ang = 0
i_ang = 0
d_ang = 0
k_p_ang = 10
k_i_ang = 0
k_d_ang = 0

#  移动参数
#  轮心距
L1 = 13.328
L2 = 12.802
#  轮轴角
a = 0.412
#  传感器
G = [[0, -1.6625], [0, 7.8375]]

#  基础参数
pie = 3.1415926
e = 0.0000001

def sin(a):
	return robot.sin(a)
def cos(a):
	return robot.cos(a)
def tan(a):
	return robot.tan(a)
def sqrt(a):
	return robot.sqrt(a)
def abs(a):
	return robot.abs(a)


def stop():
	robot.set_motor(1, 0)
	robot.set_motor(2, 0)
	robot.set_motor(3, 0)


def move(direction, angle, speed, time, distance, is_first):
	f0 = speed
	b = direction
	#  计算转速，逆时针为正
	f1 = cos(a) * sin(b) * f0 - sin(a) * cos(b) * f0 + angle * L2 * 0.01
	f2 = -cos(a) * sin(b) * f0 - sin(a) * cos(b) * f0 + angle * L2 * 0.01
	f3 = cos(b) * f0 + angle * L1 * 0.01
	#  执行
	if is_first == 1:
		robot.set_motor(3, f3 / 3)
		robot.set_motor(2, f2 / 3)
		robot.set_motor(1, f1 / 3)
		robot.set_motor(1, f1 / 3 * 2)
		robot.set_motor(2, f2 / 3 * 2)
		robot.set_motor(3, f3 / 3 * 2)
		robot.set_motor(3, f3)
		robot.set_motor(2, f2)
		robot.set_motor(1, f1)
	else:
		robot.set_motor(1, f1)
		robot.set_motor(2, f2)
		robot.set_motor(3, f3)
	if time != 0:
		robot.sleep(time)
	elif distance != 0:
		robot.reset_encoder(1)
		robot.reset_encoder(2)
		robot.reset_encoder(3)
		while True:
			x_moving = -robot.get_encoder(1) * cos(a) - robot.get_encoder(2) * cos(a) + robot.get_encoder(3)
			y_moving = robot.get_encoder(1) * sin(a) - robot.get_encoder(2) * sin(a)
			moving_distance = sqrt(x_moving ** 2 + y_moving ** 2)
			# robot.print(x_moving, y_moving, moving_distance)\
			# robot.print(robot.get_encoder(1), robot.get_encoder(2), robot.get_encoder(3))
			if moving_distance >= distance:
				break

def get_result():
	value = [[0, 0, 0, 0, 0, 10], [0, 0, 0, 0, 0, 0, 10]]
	# 读入并初步处理数据
	for i in range(5):
		gray = robot.get_channel_gray(3, i+1)
		if gray >= 2000:
			value[0][i] = 1
		else:
			value[0][i] = 0
	for i in range(6):
		gray = robot.get_gray(i+7)
		if gray >= 2500:
			value[1][i] = 1
		else:
			value[1][i] = 0
	return value


def processed_result():
	# 转换为长度
	value = get_result()
	for i in range(5):
		if value[0][i] == 1:
			if value[0][i + 1] == 1:
				value[0][5] = ((1/6*i**3-i**2+23/6*i-5)+(1/6*(i+1)**3-(i+1)**2+23/6*(i+1)-5))/2
			else:
				value[0][5] = 1 / 6 * i ** 3 - i ** 2 + 23 / 6 * i - 5
			break
	for i in range (6):
		if value[1][i] == 1:
			if value[1][i + 1] == 1:
				value[1][6] = 2 * i - 4
			else:
				value[1][6] = 2 * i - 5
	# return value[0][5], value[1][5]

	# 转换为坐标
	g = [[0, 0], [0, 0]]
	for i in range(2):
		if value[i][i + 5] != 10:
			g[i][0] = value[i][i + 5]
			g[i][1] = G[i][1]
	# return g

	#  转换为偏移量和偏航角
	if value[0][5] == 10 and value[1][6] == 10:
		return 10, 10
	elif value[0][5] == 10:
		return 10, 10
	elif value[1][6] == 10:
		return 10, 10
	else:
		if g[0][0] == g[1][0]:
			return - g[0][0], 0
		else:
			ma = (g[0][1] - g[1][1]) / (g[0][0] - g[1][0])
			ga = - ma * g[0][0] + g[0][1]
			# return ma, ga, value[0][5], value[1][5]
			offset_distance = - ga / sqrt(1 + ma ** 2)
			offset_angle = robot.atan(ma)
			return offset_distance, offset_angle

	#
	# if value[0][5] != 10 and value[1][5] != 10:
	# 	g1 = (robot.cos(c) * value[0][5], robot.sin(c) * value[0][5] + 2)
	# 	g2 = (robot.cos(d) * value[1][5], robot.sin(d) * value[1][5] + 7.25)
	# 	# 转换为两个偏移量
	# 	if g1[0] == g2[0]:
	# 		offset_distance = g1[0]
	# 		offset_angle = 0
	# 	else:
	# 		ma = (g2[0] * g1[1] - g1[0] * g2[1]) / (g2[0] - g1[0])
	# 		ga = (g1[0] * g2[1] - g2[0] * g1[1]) / (g2[1] - g1[1])
	#
	# return 10, 10

def line_navigation(speed, off_site_dis, off_site_ang, time):
	global k_p_dis, k_p_ang, p_dis, p_ang, k_i_dis, k_i_ang, i_dis, i_ang
	robot.reset_timer(0)
	while robot.get_timer_ms(0) <= time * 1000:
		a = processed_result()
		if a[0] == 10 and a[1] == 10:
			i_dis *= 0.5
			i_ang *= 0.5
		elif a[0] == 10:
			# p_dis = p_dis * 0.7 + a[0]
			# i_dis *= 0.9
			# i_ang *= 0.9
			pass
		elif a[1] == 10:
			# p_dis = p_dis * 0.7 + a[1]
			# i_dis *= 0.9
			# i_ang *= 0.9
			pass
		else:
			p_dis = a[0] + off_site_dis
			p_ang = a[1] + off_site_ang
			i_dis += p_dis
			i_ang += p_ang
		move(p_dis * k_p_dis + i_dis * k_i_dis + pie/2 - p_ang, - p_ang * k_p_ang - i_ang * k_i_ang, speed, 0, 0, 0)


def navigate_to(speed, off_site_dis, offsite_angle):
	line_navigation(speed, off_site_dis, offsite_angle, 0.5)
	while True:
		line_navigation(speed, off_site_dis, offsite_angle, 0)
		if robot.get_channel_gray(3, 1) > 2000 or robot.get_channel_gray(3, 5) > 2000:
			break


# def correction(off_site):
# 	for i in range(7):
# 		move(1, 0, -30, 0, 1500)
# 		line_navigation(30, off_site, 0.5)


def left():
	move(pie / 2, 0, 30, 0, 900, 0)
	stop()
	print(get_result())
	move(0, 200, 0, 0, 1000, 1)
	#
	# move(1, 0, 60, 0, 1700)
	# move(0, -50, 60, 0, 0)
	i = 200
	while robot.get_gray(9) <= 2500:
		move(0, i, 0, 0, 0, 0)
		i -= 0.2
	# stop()


# def right():
# 	move(1, 0, 60, 0, 1700)
# 	move(0, 50, 60, 0, 0)
# 	i = -60
# 	while robot.get_channel_gray(6, 4) <= 2000:
# 		robot.set_motor(4, i)
# 		robot.set_motor(1, i)
# 		i += 0.005
# 	stop()


def move_to(destination):
	if destination == 1:
		move(pie/2, 0, 30, 0.5, 0, 1)
		navigate_to(30, 0, 0)
		# move(-2.9, -25, 30, 0, 0, 1)
		# while robot.get_channel_gray(6, 1) <= 2500:
		# 	pass
		# robot.sleep(0.1)
		# navigate_to(30, 0, 0)
		# move(1.6, 0, 30, 0, 3000, 0)
		stop()

# 	elif destination == 2:
# 		move(1, 0, 60, 0.5, 0)
# 		navigate_to(60, 0)
# 		left()
# 		navigate_to(60, 0)
# 		right()
# 		navigate_to(60, 0)
# 		right()
# 		navigate_to(60, 0)
# 		left()
# 	# move(1, 0, 60, 0.5, 0)
# 	# move(1, 3, 60, 0, 3000)
# 	# move(1, -3, 60, 0, 3000)
# 	elif destination == 3:
# 		move(1, 0, 60, 0.5, 0)
# 		navigate_to(60, 0)
# 		navigate_to(60, 0)
# 		right()
# 		navigate_to(60, 0)
# 		left()
# 	elif destination == 4:
# 		move(1, 0, 60, 0.5, 0)
# 		navigate_to(60, 0)
# 		navigate_to(60, 0)
# 		right()
# 		navigate_to(60, 0)
# 		navigate_to(60, 0)
# 		right()
# 		navigate_to(60, 0)
# 		navigate_to(60, 0)
# 		left()
# 		navigate_to(60, 0)
# 		left()
# 		line_navigation(60, 0, 1)
# 		navigate_to(60, 0)
# 		right()
# 	elif destination == 5:
# 		move(1, 0, 60, 0.5, 0)
# 		navigate_to(60, 0)
# 		navigate_to(60, 0)
# 		right()
# 		for i in range(3):
# 			navigate_to(60, 0)
# 		right()
# 		navigate_to(60, 0)
# 		left()
# 	elif destination == 6:
# 		move(1, 0, 60, 0.5, 0)
# 		navigate_to(60, 0)
# 		navigate_to(60, 0)
# 		right()
# 		for i in range(3):
# 			navigate_to(60, 0)
# 		right()
# 		navigate_to(60, 0)
# 		navigate_to(60, 0)
# 		stop()
# 	elif destination == 7:
# 		move(1, 0, 60, 0.5, 0)
# 		navigate_to(60, 0)
# 		navigate_to(60, 0)
# 		right()
# 		for i in range(3):
# 			navigate_to(60, 0)
# 		right()
# 		navigate_to(60, 0)
# 		navigate_to(60, 0)
# 		right()
# 		navigate_to(60, 0)
# 		left()
# 	elif destination == 8:
# 		move(1, 0, 60, 0.5, 0)
# 		navigate_to(60, 0)
# 		left()
# 		navigate_to(60, 0)
# 		navigate_to(60, 0)
# 		left()
# 	elif destination == 9:
# 		move(1, 0, 60, 0.5, 0)
# 		navigate_to(60, 0)
# 		left()
# 		for i in range(3):
# 			navigate_to(60, 0)
# 		left()
# 		navigate_to(60, 0)
# 		right()
# 	elif destination == 10:
# 		move(1, 0, 60, 0.5, 0)
# 		navigate_to(60, 0)
# 		left()
# 		for i in range(3):
# 			navigate_to(60, 0)
# 		right()
# 		navigate_to(60, 0)
# 		left()
# 	elif destination == 11:
# 		move(1, 0, 60, 0.5, 0)
# 		navigate_to(60, 0)
# 		navigate_to(60, 0)
# 		right()
# 		navigate_to(60, 0)
# 		navigate_to(60, 0)
# 		right()
# 		navigate_to(60, 0)
# 		right()
#
#
# def go_back(place):
# 	# 传感器与路口齐平，面朝任务
# 	if place == 1:
# 		move(0, -30, 40, 0, 1)
# 		move(1, 0, -100, 0, 10000)
# 	elif place == 2:
# 		move(0, 15, 40, 0, 0)
# 		move(1, -10, -100, 0, 8000)
# 	elif place == 3:
# 		left()
# 		navigate_to(60, 0)
# 		right()
# 		move(1, -15, -100, 0, 9000)
# 	elif place == 4:
# 		right()
# 		navigate_to(60, 0)
# 		navigate_to(60, 0)
# 		go_back(6)
# 	elif place == 5:
# 		left()
# 		navigate_to(60, 0)
# 		move(1, 0, 60, 0, 1700)
# 		move(0, -50, 60, 0, 0)
# 		i = 60
# 		while robot.get_channel_gray(6, 2) <= 2000:
# 			robot.set_motor(4, i)
# 			robot.set_motor(1, i)
# 			i -= 0.002
# 		navigate_to(60, 0)
# 		navigate_to(60, 0)
# 		go_back(6)
# 	elif place == 6:
# 		move(1, 0, 40, 0, 2500)
# 		move(0, -90, 40, 0, 0)
# 		move(1, 0, -100, 0, 11000)
# 	elif place == 7:
# 		move(1, 0, 40, 0, 3000)
# 		move(0, -85, 40, 0, 0)
# 		move(1, 0, -100, 0, 9000)
# 	elif place == 8:
# 		move(1, 0, 40, 0, 2000)
# 		move(0, -85, 40, 0, 0)
# 		navigate_to(60, 0)
# 		navigate_to(60, 0)
# 		right()
# 		line_navigation(60, 0, 1)
# 	elif place == 9:
# 		move(0, 10, 40, 0, 0)
# 		move(1, 0, -100, 0, 10000)
# 	elif place == 10:
# 		move(0, 45, 40, 0, 0)
# 		move(1, 0, -100, 0, 12000)
#
#
# def complete_11_a():
# 	move(1, 0, 60, 0, 4500)
# 	robot.set_motor(3, -100)
# 	robot.reset_encoder(3)
# 	while True:
# 		if abs(robot.get_encoder(3)) >= 300:
# 			robot.set_motor(3, 0)
# 			break
# 	move(1, 0, -100, 0, 3000)
#
#
# def complete_11_b():
# 	move(1, 0, 60, 0, 3500)
# 	robot.set_motor(3, -100)
# 	robot.reset_encoder(3)
# 	while True:
# 		if abs(robot.get_encoder(3)) >= 300:
# 			robot.set_motor(3, 0)
# 			break
# 	move(1, 0, -100, 0, 3300)
#
#
# def complete_11_c():
# 	move_to(11)
# 	line_navigation(50, 0, 1)
# 	robot.set_motor(3, -100)
# 	robot.reset_encoder(3)
# 	while True:
# 		if abs(robot.get_encoder(3)) >= 18000:
# 			robot.set_motor(3, 0)
# 			break
# 	navigate_to(-60, 0)
# 	right()
# 	navigate_to(60, 0)
# 	left()
# 	navigate_to(60, 0)
# 	navigate_to(60, 0)
# 	right()
# 	move(0, 10, 40, 0, 0)
# 	move(1, -10, -100, 0, 8000)
#
# def complete_11_d():
# 	move(1, 0, 60, 0.5, 0)
# 	navigate_to(60, 0)
# 	navigate_to(60, 0)
# 	right()
# 	navigate_to(60, 0)
# 	move(0, 90, 40, 0, 0)
# 	robot.sleep(1)
# 	move(1, 0, 5, 0, 1000)
# 	navigate_to(-40, 0)
# 	right()
# 	navigate_to(60, 0)
# 	right()
# 	move(0, 10, 40, 0, 0)
# 	move(1, -15, -100, 0, 8000)
#
# def finish_1():
# 	robot.sleep(0.3)
# 	line_navigation(70, 0, 1)
# 	navigate_to(-60, 0)
#
# def finish_3():
# 	robot.sleep(0.3)
# 	line_navigation(70, 0, 0.5)
# 	navigate_to(-60, 0)
#
# def finish_2():
# 	line_navigation(30, 0, 0.5)
# 	robot.set_motor(3, 40)
# 	robot.reset_encoder(3)
# 	while True:
# 		if abs(robot.get_encoder(3)) >= 1500:
# 			robot.set_motor(3, 0)
# 			break
# 	navigate_to(-60, 0)
#
#
# def complete_8_1():
# 	move_to(8)
# 	robot.sleep(0.3)
# 	line_navigation(70, 0, 2)
# 	move(1, 0, -40, 0, 1000)
# 	move(0, 90, 40, 0, 0)
# 	move(1, 0, -100, 0, 5000)
#
# def complete_8_3():
# 	move_to(8)
# 	robot.sleep(0.3)
# 	line_navigation(40, 0, 1.5)
# 	move(1, 0, -40, 0, 1000)
# 	move(0, 100, 40, 0, 0)
# 	move(1, 0, -100, 0, 4000)
#
# def complete8_2():
# 	move_to(8)
# 	line_navigation(60, 0, 2)
# 	robot.set_motor(3, 40)
# 	robot.reset_encoder(3)
# 	while True:
# 		if abs(robot.get_encoder(3)) >= 1500:
# 			robot.set_motor(3, 0)
# 			break
# 	move(1, 0, -40, 0, 1000)
# 	move(0, 90, 40, 0, 0)
# 	move(1, 0, -100, 0, 5000)
#
#
# def complete_7_2():
# 	move_to(7)
# 	robot.set_motor(3, 40)
# 	robot.reset_encoder(3)
# 	while True:
# 		if abs(robot.get_encoder(3)) >= 150:
# 			robot.set_motor(3, 0)
# 			break
# 	line_navigation(30, 0, 1)
# 	robot.set_motor(3, 40)
# 	robot.reset_encoder(3)
# 	while (True):
# 		if abs(robot.get_encoder(3)) >= 1500:
# 			robot.set_motor(3, 0)
# 			break
# 	move(1, 0, -40, 0, 800)
# 	move(0, 65, 40, 0, 0)
# 	move(1, -10, 100, 0, 6000)
#
#
# def complete_7_1():
# 	move_to(7)
# 	robot.set_motor(3, 40)
# 	robot.reset_encoder(3)
# 	while (True):
# 		if abs(robot.get_encoder(3)) >= 150:
# 			robot.set_motor(3, 0)
# 			break
# 	robot.sleep(0.3)
# 	line_navigation(70, 0, 1)
# 	move(1, 0, -40, 0, 1000)
# 	move(0, 65, 40, 0, 0)
# 	move(1, -10, 100, 0, 6000)
#
# def complete_7_3():
# 	move_to(7)
# 	robot.set_motor(3, 40)
# 	robot.reset_encoder(3)
# 	while (True):
# 		if abs(robot.get_encoder(3)) >= 150:
# 			robot.set_motor(3, 0)
# 			break
# 	robot.sleep(0.3)
# 	line_navigation(40, 0, 0.5)
# 	move(1, 0, -40, 0, 1000)
# 	move(0, 65, 40, 0, 0)
# 	move(1, -10, 100, 0, 6000)
#
# def complete_6_1():
# 	move_to(6)
# 	robot.sleep(0.3)
# 	line_navigation(70, 0, 1)
# 	navigate_to(-60, 0)
# 	go_back(6)
#
# def complete_6_3():
# 	move_to(6)
# 	robot.sleep(0.3)
# 	line_navigation(40, 0, 1)
# 	navigate_to(-60, 0)
# 	go_back(6)
#
# def complete_6_2():
# 	move_to(6)
# 	line_navigation(40, 0, 1)
# 	finish_2()
# 	go_back(6)
#
# def wait_for_next_task():
# 	while True:
# 		if robot.check_key(2) == 1:
# 			return 1
# 		elif robot.check_key(1) == 1:
# 			return 0
#
# def finish_task():
# 	move_to(9)
# 	line_navigation(70, 0, 0.3)
# 	robot.sleep(0.5)
# 	go_back(9)
#
#
# def execute_task(pos, task):
# 	if pos == 6:
# 		if task == 1:
# 			complete_6_1()
# 		elif task == 3:
# 			complete_6_3()
# 		else:
# 			complete_6_2()
# 	elif pos == 7:
# 		if task == 1:
# 			complete_7_1()
# 		elif task == 3:
# 			complete_7_3()
# 		else:
# 			complete_7_2()
# 	elif pos == 8:
# 		if task == 1:
# 			complete_8_1()
# 		elif task == 3:
# 			complete_8_3()
# 		else:
# 			complete8_2()
# 	elif pos == 11:
# 		if task == 1:
# 			complete_11_a()
# 		elif task == 2:
# 			complete_11_b()
# 		elif task == 3:
# 			complete_11_c()
# 		else:
# 			complete_11_d()
# 	elif pos == 100:
# 		finish_task()
# 	else:
# 		move_to(pos)
# 		if task == 1:
# 			finish_1()
# 		elif task == 2:
# 			finish_2()
# 		else:
# 			finish_3()
# 		go_back(pos)
#
# def importance(pos, task):
# 	if pos == 7:
# 		if task != 1:
# 			robot.print("!!!!!!!!!!!\n!!!!!!!!!!!\n!!!!!!!!!!!\n!!!!!!!!!!!\n!!!!!!!!!!!\n!!!!!!!!!!!\n!!!!!!!!!!!")
# 	elif pos != 11:
# 		if task == 1:
# 			robot.print("!!!!!!!!!!!\n!!!!!!!!!!!\n!!!!!!!!!!!\n!!!!!!!!!!!\n!!!!!!!!!!!\n!!!!!!!!!!!\n!!!!!!!!!!!")
# 		if task == 2:
# 			robot.print("!!!!!!!!!!!\n!!!!!!!!!!!\n!!!!!!!!!!!\n!!!!!!!!!!!\n!!!!!!!!!!!\n!!!!!!!!!!!\n!!!!!!!!!!!")
# 	else:
# 		if task == 1:
# 			robot.print("!!!!!!!!!!!\n!!!!!!!!!!!\n!!!!!!!!!!!\n!!!!!!!!!!!\n!!!!!!!!!!!\n!!!!!!!!!!!\n!!!!!!!!!!!")
# 		elif task == 2:
# 			robot.print("!!!!!!!!!!!\n!!!!!!!!!!!\n!!!!!!!!!!!\n!!!!!!!!!!!\n!!!!!!!!!!!\n!!!!!!!!!!!\n!!!!!!!!!!!")

def main():
	move_to(1)
	# move(pie, 0, 30, 0, 0, 1)
	# robot.set_motor(4, 100)

	# robot.set_motor(3, 40)
	# robot.sleep(3)
	# stop()
	# robot.sleep(2)
	# robot.set_motor(3, 80)
	# robot.sleep(3)
	# stop()
	# while True:
	# 	print(processed_result(), '\n')
	# 	robot.sleep(3)

	# move(pie/2, 0, 50, 0, 0)
	# k_p_ang = 0
	# k_i_ang = 0
	# k_p_dis = 0.01
	# k_i_dis = 0
	# line_navigation(30, 0, 0, 100)

	# k_p_dis = 0.15
	# k_i_dis = 0.001
	# k_d_dis = 0
	# # line_navigation(30, 0, 0, 100)
	# for i in range(10):
	# 	k_d_dis = (i + 1) * 0.001
	# 	print(k_i_dis)
	# 	line_navigation(30, 0, 0, 4)
	# 	robot.sleep(3)
		# for j in range(10):
		# 	k_i_dis = (j + 1) * 0.005
		# 	print(k_p_dis, )
		# 	# navigate_to(50, 0, 0)
		# 	line_navigation(30, 0, 0,100)
		# 	robot.sleep(3)

	# value = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
	# while True:
	# 	for i in range(5):
	# 		value[0][i] = robot.get_channel_gray(6, i+1)
	# 	for i in range(5):
	# 		value[1][i] = robot.get_gray(i+7)
	# 	print(value, '\n')
	# 	robot.sleep(4)


	# value = [0, 0, 0, 0, 0]
	# while True:
	# 	for i in range(5):
	# 		value[i] = robot.get_gray(i+7)
	# 	robot.sleep(3)
	# 	print(value)

main()