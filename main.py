import robot
from task2 import *
from correct import *
from back import *


def complete_1(place, direction):
	if direction == 0 or direction == 2:
		correction()
		ability = [1, 2, 3, 4, 5, 6, 7, 9, 10]
		if place in ability:
			line_navigation(20, 1.5)
		ability = [8]
		if place in ability:
			line_navigation(20, 2.5)


def complete_2(place, direction):
	if direction == 0:
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
	elif direction == TASK_DIR_RIGHT:
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


# def finish_1(place, direction):
# 	if direction == 1 or direction == 3:
# 		# 前往
# 		move_to(place)
# 		stop()
# 		# robot.sleep(3)
# 		# # 完成
# 		complete_1(place)
# 		# # 返回
# 		# go_back(place)
#
#
# def finish_2(place, direction):
# 	if direction == 1:
# 		# 前往
# 		move_to(place)
# 		stop()
# 		# # 完成
# 		complete_2(place)
# 		# # 返回
# 		# go_back(place)
#
#
# def finish_3(place, direction):
# 	if direction == 1 or direction == 3:
# 		# 前往
# 		move_to(place)
# 		stop_and_sleep()
# 		# 完成
# 		complete_3(place, direction)
# 		# 返回
# 		go_back(place)


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
		navigate_to_next_cross(30)
		add_event(7)
		line_navigation(30, 0.5)
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


def move_to(destination, direction):
	func = [None, move_to_1, move_to_2, move_to_3, move_to_4, move_to_5, move_to_6, move_to_7, move_to_8, move_to_9,
			 move_to_10, move_to_11]
	func_side = [None, move_to_1_side, move_to_2_side, move_to_3_side, move_to_4_side, move_to_5_side,
				 move_to_6_side, move_to_7_side, move_to_8_side, move_to_9_side, move_to_10_side]
	if direction == TASK_DIR_FRONT or direction == TASK_DIR_BACK:
		func[destination]()
	else:
		func_side[destination]()


TASK_DIR_FRONT = 0
TASK_DIR_LEFT = 1
TASK_DIR_RIGHT = 2
TASK_DIR_BACK = 3

TASK_ID_1 = 0  # 一号任务
TASK_ID_2 = 1  # 二号任务
TASK_ID_3 = 2  # 三号任务
TASK_ID_11_R = 3  # 11号位置红色方块落脚点闸门
TASK_ID_11_Y = 4  # 11号位置黄色方块落脚点闸门
TASK_ID_11_B = 5  # 11号位置旋转门大任务
TASK_ID_X1 = 6  # 现场任务1
TASK_ID_X2 = 7  # 现场任务2


def execute_task(position, task_id, direction):
	if task_id == TASK_ID_1:
		complete_1(position, direction)
	elif task_id == TASK_ID_2:
		complete_2(position, direction)
	elif task_id == TASK_ID_3:
		complete_3(position, direction)
	else:
		pass


def main():
	task_list = [
		[1, TASK_ID_1, TASK_DIR_FRONT, "1_1"],
		[2, TASK_ID_1, TASK_DIR_FRONT, "1_2"],
		[3, TASK_ID_1, TASK_DIR_FRONT, "1_3"],
		[4, TASK_ID_1, TASK_DIR_FRONT, "1_4"],
		[5, TASK_ID_1, TASK_DIR_FRONT, "1_5"],
		[6, TASK_ID_1, TASK_DIR_FRONT, "1_6"],
		[7, TASK_ID_1, TASK_DIR_FRONT, "1_7"],
		[8, TASK_ID_1, TASK_DIR_FRONT, "1_8"],
		[9, TASK_ID_1, TASK_DIR_FRONT, "1_9"],
		[10, TASK_ID_1, TASK_DIR_FRONT, "1_10"],

		[1, TASK_ID_2, TASK_DIR_FRONT, "2_1"],
		[2, TASK_ID_2, TASK_DIR_FRONT, "2_2"],
		[3, TASK_ID_2, TASK_DIR_FRONT, "2_3"],
		[4, TASK_ID_2, TASK_DIR_FRONT, "2_4"],
		[5, TASK_ID_2, TASK_DIR_FRONT, "2_5"],
		[6, TASK_ID_2, TASK_DIR_FRONT, "2_6"],
		[7, TASK_ID_2, TASK_DIR_FRONT, "2_7"],
		[8, TASK_ID_2, TASK_DIR_FRONT, "2_8"],
		[9, TASK_ID_2, TASK_DIR_FRONT, "2_9"],
		[10, TASK_ID_1, TASK_DIR_FRONT, "2_10"],

		[1, TASK_ID_3, TASK_DIR_FRONT, "3_1"],
		[2, TASK_ID_3, TASK_DIR_FRONT, "3_2"],
		[3, TASK_ID_3, TASK_DIR_FRONT, "3_3"],
		[4, TASK_ID_3, TASK_DIR_FRONT, "3_4"],
		[5, TASK_ID_3, TASK_DIR_FRONT, "3_5"],
		[6, TASK_ID_3, TASK_DIR_FRONT, "3_6"],
		[7, TASK_ID_3, TASK_DIR_FRONT, "3_7"],
		[8, TASK_ID_3, TASK_DIR_FRONT, "3_8"],
		[9, TASK_ID_3, TASK_DIR_FRONT, "3_9"],
		[10, TASK_ID_3, TASK_DIR_FRONT, "3_10"],

		# [2, TASK_ID_2, TASK_DIR_FRONT, '2_2'],
		# [3, TASK_ID_3, TASK_DIR_FRONT, "3_3"],
		# [11, TASK_ID_11_R, TASK_DIR_FRONT, "11_R"],
		# [11, TASK_ID_11_Y, TASK_DIR_FRONT, "11_Y"],
		# [11, TASK_ID_11_B, TASK_DIR_FRONT, "11_B"],

		# [4, TASK_ID_X1, TASK_DIR_FRONT],
		# [5, TASK_ID_X2, TASK_DIR_FRONT],

		[999, 999, 0, "EVENT"]
	]

	task_id, pos, direction = 0, 0, 0

	next_task_index = 0
	while True:
		print("TASK To DO: ", task_list[next_task_index][3])
		while True:
			if robot.check_key(1) == 1:  # Enter
				pos, task_id, direction, name = task_list[next_task_index]
				if next_task_index < (len(task_list) - 1):
					next_task_index += 1
				break
			elif robot.check_key(2) == 1:  # LEFT
				if next_task_index > 0:
					next_task_index -= 1
				print("TASK TO DO: ", task_list[next_task_index][3])
				robot.sleep(0.3)
				continue
			elif robot.check_key(3) == 1:  # right
				if (next_task_index + 1) < len(task_list):
					next_task_index += 1
				print("TASK_TO_DO: ", task_list[next_task_index][3])
				robot.sleep(0.3)
				continue
			else:
				pass

		if TASK_ID_1 <= task_id <= TASK_ID_3:
			init_event()
			move_to(pos, direction)  # share by all position and task
			execute_task(pos, task_id, direction)
			go_back(pos)
		elif TASK_ID_11_R <= task_id <= TASK_ID_11_B:
			init_event()
			do_complete_task_pos11(task_id)
		elif task_id == TASK_ID_X1:
			pass
		elif task_id == TASK_ID_X2:
			pass
		else:
			robot.sleep(1)
			print_event()


main()
