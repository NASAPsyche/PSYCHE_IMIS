#SETUP comms on PCA9685
#remember to install adafruit_circuitpython using 'sudo pip3 install adafruit-circuitpython-pca9685' 
#as well as 'sudo pip3 install adafruit-circuitpython-servokit' 
#example https://learn.adafruit.com/16-channel-pwm-servo-driver/python-circuitpython 

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


#SETUP comms on IMU - 9DOF FXOS8700 + FXAS21002
#example https://learn.adafruit.com/nxp-precision-9dof-breakout/python-circuitpython
import board
import busio
import adafruit_fxos8700
import adafruit_fxas21002c


i2c = busio.I2C(board.SCL, board.SDA)
fxos = adafruit_fxos8700.FXOS8700(i2c)
fxas = adafruit_fxas21002c.FXAS21002C(i2c)

# Read
accel_x, accel_y, accel_z = sensor.accelerometer
mag_x, mag_y, mag_z = sensor.magnetometer
gyro_x, gyro_y, gyro_z = sensor.gyroscope
    
# Print values.
print('Acceleration (m/s^2): ({0:0.3f}, {1:0.3f}, {2:0.3f})'.format(accel_x, accel_y, accel_z)) # you could also do .format(*fxos.accelerometer)
print('Magnetometer (uTesla): ({0:0.3f}, {1:0.3f}, {2:0.3f})'.format(mag_x, mag_y, mag_z))
print('Gyroscope (radians/s): ({0:0.3f},  {1:0.3f},  {2:0.3f})'.format(gyro_x, gyro_y, gyro_z))
