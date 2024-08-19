import robot
from base import *
from correct import *


def move_to_1():  # 无特殊要求	后排传感器在路口上，难以准确脱离，20速度向前巡线0.3秒后可以做矫正
	move(2.7, 0, 30, 0, 0, 1)
	sleep_until(4, 2, 1, 1)
	stop_and_sleep()  # 到达8号任务前
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
	get_out(20)
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
	add_event(8)
	navigate_turn_right()
	add_event(9)
	navigate_to_next_cross(30)  # 移动到5号位
	add_event(10)
	move(0, 300, 0, 1)  # 掉头(或许可以省略)
	stop_and_sleep()
	add_event(11)
	navigate_to_next_cross(30)
	add_event(12)
	navigate_turn_right()
	add_event(13)
	get_out(20)  # 移动到4号位
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
	navigate_to_next_cross(30)  # 5号位前路口
	add_event(9)
	navigate_to_next_cross(30)  # 6号位前路口
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
	stop_and_sleep()  # 到8号位前
	add_event(1)
	navigate_to_next_cross(30)
	add_event(2)
	navigate_turn_left()
	add_event(3)
	navigate_to_next_cross(30)  # 9、10号位之间
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



