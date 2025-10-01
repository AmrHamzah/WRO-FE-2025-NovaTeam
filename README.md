<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Nova Team – WRO Future Engineers 2025</title>
</head>
<body style="font-family:Verdana; line-height:1.5;">

<h1 style="font-family:Verdana; font-size:40px; color:blue;">Nova Team – WRO Future Engineers 2025</h1>

<!-- Banner -->
<img src="images/banner.jpg" alt="Nova Team Banner" width="600" style="border-radius:10px; margin-bottom:20px;">

<hr>

<h1 style="font-family:Verdana; color:blue;">Table of Contents</h1>
<ul style="font-family:Verdana;">
  <li><a href="#about-us">About Us</a></li>
  <li><a href="#power">Power and Sense Management</a></li>
  <li><a href="#obstacle">Obstacle Management</a></li>
  <li><a href="#engineering">Engineering Factor</a></li>
  <li><a href="#hardware">Hardware</a></li>
  <li><a href="#software">Software</a></li>
  <li><a href="#experience">Experience and Acquired Expertise</a></li>
  <li><a href="#special-thanks">Special Thanks</a></li>
  <li><a href="#conclusion">Conclusion and Future Vision</a></li>
</ul>

<hr>

<h1 id="about-us" style="font-family:Verdana; color:blue;">About Us</h1>
<p>
We are a team of three 15-year-old Palestinians who built and programmed a robot capable of traversing a specific path in WRO.
</p>

<h2 style="font-family:Verdana; color:blue;">Amr Younis</h2>
<p>Instagram: <a href="https://www.instagram.com/amr.younis04" target="_blank">amr.younis04</a></p>

<h2 style="font-family:Verdana; color:blue;">Mohammad Abu Laban</h2>
<p>Instagram: <a href="https://www.instagram.com/mo_abu_lab" target="_blank">mo_abu_lab</a></p>

<h2 style="font-family:Verdana; color:blue;">Ibrahim Mummar</h2>
<p>Instagram: <a href="https://www.instagram.com/lbrameem_mum" target="_blank">lbrameem_mum</a></p>

<p>
The path consists of a white carpet with two lines in each corner, as well as an orange line and a blue line. The carpet measures three meters long and three meters wide, surrounded by a 10-cm-high black wooden wall, with a 10-cm-high square black wooden wall in the middle of the carpet.
</p>

<hr>

<h1 id="power" style="font-family:Verdana; color:blue;">Power and Sense Management</h1>
<p>
We used a 12.6V, 6A rechargeable lithium battery. It provides enough capacity to power all components, with correct distribution so no single part consumes more than its share.
</p>

<hr>

<h1 id="obstacle" style="font-family:Verdana; color:blue;">Obstacle Management</h1>
<p>
The robot deals with obstacles using ultrasonic sensors and a camera.
</p>
<p>
Ultrasonic technology measures the distance between obstacles and the robot, enabling it to adjust its direction.
</p>
<p>
The camera recognizes colors and sends a signal to the Raspberry Pi. For example, when detecting red, the robot reacts according to the programmed instructions.
</p>

<hr>

<h1 id="engineering" style="font-family:Verdana; color:blue;">Engineering Factor</h1>
<p>
We started with a ready-made kit and modified it to suit our task. We added additional layers to contain all the parts and ensured balanced weight distribution, placing the battery in the middle to prevent tilting.
</p>

<hr>

<h1 id="hardware" style="font-family:Verdana; color:blue;">Hardware</h1>

<h2 style="font-family:Verdana; color:blue;">1- Ground Layer</h2>
<table>
<tr>
<td style="vertical-align:top; padding-right:20px;">
<p>DC motor and MG996 servo motor</p>
</td>
<td>
<img src="images/DC_Motor.jpg" alt="DC Motor" width="200" style="border-radius:10px; float:right; margin-bottom:10px;">
<img src="images/Servo.jpg" alt="Servo Motor" width="200" style="border-radius:10px; float:right; margin-bottom:10px;">
</td>
</tr>
</table>

<h2 style="font-family:Verdana; color:blue;">2- Battery Layer</h2>
<table>
<tr>
<td style="vertical-align:top; padding-right:20px;">
<p>12.6V, 6A lithium battery</p>
</td>
<td>
<img src="images/Battery.jpg" alt="Battery" width="200" style="border-radius:10px; float:right; margin-bottom:10px;">
</td>
</tr>
</table>

