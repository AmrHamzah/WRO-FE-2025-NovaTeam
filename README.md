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
</p>
<p style="font-family:Verdana;">
This description may sound simple at first, but the real challenge is in making the robot “understand” its environment. The carpet is not just a flat surface – the colored lines are signals that the robot must detect and respond to, while the walls act as physical obstacles that force the robot to adjust its path. The middle wall makes the path even trickier, because the robot cannot just move straight; it has to make decisions in real time to avoid crashing and still follow the mission.
</p><hr><h1 style="font-family:Verdana; color:blue;">Power and Sense Management</h1>
<p style="font-family:Verdana;">
We used a 12.6-volt, 6A rechargeable lithium battery. It’s a medium-weight battery with large capacity, sufficient for all components. We distributed the power correctly so that no single component consumes more than its share.
</p>
<p style="font-family:Verdana;">
Choosing this battery was critical. If the battery were weaker, the motors would lose torque and the robot might stop in the middle of the course. If it were too heavy, the robot would struggle with speed and balance. By carefully selecting and placing it, we ensured that the power supply could support continuous operation for long practice sessions without overheating or draining too quickly. This decision improved both performance and reliability, allowing us to focus more on programming rather than constant charging.
</p>
<p style="font-family:Verdana;">
Proper power distribution is a fundamental engineering principle. We made sure to calculate the voltage and current needed for each component, so no single part gets more than it can handle. This avoids overheating, unexpected resets, or damage, making the system safer and more reliable.
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
</p>
<p style="font-family:Verdana;">
The camera also allows the robot to respond to color codes. By programming specific actions for each color, the robot can follow complex instructions on the path, making it behave like an intelligent system capable of decision-making.
</p><hr><h1 style="font-family:Verdana; color:blue;">Engineering Factor</h1>
<p style="font-family:Verdana;">
We started with a ready-made kit and modified it to suit our task. For example, we added additional layers to contain all the parts and ensured balanced weight distribution, placing the battery in the middle to prevent tilting.
</p>
<p style="font-family:Verdana;">
Although we began with a pre-assembled kit, we quickly realized that no “out of the box” solution could handle the competition requirements. That’s why modification became a key part of our engineering work. Adding layers was not just about stacking parts – it was about designing a structure where every sensor and component had a logical place. This step taught us how real engineers think: adapt, customize, and redesign until the system works as intended.
</p>
<p style="font-family:Verdana;">
We also learned about weight distribution and stability. By placing heavy components like the battery in the middle, we ensured the robot would move smoothly and not tip over when turning or accelerating.
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
</p>
<p style="font-family:Verdana;">
Each hardware component serves a specific purpose. The layers of the robot are arranged to maximize performance and allow easy access to each part. Proper wiring and connections ensure the system is reliable and maintainable.
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
<p style="font-family:Verdana;">
3 × HC-SR04<br>
Voltage: 3.3 to 5V<br>
Range: 2cm to 400cm<br>
Cost: $1 each <a href="https://a.aliexpress.com/_c2yn6jqN" target="_blank">AliExpress</a>
</p>
<p style="font-family:Verdana;">
These sensors are like the ears of the robot, constantly measuring how far away obstacles are. By placing three of them at different angles, we gave the robot a wider “field of hearing.” This allows it to detect objects not only in front but also slightly to the sides, reducing blind spots.
</p><h2 style="font-family:Verdana; color:blue;">7- Motor Driver</h2>
<p style="font-family:Verdana;">
L298N motor driver<br>
Sufficient for our motors<br>
Cost: $1.50 <a href="https://a.aliexpress.com/_c2yngsHj" target="_blank">AliExpress</a>
</p><h2 style="font-family:Verdana; color:blue;">8- Gyroscope</h2>
<p style="font-family:Verdana;">
MPU-6050 gyroscope and accelerometer<br>
Small, efficient, available<br>
Cost: $2 <a href="https://a.aliexpress.com/_c3kgzexz" target="_blank">AliExpress</a>
</p><h2 style="font-family:Verdana; color:blue;">9- Camera</h2>
<p style="font-family:Verdana;">
Ultra-wide USB camera<br>
Better than Pi camera & easier to program
</p><h2 style="font-family:Verdana; color:blue;">10- Jumper Wires</h2>
<p style="font-family:Verdana;">
Male to male, male to female, female to female<br>
Strong, reusable, Raspberry Pi compatible<br>
Cost: $3 <a href="https://a.aliexpress.com/_c3kDbtrZ" target="_blank">AliExpress</a>
</p><h2 style="font-family:Verdana; color:blue;">11- On/Off Button</h2>
<p style="font-family:Verdana;">
Regular switch<br>
Inexpensive and easy to install
</p><hr><h1 style="font-family:Verdana; color:blue;">Software</h1>
<p style="font-family:Verdana;">
<b>Language:</b> Python 3 – main Raspberry Pi language, large library support and big community<br>
<b>Operating System:</b> Linux – compatible with our Raspberry Pi version, included libraries and programming tools
</p>
<p style="font-family:Verdana;">
Using Python allows integration of libraries like OpenCV for computer vision and GPIO for sensor control. This gives the robot the ability to read its environment and make intelligent decisions. Programming in Python also connected us to a global developer community for support and ideas.
</p><hr><h1 style="font-family:Verdana; color:blue;">Experience and Acquired Expertise</h1>
<p style="font-family:Verdana;">
We gained valuable skills, including:
</p>
<ul style="font-family:Verdana;">
  <li>Team spirit, cooperation, and shared decision-making</li>
  <li>Problem-solving in programming and hardware</li>
  <li>Overcoming obstacles in our first robotics project</li>
