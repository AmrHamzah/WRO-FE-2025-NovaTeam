<h1 style="font-family:Verdana; font-size:40px; color:blue;">Nova Team – WRO Future Engineers 2025</h1>

<!-- Banner -->
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom:20px;">
  <div style="flex: 1; font-family:Verdana;">
    <p>Welcome to our official GitHub page for the WRO Future Engineers 2025 competition!</p>
  </div>
  <div>
    <img src="images/banner.jpg" alt="Nova Team Banner" width="400" style="margin-left:20px; border-radius:10px;">
  </div>
</div>

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
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom:20px;">
  <div style="flex: 1; font-family:Verdana;">
    <p>
      We are a team of three 15-year-old Palestinians who built and programmed a robot capable of traversing a specific path in WRO.
    </p>
    <h2 style="color:blue;">Amr Younis</h2>
    <p>Instagram: <a href="https://www.instagram.com/amr.younis04" target="_blank">amr.younis04</a></p>

    <h2 style="color:blue;">Mohammad Abu Laban</h2>
    <p>Instagram: <a href="https://www.instagram.com/mo_abu_lab" target="_blank">mo_abu_lab</a></p>

    <h2 style="color:blue;">Ibrahim Mummar</h2>
    <p>Instagram: <a href="https://www.instagram.com/lbrameem_mum" target="_blank">lbrameem_mum</a></p>
  </div>
  <div>
    <img src="images/Robot.jpg" alt="Team Robot" width="250" style="margin-left:20px; border-radius:10px;">
  </div>
</div>

<hr>

<h1 id="power" style="font-family:Verdana; color:blue;">Power and Sense Management</h1>
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom:20px;">
  <div style="flex: 1; font-family:Verdana;">
    <p>
      We used a 12.6V, 6A rechargeable lithium battery. It provides enough capacity to power all components, 
      with correct distribution so no single part consumes more than its share.
    </p>
  </div>
  <div>
    <img src="images/Battery.jpg" alt="Lithium Battery" width="250" style="margin-left:20px; border-radius:10px;">
  </div>
</div>

<hr>

<h1 id="obstacle" style="font-family:Verdana; color:blue;">Obstacle Management</h1>
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom:20px;">
  <div style="flex: 1; font-family:Verdana;">
    <p>
      The robot deals with obstacles using ultrasonic sensors and a camera.
      Ultrasonic technology measures the distance between obstacles and the robot, enabling it to adjust its direction.
      The camera recognizes colors and sends a signal to the Raspberry Pi. For example, when detecting red, the robot reacts according to the programmed instructions.
    </p>
  </div>
  <div>
    <img src="images/Ultrasonic.jpg" alt="Ultrasonic Sensor" width="250" style="margin-left:20px; border-radius:10px;">
  </div>
</div>

<hr>

<h1 id="engineering" style="font-family:Verdana; color:blue;">Engineering Factor</h1>
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom:20px;">
  <div style="flex: 1; font-family:Verdana;">
    <p>
      We started with a ready-made kit and modified it to suit our task. We added additional layers to contain all the parts and ensured balanced weight distribution, placing the battery in the middle to prevent tilting.
    </p>
  </div>
  <div>
    <img src="images/Robot.jpg" alt="Robot Layers" width="250" style="margin-left:20px; border-radius:10px;">
  </div>
</div>

<hr>

<h1 id="hardware" style="font-family:Verdana; color:blue;">Hardware</h1>

<!-- Ground + Servo Motor -->
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom:20px;">
  <div style="flex: 1; font-family:Verdana;">
    <h2 style="color:blue;">1- Ground Layer</h2>
    DC motor and servo motor (MG996). Available in Palestine and suitable for our task. <br>
    Cost: $95 <a href="https://a.aliexpress.com/_c3kFLPlv" target="_blank">AliExpress</a>
  </div>
  <div>
    <img src="images/Servo.jpg" alt="Servo Motor" width="250" style="margin-left:20px; border-radius:10px;">
  </div>
</div>

<!-- Battery Layer -->
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom:20px;">
  <div style="flex: 1; font-family:Verdana;">
    <h2 style="color:blue;">2- Battery Layer</h2>
    12.6V, 6A lithium battery with high voltage and adjustable output.
  </div>
  <div>
    <img src="images/Battery.jpg" alt="Battery" width="250" style="margin-left:20px; border-radius:10px;">
  </div>
</div>

<!-- Power Converter Layer -->
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom:20px;">
  <div style="flex: 1; font-family:Verdana;">
    <h2 style="color:blue;">3- Power Converter Layer</h2>
    XL4015 (32V → 1.25V adjustable). Easy to install. <br>
    Cost: $1 <a href="https://a.aliexpress.com/_c38oxv2b" target="_blank">AliExpress</a>
  </div>
  <div>
    <img src="images/Converter.jpg" alt="DC Converter" width="250" style="margin-left:20px; border-radius:10px;">
  </div>
</div>

<!-- Raspberry Pi + Sensors Layer -->
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom:20px;">
  <div style="flex: 1; font-family:Verdana;">
    <h2 style="color:blue;">4- Sensors and Controller Layer</h2>
    Raspberry Pi 4 8GB RAM, MPU-6050 gyroscope, 3 × HC-SR04 ultrasonic sensors, ultra-wide USB camera, L298N motor driver, jumper wires, power button.  
    Cost of Raspberry Pi: $92 <a href="https://a.aliexpress.com/_c2yjCN0B" target="_blank">AliExpress</a>
  </div>
  <div>
    <img src="images/RaspberryPi.jpg" alt="Raspberry Pi Layer" width="250" style="margin-left:20px; border-radius:10px;">
  </div>
</div>

<hr>

<h1 id="software" style="font-family:Verdana; color:blue;">Software</h1>
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom:20px;">
  <div style="flex: 1; font-family:Verdana;">
    <p>
      We programmed the robot using Python 3 on Linux. Python libraries like OpenCV and GPIO allowed us to integrate computer vision and control motors & sensors effectively.
    </p>
  </div>
  <div>
    <img src="images/Software.jpg" alt="Software" width="250" style="margin-left:20px; border-radius:10px;">
  </div>
</div>

<hr>

<h1 id="experience" style="font-family:Verdana; color:blue;">Experience and Acquired Expertise</h1>
<p style="font-family:Verdana;">
We gained teamwork, problem-solving, and technical skills in both programming and hardware.  
We developed expertise in sensor integration, motor control, and computer vision for robotics.
</p>

<hr>

<h1 id="special-thanks" style="font-family:Verdana; color:blue;">Special Thanks</h1>
<p style="font-family:Verdana;">
Engineer Wissam Nasriyah – guidance from zero to hero.<br>
Engineer Mohammed Dababseh and Supervisor Abeer Mosa – valuable support.
</p>

<hr>

<h1 id="conclusion" style="font-family:Verdana; color:blue;">Conclusion and Future Vision</h1>
<p style="font-family:Verdana;">
This project was about building a robot and proving what motivated students can achieve.  
Next, we aim to expand into real-world robotics solutions to help people daily.  
<b>Nova Team – Building today, imagining tomorrow</b>
</p>
