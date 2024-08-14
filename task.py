import robot
from base import *


def move_to(destination):
	if destination == 1:  # 后排传感器离开路口
		leave()
		navigate_to(30)
		left()
		navigate_to(30)
		# 直走
		move(pie / 2, 0, 30, 0, 0, 0)
		# 等到左侧传感器识别到线
		wait_for(4, 0, 1, 0.5)
		navigate_to(30)
		right()
		navigate_to(30)
		right()
		navigate_to(30)
		left()
		get_out(20)
		stop()

		# 前排传感器在1号位前十字路口，无矫正
	elif destination == 2:
		leave()
		navigate_to(30, 0)
		stop()
		move(1.25, 0, 30, 0, 0, 0)
		robot.sleep(0.5)
		while get_sensor_data()[0][5] == 10:
			pass
		get_out(10)
		baby_navigation(10, 0)
		stop()
		correction()

	elif destination == 3:
		leave()
		navigate_to(30, 0)
		move(pie / 2, 0, 30, 0, 0, 0)
		wait_for(4, 2, 1, 0.5)
		right()
		navigate_to(30, 0)
		left()
		get_out(20)
		baby_navigation(20, 0.3)
		correction()
		stop()

	elif destination == 4:
		leave()
		navigate_to(30, 0)
		move(pie / 2, 0, 30, 0, 0, 1)
		wait_for(4, 2, 1, 0.5)
		right()
		navigate_to(30, 1)
		navigate_to(30, 1)
		move(1.3, 0, 30, 0, 0, 1)
		wait_for(4, 0, 1, 0.5)
		left()
		navigate_to(30, 0)
		right()
		get_out(20)
		baby_navigation(20, 0.5)
		correction()
		print(get_sensor_data())

	elif destination == 5:
		leave()
		navigate_to(30, 0)
		move(pie / 2, 0, 30, 0, 0, 1)
		robot.sleep(0.5)
		while get_sensor_data()[0][5] == 10:
			pass
		stop()
		right()
		navigate_to(30, 1)
		navigate_to(30, 1)
		move(pie / 2, 0, 30, 0, 0, 1)
		robot.sleep(0.5)
		while get_sensor_data()[0][5] == 10:
			pass
		right()
		navigate_to(30, 0)
		left()
		get_out(20)

	elif destination == 6:
		move(- pie / 2, 0, 20, 0, 0, 1)
		while robot.get_gray(7) < 2500:
			pass
		move(pie / 2, 0, 20, 0, 400, 1)
		stop()
		robot.sleep(0.1)
		move(pie, 0, 30, 0, 0, 1)
		robot.sleep(1)
		while get_sensor_data()[0][5] == 10:
			pass
		robot.sleep(0.5)
		while get_sensor_data()[0][5] == 10:
			pass
		stop()
		correction()

	elif destination == 7:
		move(- pie / 2, 0, 20, 0, 0, 1)
		while robot.get_gray(7) < 2500:
			pass
		move(pie / 2, 0, 20, 0, 400, 1)
		stop()
		robot.sleep(0.1)
		move(pie, 0, 30, 0, 0, 1)
		robot.sleep(1)
		while get_sensor_data()[0][5] == 10:
			pass
		correction()

	elif destination == 8:  # 位子随缘，听凭风引
		move(2.7, 0, 30, 0, 0, 0)
		wait_for(4, 2, 1, 1)
		navigate_to(30)
		i = -300
		while get_sensor_data()[0][5] != 10:
			for j in range(3):
				move(0, i, 0, 0, 0, 0)
				i *= 0.999
		print(get_sensor_data())
		while get_sensor_data()[0][2] < 2000:
			for j in range(3):
				move(0, i, 0, 0, 0, 0)
				i *= 0.999
		stop()
		robot.sleep(0.1)
		line_navigation(30, 1)
		stop()

	elif destination == 9:  # 后排传感器离开路口
		move(2.7, 0, 30, 0, 0, 1)
		wait_for(4, 2, 1, 1)
		stop_and_sleep()
		navigate_to(30)
		left()
		navigate_to(30)
		left()
		navigate_to(30)
		right()
		get_out(30)
		stop()

	elif destination == 10:  # 后排传感器离开路口
		move(2.7, 0, 30, 0, 0, 1)
		wait_for(4, 2, 1, 1)
		stop_and_sleep()
		navigate_to(30)
		left()
		navigate_to(30)
		right()
		navigate_to(30)
		left()
		get_out(20)
		stop_and_sleep()
		line_navigation(20, 0.5)
		stop_and_sleep()
		correction()
		stop_and_sleep()
		stop()

	elif destination == 11:
		correction()
		navigate_to(30, 0, 0, 0)
		navigate_to(30, 0, 0, 1)
		left()
		stop()
		correction()
		navigate_to(30, 0, 0, 0)
		navigate_to(30, 0, 0, 1)
		left()
		stop()
		correction()
		navigate_to(30, 0, 0, 0)
		navigate_to(30, 0, 0, 1)
		left()
		stop()

	elif destination == 12:
		left()
		stop()
		correction()
		navigate_to(30, 0, 0, 0)
		navigate_to(30, 0, 0, 1)
		left()
		left()
		stop()
		correction()
		navigate_to(30, 0, 0, 0)
		navigate_to(30, 0, 0, 1)
		left()

	else:
		left()
		stop()
		correction()
		navigate_to(30, 0, 0, 0)
		navigate_to(30, 0, 0, 1)
		left()
		left()
		stop()
		correction()
		navigate_to(30, 0, 0, 0)
		navigate_to(30, 0, 0, 1)
		left()


