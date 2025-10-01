<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Nova Team – WRO Future Engineers 2025</title>
<style>
  body { font-family:Verdana; line-height:1.5; }
  a { text-decoration:none; color:blue; } /* يلغي أي خط تحت الروابط */
  h1, h2 { color:blue; text-decoration:none; } /* يلغي أي خط تحت العناوين */
  code, pre { display:none; } /* يخفي أي صندوق كود */
  img { border-radius:10px; margin-bottom:10px; }
  .right-img { float:right; margin-left:20px; margin-bottom:20px; }
</style>
</head>
<body>

<h1 style="font-size:40px;">Nova Team – WRO Future Engineers 2025</h1>

<!-- Banner -->
<img src="images/banner.jpg" alt="Nova Team Banner" style="width:100%; max-width:800px; margin-bottom:20px;">

<h2>Table of Contents</h2>
<ul>
  <li><a href="#about-us">About Us</a></li>
  <li><a href="#power-sense">Power and Sense Management</a></li>
  <li><a href="#obstacle">Obstacle Management</a></li>
  <li><a href="#engineering">Engineering Factor</a></li>
  <li><a href="#hardware">Hardware</a></li>
  <li><a href="#software">Software</a></li>
  <li><a href="#experience">Experience and Acquired Expertise</a></li>
  <li><a href="#special-thanks">Special Thanks</a></li>
  <li><a href="#conclusion">Conclusion and Future Vision</a></li>
</ul>
<hr>

<h1 id="about-us">About Us</h1>
<p>We are a team of three members:</p>

<h2>Amr Younis</h2>
<p>
A fifteen-year-old Palestinian.<br>
Instagram: <a href="https://www.instagram.com/amr.younis04" target="_blank">amr.younis04</a>
</p>

<h2>Mohammad Abu Laban</h2>
<p>
A fifteen-year-old Palestinian.<br>
Instagram: <a href="https://www.instagram.com/mo_abu_lab" target="_blank">mo_abu_lab</a>
</p>

<h2>Ibrahim Mummar</h2>
<p>
A fifteen-year-old Palestinian.<br>
Instagram: <a href="https://www.instagram.com/lbrameem_mum" target="_blank">lbrameem_mum</a>
</p>

<p>
We are pleased to introduce our project, which involves building and programming a robot capable of traversing a specific path. This path consists of a white carpet with two lines in each corner, as well as an orange line and a blue line. The carpet measures three meters long and three meters wide, surrounded by a 10-cm-high black wooden wall, with a 10-cm-high square black wooden wall in the middle of the carpet.
</p>

<hr>

<h1 id="power-sense">Power and Sense Management</h1>
<p>
We used a 12.6-volt, 6A rechargeable lithium battery. It’s a medium-weight battery with large capacity, sufficient for all components. We distributed the power correctly so that no single component consumes more than its share.
</p>

<img src="images/Battery.jpg" alt="Lithium Battery" class="right-img">

<hr>

<h1 id="obstacle">Obstacle Management</h1>
<p>The robot deals with obstacles using ultrasonic sensors and a camera.</p>
<p>Ultrasonic technology measures the distance between the obstacle and the robot, enabling it to adjust its direction. It works by sending out sound waves and measuring their bounce.</p>
<p>The camera recognizes colors and sends a signal to the Raspberry Pi. For example, when detecting red, the robot reacts according to the instructions we programmed.</p>

<img src="images/Ultrasonic.jpg" alt="Ultrasonic Sensor" class="right-img">
<img src="images/Camera.jpg" alt="Camera" class="right-img">

<hr>

<h1 id="engineering">Engineering Factor</h1>
<p>
We started with a ready-made kit and modified it to suit our task. For example, we added additional layers to contain all the parts and ensured balanced weight distribution, placing the battery in the middle to prevent tilting.
</p>

<hr>

<h1 id="hardware">Hardware</h1>

<h2>1- The Robot</h2>
<table>
<tr>
<td style="vertical-align:top; padding-right:20px;">
<p>
We modified a ready-made kit by adding one acrylic layer and two plastic layers, giving us four in total:
<ul>
  <li>Ground layer: DC motor and servo motor</li>
  <li>Second layer: Battery</li>
  <li>Third layer: Power button and power regulation circuit</li>
  <li>Fourth layer: Raspberry Pi, gyroscope, three ultrasonic sensors, camera and motor driver</li>
</ul>
All connected with jumper wires.
</p>
</td>
<td>
<img src="images/Motor.jpg" alt="Motor" width="300" class="right-img">
<img src="images/Servo.jpg" alt="Servo Motor" width="300" class="right-img">
</td>
</tr>
</table>

<h2>2- Kit Used</h2>
<p>
MG996 car model servo and DC motor<br>
Available in Palestine and suitable for our task<br>
Cost: $95 <a href="https://a.aliexpress.com/_c3kFLPlv" target="_blank">AliExpress</a>
</p>

