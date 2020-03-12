import time
import board
import busio
import adafruit_fxas21002c

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_fxas21002c.FXAS21002C(i2c)

while True:
    gyro_x, gyro_y, gyro_z = sensor.gyroscope
    print('Gyroscope (radians/s): ({0:0.3f},  {1:0.3f},  {2:0.3f})'.format(gyro_x, gyro_y, gyro_z))
    time.sleep(1.0)