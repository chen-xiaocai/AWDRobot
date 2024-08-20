from correct import *
from move1 import *


def complete_1(place, direction):
	if direction == TASK_DIR_FRONT or direction == TASK_DIR_BACK:
		correction()
		ability = [1, 2, 3, 4, 5, 6, 7, 9, 10]
		if place in ability:
			line_navigation(20, 1.5)
		else:
			line_navigation(20, 2.5)
	else:
		ability = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
		if place in ability:
			move(pie / 2, 0, 20, 1.5)
			stop()


def complete_2(place, direction):
	if direction == TASK_DIR_FRONT:
		correction()
		ability = [1, 2, 3, 4, 5, 6, 7, 9, 10]
		if place in ability:
			line_navigation(20, 0.8)
			stop_and_sleep()
			move(0, 0, 20, 0.1)
			stop_and_sleep()
			robot.reset_encoder(4)
			robot.set_motor(4, 100)
			while robot.get_encoder(4) < 1100:
				pass
			robot.set_motor(4, 0)
		ability = [8]
		if place in ability:
			line_navigation(20, 1.5)
			stop_and_sleep()
			move(0, 0, 20, 0.1)
			stop_and_sleep()
			robot.reset_encoder(4)
			robot.set_motor(4, 100)
			while robot.get_encoder(4) < 1100:
				pass
			robot.set_motor(4, 0)
	else:
		move(pie / 2, 0, 20, 0.8)
		stop_and_sleep()
		move(0, 0, 20, 0.1)
		stop_and_sleep()
		robot.reset_encoder(4)
		robot.set_motor(4, 100)
		while robot.get_encoder(4) < 1100:
			pass
		robot.set_motor(4, 0)


def complete_3(place, direction):
	if direction == TASK_DIR_FRONT:
		correction()
		if place == 8:
			line_navigation(20, 2)
		else:
			line_navigation(20, 1)
		move(-pie / 2, 0, 20, 0.2)
		move(pie / 2, 0, 100, 0.5)
		stop()
	elif direction == TASK_DIR_BACK:
		correction()
		if place == 8:
			line_navigation(20, 2)
		# 往后退一定距离，准备动作
		move(-pie / 2, 0, 10)  # 退后一点点
		value = get_sensor_data()[1]
		while value[0] < 2000 and value[4] < 2000:
			value = get_sensor_data()[1]
		stop()

		# 第一次往下啄
		robot.set_motor(4, 30)  # 向下啄
		robot.sleep(0.4)
		robot.set_motor(4, -100)  # 抬起鸡嘴
		robot.sleep(0.06)
		robot.set_motor(4, 0)
		stop_and_sleep()

		# 前进到底顶住道具
		line_navigation(30, 0.5)

		# 开始钩道具动作
		robot.set_motor(4, 20)  # 钩住
		robot.sleep(0.17)
		robot.set_motor(4, 0)

		# 往后退
		move(-pie / 2, 0, 10, 0, 0, 1)  # 往后退将红方块拉出
		robot.sleep(1)

		# 往前走适配goback
		robot.set_motor(4, -100)  # 抬起鸡嘴
		robot.sleep(0.06)
		robot.set_motor(4, 0)
		move(pie / 2, 0, 20, 1)
		stop()




def do_complete_task_pos11(task):
	if task == TASK_ID_11_Y:
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
		move(pie, 0, 50, 0.5)
		stop()
	elif task == TASK_ID_11_R:
		move(pie / 2, 0, 20, 0.5)
		navigate_to_next_cross(20)
		move(-pie / 2, 0, 10, 0.5, 0, 1)
		stop_and_sleep()
		move(0, 0, 10, 0.9, 0, 1)
		stop()
		robot.set_motor(4, -100)
		robot.sleep(0.07)
		robot.set_motor(4, 0)
		move(pie, 0, 10, 0.3)
		stop_and_sleep()
		robot.set_motor(4, -100)
		robot.sleep(0.07)
		robot.set_motor(4, 0)
		move(-pie / 2, 0, 30, 0.5)
		stop()
	elif task == TASK_ID_11_B:
		add_event(1103)
		move_to_11()  # 前往
		line_navigation(20, 0.3)  # 完成任务
		stop()
		add_event(1)
		correction()  # 矫正
		add_event(2)
		stop()
		robot.sleep(2)
		line_navigation(30, 1)  # 捅方块
		stop_and_sleep()
		robot.set_motor(4, 100)  # 转摇杆
		robot.sleep(1.8)
		robot.set_motor(4, 0)
		move(-pie / 2, 0, 10, 0.8)  # 前往黄色方块任务区域
		stop_and_sleep()
		move(0, 0, 20)  # 向右平移
		sleep_until(4, 2, 1, 0.5)
		stop_and_sleep()
		add_event(3)
		navigate_to_next_cross(30)
		add_event(4)
		get_out(20)
		add_event(5)
		correction()
		add_event(6)
		line_navigation(20, 0.9)  # 到黄色方块旁边
		move(0, 300, 0, 0.5)  # 转向黄色方块
		stop_and_sleep()
		move(pie / 2, 0, 20, 0.7)  # 捅黄色方块,反复捅确保捅下
		move(-pie / 2, 0, 20, 0.3)
		move(0, 0, 20, 0.3)
		move(pie / 2, 0, 20, 0.5)
		move(-pie / 2, 0, 20, 0.5)  # 返回
		move(0, -300, 0, 0.5)
		stop_and_sleep()
		line_navigation(30, 1)
		navigate_to_next_cross(30)
		add_event(8)
		navigate_turn_left()
		add_event(9)
		move(1.9, 0, 50, 1.5)
		stop()

	elif task == 4:
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
	else:
		raise ValueError("invalid task:{}".format(task))
