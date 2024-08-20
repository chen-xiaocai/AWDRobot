import robot
from base import *
from correct import *


def go_back_1_left():
	move(-pie / 2, 0, 20, 0.5, 0, 1)
	move(0, 0, 30, 1, 0, 1)
	move(0, -300, 0, 0.25, 0)
	move(pie/2, 0, 50, 2, 0, 1)
	stop()


def go_back_1_right():
	pass


def go_back_2_left():
	move(-pie / 2, 0, 20, 0.5, 0, 1)
	move(0, -300, 0, 0.45, 0)
	move(pie/2, 0, 50, 2, 0, 1)
	stop()


def go_back_2_right():
	pass


def go_back_3_left():
	move(-pie / 2, 0, 20, 0.5, 0, 1)
	move(0, 0, 20, 0, 0, 1)
	sleep_until(4, 2, 1, 0)
	correction()
	move(0, -300, 0, 1, 0)
	stop_and_sleep()
	navigate_to_next_cross(30)
	navigate_to_next_cross(30)
	navigate_turn_left()
	move(pie / 2 + 0.5, 0, 50, 1.5)
	stop()


def go_back_3_right():
	pass


def up_line_short():
	navigate_to_next_cross(30)
	navigate_to_next_cross(30)
	navigate_to_next_cross(30)
	navigate_turn_left()
	move(pie / 2, 0, 50, 1.5)
	stop()


def up_line_common():
	navigate_to_next_cross(30)
	navigate_turn_left()
	up_line_short()


def go_back_4_left():
	pass


def go_back_4_right():
	move(-pie / 2, 0, 20, 0.5, 0, 1)
	move(pie, 0, 20)
	sleep_until(4, 2, 1, 0)
	move(-pie / 2, 0, 20, 0.5)
	move(pie, 0, 20)
	sleep_until(4, 2, 1, 0.5)
	up_line_common()


def go_back_5_left():
	move(-pie / 2, 0, 20, 0.5, 0, 1)  # 往后退
	move(0, 0, 20, 0, 0, 1)
	sleep_until(4, 2, 1, 0)
	sleep_until(4, 2, 1, 0.5)
	move(0, -300, 0, 0.5, 0)
	stop_and_sleep()
	up_line_short()


def go_back_5_right():
	pass


def go_back_6_left():
	move(-pie / 2, 0, 20, 0.3, 0, 1)  # 往后退
	move(0, 0, 20, 1.5)
	move(pie / 2, 0, 20)
	sleep_until(4, 2, 1, 0)
	get_out(20)
	correction()
	navigate_to_next_cross(20)
	move(pie, 0, 20, 0.7)
	stop_and_sleep()
	move(pie / 2, 0, 50, 1.5)
	stop()


def go_back_6_right():
	pass


def go_back_7_left():
	pass


def go_back_7_right():
	move(-pie / 2, 0, 50, 0.5)
	stop()


def go_back_8_left():
	move(-pie / 2, 0, 50, 0.5)
	stop()


def go_back_8_right():
	pass


def go_back_9_left():
	pass


def go_back_9_right():
	move(-pie / 2, 0, 20, 0.3)
	move(pie, 0, 30)
	sleep_until(4, 2, 1, 0)
	move(2.6, 0, 50, 1.3)
	stop()


def go_back_10_left():
	move(-pie / 2, 0, 20, 0.3)
	move(-0.35, 0, 50, 2)
	stop()


def go_back_10_right():
	pass
