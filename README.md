<h1 style="font-family:Verdana; font-size:40px; color:blue;">Nova Team – WRO Future Engineers 2025</h1>

<!-- Banner -->
<img src="images/banner.jpg" alt="Nova Team Banner" style="width:100%; max-width:800px;">

<h2 style="font-family:Verdana; color:blue;">Table of Contents</h2>
<ul style="font-family:Verdana;">
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

<h1 id="about-us" style="font-family:Verdana; color:blue;">About Us</h1>
<p style="font-family:Verdana;">
We are a team of three members:
</p>

<h2 style="font-family:Verdana; color:blue;">Amr Younis</h2>
<p style="font-family:Verdana;">
A fifteen-year-old Palestinian.<br>
Instagram: <a href="https://www.instagram.com/amr.younis04" target="_blank">amr.younis04</a>
</p>

<h2 style="font-family:Verdana; color:blue;">Mohammad Abu Laban</h2>
<p style="font-family:Verdana;">
A fifteen-year-old Palestinian.<br>
Instagram: <a href="https://www.instagram.com/mo_abu_lab" target="_blank">mo_abu_lab</a>
</p>

<h2 style="font-family:Verdana; color:blue;">Ibrahim Mummar</h2>
<p style="font-family:Verdana;">
A fifteen-year-old Palestinian.<br>
Instagram: <a href="https://www.instagram.com/lbrameem_mum" target="_blank">lbrameem_mum</a>
</p>

<p style="font-family:Verdana;">
We are pleased to introduce our project, which involves building and programming a robot capable of traversing a specific path. This path consists of a white carpet with two lines in each corner, as well as an orange line and a blue line. The carpet measures three meters long and three meters wide, surrounded by a 10-cm-high black wooden wall, with a 10-cm-high square black wooden wall in the middle of the carpet.
</p>

<hr>

<h1 id="power-sense" style="font-family:Verdana; color:blue;">Power and Sense Management</h1>
<p style="font-family:Verdana;">
We used a 12.6-volt, 6A rechargeable lithium battery. It’s a medium-weight battery with large capacity, sufficient for all components. We distributed the power correctly so that no single component consumes more than its share.
</p>

<img src="images/Battery.jpg" alt="Lithium Battery" style="width:300px;">

<hr>

<h1 id="obstacle" style="font-family:Verdana; color:blue;">Obstacle Management</h1>
<p style="font-family:Verdana;">
The robot deals with obstacles using ultrasonic sensors and a camera.
</p>
<p style="font-family:Verdana;">
Ultrasonic technology measures the distance between the obstacle and the robot, enabling it to adjust its direction. It works by sending out sound waves and measuring their bounce.
</p>
<p style="font-family:Verdana;">
The camera recognizes colors and sends a signal to the Raspberry Pi. For example, when detecting red, the robot reacts according to the instructions we programmed.
</p>

<img src="images/Ultrasonic.jpg" alt="Ultrasonic Sensor" style="width:300px;">
<img src="images/Camera.jpg" alt="Camera" style="width:300px;">

<hr>

<h1 id="engineering" style="font-family:Verdana; color:blue;">Engineering Factor</h1>
<p style="font-family:Verdana;">
We started with a ready-made kit and modified it to suit our task. For example, we added additional layers to contain all the parts and ensured balanced weight distribution, placing the battery in the middle to prevent tilting.
</p>

<hr>

<h1 id="hardware" style="font-family:Verdana; color:blue;">Hardware</h1>

<h2 style="font-family:Verdana; color:blue;">1- The Robot</h2>
<p style="font-family:Verdana;">
We modified a ready-made kit by adding one acrylic layer and two plastic layers, giving us four in total:
</p>
<ul style="font-family:Verdana;">
  <li>Ground layer: DC motor and servo motor</li>
  <li>Second layer: Battery</li>
  <li>Third layer: Power button and power regulation circuit</li>
  <li>Fourth layer: Raspberry Pi, gyroscope, three ultrasonic sensors, camera and motor driver</li>
</ul>
<p style="font-family:Verdana;">
All connected with jumper wires.
</p>
<img src="images/Motor.jpg" alt="Motor" style="width:300px;">
<img src="images/Servo.jpg" alt="Servo Motor" style="width:300px;">

<h2 style="font-family:Verdana; color:blue;">2- Kit Used</h2>
<p style="font-family:Verdana;">
MG996 car model servo and DC motor<br>
Available in Palestine and suitable for our task<br>
Cost: $95 <a href="https://a.aliexpress.com/_c3kFLPlv" target="_blank">AliExpress</a>
</p>

