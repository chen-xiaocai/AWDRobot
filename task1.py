import robot
from base import *
from correct import *


def move_to_1():  # 无特殊要求	后排传感器在路口上，难以准确脱离，20速度向前巡线0.3秒后可以做矫正
	move(2.7, 0, 30, 0, 0, 1)
	sleep_until(4, 2, 1, 1)
	stop_and_sleep()
	add_event(1)
	navigate_to_next_cross(30)
	add_event(2)
	navigate_turn_left()
	add_event(3)
	navigate_to_next_cross(30)
	add_event(4)
	navigate_turn_right()
	add_event(5)
	navigate_to_next_cross(30)
	add_event(6)
	navigate_turn_right()
	add_event(7)
	navigate_to_next_cross(30)
	add_event(8)
	navigate_turn_left()
	# line_navigation(20, 0.3)  # 巡线0.3秒后可做矫正
	stop()
	add_event(9)


def move_to_2():  # 1、3号轮贴边	后排传感器脱离路口
	leave_base()
	add_event(1)
	navigate_to_next_cross(30)
	add_event(2)
	move(pie / 2, 0, 30, 0, 0, 0)
	sleep_until(4, 2, 1, 0.5)
	add_event(3)
	move(0, 0, 20, 0.3, 0, 1)
	stop_and_sleep()
	add_event(4)
	get_out(20)
	stop()
	add_event(5)


def move_to_3():  # 1、3号轮贴边	后排传感器脱离路口
	leave_base()
	add_event(1)
	navigate_to_next_cross(30)
	add_event(2)
	move(pie / 2, 0, 30, 0, 0, 0)
	sleep_until(4, 2, 1, 0.5)
	add_event(3)
	move(pie / 2, 0, 30, 0, 600, 0)
	stop()
	move(0, -300, 0, 0.5)
	stop_and_sleep()
	add_event(4)
	line_navigation(30, 1)
	add_event(5)
	navigate_to_next_cross(30)
	add_event(6)
	navigate_turn_left()
	add_event(7)
	get_out(20)
	stop()
	add_event(8)


def move_to_4():  # 1、3号轮贴边	后排传感器脱离路口
	leave_base()
	add_event(1)
	navigate_to_next_cross(30)
	add_event(2)
	move(pie / 2, 0, 30, 0, 0, 0)
	sleep_until(4, 2, 1, 0.5)
	move(pie / 2, 0, 30, 0, 600, 0)
	stop()
	add_event(3)
	move(0, -300, 0, 0.5)
	stop_and_sleep()
	add_event(4)
	line_navigation(30, 1)
	add_event(5)
	navigate_to_next_cross(30)
	add_event(6)
	navigate_to_next_cross(30)
	add_event(7)
	move(pie / 2, 0, 30)
	sleep_until(4, 4, 1, 0.5)
	add_event(8)
	navigate_turn_right()
	add_event(9)
	navigate_to_next_cross(30)
	add_event(10)
	move(0, 300, 0, 1)
	stop_and_sleep()
	add_event(11)
	navigate_to_next_cross(30)
	add_event(12)
	navigate_turn_right()
	add_event(13)
	get_out(20)
	stop()
	add_event(14)


def bland_turn_right():
	move(0, -300, 0, 0.5)
	stop_and_sleep()


def move_to_5():  # 1、3号轮贴边	后排传感器脱离路口
	leave_base()
	add_event(1)
	navigate_to_next_cross(30)
	# 直行一直等到4-2传感器找到黑线
	move(pie / 2, 0, 30, 0, 0, 0)
	sleep_until(4, 2, 1, 0.5)
	add_event(2)
	# 直行600 tick
	move(pie / 2, 0, 30, 0, 600, 0)
	bland_turn_right()
	add_event(3)
	line_navigation(30, 1)
	stop()
	add_event(4)
	navigate_to_next_cross(30)
	add_event(5)
	navigate_to_next_cross(30)
	add_event(6)
	move(pie / 2, 0, 30)
	sleep_until(4, 4, 1, 0.5)
	add_event(7)
	navigate_turn_right()
	add_event(8)
	navigate_to_next_cross(30)
	add_event(9)
	navigate_turn_left()
	add_event(10)
	get_out(20)
	stop()


def move_to_6():  # 1、3号轮贴边	后排传感器脱离路口
	leave_base()
	add_event(1)
	navigate_to_next_cross(30)
	add_event(2)
	move(pie / 2, 0, 30, 0, 0, 0)
	sleep_until(4, 2, 1, 0.5)
	move(pie / 2, 0, 30, 0, 600, 0)
	stop()
	add_event(3)
	move(0, -300, 0, 0.5)
	stop_and_sleep()  # 二号位面前朝右
	add_event(4)
	line_navigation(30, 1)
	add_event(5)
	navigate_to_next_cross(30)
	add_event(6)
	navigate_to_next_cross(30)
	add_event(7)
	move(pie / 2, 0, 30)
	sleep_until(4, 4, 1, 0.5)  # 四五号位之间
	add_event(8)
	navigate_turn_right()
	navigate_to_next_cross(30)
	add_event(9)
	navigate_to_next_cross(30)
	add_event(10)
	get_out(20)
	add_event(11)
	stop()


