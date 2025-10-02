import time 
import smbus
from time import sleep 
from gpiozero import Motor , Servo , DistanceSensor


x = 0 

mtr = Motor(forward=20,backward=12)
srv = Servo(17)
base_servo = 0.018
base_speed = (0.4)
last_time = time.time()

MPU_ADDR = 0x68       
bus = smbus.SMBus(1)  
PWR_MGMT_1 = 0x6B     
GYRO_XOUT_H = 0x43    
GYRO_YOUT_H = 0x45    
GYRO_ZOUT_H = 0x47   


def update_angle():
    global angle, last_time
    now = time.time()
    dt = now - last_time
    last_time = now

    high = bus.read_byte_data(MPU_ADDR, GYRO_ZOUT_H)
    low  = bus.read_byte_data(MPU_ADDR, GYRO_ZOUT_H + 1)
    gz = (high << 8) | low
    if gz & 0x8000:
        gz = -((65535 - gz) + 1)
    gz = gz / 131.0

    angle += gz * dt
    return angle 
def correct_steering():
    current_angle = update_angle()
    correction = Kp * current_angle
    steering.value = max(-1, min(1, base_servo + correction))
    return current_angle
def dist(TRIG19 = 99999, ECHO19 = 999999):
    ultrasonc = DistanceSensor(echo = ECHO19 , trigger = TRIG19 )
    dst = ultrasonc.distance
    distcm = int( dst * 100  )
    return distcm 


def movestraightforward(duration=0.2, base_speed=0.4):
    """
    تحرك الروبوت للأمام بسرعة base_speed لمدة duration (بالثواني) ثم يتوقف.
    """
    mtr.forward(base_speed)
    sleep(duration)
    mtr.stop()

def stoptherobot():
    srv.value = 0 
    mtr.stop()
    angle = 0 


def turn90dgreesright():
    mtr.forward(0.34)
    srv.value = 0.5
    sleep(0.7)
    mtr.stop()
    srv.value = 0

def turn90dgreesleft():
    mtr.forward(0.34)
    srv.value = -0.5
    sleep(0.7)
    mtr.stop()
    srv.value = 0

def movestraightforward_gyro(duration=1.0, base_speed=0.4, Kp=0.03):
    """
    تحرك الروبوت للأمام مع تصحيح الاتجاه باستخدام الجايروسكوب.
    duration: مدة الحركة بالثواني
    base_speed: سرعة الموتور
    Kp: معامل التصحيح (جرب 0.02 إلى 0.05 حسب التجربة)
    """
    global last_time
    angle = 0.0
    last_time = time.time()
    mtr.forward(base_speed)
    start = time.time()
    while time.time() - start < duration:
        now = time.time()
        dt = now - last_time
        last_time = now
        # تحديث الزاوية
        high = bus.read_byte_data(MPU_ADDR, GYRO_ZOUT_H)
        low = bus.read_byte_data(MPU_ADDR, GYRO_ZOUT_H + 1)
        gz = (high << 8) | low
        if gz & 0x8000:
            gz = -((65535 - gz) + 1)
        gz = gz / 131.0
        angle += gz * dt
        # تصحيح السيرفو
        correction = Kp * angle
        srv.value = max(-1, min(1, correction))
        sleep(0.02)
    mtr.stop()
    srv.value = 0

def turn_small_right():
    mtr.forward(0.34)
    srv.value = 0.5
    sleep(0.15)  # مدة قصيرة جداً
    mtr.stop()
    srv.value = 0

def turn_small_left():
    mtr.forward(0.34)
    srv.value = -0.5
    sleep(0.15)  # مدة قصيرة جداً
    mtr.stop()
    srv.value = 0
