from base import *


def move_to(destination):
	if destination == 1:
		move(2.8, 0, 30, 0, 0, 1)
		wait_for(4, 3, True, 1)
		navigate_to(30, 0, 0, 1)
		move(1.7, 0, 30, 0, 0, 0)
		wait_for(3, 3, True, 0.5)
		get_out(20)
		stop_and_sleep()
		correction()
		stop()

	elif destination == 2:
		leave()
		navigate_to(30, 0, 0, 0)
		stop()
		move(1.25, 0, 30, 0, 0, 0)
		robot.sleep(0.5)
		while get_result()[0][5] == 10:
			pass
		get_out(10)
		baby_navigation(10, 0, 0, 0.3)
		stop()
		correction()

	elif destination == 3:
		leave()
		navigate_to(30, 0, 0, 0)
		move(pie / 2, 0, 30, 0, 0, 0)
		robot.sleep(0.5)
		# while get_result()[0][5] == 10:
		# 	pass
		right()
		navigate_to(30, 0, 0, 1)
		left()
		robot.sleep(0.1)
		get_out(20)
		correction()
		stop()

	elif destination == 4:
		leave()
		navigate_to(30, 0, 0, 0)
		move(pie / 2, 0, 30, 0, 0, 1)
		robot.sleep(0.5)
		while get_result()[0][5] == 10:
			pass
		stop()
		right()
		navigate_to(30, 0, 0, 1)
		navigate_to(30, 0, 0, 1)
		move(1.4, 0, 30, 0, 0, 1)
		robot.sleep(0.5)
		# while get_result()[0][5] == 10:
		# 	pass
		left()
		navigate_to(30, 0, 0, 0)
		right()
		get_out(20)

	elif destination == 5:
		leave()
		navigate_to(30, 0, 0, 0)
		move(pie / 2, 0, 30, 0, 0, 1)
		robot.sleep(0.5)
		while get_result()[0][5] == 10:
			pass
		stop()
		right()
		navigate_to(30, 0, 0, 1)
		navigate_to(30, 0, 0, 1)
		move(pie / 2, 0, 30, 0, 0, 1)
		robot.sleep(0.5)
		while get_result()[0][5] == 10:
			pass
		right()
		navigate_to(30, 0, 0, 0)
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
		while get_result()[0][5] == 10:
			pass
		robot.sleep(0.5)
		while get_result()[0][5] == 10:
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
		while get_result()[0][5] == 10:
			pass
		correction()

	elif destination == 8:
		move(2.7, 0, 30, 0, 0, 0)
		robot.sleep(1)
		while robot.get_channel_gray(3, 3) < 1500:
			pass
		move(0, 300, 0, 0, 3520, 1)
		stop()

	elif destination == 9:
		leave()
		navigate_to(30, 0, 0, 0)
		stop()
		robot.sleep(0.1)
		left()
		navigate_to(30, 0, 0, 1)
		move(pie / 2, 0, 30, 0, 0, 0)
		robot.sleep(0.5)
		while get_result()[0][5] == 10:
			pass
		navigate_to(30, 0, 0, 1)
		stop()
		robot.sleep(0.3)
		left()
		navigate_to(30, 0, 0, 1)
		stop()
		robot.sleep(0.3)
		right()
		get_out(20)
		correction()

	elif destination == 10:
		move(2.65, 0, 30, 0, 0, 0)
		robot.sleep(1)
		while robot.get_channel_gray(3, 3) < 1500:
			pass
		robot.sleep(0.5)
		while robot.get_channel_gray(3, 3) < 1500:
			pass
		correction()
		navigate_to(30, 0, 0, 0)
		navigate_to(30, 0, 0, 1)
		left()
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
		move(-1.3, 0, 30, 0, 7000, 1)
		stop()

	elif place == 2:
		move(pie, 0, 20, 0, 1000, 1)
		move(-pie / 2, 0, 50, 0, 4000, 1)
		stop()

	elif place == 3:
		i = 300
		for j in range(3):
			move(0, i, 0, 0, 0, 0)
			i *= 0.997
		robot.sleep(0.3)
		while get_result()[0][2] == 0:
			for j in range(3):
				move(0, i, 0, 0, 0, 0)
				i *= 0.997
		stop_and_sleep()
		navigate_to(30, 0, 0, 1)
		right()
		go_back(2)

	elif place == 4:  # 前排传感器在蓝线处
		i = 300
		for j in range(3):
			move(0, i, 0, 0, 0, 0)
			i *= 0.998
		robot.sleep(0.3)
		while get_result()[0][2] == 0:
			for j in range(3):
				move(0, i, 0, 0, 0, 0)
				i *= 0.998
		stop_and_sleep()
		move(2.3, 0, 30, 0, 0, 0)
		wait_for(4, 3, 1, 0.5)
		navigate_to(30, 0, 0, 0)
		navigate_to(30, 0, 0, 1)
		right()
		go_back(2)

	elif place == 5:  # 前排传感器在蓝线处
		i = 300
		for j in range(3):
			move(0, i, 0, 0, 0, 0)
			i *= 0.998
		robot.sleep(0.3)
		while get_result()[0][2] == 0:
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
		while get_result()[0][2] == 0:
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


