# Nova Team – WRO Future Engineers 2025

![Banner](images/banner.jpg)

## Table of Contents
- [About Us](#about-us)
- [Power and Sense Management](#power-and-sense-management)
- [Obstacle Management](#obstacle-management)
- [Engineering Factor](#engineering-factor)
- [Hardware](#hardware)
- [Software](#software)
- [Experience and Acquired Expertise](#experience-and-acquired-expertise)
- [Special Thanks](#special-thanks)
- [Conclusion and Future Vision](#conclusion-and-future-vision)

---

## About Us

We are a team of three 15-year-old Palestinians who built and programmed a robot capable of traversing a specific path in WRO.

| Member | Instagram | Photo |
|--------|----------|-------|
| **Amr Younis** | [amr.younis04](https://www.instagram.com/amr.younis04) | ![Amr](images/Robot.jpg) |
| **Mohammad Abu Laban** | [mo_abu_lab](https://www.instagram.com/mo_abu_lab) | ![Mohammad](images/Robot.jpg) |
| **Ibrahim Mummar** | [lbrameem_mum](https://www.instagram.com/lbrameem_mum) | ![Ibrahim](images/Robot.jpg) |

This path consists of a white carpet with two lines in each corner, as well as an orange line and a blue line. The carpet measures three meters long and three meters wide, surrounded by a 10-cm-high black wooden wall, with a 10-cm-high square black wooden wall in the middle of the carpet.

---

## Power and Sense Management

We used a 12.6V, 6A rechargeable lithium battery. It provides enough capacity to power all components, with correct distribution so no single part consumes more than its share.

![Battery](images/Battery.jpg)

---

## Obstacle Management

The robot deals with obstacles using ultrasonic sensors and a camera.  

- Ultrasonic technology measures the distance between obstacles and the robot, enabling it to adjust its direction.  
- The camera recognizes colors and sends a signal to the Raspberry Pi. For example, when detecting red, the robot reacts according to the programmed instructions.

![Ultrasonic Sensor](images/Ultrasonic.jpg)

---

## Engineering Factor

We started with a ready-made kit and modified it to suit our task. We added additional layers to contain all the parts and ensured balanced weight distribution, placing the battery in the middle to prevent tilting.

![Robot Layers](images/Robot.jpg)

---

## Hardware

### 1- The Robot
We modified a ready-made kit by adding one acrylic layer and two plastic layers, giving us four in total:

- Ground layer: DC motor and servo motor
- Second layer: Battery
- Third layer: Power button and power regulation circuit
- Fourth layer: Raspberry Pi, gyroscope, three ultrasonic sensors, camera and motor driver

All connected with jumper wires.

### 2- Kit Used
MG996 car model servo and DC motor. Available in Palestine and suitable for our task.  
Cost: $95 [AliExpress](https://a.aliexpress.com/_c3kFLPlv)  

### 3- Microcontroller
Raspberry Pi 4 8GB RAM. Fast CPU, Python support, available locally.  
Cost: $92 [AliExpress](https://a.aliexpress.com/_c2yjCN0B)  

### 4- Battery
12.6V, 6A lithium battery. High voltage & capacity, adjustable output.

### 5- DC Power Converter
XL4015 (32V → 1.25V adjustable). Easy to install.  
Cost: $1 [AliExpress](https://a.aliexpress.com/_c38oxv2b)  

### 6- Ultrasonic Sensors
3 × HC-SR04. Voltage: 3.3 to 5V, range: 2cm to 400cm.  
Cost: $1 each [AliExpress](https://a.aliexpress.com/_c38oxv2b)  

### 7- Motor Driver
L298N motor driver. Sufficient for our motors.  
Cost: $1.50 [AliExpress](https://a.aliexpress.com/_c38oxv2b)  

### 8- Gyroscope
MPU-6050 gyroscope and accelerometer. Small, efficient, available.  
Cost: $2 [AliExpress](https://a.aliexpress.com/_c38oxv2b)  

### 9- Camera
Ultra-wide USB camera. Better than Pi camera & easier to program.

### 10- Jumper Wires
Male to male, male to female, female to female. Strong, reusable, Raspberry Pi compatible.  
Cost: $3 [AliExpress](https://a.aliexpress.com/_c38oxv2b)  

### 11- On/Off Button
Regular switch, inexpensive and easy to install.

---

## Software

- Language: Python 3, main Raspberry Pi language, large library support, big community.  
- Operating System: Linux compatible with our Raspberry Pi version, includes all libraries and programming tools.

![Software](images/Software.jpg)

---

## Experience and Acquired Expertise

We gained valuable skills:

- Team spirit, cooperation, and shared decision-making.  
- Problem-solving in programming and hardware.  
- Overcoming obstacles in our first robotics project.

Advanced technical expertise:

- Developing intelligent systems based on computer vision and integrating multiple sensors to increase robot awareness of the surrounding environment.  
- Developing an integrated vehicle based on open source components, including motors, sensors, and electromechanical control systems, with the ability to be modified and continuously developed to enhance performance and reliability.

---

## Special Thanks

Engineer Wissam Nasriyah – guidance from zero to hero.  
Engineer Mohammed Dababseh and Supervisor Abeer Mosa – valuable support in several tasks.

---

## Conclusion and Future Vision

This project was about building a robot and proving what motivated students can achieve.  
Next, we aim to expand into real-world robotics solutions to help people daily.  

**Nova Team – Building today, imagining tomorrow**
