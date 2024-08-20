# import robot
# from base import *
# from correct import *
#
#
# def move_to_6_left():
# 	leave_base()
# 	add_event(1)
# 	navigate_to_next_cross(30)
# 	add_event(2)
# 	move(pie / 2, 0, 30, 0, 0, 0)
# 	sleep_until(4, 2, 1, 0.5)
# 	move(pie / 2, 0, 30, 0, 600, 0)
# 	stop()
# 	add_event(3)
# 	move(0, -300, 0, 0.5)
# 	stop_and_sleep()  # 二号位面前朝右
# 	add_event(4)
# 	line_navigation(30, 1)
# 	add_event(5)
# 	navigate_to_next_cross(30)
# 	add_event(6)
# 	navigate_to_next_cross(30)
# 	add_event(7)
# 	move(pie / 2, 0, 30)
# 	sleep_until(4, 4, 1, 0.5)  # 四五号位之间
# 	add_event(8)
# 	navigate_turn_right()
# 	navigate_to_next_cross(30)  # 5号位前路口
# 	add_event(9)
# 	navigate_to_next_cross(30)  # 6号位前路口
# 	navigate_turn_right()
# 	get_out(20)
# 	correction()
# 	move(-pie / 2, 0, 20)
# 	sleep_until(4, 0, 1, 0)
# 	robot.sleep(0.8)
# 	move(pie, 0, 20, 1.5)  # 移动至6号位侧面
# 	stop()
#
#
# def move_to_6_right():
# 	leave_base()
# 	add_event(1)
# 	navigate_to_next_cross(30)
# 	add_event(2)
# 	move(pie / 2, 0, 30, 0, 0, 0)
# 	sleep_until(4, 2, 1, 0.5)
# 	move(pie / 2, 0, 30, 0, 600, 0)
# 	stop()
# 	add_event(3)
# 	move(0, -300, 0, 0.5)
# 	stop_and_sleep()  # 二号位面前朝右
# 	add_event(4)
# 	line_navigation(30, 1)
# 	add_event(5)
# 	navigate_to_next_cross(30)
# 	add_event(6)
# 	navigate_to_next_cross(30)
# 	add_event(7)
# 	move(pie / 2, 0, 30)
# 	sleep_until(4, 4, 1, 0.5)  # 四五号位之间
# 	add_event(8)
# 	navigate_turn_right()
# 	navigate_to_next_cross(30)  # 5号位前路口
# 	add_event(9)
# 	navigate_to_next_cross(30)  # 6号位前路口
# 	add_event(10)
# 	navigate_turn_right()
# 	navigate_turn_left()
# 	correction()
# 	move(0, 0, 20, 1.5)
# 	stop()
#
#
#
#
# def move_to_7_left():
# 	leave_base()
# 	add_event(1)
# 	navigate_to_next_cross(30)
# 	add_event(2)
# 	move(pie / 2, 0, 30, 0, 0, 0)
# 	sleep_until(4, 2, 1, 0.5)
# 	move(pie / 2, 0, 30, 0, 600, 0)
# 	stop()
# 	add_event(3)
# 	move(0, -300, 0, 0.5)
# 	stop_and_sleep()  # 二号位面前朝右
# 	add_event(4)
# 	line_navigation(30, 1)
# 	add_event(5)
# 	navigate_to_next_cross(30)
# 	add_event(6)
# 	navigate_to_next_cross(30)
# 	add_event(7)
# 	move(pie / 2, 0, 30)
# 	sleep_until(4, 4, 1, 0.5)  # 四五号位之间
# 	add_event(8)
# 	navigate_turn_right()
# 	navigate_to_next_cross(30)  # 5号位前路口
# 	add_event(9)
# 	navigate_to_next_cross(30)  # 6号位前路口
# 	navigate_turn_right()
# 	get_out(20)
# 	correction()
# 	move(pie, 0, 20, 1.5)
# 	stop()
#
#
# def move_to_7_right():  # 朝右，2，3号轮贴边
# 	move(pie / 2, 0, 20, 1.5)
# 	move(0, 0, 20, 0.4)
# 	stop()
#
#
#
