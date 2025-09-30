<h1 style="font-family:Verdana; font-size:40px; color:blue;">Nova Team – WRO Future Engineers 2025</h1>

<h1 style="font-family:Verdana; color:blue;">About Us</h1>
<p style="font-family:Verdana;">
We are a team of three members:
</p><h2 style="font-family:Verdana; color:blue;">Amr Younis</h2>
<p style="font-family:Verdana;">
A fifteen-year-old Palestinian.<br>
Instagram: <a href="https://www.instagram.com/amr.younis04" target="_blank">amr.younis04</a>
</p><h2 style="font-family:Verdana; color:blue;">Mohammad Abu Laban</h2>
<p style="font-family:Verdana;">
A fifteen-year-old Palestinian.<br>
Instagram: <a href="https://www.instagram.com/mo_abu_lab" target="_blank">mo_abu_lab</a>
</p><h2 style="font-family:Verdana; color:blue;">Ibrahim Mummar</h2>
<p style="font-family:Verdana;">
A fifteen-year-old Palestinian.<br>
Instagram: <a href="https://www.instagram.com/lbrameem_mum" target="_blank">lbrameem_mum</a>
</p><p style="font-family:Verdana;">
We are pleased to introduce our project, which involves building and programming a robot capable of traversing a specific path. This path consists of a white carpet with two lines in each corner, as well as an orange line and a blue line. The carpet measures three meters long and three meters wide, surrounded by a 10-cm-high black wooden wall, with a 10-cm-high square black wooden wall in the middle of the carpet.
</p><hr><h1 style="font-family:Verdana; color:blue;">Power and Sense Management</h1>
<p style="font-family:Verdana;">
We used a 12.6-volt, 6A rechargeable lithium battery. It’s a medium-weight battery with large capacity, sufficient for all components. We distributed the power correctly so that no single component consumes more than its share.
</p>
<p style="font-family:Verdana;">
Choosing this battery was critical. If the battery were weaker, the motors would lose torque and the robot might stop in the middle of the course. If it were too heavy, the robot would struggle with speed and balance. By carefully selecting and placing it, we ensured that the power supply could support continuous operation for long practice sessions without overheating or draining too quickly. This decision improved both performance and reliability, allowing us to focus more on programming rather than constant charging.
</p>

<hr><h1 style="font-family:Verdana; color:blue;">Obstacle Management</h1>
<p style="font-family:Verdana;">
The robot deals with obstacles using ultrasonic sensors and a camera.
</p>
<p style="font-family:Verdana;">
Ultrasonic technology measures the distance between the obstacle and the robot, enabling it to adjust its direction. It works by sending out sound waves and measuring their bounce.
</p>
<p style="font-family:Verdana;">
The camera recognizes colors and sends a signal to the Raspberry Pi. For example, when detecting red, the robot reacts according to the instructions we programmed.
</p>
<p style="font-family:Verdana;">
This dual system – ultrasonic plus vision – is similar to how humans use both hearing and sight. Ultrasonic sensors act like ears, quickly sensing nearby objects even if they’re not visible. The camera acts like eyes, allowing the robot to interpret colors as “commands.” Together, they form a smart decision-making system. For instance, if the ultrasonic detects an obstacle at 15 cm, the robot immediately slows down, while the camera might confirm if it’s a wall, a corner, or a colored line. This combination prevents mistakes and makes the robot’s navigation more natural and adaptive.
</p><hr><h1 style="font-family:Verdana; color:blue;">Engineering Factor</h1>
<p style="font-family:Verdana;">
We started with a ready-made kit and modified it to suit our task. For example, we added additional layers to contain all the parts and ensured balanced weight distribution, placing the battery in the middle to prevent tilting.
</p>
<p style="font-family:Verdana;">
Although we began with a pre-assembled kit, we quickly realized that no “out of the box” solution could handle the competition requirements. That’s why modification became a key part of our engineering work. Adding layers was not just about stacking parts – it was about designing a structure where every sensor and component had a logical place. This step taught us how real engineers think: adapt, customize, and redesign until the system works as intended.
</p><hr><h1 style="font-family:Verdana; color:blue;">Hardware</h1><h2 style="font-family:Verdana; color:blue;">1- The Robot</h2>
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
</p><h2 style="font-family:Verdana; color:blue;">2- Kit Used</h2>
<p style="font-family:Verdana;">
MG996 car model servo and DC motor<br>
Available in Palestine and suitable for our task<br>
Cost: $95 <a href="https://a.aliexpress.com/_c3kFLPlv" target="_blank">AliExpress</a>
</p><h2 style="font-family:Verdana; color:blue;">3- Microcontroller</h2>
<p style="font-family:Verdana;">
Raspberry Pi 4 8GB RAM<br>
Fast CPU, Python support, and available locally<br>
Cost: $92 <a href="https://a.aliexpress.com/_c2yjCN0B" target="_blank">AliExpress</a>
</p><h2 style="font-family:Verdana; color:blue;">4- Battery</h2>
<p style="font-family:Verdana;">
12.6V, 6A lithium battery<br>
High voltage & capacity, adjustable output
</p><h2 style="font-family:Verdana; color:blue;">5- DC Power Converter</h2>
<p style="font-family:Verdana;">
XL4015 (32V → 1.25V adjustable)<br>
Easy to install<br>
Cost: $1 <a href="https://a.aliexpress.com/_c38oxv2b" target="_blank">AliExpress</a>
</p><h2 style="font-family:Verdana; color:blue;">6- Ultrasonic Sensors</h2>
