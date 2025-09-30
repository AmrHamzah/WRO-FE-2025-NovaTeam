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

def movestraightforward(base_speed=0.4, base_servo=0.018, Kp=0.03):

    angle = 0.0
    last_time = time.time()
    motor.forward(base_speed)

    while True:
        now = time.time()
        dt = now - last_time
        last_time = now

        angle = update_angle()

        correct = Kp * angle
        steering.value = max(-0.9, min(0.9, base_servo + correct))

        print(f"Angle={angle:.2f}° | Steering={steering.value:.2f}")

def stoptherobot():
    srv.value = 0 
    mtr.stop()
    angle = 0 

def turn90dgreleft():
    srvo.value = left_srvo_value 
    mtr.forward(base_speed)
    sleep(2)

def turn90dgreright():
    srvo.value = right_srvo_value 
    mtr.forward(base_speed)
    sleep(2)
def turn90dgreesright():
    motor.forward(0.34)
    servo.value = 0.478
    sleep (5.0)
turn90dgrees()
motor.stop()
servo.value = 0
def turn90dgreesleft():
    motor.forward(0.34)
    servo.value = 0.478
    sleep (5.0)
turn90dgrees()
motor.stop()
servo.value = 0