</ul>
<p style="font-family:Verdana;">
We also developed advanced technical expertise, such as:
</p>
<ul style="font-family:Verdana;">
  <li>Developing intelligent systems based on computer vision and integrating multiple sensors.</li>
  <li>Creating an integrated vehicle using open-source components.</li>
  <li>Designing with a focus on performance, modification, and reliability.</li>
</ul>
<p style="font-family:Verdana;">
These experiences taught us critical thinking, problem-solving, and how to iterate on a project when things don’t work as expected. Each obstacle became an opportunity to learn and improve.
</p><hr><h1 style="font-family:Verdana; color:blue;">Challenges & Solutions</h1>
<ul style="font-family:Verdana;">
  <li><b>Challenge:</b> Robot tilting due to battery weight.<br><b>Solution:</b> Placed battery at the center for better balance.</li>
  <li><b>Challenge:</b> Ultrasonic sensors gave noisy readings.<br><b>Solution:</b> Added averaging and calibration in software.</li>
  <li><b>Challenge:</b> Camera had trouble detecting colors under low light.<br><b>Solution:</b> Adjusted image processing parameters in OpenCV.</li>
</ul><hr><h1 style="font-family:Verdana; color:blue;">Future Improvements</h1>
<ul style="font-family:Verdana;">
  <li>Adding AI-based obstacle prediction.</li>
  <li>Using a lighter, higher-capacity battery.</li>
  <li>Improving speed and efficiency with better motors.</li>
</ul>
<p style="font-family:Verdana;">
We plan to continuously refine the robot’s capabilities, making it smarter, faster, and more adaptive to complex paths in future competitions.
</p><hr><h1 style="font-family:Verdana; color:blue;">Special Thanks</h1>
<p style="font-family:Verdana;">
Engineer <b>Wissam Nasriyah</b> for guiding us from zero to hero.<br>
Engineer <b>Mohammed Dababseh</b> and Supervisor <b>Abeer Mosa</b> for their support in several tasks.
</p>

<hr>

<h1 style="font-family:Verdana; color:blue;">Conclusion and Future Vision</h1>
<p style="font-family:Verdana;">
For us, this project was not just about building a robot — it was about proving what a group of motivated students can achieve with creativity, persistence, and teamwork. 
<br><br>
Our next steps will focus on turning our passion for robotics into solutions that can help people in everyday life. From intelligent navigation systems to practical automation, we want to expand the boundaries of what we can design and build. 
<br><br>
This is only the beginning of our journey. With every challenge, we see an opportunity to grow and innovate. 
<br><br>
<b>Nova Team – Building today, imagining tomorrow 🚀</b>
</p>
