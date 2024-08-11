# *** Abilix Programme
# *** http://www.abilix.com
import robot

#  pid
p_dis = 0
i_dis = 0
d_dis = 0
k_p_dis = 0.1
k_i_dis = 0.005
k_d_dis = 0
p_ang = 0
i_ang = 0
d_ang = 0
k_p_ang = 120
k_i_ang = 3
k_d_ang = 0
p_baby = 0
k_p_baby = 3

#  移动参数
#  轮心距
L1 = 13.328
L2 = 12.802
#  轮轴角
a = 0.412
#  传感器
G = ([(-5, 7.8375), (-2, 7.8375), (0, 7.8375), (2, 7.8375), (5, 7.8375)],
	 [(-4, -2), (-2, -2), (-2, 0), (0, 0), (2, 0), (2, -2), (4, -2)])

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
		stop()
		for i in range(800):
			robot.set_motor(3, f3 / 800 * (i + 1))
			robot.set_motor(2, f2 / 800 * (i + 1))
			robot.set_motor(1, f1 / 800 * (i + 1))
	else:
		robot.set_motor(3, f3)
		robot.set_motor(2, f2)
		robot.set_motor(1, f1)

	if time != 0:
		robot.sleep(time)
	elif distance != 0:
		robot.reset_encoder(1)
		robot.reset_encoder(2)
		robot.reset_encoder(3)
		while True:
			x_moving = robot.get_encoder(3)
			y_moving = sin(a) * robot.get_encoder(1) - sin(a) * robot.get_encoder(2)
			moving_distance = sqrt(x_moving ** 2 + y_moving ** 2)
			# robot.print(x_moving, y_moving, moving_distance)\
			# robot.print(robot.get_encoder(1), robot.get_encoder(2), robot.get_encoder(3))
			if moving_distance > distance:
				break


def get_result():
	value = [[0, 0, 0, 0, 0, 10], [0, 0, 0, 0, 0, 0, 0, 10]]
	# 读入并初步处理数据
	for i in range(5):
		gray = robot.get_channel_gray(4, i + 1)
		if gray >= 2000:
			value[0][i] = 1
	for i in range(7):
		gray = robot.get_gray(11 - i)
		if gray >= 2000:
			value[1][i] = 1
			# print(gray, i)

	for i in range(5):  # 转换为长度
		if value[0][i] == 1:
			value[0][5] = i
			break
	for i in range(7):
		if value[1][i] == 1:
			value[1][7] = i
			break
	return value


def processed_result():
	# 转换为长度
	value = get_result()

	#  转换为偏移量和偏航角
	if value[0][5] == 10 or value[1][7] == 10:
		return 10, 10
	else:
		# 转换为坐标
		g = [G[0][value[0][5]], G[1][value[1][7]]]
		# print (g)
		if g[0][0] == g[1][0]:
			return g[0][0], pie / 2
		else:
			ma = (g[0][1] - g[1][1]) / (g[0][0] - g[1][0])
			ga = - ma * g[0][0] + g[0][1]
			# return ma, ga, value[0][5], value[1][5]
			offset_distance = - ga / sqrt(1 + ma ** 2)
			offset_angle = (robot.atan(ma) + pie) % pie
			if ma * ga > 0:
				offset_distance = -abs(offset_distance)
			else:
				offset_distance = abs(offset_distance)
			return offset_distance, offset_angle


def change_motor_state(speed, offsite_dis, offsite_ang):
	global k_p_dis, k_p_ang, p_dis, p_ang, k_i_dis, k_i_ang, i_dis, i_ang
	a = processed_result()
	print (a)
	if a[0] == 10:
		i_dis *= 0.9
		i_ang *= 0.9
	else:
		p_dis = -a[0] + offsite_dis
		p_ang = a[1] + offsite_ang - pie / 2
		i_dis += p_dis
		i_ang += p_ang
	move(p_dis * k_p_dis + i_dis * k_i_dis + p_ang + pie / 2, p_ang * k_p_ang + i_ang * k_i_ang, speed, 0, 0, 0)


# move(pie / 2, p_ang * k_p_ang + i_ang * k_i_ang, speed, 0, 0, 0)
# move(p_dis * k_p_dis + i_dis * k_i_dis + p_ang + pie / 2, 0, speed, 0, 0, 0)


def line_navigation(speed, offsite_dis, offsite_ang, time):
	robot.reset_timer(0)
	change_motor_state(speed, offsite_dis, offsite_ang)
	while robot.get_timer_ms(0) < time * 1000:
		change_motor_state(speed, offsite_dis, offsite_ang)


