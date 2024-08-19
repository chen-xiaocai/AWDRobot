import robot
from task1 import *


def move_to_1_side():
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
	robot.sleep(0.2)
	correction()
	move(pie, 0, 20, 1.4)  # 移动到1号位侧面
	stop()


def move_to_2_side():
	leave_base()
	navigate_to_next_cross(30)
	navigate_turn_left()
	navigate_to_next_cross(30)
	navigate_turn_right()
	navigate_to_next_cross(30)
	navigate_turn_right()
	line_navigation(20, 0.5)  # 移动至2号位前（
	correction()
	move(-pie / 2, 0, 20)
	sleep_until(4, 4, 1, 0)
	move(pie, 0, 20, 1.7)  # 移动至2号位侧面(
	stop()


def move_to_3_side():
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
	navigate_to_next_cross(30)
	navigate_turn_left()
	line_navigation(20, 0.3)
	correction()
	move(-pie / 2, 0, 20)
	sleep_until(4, 0, 1, 0)
	move(0, 0, 20, 1.5)  # 移动至3号位侧面（
	stop()


def move_to_4_side():
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
	move(-pie / 2, 0, 20, 0.5)
	correction()
	move(0, 0, 20, 1.5)  # 移动至4号位侧面（
	stop()


def move_to_5_side():
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
	navigate_turn_right()
	navigate_to_next_cross(30)
	move(-pie / 2, 0, 20, 0.8)
	correction()
	move(pie, 0, 20, 1.5)
	stop()


def move_to_6_side():
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
	navigate_turn_right()
	get_out(20)
	correction()
	move(-pie / 2, 0, 20)
	sleep_until(4, 0, 1, 0)
	robot.sleep(0.8)
	move(pie, 0, 20, 1.5)  # 移动至6号位侧面
	stop()


def move_to_7_side():  # 朝右，2，3号轮贴边
	move(pie / 2, 0, 20, 1.5)
	move(0, 0, 20, 0.3)
	stop()


def move_to_8_side():  # 朝左，2、3号轮贴边
	move(pie / 2, 0, 20, 1)
	move(pie, 0, 20, 0.3)
	stop()


def move_to_9_side():
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
	get_out(20)
	correction()
	move(-pie / 2, 0, 20, 0.3)
	move(0, 0, 20, 1.5)
	stop()


def move_to_10_side():
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
	navigate_turn_right()
	get_out(20)
	correction()
	move(-pie / 2, 0, 20, 0.3)
	move(pie, 0, 20, 1.5)
	stop()

