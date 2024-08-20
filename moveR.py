import robot
from base import *
from correct import *




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



def move_to_5_right():
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
	navigate_to_next_cross(30)  # 移动到5号位
	get_out(30)
	navigate_turn_left()
	move(-pie / 2, 0, 20, 0)
	sleep_until(0, 1, 1, 0)
	move(pie / 2, 0, 20, 0.2)
	correction()
	move(0, 0, 20, 1.5)
	stop()


def move_to_6_right():
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
	navigate_turn_right()
	navigate_turn_left()
	correction()
	move(0, 0, 20, 1.5)
	stop()

def move_to_7_right():  # 朝右，2，3号轮贴边
	move(pie / 2, 0, 20, 1.5)
	move(0, 0, 20, 0.4)
	stop()


def move_to_8_right():
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
	move(0, 300, 0, 1)
	stop_and_sleep()
	correction()
	move(pie / 2, 0, 20, 0.3)
	move(0, 0, 20, 1.5)
	stop()

def move_to_9_right():
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
	move(0, 0, 20, 1.65)
	stop()



def move_to_10_right():
	pass
