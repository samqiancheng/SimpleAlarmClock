#- Alarm.py

'''''''''''''''''''''''''''''''''
'Simple Python Alarm clock      '
'''''''''''''''''''''''''''''''''

import os, sys, time
import threading

def _alarming():
	print('Alarm !!!!!')

class Alarm(threading.Thread):
	def __init__(self,hours,minutes):
		super(Alarm,self).__init__()
		self.hour = hours
		self.minute = minutes
		self.running = True
	def run(self):
		while self.running:
			cur_h, cur_m = time.localtime()[3:5]
			if cur_m == self.minute and cur_h == self.hour:
				_alarming()
				#- Exit program after the alarm
				exit()
	def kill(self):
		self.running = False

#- Argument from command line
hour, minute = [int(i) for i in sys.argv[1:]]

print('Alarm time is {}:{}'.format(hour,minute))

alarm = Alarm(hour,minute)
alarm.start()

while alarm.isAlive():
	input_value = input()
	if input_value.lower() == 'stop':
		alarm.kill()
		print('Program exits as user stops')
		break