def baby_change(speed, offsite_dis, offsite_ang):
	global p_baby, k_p_baby
	value = get_result()[0]
	for i in range(5):
		if value[i] == 1:
			p_baby = 1 / 6 * i ** 3 - i ** 2 + 23 / 6 * i - 5
			break
	robot.set_motor(1, cos(a) * speed - p_baby * k_p_baby)
	robot.set_motor(2, - cos(a) * speed - p_baby * k_p_baby)


def baby_navigation(speed, offsite_dis, offsite_ang, time):
	robot.reset_timer(1)
	baby_change(speed, offsite_dis, offsite_ang)
	while robot.get_timer_ms(1) < time * 1000:
		baby_change(speed, offsite_dis, offsite_ang)


def navigate_to(speed, offsite_dis, offsite_angle, is_cross):
	if is_cross != 0:
		get_out(speed)
	while True:
		line_navigation(speed, offsite_dis, offsite_angle, 0)
		if robot.get_channel_gray(4, 1) > 2000 or robot.get_channel_gray(4, 5) > 2000:
			break


def left():
	move(pie / 2, 0, 30, 0, 600, 0)
	i = 300
	for j in range(3):
		move(0, i, 0, 0, 0, 0)
		i *= 0.997
	robot.sleep(0.3)
	while get_result()[0][2] == 0:
		for j in range(3):
			move(0, i, 0, 0, 0, 0)
			i *= 0.997
	stop()
	robot.sleep(0.1)


def right():
	move(pie / 2, 0, 30, 0, 600, 0)
	i = -300
	for j in range(3):
		move(0, i, 0, 0, 0, 0)
		i *= 0.997
	robot.sleep(0.3)
	while get_result()[0][2] == 0:
		for j in range(3):
			move(0, i, 0, 0, 0, 0)
			i *= 0.997
	stop()
	robot.sleep(0.1)


def get_out(speed):
	while robot.get_gray(5) < 2000 and robot.get_gray(11) < 2000:
		baby_change(30, 0, 0)
	while robot.get_gray(5) > 2000 or robot.get_gray(11) > 2000:
		baby_change(30, 0, 0)


def leave():
	move(pie / 2, 0, 30, 0, 0, 1)
	while robot.get_gray(5) < 2500 and robot.get_gray(11) < 2500:
		pass
	while robot.get_gray(5) > 2500 and robot.get_gray(11) > 2500:
		pass


def stop_and_sleep():
	stop()
	robot.sleep(0.1)


def wait_for(port, channel, condition, wait):
	robot.sleep(wait)
	if port == 4:
		while get_result()[0][channel] != condition:
			pass
	else:
		while get_result()[1][port] != condition:
			pass


def correction():
	result = processed_result()
	if result[0] != 10:  # 如果能找到线
		# 平移直到中心点在线上
		if result[0] > 0:
			move(result[1] - pie / 2, 0, 10, 0, 0, 1)
		elif result[0] < 0:
			move(result[1] + pie / 2, 0, 10, 0, 0, 1)
		wait_for(3, 0, 1, 0)
		robot.sleep(0.1)
		stop_and_sleep()
		# 旋转直到转正
		if result[1] - pie / 2 > 0:
			move(0, 50, 0, 0, 0, 1)
		elif result[1] - pie / 2 < 0:
			move(0, -50, 0, 0, 0, 1)
		else:
			return
		robot.reset_timer(2)
		while robot.get_timer_ms(2) < 3000:  # 三秒内如果转不正就退出
			result = processed_result()
			if result[1] != 10:  # 每次识别到线对旋转方向进行一次更正
				if result[1] - pie / 2 > 0:
					move(0, 50, 0, 0, 0, 0)
				elif result[1] - pie / 2 < 0:
					move(0, -50, 0, 0, 0, 0)
				else:
					robot.sleep(0.2)
					stop()
					return
	else:  # 否则左右转弯直到找到线（找不到线会挂）
		robot.reset_timer(3)
		robot.reset_timer(2)
		move(0, 100, 0, 0, 0, 0)
		while robot.get_timer_ms(2) < 1000:
			if processed_result()[0] != 10:
				correction()  # 找到线后进行矫正
				return
		while robot.get_timer_ms(3) < 5000:  # 限时五秒内找到线
			robot.reset_timer(2)
			move(0, -100, 0, 0, 0, 0)
			while robot.get_timer_ms(2) < 2000:
				if processed_result()[0] != 10:
					correction()  # 找到线后进行矫正
					return
			robot.reset_timer(2)
			move(0, 100, 0, 0, 0, 0)
			while robot.get_timer_ms(2) < 2000:
				if processed_result()[0] != 10:
					correction()  # 找到线后进行矫正
					return



