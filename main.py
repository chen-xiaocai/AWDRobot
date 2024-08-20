import robot
from move1 import *
from dotask import *
from back import *



def move_to(destination, direction):
	func = [None, move_to_1, move_to_2, move_to_3, move_to_4, move_to_5, move_to_6, move_to_7, move_to_8, move_to_9,
			 move_to_10, move_to_11]
	func_left = []
	func_right = []
	# func_left = [None, move_to_1_left, move_to_2_left, move_to_3_left, move_to_4_left, None,
	# 			 move_to_6_left, move_to_7_left, move_to_8_left, move_to_9_left, move_to_10_left]
	# func_right = [None, move_to_1_right, move_to_2_right, move_to_3_right, move_to_4_right, None,
	# 			 move_to_6_right, move_to_7_right, move_to_8_right, move_to_9_right, move_to_10_right]
	if direction == TASK_DIR_FRONT or direction == TASK_DIR_BACK:
		func[destination]()
	elif direction == TASK_DIR_LEFT:
		func_left[destination]()
	else:
		func_right[destination]()


def go_back(from_pos, direction):
	func = [None, go_back_1, go_back_2, go_back_3, go_back_4, go_back_5, go_back_6, go_back_7, go_back_8,
			go_back_9, go_back_10]
	func_left = []
	func_right = []

	# func_left = [None, go_back_1_left, go_back_2_left, go_back_3_left, go_back_4_left, go_back_5_left, go_back_6_left, go_back_7_left, go_back_8_left,
	# 		go_back_9_left, go_back_10_left]
	# func_right = [None, go_back_1_right, go_back_2_right, go_back_3_right, go_back_4_right, go_back_5_right, go_back_6_right, go_back_7_right, go_back_8_right,
	# 		go_back_9_right, go_back_10_right]
	if direction == TASK_DIR_FRONT or direction == TASK_DIR_BACK:
		func[from_pos]()
	elif direction == TASK_DIR_LEFT:
		func_left[from_pos]()
	else:
		func_right[from_pos]()


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
		# [1, TASK_ID_1, TASK_DIR_FRONT, '1_1'],
		# [2, TASK_ID_1, TASK_DIR_FRONT, '1_2'],
		[3, TASK_ID_1, TASK_DIR_FRONT, '1_3'],
		# [4, TASK_ID_1, TASK_DIR_FRONT, '1_4'],
		# [5, TASK_ID_1, TASK_DIR_FRONT, '1_5'],
		# [6, TASK_ID_1, TASK_DIR_FRONT, '1_6'],
		# [7, TASK_ID_1, TASK_DIR_FRONT, '1_7'],
		# [8, TASK_ID_1, TASK_DIR_FRONT, '1_8'],
		# [9, TASK_ID_1, TASK_DIR_FRONT, '1_9'],
		# [10, TASK_ID_1, TASK_DIR_FRONT, '1_10'],

		# [1, TASK_ID_2, TASK_DIR_FRONT, '2_1'],
		# [2, TASK_ID_2, TASK_DIR_FRONT, '2_2'],
		# [3, TASK_ID_2, TASK_DIR_FRONT, '2_3'],
		# [4, TASK_ID_2, TASK_DIR_FRONT, '2_4'],
		# [5, TASK_ID_2, TASK_DIR_FRONT, '2_5'],
		# [6, TASK_ID_2, TASK_DIR_FRONT, '2_6'],
		# [7, TASK_ID_2, TASK_DIR_FRONT, '2_7'],
		[8, TASK_ID_2, TASK_DIR_FRONT, '2_8'],
		# [9, TASK_ID_2, TASK_DIR_FRONT, '2_9'],
		# [10, TASK_ID_2, TASK_DIR_FRONT, '2_10'],

		# [1, TASK_ID_3, TASK_DIR_FRONT, '3_1'],
		# [2, TASK_ID_3, TASK_DIR_FRONT, '3_2'],
		# [3, TASK_ID_3, TASK_DIR_FRONT, '3_3'],
		# [4, TASK_ID_3, TASK_DIR_FRONT, '3_4'],
		# [5, TASK_ID_3, TASK_DIR_FRONT, '3_5'],
		# [6, TASK_ID_3, TASK_DIR_FRONT, '3_6'],
		# [7, TASK_ID_3, TASK_DIR_FRONT, '3_7'],
		# [8, TASK_ID_3, TASK_DIR_FRONT, '3_8'],
		# [9, TASK_ID_3, TASK_DIR_BACK, '3_9'],
		[10, TASK_ID_3, TASK_DIR_FRONT, '3_10'],
		[11, TASK_ID_11_R, TASK_DIR_FRONT, "11_R"],
		[11, TASK_ID_11_Y, TASK_DIR_FRONT, "11_Y"],
		[11, TASK_ID_11_B, TASK_DIR_FRONT, "11_B"],
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
			go_back(pos, direction)
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
