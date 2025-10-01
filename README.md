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

We are a team of three members:

### Amr Younis
A fifteen-year-old Palestinian.  
Instagram: [amr.younis04](https://www.instagram.com/amr.younis04)

### Mohammad Abu Laban
A fifteen-year-old Palestinian.  
Instagram: [mo_abu_lab](https://www.instagram.com/mo_abu_lab)

### Ibrahim Mummar
A fifteen-year-old Palestinian.  
Instagram: [lbrameem_mum](https://www.instagram.com/lbrameem_mum)

We are pleased to introduce our project, which involves building and programming a robot capable of traversing a specific path. This path consists of a white carpet with two lines in each corner, as well as an orange line and a blue line. The carpet measures three meters long and three meters wide, surrounded by a 10-cm-high black wooden wall, with a 10-cm-high square black wooden wall in the middle of the carpet.

---

## Power and Sense Management

<table>
<tr>
<td>

We used a 12.6-volt, 6A rechargeable lithium battery. It’s a medium-weight battery with large capacity, sufficient for all components. We distributed the power correctly so that no single component consumes more than its share.

</td>
<td>

<img src="images/Battery.jpg" alt="Battery" width="200">

</td>
</tr>
</table>

---

## Obstacle Management

<table>
<tr>
<td>

The robot deals with obstacles using ultrasonic sensors and a camera.

Ultrasonic technology measures the distance between the obstacle and the robot, enabling it to adjust its direction. It works by sending out sound waves and measuring their bounce.

The camera recognizes colors and sends a signal to the Raspberry Pi. For example, when detecting red, the robot reacts according to the instructions we programmed.

</td>
<td>

<img src="images/Ultrasonic.jpg" alt="Ultrasonic Sensor" width="200"><br>
<img src="images/Camera.jpg" alt="Camera" width="200">

</td>
</tr>
</table>

---

## Engineering Factor

We started with a ready-made kit and modified it to suit our task. For example, we added additional layers to contain all the parts and ensured balanced weight distribution, placing the battery in the middle to prevent tilting.

---

## Hardware

### 1- The Robot

We modified a ready-made kit by adding one acrylic layer and two plastic layers, giving us four in total:

- Ground layer: DC motor and servo motor
- Second layer: Battery
- Third layer: Power button and power regulation circuit
- Fourth layer: Raspberry Pi, gyroscope, three ultrasonic sensors, camera and motor driver

All connected with jumper wires.

<table>
<tr>
<td>

</td>
<td>

<img src="images/Motor.jpg" alt="Motor" width="200"><br>
<img src="images/Servo.jpg" alt="Servo Motor" width="200">

</td>
</tr>
</table>

### 2- Kit Used

MG996 car model servo and DC motor  
Available in Palestine and suitable for our task  
Cost: $95 [AliExpress](https://a.aliexpress.com/_c3kFLPlv)

### 3- Microcontroller

Raspberry Pi 4 8GB RAM  
Fast CPU, Python support, and available locally  
Cost: $92 [AliExpress](https://a.aliexpress.com/_c2yjCN0B)

<img src="images/RaspberryPi.jpg" alt="Raspberry Pi" width="200">

### 4- Battery

12.6V, 6A lithium battery  
High voltage & capacity, adjustable output

<img src="images/Battery.jpg" alt="Battery" width="200">

### 5- DC Power Converter

XL4015 (32V → 1.25V adjustable)  
Easy to install  
Cost: $1 [AliExpress](https://a.aliexpress.com/_c38oxv2b)

<img src="images/Converter.jpg" alt="DC Converter" width="200">

### 6- Ultrasonic Sensors

3 × HC-SR04  
Voltage: 3.3 to 5V  
Range: 2cm to 400cm  
Cost: $1 each [AliExpress](https://a.aliexpress.com/_c2yngsHj)

<img src="images/Ultrasonic.jpg" alt="Ultrasonic Sensor" width="200">

### 7- Motor Driver

L298N motor driver  
Sufficient for our motors  
Cost: $1.50 AliExpress

<img src="images/MotorDriver.jpg" alt="Motor Driver" width="200">

### 8- Gyroscope

MPU-6050 gyroscope and accelerometer  
Small, efficient, available  
Cost: $2 AliExpress

<img src="images/Gyroscope.jpg" alt="Gyroscope" width="200">

### 9- Camera

Ultra-wide USB camera  
Better than Pi camera & easier to program

<img src="images/Camera.jpg" alt="Camera" width="200">

### 10- Jumper Wires

Male to male, male to female, female to female  
Strong, reusable, Raspberry Pi compatible  
Cost: $3 AliExpress

<img src="images/JumperWires.jpg" alt="Jumper Wires" width="200">

### 11- On/Off Button

Regular switch  
Inexpensive and easy to install

<img src="images/OnOffButton.jpg" alt="On/Off Button" width="150">

---

## Software

We programmed the robot using Python 3 on Linux (Raspberry Pi OS). Python was chosen for its large library support and flexibility. Libraries such as OpenCV were used for image processing, while GPIO libraries allowed us to control motors and sensors.

---

## Experience and Acquired Expertise

This project gave us valuable skills:

- Teamwork and decision-making
- Problem-solving in programming and hardware
- Overcoming obstacles in robotics for the first time

We also gained technical expertise:

- Computer vision and sensor integration
- Open-source robotics design
- Balancing power, weight, and stability in engineering design

---

## Special Thanks

Engineer Wissam Nasriyah – for guiding us from zero to hero.  
Engineer Mohammed Dababseh and Supervisor Abeer Mosa – for their valuable support.

---

## Conclusion and Future Vision

This project was not just about building a robot — it was about proving what motivated students can achieve with creativity, persistence, and teamwork.

Our next steps will focus on turning our passion for robotics into solutions that can help people in everyday life. From intelligent navigation systems to practical automation, we aim to expand the boundaries of what we can design and build.

**Nova Team – Building today, imagining tomorrow**