def go_back(place):  # 中心点在转角
	if place == 1:
		move(-pie / 2, 0, 30, 0, 1000, 1)
		move(-1.2, 0, 30, 0, 6000, 1)
		stop()

	elif place == 2:
		move(-pie / 2, 0, 30, 0, 1000, 1)
		move(pie, 0, 20, 0, 1000, 1)
		move(-pie / 2, 0, 50, 0, 4000, 1)
		stop()

	elif place == 3:
		move(-pie / 2, 0, 30, 0, 0, 1)
		wait_for(0, 2, 1, 0)
		stop_and_sleep()
		i = 300
		for j in range(3):
			move(0, i, 0, 0, 0, 0)
			i *= 0.998
		robot.sleep(0.3)
		while get_sensor_data()[0][2] == 0:
			for j in range(3):
				move(0, i, 0, 0, 0, 0)
				i *= 0.998
		navigate_to(30, 0)
		right()
		move(pie, 0, 20, 0, 1000, 1)
		move(-pie / 2, 0, 50, 0, 4000, 1)
		stop()

	elif place == 4:  # 前排传感器在蓝线处
		move(-pie / 2, 0, 20, 0, 300, 1)
		i = 300
		for j in range(3):
			move(0, i, 0, 0, 0, 0)
			i *= 0.999
		robot.sleep(0.3)
		while get_sensor_data()[0][2] == 0:
			for j in range(3):
				move(0, i, 0, 0, 0, 0)
				i *= 0.999
		stop_and_sleep()
		move(2.2, 0, 30, 0, 0, 0)
		wait_for(4, 0, 1, 0.5)
		baby_navigation(30, 2)
		navigate_to(30, 0, 0, 0)
		right()
		move(pie, 0, 20, 0, 1000, 1)
		move(-pie / 2, 0, 50, 0, 4000, 1)
		stop()

	elif place == 5:  # 前排传感器在蓝线处
		i = 300
		for j in range(3):
			move(0, i, 0, 0, 0, 0)
			i *= 0.998
		robot.sleep(0.3)
		while get_sensor_data()[0][2] == 0:
			for j in range(3):
				move(0, i, 0, 0, 0, 0)
				i *= 0.998
		stop_and_sleep()
		navigate_to(30, 0, 0, 0)
		move(pie / 2, 0, 30, 0, 0, 0)
		wait_for(4, 2, 1, 0.5)
		right()
		navigate_to(30, 0, 0, 0)
		left()
		navigate_to(30, 0, 0, 0)
		navigate_to(30, 0, 0, 1)
		right()
		go_back(2)

	elif place == 6:
		i = -300
		for j in range(3):
			move(0, i, 0, 0, 0, 0)
			i *= 0.997
		robot.sleep(0.3)
		while get_sensor_data()[0][2] == 0:
			for j in range(3):
				move(0, i, 0, 0, 0, 0)
				i *= 0.997
		navigate_to(30, 0, 0, 0)
		stop_and_sleep()
		move(pie, 0, 30, 0, 1000, 1)
		stop_and_sleep()
		move(pie / 2, 0, 50, 0, 3000, 1)
		stop()

	elif place == 7:
		move(0, 0, 50, 1, 0, 0)
		stop()

	elif place == 8:
		move(pie, 0, 30, 0, 2000, 1)
		stop()

	elif place == 9:
		move(-pie / 2, 0, 30, 0, 5000, 1)
		stop()

	elif place == 10:
		move(-2.4, 0, 30, 0, 7500, 1)
		stop()


