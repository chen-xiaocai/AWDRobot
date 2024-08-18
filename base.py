# *** Abilix Programme
# *** http://www.abilix.com
import robot

#  pid
p_dis = 0
i_dis = 0
d_dis = 0
k_p_dis = 0.07
k_i_dis = 0.005
k_d_dis = 0
p_ang = 0
i_ang = 0
d_ang = 0
k_p_ang = 100
k_i_ang = 3
k_d_ang = 0
p_baby = 0
k_p_baby = 5

#  轮心距
L1 = 10
L2 = 12.802
#  轮轴角
a = 0.412
#  传感器
G = ([(-5, 7.8375), (-2, 7.8375), (0, 7.8375), (2, 7.8375), (5, 7.8375)], [(-4, -2), (-2, 0), (0, 0), (2, 0), (4, -2)])

#  基础参数
pie = 3.1415926
e = 0.0000001

#  电机转速
f1 = 0
f2 = 0
f3 = 0


def sin(a):
	return robot.sin(a)


def cos(a):
	return robot.cos(a)


def tan(a):
	return robot.tan(a)


def sqrt(a):
	return robot.sqrt(a)


def stop():
	# 1/2/3号电机为移动电机
	robot.set_motor(1, 0)
	robot.set_motor(2, 0)
	robot.set_motor(3, 0)


def move(direction, angle, speed, time=0.0, distance=0, is_first=0):
	f0 = speed
	b = direction
	# 计算转速，逆时针为正
	f1 = cos(a) * sin(b) * f0 - sin(a) * cos(b) * f0 + angle * L2 * 0.01
	f2 = -cos(a) * sin(b) * f0 - sin(a) * cos(b) * f0 + angle * L2 * 0.01
	f3 = cos(b) * f0 + angle * L1 * 0.01

	# 执行
	if is_first == 1:  # 缓慢提高转速(电机不支持小数)
		stop()
		for i in range(800):
			robot.set_motor(3, f3 / 800 * (i + 1))
			robot.set_motor(2, f2 / 800 * (i + 1))
			robot.set_motor(1, f1 / 800 * (i + 1))
	else:  # 直接设置转速
		robot.set_motor(3, f3)
		robot.set_motor(2, f2)
		robot.set_motor(1, f1)

	if time != 0:  # 移动time秒后退出
		robot.sleep(time)
	elif distance != 0:  # 移动distance后退出
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


def get_sensor_data():
	value = [[0, 0, 0, 0, 0, 10], [0, 0, 0, 0, 0, 10]]
	# 读入数据
	for i in range(5):
		value[0][i] = robot.get_channel_gray(4, i + 1)
	for i in range(5):
		value[1][i] = robot.get_gray(i + 7)
	# 转换为编号
	priority = [2, 1, 3, 0, 4]  # 优先级高的通道为1时忽略其他通道读数
	for i in range(2):
		for j in range(5):
			if value[i][priority[j]] > 2000:
				value[i][5] = priority[j]
				break
	return value


def get_current_position(value):
	#  转换为偏移量和偏航角
	if value[0][5] == 10 or value[1][5] == 10:
		return 10, 10
	else:
		# 查表将编号转换为坐标
		g = [G[0][value[0][5]], G[1][value[1][5]]]
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


def change_motor_state(speed):
	global k_p_dis, k_p_ang, p_dis, p_ang, k_i_dis, k_i_ang, i_dis, i_ang
	result = get_current_position(get_sensor_data())
	if result[0] == 10:
		value = get_sensor_data()[0]
		if value[5] != 10:
			distance = [-5, -2, 0, 2, 5]
			global p_baby, k_p_baby
			p_baby = distance[value[5]]
			# robot.set_motor(1, cos(a) * speed - p_baby * k_p_baby)
			# robot.set_motor(2, - cos(a) * speed - p_baby * k_p_baby)
		else:
			move(pie / 2, 0, 30)
	else:
		p_dis = -result[0]
		# p_ang = result[1] - pie / 2
		# i_dis += p_dis
		# i_ang += p_ang
		# print(p_dis)
		# print(p_dis)
		move(p_dis * k_p_dis + i_dis * k_i_dis + p_ang + pie / 2, p_ang * k_p_ang + i_ang * k_i_ang, speed, 0, 0, 0)


def line_navigation(speed, time=0.0):
	robot.reset_timer(0)
	# change_motor_state(speed)
	baby_change(speed)
	if time != 0:
		while robot.get_timer_ms(0) < time * 1000:
			baby_change(speed)


def baby_change(speed):
	value = get_sensor_data()[0]
	if value[5] != 10:
		distance = [-5, -2, 0, 2, 5]
		global p_baby, k_p_baby
		p_baby = distance[value[5]]
		robot.set_motor(1, cos(a) * speed - p_baby * k_p_baby)
		robot.set_motor(2, - cos(a) * speed - p_baby * k_p_baby)
		robot.set_motor(3, 0)
	else:
		move(pie / 2, 0, speed)


