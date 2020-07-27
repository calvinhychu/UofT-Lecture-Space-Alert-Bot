from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.firefox.options import Options
import smtplib
import time


class Acorn:
    """Initialized a search section with Acorn login information,
    course and email

    """

    def __init__(self, utorid, password, email, email_pwd, contact):
        """
        Initialize a Acorn login session bot using Firefox with Acorn utorid,
        Acorn password, email address, email password using Firefox
        """
        self.utorid = utorid
        self.password = password
        self.email = email
        self.email_pwd = email_pwd
        self.contact = contact
        options = Options()
        options.add_argument('--headless')
        self.bot = webdriver.Firefox(options=options)

    def login(self):
        login_session = self.bot
        login_session.get('https://acorn.utoronto.ca/')
        time.sleep(4)
        username = login_session.find_element_by_id('username')
        password = login_session.find_element_by_id('password')
        username.clear()
        password.clear()
        username.send_keys(self.utorid)
        password.send_keys(self.password)
        password.send_keys('\ue006')
        time.sleep(8)
        login_session.get('https://acorn.utoronto.ca/sws/#/courses/0')

    def find_course(self, co, term, lecture):
        time.sleep(3)
        login_session = self.bot
        course_code = co.upper() + ' ' + term.upper()
        course = login_session.find_element_by_id('typeaheadInput')
        course.clear()
        course.send_keys(co.upper())
        time.sleep(2)
        course.click()
        login_session.find_element_by_xpath(
            "//*/span[contains(text(),'" + course_code + "')]").click()
        time.sleep(5)
        a = 0
        for lec in lecture:
            lecture_code = lec[0:3].upper() + '-' + lec[3:].upper()
            number_of_space = login_session.find_element_by_id(
                lecture_code).find_element_by_css_selector(
                "span[data-ng-bind-html='getSpaceAvailabilityMessage(currentCourse, info, modalCourse.isPlannedItem)']")
            try:
                c = number_of_space.text
                n = int(c[0])
                if n != 0:
                    print('ava')
                    self.send_email(co, term, lec, c)
                    a = 1
            except ValueError:
                print("FULL")
            except IndexError:
                print(
                    "Unable to check availability due to glitch on webscrapping "
                    "on Acorn, will try again.")
        time.sleep(2)
        if a == 1:
            login_session.close()
            return True
        login_session.find_element_by_class_name("close.icon-cancel").click()
        time.sleep(4)
        self.find_course(co, term, lecture)

    def send_email(self, co, term, lecture, number_of_space):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.email, self.email_pwd)
        subject = f"Space is now available for session {lecture.upper()} in " \
                  f"{co.upper()}{term.upper()}! Enroll NOW!"
        body = f"There is {number_of_space} space for session {lecture} in " \
               f"{co}{term}! Enroll now on Acorn to secure your spot!\n" \
               f"Automated Course Search bot will " \
               f"now be disabled."
        msg = f'Subject: {subject}\n\n{body}'
        server.sendmail(self.email, self.contact, msg)
        print('sent!')
        server.quit()
