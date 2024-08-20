import robot
from correct import *

def move_to_1_left():
	move(2.7, 0, 30, 0, 0, 1)
	sleep_until(4, 2, 1, 1)
	stop_and_sleep()  # 到达8号任务前
	navigate_to_next_cross(30)
	navigate_turn_left()
	navigate_to_next_cross(30)
	navigate_turn_right()
	navigate_to_next_cross(30)  # 移动到10号为前路口转交处
	navigate_turn_right()
	move(-pie / 2, 0, 20)
	sleep_until(4, 4, 1, 0)
	robot.sleep(0.15)
	correction()
	move(pie, 0, 20, 1.4)  # 移动到1号位侧面
	stop()


def move_to_1_right():
	leave_base()
	navigate_to_next_cross(40)
	navigate_turn_left()
	navigate_to_next_cross(40)
	navigate_turn_right()
	navigate_to_next_cross(40)
	navigate_turn_right()
	navigate_turn_right()
	correction()
	navigate_to_next_cross(20)
	move(pie / 2, 0, 20, 0.3)
	move(0, 0, 20, 1.5)
	stop()


def move_to_2_left():
	leave_base()
	navigate_to_next_cross(30)
	navigate_turn_left()
	navigate_to_next_cross(30)
	navigate_turn_right()
	navigate_to_next_cross(30)
	navigate_turn_right()
	line_navigation(20, 0.5)  # 移动至2号位前（
	correction()
	move(-pie / 2, 0, 20, 0.3)
	move(pie, 0, 20, 1.5)  # 移动至2号位侧面(
	stop()


def move_to_2_right():
	leave_base()
	add_event(1)
	navigate_to_next_cross(30)
	add_event(2)
	move(pie / 2, 0, 30, 0, 0, 0)
	sleep_until(4, 2, 1, 0.5)  # 移动至2号位
	add_event(3)
	move(pie / 2, 0, 30, 0, 600, 0)
	stop()
	move(0, -300, 0, 0.5)
	stop_and_sleep()  # 转弯
	add_event(4)
	line_navigation(30, 1)
	add_event(5)
	navigate_to_next_cross(30)  # 移动至3号位路口
	navigate_turn_right()
	navigate_to_next_cross(30)
	move(-pie / 2, 0, 20, 0.5)
	correction()
	move(0, 0, 1.5, 1.5)
	stop()


def move_to_3_left():
	leave_base()
	add_event(1)
	navigate_to_next_cross(30)
	add_event(2)
	move(pie / 2, 0, 30, 0, 0, 0)
	sleep_until(4, 2, 1, 0.5)  # 移动至2号位
	add_event(3)
	move(pie / 2, 0, 30, 0, 600, 0)
	stop()
	move(0, -300, 0, 0.5)
	stop_and_sleep()  # 转弯
	add_event(4)
	line_navigation(30, 1)
	add_event(5)
	navigate_to_next_cross(30)  # 移动至3号位路口
	move(-pie / 2, 0, 20, 0.6)
	correction()
	move(pie, 0, 20, 1.5)
	stop()


def move_to_3_right():
	leave_base()
	add_event(1)
	navigate_to_next_cross(30)
	add_event(2)
	move(pie / 2, 0, 30, 0, 0, 0)
	sleep_until(4, 2, 1, 0.5)  # 移动到2号位
	move(pie / 2, 0, 30, 0, 600, 0)
	stop()
	add_event(3)
	move(0, -300, 0, 0.5)
	stop_and_sleep()
	add_event(4)
	line_navigation(30, 1)
	add_event(5)
	navigate_to_next_cross(30)  # 移动到3号位
	add_event(6)
	navigate_to_next_cross(30)
	navigate_turn_left()
	navigate_to_next_cross(30)
	move(-pie / 2, 0, 30, 0.3)
	correction()
	move(0, 0, 20, 1.5)
	stop()


def move_to_4_left():
	pass


def move_to_4_right():
	leave_base()
	add_event(1)
	navigate_to_next_cross(30)
	add_event(2)
	move(pie / 2, 0, 30, 0, 0, 0)
	sleep_until(4, 2, 1, 0.5)  # 移动到2号位
	move(pie / 2, 0, 30, 0, 600, 0)
	stop()
	add_event(3)
	move(0, -300, 0, 0.5)
	stop_and_sleep()
	add_event(4)
	line_navigation(30, 1)
	add_event(5)
	navigate_to_next_cross(30)  # 移动到3号位
	add_event(6)
	navigate_to_next_cross(30)
	add_event(7)
	move(pie / 2, 0, 30)
	sleep_until(4, 4, 1, 0.5)
	navigate_turn_left()
	move(-pie / 2, 0, 20, 0.4)
	correction()
	move(0, 0, 20, 1.5)  # 移动至4号位侧面（
	stop()

#
# def move_to_5_left():
# 	leave_base()
# 	add_event(1)
# 	navigate_to_next_cross(30)
# 	add_event(2)
# 	move(pie / 2, 0, 30, 0, 0, 0)
# 	sleep_until(4, 2, 1, 0.5)  # 移动到2号位
# 	move(pie / 2, 0, 30, 0, 600, 0)
# 	stop()
# 	add_event(3)
# 	move(0, -300, 0, 0.5)
# 	stop_and_sleep()
# 	add_event(4)
# 	line_navigation(30, 1)
# 	add_event(5)
# 	navigate_to_next_cross(30)  # 移动到3号位
# 	add_event(6)
# 	navigate_to_next_cross(30)
# 	add_event(7)
# 	move(pie / 2, 0, 30)
# 	sleep_until(4, 4, 1, 0.5)
# 	navigate_turn_right()
# 	navigate_to_next_cross(30)  # 移动到5号位
# 	move(-pie / 2, 0, 20, 0.6)
# 	correction()
# 	move(pie, 0, 20, 1.5)
# 	stop()
#
#
# def move_to_5_right():
# 	leave_base()
# 	add_event(1)
# 	navigate_to_next_cross(30)
# 	add_event(2)
# 	move(pie / 2, 0, 30, 0, 0, 0)
# 	sleep_until(4, 2, 1, 0.5)  # 移动到2号位
# 	move(pie / 2, 0, 30, 0, 600, 0)
# 	stop()
# 	add_event(3)
# 	move(0, -300, 0, 0.5)
# 	stop_and_sleep()
# 	add_event(4)
# 	line_navigation(30, 1)
# 	add_event(5)
# 	navigate_to_next_cross(30)  # 移动到3号位
# 	add_event(6)
# 	navigate_to_next_cross(30)
# 	add_event(7)
# 	move(pie / 2, 0, 30)
# 	sleep_until(4, 4, 1, 0.5)
# 	navigate_turn_right()
# 	navigate_to_next_cross(30)  # 移动到5号位
# 	get_out(30)
# 	navigate_turn_left()
# 	move(-pie / 2, 0, 20, 0)
# 	sleep_until(0, 1, 1, 0)
# 	move(pie / 2, 0, 20, 0.2)
# 	correction()
# 	move(0, 0, 20, 1.5)
# 	stop()
#
#