<h2 style="font-family:Verdana; color:blue;">3- Power Converter</h2>
<table>
<tr>
<td style="vertical-align:top; padding-right:20px;">
<p>XL4015 (32V → 1.25V adjustable)</p>
</td>
<td>
<img src="images/Converter.jpg" alt="DC Converter" width="200" style="border-radius:10px; float:right; margin-bottom:10px;">
</td>
</tr>
</table>

<h2 style="font-family:Verdana; color:blue;">4- Ultrasonic Sensors</h2>
<table>
<tr>
<td style="vertical-align:top; padding-right:20px;">
<p>3 × HC-SR04 ultrasonic sensors</p>
</td>
<td>
<img src="images/Ultrasonic1.jpg" alt="Ultrasonic Sensor 1" width="150" style="border-radius:10px; float:right; margin-bottom:5px;">
<img src="images/Ultrasonic2.jpg" alt="Ultrasonic Sensor 2" width="150" style="border-radius:10px; float:right; margin-bottom:5px;">
<img src="images/Ultrasonic3.jpg" alt="Ultrasonic Sensor 3" width="150" style="border-radius:10px; float:right; margin-bottom:5px;">
</td>
</tr>
</table>

<h2 style="font-family:Verdana; color:blue;">5- Motor Driver</h2>
<table>
<tr>
<td style="vertical-align:top; padding-right:20px;">
<p>L298N motor driver</p>
</td>
<td>
<img src="images/MotorDriver.jpg" alt="Motor Driver" width="200" style="border-radius:10px; float:right; margin-bottom:10px;">
</td>
</tr>
</table>

<h2 style="font-family:Verdana; color:blue;">6- Gyroscope</h2>
<table>
<tr>
<td style="vertical-align:top; padding-right:20px;">
<p>MPU-6050 gyroscope and accelerometer</p>
</td>
<td>
<img src="images/Gyroscope.jpg" alt="Gyroscope" width="200" style="border-radius:10px; float:right; margin-bottom:10px;">
</td>
</tr>
</table>

<h2 style="font-family:Verdana; color:blue;">7- Camera</h2>
<table>
<tr>
<td style="vertical-align:top; padding-right:20px;">
<p>Ultra-wide USB camera</p>
</td>
<td>
<img src="images/Camera.jpg" alt="Camera" width="200" style="border-radius:10px; float:right; margin-bottom:10px;">
</td>
</tr>
</table>

<h2 style="font-family:Verdana; color:blue;">8- Jumper Wires</h2>
<table>
<tr>
<td style="vertical-align:top; padding-right:20px;">
<p>Male to male, male to female, female to female, reusable</p>
</td>
<td>
<img src="images/JumperWires.jpg" alt="Jumper Wires" width="200" style="border-radius:10px; float:right; margin-bottom:10px;">
</td>
</tr>
</table>

<h2 style="font-family:Verdana; color:blue;">9- On/Off Button</h2>
<table>
<tr>
<td style="vertical-align:top; padding-right:20px;">
<p>Regular switch</p>
</td>
<td>
<img src="images/OnOffButton.jpg" alt="On/Off Button" width="150" style="border-radius:10px; float:right; margin-bottom:10px;">
</td>
</tr>
</table>

<hr>

<h1 id="software" style="font-family:Verdana; color:blue;">Software</h1>
<p>
We programmed the robot using Python 3 on Linux. Python libraries like OpenCV and GPIO allowed us to integrate computer vision and control motors & sensors effectively.
</p>

<hr>

<h1 id="experience" style="font-family:Verdana; color:blue;">Experience and Acquired Expertise</h1>
<p>
We gained teamwork, problem-solving, and technical skills in both programming and hardware.<br>
We developed expertise in sensor integration, motor control, and computer vision for robotics.
</p>

<hr>

<h1 id="special-thanks" style="font-family:Verdana; color:blue;">Special Thanks</h1>
<p>
Engineer Wissam Nasriyah – guidance from zero to hero.<br>
Engineer Mohammed Dababseh and Supervisor Abeer Mosa – valuable support.
</p>

<hr>

<h1 id="conclusion" style="font-family:Verdana; color:blue;">Conclusion and Future Vision</h1>
<p>
This project was about building a robot and proving what motivated students can achieve.<br>
Next, we aim to expand into real-world robotics solutions to help people daily.<br>
<b>Nova Team – Building today, imagining tomorrow 🚀</b>
</p>

</body>
</html>
