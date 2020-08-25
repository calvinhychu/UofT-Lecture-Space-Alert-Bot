<html>
<h1>University of Toronto course enrollment alert</h1>
<body>An automated bot to check if any open space is available for courses in University of Toronto using the ACORN system. Designed for checking course availability after waitlist is dropped.
<ul>
  <li>Able to continually checking courses without user involvement</li>
  <li>Work in background</li>
  <li>Able to check for multiple lecture sections for course</li>
  <li>Email alert is sent to a chosen email address if an open space for a lecture section is found to alert user to enroll</li>
  <li>Works for both UTSG and UTM</li>
  <li>Intuitive GUI available</li>
  <!-- Add picture and gif -->
</ul>
</body>
<section>
<h2>Prerequisites</h2>
<body>
	<ul>
		<li>Firefox installed</li>
		<li>Have a Gmail account ready, this will be the account that sends the email alert</li>
		<li>Enable SMTP mail with the Gmail account by following this <a href="https://www.youtube.com/watch?v=D-NYmDWiFjU">link</a></li>
	</ul>
</body>
<h2>Usage</h2>
<body>
<ol>
  <li>Close Firefox browser</li>
  <li>Enter your UTORid in the entry field next to UTORid:</li>
  <li>Enter your UToronto account password in the entry field next to Password:</li>
  <li>Enter course code you intend to search for in the entry field next to Course:. e.g. CSC148H1 or MAT137Y1</li>
  <li>Choose your section code</li>
  <li>Enter lecture section code you intend to search for in the entry field next to Lecture: e.g. LEC0101.</li>
  If intended to search for more than 1 lecture section separate each lecture code by 1 space e.g. LEC0101 LEC5101
  <li>Enter your Gmail account address in the entry field next to Email: ,this is the email account that will send out the alert email</li>
  <li>Enter email account password in the entry field next to Email pwd: </li>
  <li>Enter the email address you want the alert email to be send in the entry field next to Send To:</li>
  <b>NOTE:</b> This program will continuously run until it finds an open slot for given lecture sections or user closes the program.
</ol>
</body>
<h2>How it works?</h2>
<ul>
	<li>Utilizing selenium module in Python to initialize bot and scrap data from ACORN</li> 
	<li>Used Tkiner module for simple GUI</li>
	<li>SMTP module to send alert email</li>
</ul>
<h2>Contributing</h2>
This is a program designed for students, by students. Hence, all source code is available and any contribution is welcome. Please check or raise issues in the issue tab.
<h3>Clone</h3>
```
git clone https://github.com/calvinhychu/UofT-Lecture-Space-Alert-Bot.git
```
<h2>Disclaimer</h2>
</html>