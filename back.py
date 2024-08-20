import robot
from base import *
from correct import *


def go_back_1():  # 无特殊要求
	move(-pie / 2, 0, 30, 0, 1000, 1)
	move(-1.2, 0, 30, 0, 6000, 1)
	stop()


def go_back_2():  # 车顶着道具
	move(-pie / 2, 0, 30, 0, 1000, 1)
	move(pie, 0, 20, 0, 1000, 1)
	move(-pie / 2, 0, 50, 0, 4000, 1)
	stop()


def go_back_3():  # 车顶着道具
	move(-pie / 2, 0, 30, 0.5, 0, 1)
	move(0, 300, 0, 0.5)
	stop_and_sleep()
	navigate_to_next_cross(30)
	navigate_to_next_cross(30)
	navigate_turn_left()
	move(pie / 2, 0, 50, 1.5)
	stop()


def go_back_4():  # 无特殊要求
	move(-pie / 2, 0, 20, 0.5, 300, 1)
	move(0, -300, 0, 1)
	move(pie, 0, 20, 0.7)
	move(pie / 2, 0, 30, 0.8)
	navigate_to_next_cross(30)
	navigate_to_next_cross(30)
	navigate_to_next_cross(30)
	navigate_turn_left()
	move(pie / 2, 0, 50, 1.5)
	stop()


def go_back_5():  # 顶着任务(最好)
	move(-pie / 2, 0, 20, 0.3, 0, 1)
	move(0, 300, 0, 0.5)
	stop_and_sleep()
	move(pie / 2, 0, 20, 0.7)
	move(pie, 0, 20)
	sleep_until(4, 2, 1, 0)
	sleep_until(4, 2, 1, 0.5)
	navigate_to_next_cross(30)
	navigate_turn_left()
	navigate_to_next_cross(30)
	navigate_to_next_cross(30)
	navigate_to_next_cross(30)
	navigate_turn_left()
	move(pie / 2, 0, 50, 1.5)
	stop()


def go_back_6():  # 顶到任务，7号位为横
	move(-pie / 2, 0, 20)
	sleep_until(4, 4, 1, 0)
	move(pie / 2, 0, 20, 0.2)
	navigate_turn_right()
	navigate_to_next_cross(20)
	move(pie, 0, 20, 0.7)
	stop_and_sleep()
	move(pie / 2, 0, 50, 1.5)
	stop()


def go_back_6_():
	move(-pie / 2, 0, 20, 0.3, 0, 1)
	move(0, 300, 0, 1)
	stop_and_sleep()
	move(-pie / 2, 0, 20, 0.7)
	navigate_to_next_cross(30)
	navigate_to_next_cross(30)
	move(pie / 2, 0, 30, 0, 600, 0)
	move(0, 300, 0, 0.5)
	stop_and_sleep()
	move(pie / 2, 0, 30)
	sleep_until(4, 4, 1, 0)
	navigate_turn_right()
	navigate_to_next_cross(30)
	navigate_turn_left()
	navigate_to_next_cross(30)
	navigate_to_next_cross(30)
	navigate_to_next_cross(30)
	navigate_turn_left()
	move(pie / 2, 0, 50, 1.3)
	stop()


def go_back_7():  # 顶着任务
	move(-pie / 2, 0, 20, 0.3, 0, 1)
	move(0, 0, 20, 0.5, 0, 0)
	move(pie / 2, 0, 20, 0.3)
	move(0, 0, 20, 1.5)
	stop()


def go_back_8():  # 顶着任务
	move(-pie / 2, 0, 20, 0.3, 0, 1)
	move(pie, 0, 30, 1.5)
	stop()


def go_back_9():
	move(-pie / 2, 0, 30, 0, 5500, 1)
	stop()


def go_back_10():
	move(-pie / 2, 0, 20, 1, 0, 1)
	move(-pie*3/4, 0, 50, 2, 0, 1)
	stop()
