import robot
from task1 import *


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


def complete_3(place, direction):
	if direction == 1:
		ability = [1, 3, 4, 5, 6, 9]
		if place in ability:  # 无需矫正的
			line_navigation(20, 1)
			move(-pie / 2, 0, 20, 0.2)
			move(pie / 2, 0, 100, 0.5)
			stop()
		ability = [10]
		if place in ability:
			line_navigation(20, 0.3)
			correction()
			move(0, 0, 20, 0.3)
			correction()
			stop_and_sleep()
			line_navigation(30, 0.5)
			stop()
		ability = [2]
		if place in ability:
			line_navigation(20, 0.1)
			correction()
			move(0, 0, 20, 0.3)
			correction()
			stop_and_sleep()
			line_navigation(30, 1.5)
			stop()
		ability = [7]
		if place in ability:
			correction()
			move(0, 0, 20, 0.3)
			stop()
			move(0, -100, 0, 0.3)
			stop_and_sleep()
			correction()
			stop_and_sleep()
			line_navigation(30, 1)
			stop()
		ability = [8]
		if place in ability:
			line_navigation(20, 1.5)
			correction()
			move(0, 0, 20, 0.3)
			correction()
			stop_and_sleep()
			line_navigation(30, 1)
			stop()
	elif direction == 3:
		ability = [1, 2, 3, 8, 9, 10]
		if place in ability:  # 前排传感器大约在路口
			line_navigation(15, 1.5)
			correction()
			robot.set_motor(1, 100)
			robot.set_motor(2, -100)
			robot.sleep(0.5)
			stop_and_sleep()
			correction()

			# 往后退一定距离，准备动作
			move(-pie / 2, 0, 10, 0.4, 0, 1)  # 退后一点点
			stop_and_sleep()
			correction()

			# 第一次往下啄
			robot.set_motor(4, 10)  # 向下啄
			robot.sleep(1.3)
			robot.set_motor(4, -50)  # 抬起鸡嘴
			robot.sleep(0.13)
			robot.set_motor(4, 0)
			stop_and_sleep()

			# 前进到底顶住道具
			line_navigation(15, 0.5)
			robot.set_motor(1, 100)
			robot.set_motor(2, -100)
			robot.sleep(0.5)
			stop_and_sleep()
			correction()
			move(0, 0, 10, 0.2, 0, 1)
			stop()
			correction()
			stop_and_sleep()
			move(pie / 2, 0, 10)

			# 开始钩道具动作
			for i in range(3):  # 反复通红色方块使其归位
				robot.set_motor(4, 6)  # 向下啄
				robot.sleep(0.8)
				robot.set_motor(4, -3)
				robot.sleep(0.5)
				robot.set_motor(4, -100)  # 抬起鸡嘴
				robot.sleep(0.03)
				robot.set_motor(4, 0)
				stop_and_sleep()
			robot.set_motor(4, 6)  # 钩住
			robot.sleep(0.7)
			robot.set_motor(4, 1)

			# 往后退
			move(-pie / 2, 0, 10, 0, 0, 1)  # 往后退将红方块拉出
			robot.sleep(0.1)
			robot.set_motor(4, 0)
			robot.sleep(2)
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
		stop_and_sleep()
		# 完成
		complete_3(place, direction)
		# 返回
		go_back(place)


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
	if task == 3:
		move_to_11()  # 前往
		line_navigation(20, 0.3)  # 完成任务
		correction()
		line_navigation(10, 2)
		stop_and_sleep()
		robot.set_motor(4, 100)
		robot.sleep(1.8)
		robot.set_motor(4, 0)
		move(-pie / 2, 0, 10, 0.5)
		stop_and_sleep()
		move(0, 0, 10)
		sleep_until(4, 2, 1, 0.5)
		stop_and_sleep()
		navigate_to_next_cross(30)
		stop()
	if task == 4:
		leave_base()
		navigate_to_next_cross(30)
		move(pie / 2, 0, 30, 0, 0, 0)
		sleep_until(4, 2, 1, 0.5)
		move(pie / 2, 0, 30, 0, 600, 0)
		stop()
		move(0, -300, 0, 0.5)
		stop_and_sleep()
		get_out(20)
		line_navigation(10, 1)
		stop()


def main():
	init_event()
	move_to_10()
	complete_3(10, 1)
	go_back_10()
	print_event()

	# while True:
	# 	if robot.check_key(1):
	# 		print(get_sensor_data())
	# 	robot.sleep(1)

	# while True:
	# 	move(0, 0, 20, 2)
	# 	stop_and_sleep()
	# 	move(pie, 0, 20, 2)
	# 	stop_and_sleep()

main()
