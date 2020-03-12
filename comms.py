 #SETUP comms on PCA9685
#remember to install adafruit_circuitpython using 'sudo pip3 install adafruit-circuitpython-pca9685' 
#as well as 'sudo pip3 install adafruit-circuitpython-servokit' 

#imports
import board
import busio
import adafruit_pca9685

i2c = busio.I2C(board.SCL, board.SDA)
pca = adafruit_pca9685.PCA9685(i2c)

#use this to set the entire board's PWM freq example sets it to 60Hz
pca.frequency = 60

#channel_0 can control the 0th channel on the board
channel_0 = pca.channels[0]

#set duty cycle to 100%
channel_0.duty_cycle = 0xffff



