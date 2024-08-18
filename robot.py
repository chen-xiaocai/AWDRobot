
import math
import time
import simulator

def sin(x):
	return math.sin(x)


def cos(x):
	return math.cos(x)


def tan(x):
	return math.tan(x)


def atan(x):
	return math.atan(x)


def sqrt(x):
	return math.sqrt(x)
# def abs(x):
# 	return math.abs(x)


def sleep(x):
	time.sleep(x)


def get_cur_time_ms():
	return abs(time.time()*1000)


timers = []
for i in range(10):
	timers.append(0)


def reset_timer(timer):
	timers[timer] = get_cur_time_ms()


def get_timer_ms(timer):
	return get_cur_time_ms() - timers[timer]

class motor:
	def __init__(self, id):
		self._id = id
		self._speed = 0
		self._distance = 0
		self._start_time = 0

	def set_speed(self, speed):
		self._distance += (get_cur_time_ms() - self._start_time) * self._speed
		self._speed = speed
		self._start_time = get_cur_time_ms()
		# print("set motor {} speed to {}, distance {}".format(self._id, self._speed, self._distance))

	def get_speed(self):
		return self._speed

	def get_distance(self):
		return self._distance + (get_cur_time_ms() - self._start_time) * self._speed

motors= []
for i in range(10):
	motors.append(motor(i))

def set_motor(port, speed):
	return motors[port].set_speed(speed)


class Encoder:
	def __init__(self, port):
		self._port = port
		self._distance = 0

	def reset(self):
		self._distance = motors[self._port].get_distance()

	def get(self):
		return motor[self._port].get_distance() - self._distance


encoders = []
for i in range(10):
	encoders.append(Encoder(i))


def reset_encoder(port):
	encoders[port].reset()


def get_encoder(port):
	encoders[port].get()


class GraySensor:
	def __init__(self, id):
		self._id = id

	def read(self):
		return simulator.get_sensor_value(self._id)


gray_sensors = []
for i in range(20):
	gray_sensors.append(GraySensor(i))


def get_channel_gray(port, channel):
	return gray_sensors[channel].read()


def get_gray(port):
	return gray_sensors[12 - port].read()

# def start_sensor_thread():
# 	thread = simulator.SensorThread()
# 	thread.start()

# start_sensor_thread()

def check_key(key_id):
	return 1