def finish_1(place, direction):
	if direction == 1 or direction == 3:
		# 前往
		# move_to(place)
		# 完成
		baby_navigation(30, 0, 0, 1.5)
		# 返回
		move(-pie / 2, 0, 30, 0, 1000, 1)
		go_back(place)
	# if place == 1:
	# 	if direction == 1 or direction == 3:
	# 		#  前往1号位前方
	# 		# move(2.8, 0, 30, 0, 0, 1)
	# 		# wait_for(4, 3, True, 1)
	# 		# navigate_to(30, 0, 0, 1)
	# 		# move(1.7, 0, 30, 0, 0, 0)
	# 		# wait_for(3, 3, True, 0.5)
	# 		# get_out(20)
	# 		# stop_and_sleep()
	# 		# correction(-1)
	# 		# stop()
	# 		#  完成任务
	# 		baby_navigation(30, 0, 0, 1.5)
	# 		# 返回
	# 		stop_and_sleep()
	# 		move(-1.3, 0, 30, 0, 7000, 1)
	# 		stop()
	# 	else:
	# 		#  完成
	# 		move(pie, -10, 30, 0, 3000, 1)
	# 		stop_and_sleep()
	# 		move(pie / 2, 0, 50, 0, 1500, 1)
	# 		stop_and_sleep()
	# 		#  返回
	# 		move(-pie / 2, 0, 30, 0, 700, 1)
	# 		stop_and_sleep()
	# 		move(0, 15, 30, 0, 3000, 1)
	# 		stop_and_sleep()
	# 		move(0.6, 0, 50, 0, 5000, 1)
	# 		stop_and_sleep()
	# 		move(pie / 2, 0, 50, 0, 4000, 1)
	# 		stop()
	# elif place == 2:
	# 	if direction == 1 or direction == 3:
	# 		# 前往
	# 		# leave()
	# 		# navigate_to(30, 0, 0, 0)
	# 		# stop()
	# 		# move(1.25, 0, 30, 0, 0, 0)
	# 		# robot.sleep(0.5)
	# 		# while get_result()[0][5] == 10:
	# 		# 	pass
	# 		# get_out(10)
	# 		# baby_navigation(10, 0, 0, 0.3)
	# 		# stop()
	# 		# correction(-1)
	# 		# 完成
	# 		baby_navigation(30, 0, 0, 1.5)
	# 		#  返回
	# 		stop_and_sleep()
	# 		move(-1.6, 0, 50, 0, 6000, 0)
	# 		stop()
	# 	else:
	# 		move(pie, 0, 20, 0, 3000, 1)
	# 		stop_and_sleep()
	#
	#
	#
