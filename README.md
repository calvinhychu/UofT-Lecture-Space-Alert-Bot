# UofT-Lecture-Space-Alert-Bot

An automated bot to check if any open space is available for courses in University of Toronto using the ACORN system. Designed for checking course availability after waitlist is dropped.

- Able to continually checking courses without user involvement
- Work in background
- Able to check for multiple lecture sections for course
- Email alert is sent to a chosen email address if an open space for a lecture section is found to alert user to enroll
- Works for both UTSG and UTM
- Intuitive GUI available as an executable file generated via Pyinstaller 

## Demo 
<b>NOTE:</b> UofT-Lecture-Space-Alert-Bot will run in headless mode so user won't see a popup Firefox browser but instead the program will run in background. The demo below where there is a Firefox browser popup after submiting infomation in GUI is only to demonstrate how this program works.

### Entering info to GUI:
<img src="./misc/demo1.gif" width = 350 height = 300/>

### Bot starting after submitted info:
<img src="./misc/demo2.gif">

## Getting Started

### Prerequisites
- Firefox installed. Click [here](https://www.mozilla.org/en-US/firefox/new/) for official Firefox download link.
- Have a Gmail account ready, this will be the account that sends the email alert. Click [here](https://accounts.google.com/signup?hl=en) to sign-up for a Gmail account.
- Enable SMTP mail with the Gmail account by following this [link](https://www.youtube.com/watch?v=D-NYmDWiFjU).
- Download appropriate version of mozilla/geckodriver based on your OS [here](https://github.com/mozilla/geckodriver/releases)

### Clone this project

```bash
  git clone https://github.com/calvinhychu/UofT-Lecture-Space-Alert-Bot/
```
### Contributing
This is a program designed for students, by students. Hence, all source code is available and any contribution is welcome. Please check or raise issues in the issue tab.

## Usage
1. Clone this project or just download UofT-Lecture-Space-Alert-Bot.exe
2. Place geckodriver.exe you downloaded at the same directory as UofT-Lecture-Space-Alert-Bot.exe
3. Close Firefox browser
4. Open UofT-Lecture-Space-Alert-Bot.exe or run gui.py
5. Enter your UTORid in the entry field next to UTORid:
6. Enter your UToronto account password in the entry field next to Password:
7. Enter course code you intend to search for in the entry field next to Course:. e.g. CSC148H1 or MAT137Y1
8. Choose your section code by clicking one of the radio button F, S or Y
9. Enter lecture section code you intend to search for in the entry field next to Lecture: e.g. LEC0101.
10. If intended to search for more than 1 lecture section separate each lecture code by 1 space e.g. LEC0101 LEC5101
11. Enter your Gmail account address in the entry field next to Email: ,this is the email account that will send out the alert email
12. Enter email account password in the entry field next to Email pwd: 
13. Enter the email address you want the alert email to be send in the entry field next to Send To:
- <b>NOTE:</b> This program will continuously run until it finds an open space for given lecture sections or user closes the program.)

## How it works?
- Utilizing selenium module in Python to initialize bot and scrap data from ACORN
- Used Tkinter module for simple GUI
- Used SMTP module to send alert email

## Privacy
No privacy information like ACORN username and password or email password is collected or retained by UofT-Lecture-Space-Alert-Bot

## Disclaimer
UofT-Lecture-Space-Alert-Bot is not affiliated with University of Toronto or its ACORN system, it is only intended to be used for non-profit purposes.
None of the authors, contributors, administrators, vandals, or anyone else connected with UofT-Lecture-Space-Alert-Bot, in any way whatsoever, can be responsible for your use of this program. Any action action you take upon using this program is strictly at your own risk.