def move_to_7():  # 倒着	随缘
	move(-pie / 2, 0, 20, 0.6)
	add_event(1)
	move(3.1, 0, 20)
	robot.sleep(0.5)
	sleep_until(4, 2, 1, 1)
	stop()
	add_event(2)


def move_to_7_():
	leave_base()
	add_event(1)
	navigate_to_next_cross(30)
	add_event(2)
	move(pie / 2, 0, 30, 0, 0, 0)
	sleep_until(4, 2, 1, 0.5)
	add_event(3)
	move(pie / 2, 0, 30, 0, 600, 0)
	stop()
	move(0, -300, 0, 0.5)
	stop_and_sleep()
	add_event(4)
	line_navigation(30, 1)
	add_event(5)
	navigate_to_next_cross(30)
	add_event(6)
	navigate_to_next_cross(30)
	add_event(7)
	move(pie / 2, 0, 30)
	sleep_until(4, 4, 1, 0.5)
	add_event(8)
	navigate_turn_right()
	add_event(9)
	navigate_to_next_cross(30)
	add_event(10)
	navigate_to_next_cross(30)
	add_event(10)
	navigate_turn_right()
	add_event(11)
	navigate_to_next_cross(30)
	add_event(12)
	navigate_turn_left()
	add_event(13)
	get_out(20)
	stop()
	add_event(14)


def move_to_8():  # 无特殊要求	路口掉头
	move(2.7, 0, 30, 0, 0, 1)
	sleep_until(4, 2, 1, 1)
	stop_and_sleep()
	add_event(1)
	navigate_to_next_cross(30)
	add_event(2)
	move(0, -300, 0, 0, 0, 0)
	sleep_until(4, 2, 1, 0.5)
	stop()
	add_event(3)


def move_to_9():  # 无特殊要求	后排传感器脱离路口
	move(2.7, 0, 30, 0, 0, 1)
	sleep_until(4, 2, 1, 1)
	stop_and_sleep()
	add_event(1)
	navigate_to_next_cross(30)
	add_event(2)
	navigate_turn_left()
	add_event(3)
	navigate_to_next_cross(30)
	add_event(4)
	navigate_turn_left()
	add_event(5)
	navigate_to_next_cross(30)
	add_event(6)
	navigate_turn_right()
	add_event(7)
	get_out(20)
	stop()
	add_event(8)


def move_to_10():  # 无特殊要求	后排传感器脱离路口
	move(2.7, 0, 30, 0, 0, 1)
	sleep_until(4, 2, 1, 1)
	stop_and_sleep()
	add_event(1)
	navigate_to_next_cross(30)
	add_event(2)
	navigate_turn_left()
	add_event(3)
	navigate_to_next_cross(30)
	add_event(4)
	navigate_turn_right()
	add_event(5)
	navigate_to_next_cross(30)
	add_event(6)
	navigate_turn_left()
	add_event(7)
	get_out(20)
	stop()
	add_event(8)


def move_to_11():  # 1、3号轮贴边	后排传感器脱离路口
	leave_base()
	navigate_to_next_cross(30)
	add_event(2)
	move(pie / 2, 0, 30, 0, 0, 0)
	sleep_until(4, 2, 1, 0.5)
	move(pie / 2, 0, 30, 0, 600, 0)
	stop()
	move(0, -300, 0, 0.5)
	stop_and_sleep()
	add_event(3)
	line_navigation(30, 1)
	add_event(4)
	navigate_to_next_cross(30)
	add_event(5)
	line_navigation(30, 0.5)
	navigate_to_next_cross(30)
	add_event(6)
	navigate_turn_right()
	add_event(7)
	navigate_to_next_cross(30)
	add_event(8)
	navigate_turn_right()
	add_event(9)
	get_out(20)
	stop()
	add_event(10)
	robot.set_motor(4, 100)  # 将机械臂放下
	robot.sleep(0.1)
	robot.set_motor(4, 0)


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
	move(-pie / 2, 0, 30, 0.3, 0, 1)
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
	move(-pie / 2, 0, 20, 0.3, 0, 1)
	move(0, 300, 0, 1)
	stop_and_sleep()
	move(-pie / 2, 0, 20, 0.7)
	navigate_to_next_cross(30)
	navigate_turn_left()
	navigate_to_next_cross(30)
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


def go_back(from_pos):
	func = [go_back_1, go_back_2, go_back_3, go_back_4, go_back_5, go_back_6, go_back_7, go_back_8,
			go_back_9, go_back_10]

	func[from_pos-1]()


def move_to(destination):
	func = [move_to_1, move_to_2, move_to_3, move_to_4, move_to_5, move_to_6, move_to_7, move_to_8,
			move_to_9, move_to_10, move_to_11]
	func[destination - 1]()