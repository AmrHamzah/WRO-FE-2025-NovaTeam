from time import sleep
from mainfuncions import (
    movestraightforward_gyro, dist, stoptherobot,
    turn90dgreesright, turn90dgreesleft,
    movestraightforward
)
from gpiozero import Button

# زر التشغيل على GPIO 21 (غيره حسب توصيلك)
start_button = Button(21)

def dist_left():
    return dist(TRIG19=23, ECHO19=24)

def dist_right():
    return dist(TRIG19=27, ECHO19=22)

def open_task():
    min_dist = 100  
    laps = 6
    sides = 4
    for lap in range(laps):
        for side in range(sides):
            while True:
                d = dist(ECHO19=6, TRIG19=5)
                left = dist_left()
                right = dist_right()
                print(f"Front distance: {d} | Left: {left} | Right: {right}")
                if d < min_dist:
                    stoptherobot()
                    print("Stopped: Close to front wall")
                    break
                print("Action: Move straight with gyro correction")
                movestraightforward_gyro(duration=1.2)
            left = dist_left()
            
            right = dist_right()
            if left == 100:
                print("Turn left (left = 100)")
                turn90dgreesleft()
            elif right == 100:
                print("Turn right (right = 100)")
                turn90dgreesright()
            else:
                print("No turn: neither sensor reads 100. Moving straight.")
                movestraightforward_gyro(duration=0.5)
            sleep(0.2)
    stoptherobot()
    print("did 3 laps ")

if __name__ == "__main__":
    print("اضغط على الزر لبدء المهمة...")
    start_button.wait_for_press()
    print("بدأت المهمة!")
    open_task()