<h2>3- Microcontroller</h2>
<table>
<tr>
<td style="vertical-align:top; padding-right:20px;">
<p>
Raspberry Pi 4 8GB RAM<br>
Fast CPU, Python support, and available locally<br>
Cost: $92 <a href="https://a.aliexpress.com/_c2yjCN0B" target="_blank">AliExpress</a>
</p>
</td>
<td>
<img src="images/RaspberryPi.jpg" alt="Raspberry Pi" width="300" class="right-img">
</td>
</tr>
</table>

<h2>4- Battery</h2>
<table>
<tr>
<td style="vertical-align:top; padding-right:20px;">
<p>12.6V, 6A lithium battery<br>High voltage & capacity, adjustable output</p>
</td>
<td>
<img src="images/Battery.jpg" alt="Battery" width="300" class="right-img">
</td>
</tr>
</table>

<h2>5- DC Power Converter</h2>
<table>
<tr>
<td style="vertical-align:top; padding-right:20px;">
<p>XL4015 (32V → 1.25V adjustable)<br>Easy to install<br>Cost: $1 <a href="https://a.aliexpress.com/_c38oxv2b" target="_blank">AliExpress</a></p>
</td>
<td>
<img src="images/Converter.jpg" alt="DC Converter" width="300" class="right-img">
</td>
</tr>
</table>

<h2>6- Ultrasonic Sensors</h2>
<table>
<tr>
<td style="vertical-align:top; padding-right:20px;">
<p>3 × HC-SR04<br>Voltage: 3.3 to 5V<br>Range: 2cm to 400cm<br>Cost: $1 each <a href="https://a.aliexpress.com/_c2yngsHj" target="_blank">AliExpress</a></p>
</td>
<td>
<img src="images/Ultrasonic.jpg" alt="Ultrasonic Sensor" width="300" class="right-img">
</td>
</tr>
</table>

<h2>7- Motor Driver</h2>
<table>
<tr>
<td style="vertical-align:top; padding-right:20px;">
<p>L298N motor driver<br>Sufficient for our motors<br>Cost: $1.50 AliExpress</p>
</td>
<td>
<img src="images/MotorDriver.jpg" alt="Motor Driver" width="300" class="right-img">
</td>
</tr>
</table>

<h2>8- Gyroscope</h2>
<table>
<tr>
<td style="vertical-align:top; padding-right:20px;">
<p>MPU-6050 gyroscope and accelerometer<br>Small, efficient, available<br>Cost: $2 AliExpress</p>
</td>
<td>
<img src="images/Gyroscope.jpg" alt="Gyroscope" width="300" class="right-img">
</td>
</tr>
</table>

<h2>9- Camera</h2>
<table>
<tr>
<td style="vertical-align:top; padding-right:20px;">
<p>Ultra-wide USB camera<br>Better than Pi camera & easier to program</p>
</td>
<td>
<img src="images/Camera.jpg" alt="Camera" width="300" class="right-img">
</td>
</tr>
</table>

<h2>10- Jumper Wires</h2>
<table>
<tr>
<td style="vertical-align:top; padding-right:20px;">
<p>Male to male, male to female, female to female<br>Strong, reusable, Raspberry Pi compatible<br>Cost: $3 AliExpress</p>
</td>
<td>
<img src="images/JumperWires.jpg" alt="Jumper Wires" width="300" class="right-img">
</td>
</tr>
</table>

<h2>11- On/Off Button</h2>
<table>
<tr>
<td style="vertical-align:top; padding-right:20px;">
<p>Regular switch<br>Inexpensive and easy to install</p>
</td>
<td>
<img src="images/OnOffButton.jpg" alt="On/Off Button" width="150" class="right-img">
</td>
</tr>
</table>

<hr>

<h1 id="software">Software</h1>
<p>We programmed the robot using Python 3 on Linux (Raspberry Pi OS). Python was chosen for its large library support and flexibility. Libraries such as OpenCV were used for image processing, while GPIO libraries allowed us to control motors and sensors.</p>

<hr>

<h1 id="experience">Experience and Acquired Expertise</h1>
<p>This project gave us valuable skills:</p>
<ul>
  <li>Teamwork and decision-making</li>
  <li>Problem-solving in programming and hardware</li>
  <li>Overcoming obstacles in robotics for the first time</li>
</ul>

<p>We also gained technical expertise:</p>
<ul>
  <li>Computer vision and sensor integration</li>
  <li>Open-source robotics design</li>
  <li>Balancing power, weight, and stability in engineering design</li>
</ul>

<hr>

<h1 id="special-thanks">Special Thanks</h1>
<p>Engineer Wissam Nasriyah – for guiding us from zero to hero.<br>
Engineer Mohammed Dababseh and Supervisor Abeer Mosa – for their valuable support.</p>

<hr>

<h1 id="conclusion">Conclusion and Future Vision</h1>
<p>This project was not just about building a robot — it was about proving what motivated students can achieve with creativity, persistence, and teamwork.</p>
<p>Our next steps will focus on turning our passion for robotics into solutions that can help people in everyday life. From intelligent navigation systems to practical automation, we aim to expand the boundaries of what we can design and build.</p>
<p><b>Nova Team – Building today, imagining tomorrow</b></p>

</body>
</html>
