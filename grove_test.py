#!/usr/bin/env python

# GrovePi LED blink Example for the Grove LED Socket (http://www.seeedstudio.com/wiki/Grove_-_LED_Socket_Kit)
#
# The GrovePi connects the Raspberry Pi and Grove sensors.  You can learn more about GrovePi here:  http://www.dexterindustries.com/GrovePi
#
# Have a question about this example?  Ask on the forums here:  http://www.dexterindustries.com/forum/?forum=grovepi
#
# LICENSE: 
# These files have been made available online through a [Creative Commons Attribution-ShareAlike 3.0](http://creativecommons.org/licenses/by-sa/3.0/) license.
import time
import grovepi

# Connect the Grove LED to digital port D4
led = 5

sound_sensor = 0
temp_sensor = 7
sonic_sensor = 4

i = 0; 
# intensite

#grovepi.pinMode(sound_sensor,"INPUT");
grovepi.pinMode(led,"OUTPUT")

time.sleep(1)

while True:
    try:
	[temp,hum] = grovepi.dht(temp_sensor,1)

	print temp,"C ",hum,"H"

	#d = grovepi.ultrasonicRead(sonic_sensor);
	#t = grovepi.temp(temp_sensor, '1.1');
	#print t,"C"	

	#sensor_value = grovepi.analogRead(sound_sensor)
        #print sensor_value

	#i = 255 - d * 3;

	#if i < 0:
        #    i = 0

        # Current brightness
        #print i

        # Give PWM output to LED
        #grovepi.analogWrite(led,i)


        #Blink the LED
        #digitalWrite(led,1)		# Send HIGH to switch on LED
        #time.sleep(0.1)

        #digitalWrite(led,0)		# Send LOW to switch off LED
        #time.sleep(0.1)

    except KeyboardInterrupt:	# Turn LED off before stopping
        digitalWrite(led,0)
        break
    except IOError:				# Print "Error" if communication error encountered
        print "Error"