<h2 style="font-family:Verdana; color:blue;">3- Microcontroller</h2>
<p style="font-family:Verdana;">
Raspberry Pi 4 8GB RAM<br>
Fast CPU, Python support, and available locally<br>
Cost: $92 <a href="https://a.aliexpress.com/_c2yjCN0B" target="_blank">AliExpress</a>
</p>
<img src="images/RaspberryPi.jpg" alt="Raspberry Pi" style="width:300px;">

<h2 style="font-family:Verdana; color:blue;">4- Battery</h2>
<p style="font-family:Verdana;">
12.6V, 6A lithium battery<br>
High voltage & capacity, adjustable output
</p>

<h2 style="font-family:Verdana; color:blue;">5- DC Power Converter</h2>
<p style="font-family:Verdana;">
XL4015 (32V → 1.25V adjustable)<br>
Easy to install<br>
Cost: $1 <a href="https://a.aliexpress.com/_c38oxv2b" target="_blank">AliExpress</a>
</p>
<img src="images/Converter.jpg" alt="DC Converter" style="width:300px;">

<h2 style="font-family:Verdana; color:blue;">6- Ultrasonic Sensors</h2>
<p style="font-family:Verdana;">
3 × HC-SR04<br>
Voltage: 3.3 to 5V<br>
Range: 2cm to 400cm<br>
Cost: $1 each <a href="https://a.aliexpress.com/_c2yngsHj" target="_blank">AliExpress</a>
</p>

<h2 style="font-family:Verdana; color:blue;">7- Motor Driver</h2>
<p style="font-family:Verdana;">
L298N motor driver<br>
Sufficient for our motors<br>
Cost: $1.50 AliExpress
</p>
<img src="images/MotorDriver.jpg" alt="Motor Driver" style="width:300px;">

<h2 style="font-family:Verdana; color:blue;">8- Gyroscope</h2>
<p style="font-family:Verdana;">
MPU-6050 gyroscope and accelerometer<br>
Small, efficient, available<br>
Cost: $2 AliExpress
</p>
<img src="images/Gyroscope.jpg" alt="Gyroscope" style="width:300px;">

<h2 style="font-family:Verdana; color:blue;">9- Camera</h2>
<p style="font-family:Verdana;">
Ultra-wide USB camera<br>
Better than Pi camera & easier to program
</p>

<h2 style="font-family:Verdana; color:blue;">10- Jumper Wires</h2>
<p style="font-family:Verdana;">
Male to male, male to female, female to female<br>
Strong, reusable, Raspberry Pi compatible<br>
Cost: $3 AliExpress
</p>
<img src="images/JumperWires.jpg" alt="Jumper Wires" style="width:300px;">

<h2 style="font-family:Verdana; color:blue;">11- On/Off Button</h2>
<p style="font-family:Verdana;">
Regular switch<br>
Inexpensive and easy to install
</p>

<hr>

<h1 id="software" style="font-family:Verdana; color:blue;">Software</h1>
<p style="font-family:Verdana;">
We programmed the robot using Python 3 on Linux (Raspberry Pi OS). Python was chosen for its large library support and flexibility. Libraries such as OpenCV were used for image processing, while GPIO libraries allowed us to control motors and sensors.
</p>

<hr>

<h1 id="experience" style="font-family:Verdana; color:blue;">Experience and Acquired Expertise</h1>
<p style="font-family:Verdana;">
This project gave us valuable skills:
</p>
<ul style="font-family:Verdana;">
  <li>Teamwork and decision-making</li>
  <li>Problem-solving in programming and hardware</li>
  <li>Overcoming obstacles in robotics for the first time</li>
</ul>

<p style="font-family:Verdana;">
We also gained technical expertise:
</p>
<ul style="font-family:Verdana;">
  <li>Computer vision and sensor integration</li>
  <li>Open-source robotics design</li>
  <li>Balancing power, weight, and stability in engineering design</li>
</ul>

<hr>

<h1 id="special-thanks" style="font-family:Verdana; color:blue;">Special Thanks</h1>
<p style="font-family:Verdana;">
Engineer Wissam Nasriyah – for guiding us from zero to hero.<br>
Engineer Mohammed Dababseh and Supervisor Abeer Mosa – for their valuable support.
</p>

<hr>

<h1 id="conclusion" style="font-family:Verdana; color:blue;">Conclusion and Future Vision</h1>
<p style="font-family:Verdana;">
This project was not just about building a robot — it was about proving what motivated students can achieve with creativity, persistence, and teamwork.
</p>
<p style="font-family:Verdana;">
Our next steps will focus on turning our passion for robotics into solutions that can help people in everyday life. From intelligent navigation systems to practical automation, we aim to expand the boundaries of what we can design and build.
</p>
<p style="font-family:Verdana;">
<b>Nova Team – Building today, imagining tomorrow</b>
</p>