def baby_navigation(speed, time=0):
	robot.reset_timer(1)
	baby_change(speed)
	while robot.get_timer_ms(1) < time * 1000:
		baby_change(speed)


# 如果初始状态前排传感器外侧通道识别到线就往前以移动至脱离
def navigate_to_next_cross(speed):
	global p_dis, p_ang, p_baby
	p_dis = 0
	p_ang = 0
	p_baby = 0
	value = get_sensor_data()
	if value[0][0] > 2000 or value[0][4] > 2000:
		while value[0][0] > 2000 or value[0][4] > 2000:
			line_navigation(speed, 0.5)
			value = get_sensor_data()
	value = get_sensor_data()
	while value[0][0] < 2000 and value[0][4] < 2000:
		line_navigation(speed)
		value = get_sensor_data()


def baby_navigate_to(speed, is_cross, offsite_dis=0, offsite_ang=0):
	global p_baby
	p_baby = 0
	if is_cross != 0:
		move(pie / 2, 0, speed)
		value = get_sensor_data()
		while value[0][0] == 1 or value[0][4] == 1:
			value = get_sensor_data()
	value = get_sensor_data()
	# 集成传感器0/4任意一个碰到黑线退出
	while value[0][0] == 0 and value[0][4] == 0:
		value = get_sensor_data()
		baby_change(30)


def navigate_turn_left():
	move(pie / 2, 0, 30, 0, 600, 0)
	stop()
	move(0, 300, 0)
	robot.sleep(0.2)
	while get_sensor_data()[0][5] != 10:
		pass
	while get_sensor_data()[0][2] < 2000:
		pass
	stop_and_sleep()


def navigate_turn_right():
	move(pie / 2, 0, 30, 0, 600, 0)
	stop()
	move(0, -300, 0)
	robot.sleep(0.2)
	while get_sensor_data()[0][5] != 10:
		pass
	while get_sensor_data()[0][2] < 2000:
		pass
	stop_and_sleep()


# 用前排集成传感器巡线一直等到后排传感器5/11都识别不到线
def get_out(speed):
	# 当7/11传感器识别都识别不到的时候，用前排集成传感器巡线
	while robot.get_gray(7) < 2000 and robot.get_gray(11) < 2000:
		baby_change(30)
	# 当7/11传感器都识别不到线的时候，用前排集成传感器继续巡线
	while robot.get_gray(7) > 2000 or robot.get_gray(11) > 2000:
		baby_change(30)


def leave_base():
	move(pie / 2, 0, 30, 0, 0, 1)
	# 等待集成port 4， channel 2 （集成中间传感器） 找到黑线
	sleep_until(4, 2, 1, 0)
	value = get_sensor_data()
	# 等待集成传感器外侧两个都离开黑线
	while value[0][5] == 0 or value[0][5] == 4:
		value = get_sensor_data()

	# 等待独立传感器5、11 任意一个碰到黑线
	while robot.get_gray(5) < 2500 and robot.get_gray(11) < 2500:
		baby_change(30)

	# 等待独立传感器5、11 都离开黑线
	while robot.get_gray(5) > 2000 or robot.get_gray(11) > 2000:
		baby_change(30)

	# print(get_result())


def stop_and_sleep():
	stop()
	robot.sleep(0.1)


def sleep_until(port, channel, condition, wait):
	robot.sleep(wait)
	if condition == 1:
		if port == 4:
			while get_sensor_data()[0][channel] < 2000:
				pass
		else:
			while get_sensor_data()[1][channel] < 2000:
				pass
	else:
		if port == 4:
			while get_sensor_data()[0][channel] > 2000:
				pass
		else:
			while get_sensor_data()[1][channel] > 2000:
				pass


def line_find(position):
	return position[0] != 10


def turn_to_find_line():
	if line_find(get_current_position(get_sensor_data())):
		return
	robot.reset_timer(2)
	move(0, 200, 0, 0, 0, 0)
	while robot.get_timer_ms(2) < 1500:
		if line_find(get_current_position(get_sensor_data())):
			stop()
			return
	robot.reset_timer(2)
	move(0, -200, 0, 0, 0, 0)
	while robot.get_timer_ms(2) < 3000:
		if line_find(get_current_position(get_sensor_data())):
			stop()
			return



events = []


def init_event():
	global events
	events = []
	robot.reset_timer(3)


def add_event(event_id):
	events.append([robot.get_timer_ms(3), event_id, get_sensor_data(), [f1, f2, f3]])


def print_event():
	robot.sleep(0.5)
	print("start")
	event = -1
	while True:
		if robot.check_key(1) == 1:
			print("end")
			robot.sleep(0.5)
			return
		elif robot.check_key(2) == 1:
			if event > 0:
				event -= 1
				for data in events[event]:
					print(data)
			else:
				print("out_of_range")
			robot.sleep(0.5)
		elif robot.check_key(3) == 1:
			if event < len(events) - 1:
				event += 1
				for data in events[event]:
					print(data)
				robot.sleep(0.5)
			else:
				print("out_of_range")
