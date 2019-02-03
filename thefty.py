# imports
import time
import pygame
from osascript import osascript




import random




# config
alarmSoundFile = 'leroy.mp3'
alarmVolume = 30



# functions
def isCharging():
	# returns True if Laptop is currently charging, else False
	return random.choice([True, False])

def setVolume(vol, mut):
	# restores Volume to input values (vol, mut as Strings)
	mute = 'with' if (mut == 'true') else 'without'
	osascript('set volume %s output muted output volume %s' % (mute, vol))

def getVolume():
	# returns the current volume and muted as strings
	vol = osascript('output volume of (get volume settings)')[1]
	mut = osascript('output muted of (get volume settings)')[1]

	return vol, mut

def playMP3(file):
	# plays the specified .mp3-file
	pygame.init()
	pygame.mixer.init()
	pygame.mixer.music.load(file)
	pygame.mixer.music.set_volume(1)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy(): 
		pygame.time.Clock().tick(10)



def soundAlarm():
	# plays the alarm sound specified in config
	setVolume(alarmVolume, 'false')

	# sound alarm
	playMP3(alarmSoundFile)

	print('alarm')

	# end soundAlarm


def surveillance():
	# loop every XXs, check if cable still plugged in, alarm if not
	print('\nThefty started. Terminate with Ctrl-C.\n')

	while True:
		time.sleep(1.500)
		if not isCharging(): soundAlarm()



# init
try:
	if not isCharging():
		print('\nPlease plug in charger and try again.\n')
	else:
		prevVol, prevMut = getVolume()
		surveillance()

except KeyboardInterrupt:
	# return system volume to before state
	setVolume(prevVol, prevMut)
	print('\n\nWelcome Back!\n')
	exit()