def complete_1(place):
	if place == 1:
		pass
	elif place == 10:
		line_navigation(20, 0.5)


def complete_2(place):
	if place == 1:
		pass
	elif place == 10:
		line_navigation(20, 0.5)
		stop()
		robot.reset_encoder(4)
		robot.set_motor(4, 100)
		while robot.get_encoder(4) < 1100:
			pass
		robot.set_motor(4, 0)


def complete_3(place):
	if place == 1:
		pass
	elif place == 10:
		line_navigation(20, 0.5)
		robot.set_motor(2, -100)
		robot.sleep(1)
		stop()


def finish_1(place, direction):
	if direction == 1 or direction == 3:
		# 前往
		move_to(place)
		stop()
		# robot.sleep(3)
		# # 完成
		complete_1(place)
		# # 返回
		# go_back(place)


def finish_2(place, direction):
	if direction == 1:
		# 前往
		move_to(place)
		stop()
		# # 完成
		complete_2(place)
		# # 返回
		# go_back(place)


def finish_3(place, direction):
	if direction == 1 or direction == 3:
		# 前往
		move_to(place)
		stop()
		# robot.sleep(3)
		# # 完成
		complete_3(place)
		# # 返回
		# go_back(place)


def finish_11(task):
	if task == 1:
		move(0, 0, 10, 3.2, 0, 1)
		stop_and_sleep()
		move(pie / 2, 0, 10, 2, 0, 1)
		stop_and_sleep()
		robot.set_motor(4, 100)
		robot.sleep(0.07)
		robot.set_motor(4, 0)
		move(-pie / 2, 0, 10, 0.2, 0, 1)
		stop_and_sleep()
		robot.set_motor(4, 100)
		robot.sleep(0.07)
		robot.set_motor(4, 0)
	elif task == 2:
		move(pie / 2, 0, 10, 3, 0, 1)
		stop_and_sleep()
		move(0, 0, 10, 0.9, 0, 1)
		robot.set_motor(4, -50)
		robot.sleep(0.15)
		robot.set_motor(4, 0)
		stop()


def main():
	print("v1")
	navigate_to(30)  # 移动至任务面前（顶住）
	left()
	get_out(20)
	line_navigation(20, 1)
	stop_and_sleep()

	move(-pie / 2, 0, 10, 0.3, 0, 1)  # 退后一点点
	stop_and_sleep()

	robot.set_motor(4, 50)  # 向下啄
	robot.sleep(0.13)
	robot.set_motor(4, -50)  # 抬起鸡嘴
	robot.sleep(0.13)
	robot.set_motor(4, 0)
	stop_and_sleep()

	move(pie / 2, 0, 10, 0.5, 0, 1)  # 往前走，顶到
	stop_and_sleep()

	robot.set_motor(4, 50)  # 再次啄
	robot.sleep(0.07)
	robot.set_motor(4, 1)  # 保持鸡嘴不被顶起
	move(-pie / 2, 0, 10, 0.7, 0, 1)  # 往后退将红方块拉出
	stop_and_sleep()
	robot.set_motor(4, -50)  # 抬起鸡嘴
	robot.sleep(0.13)
	robot.set_motor(4, 0)



main()
