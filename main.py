from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.firefox.options import Options
import smtplib
import time


class Acorn:
    """A bot that starts a search section with Acorn login information,
    course info and email

    === Private Attributes ===
    _utorid:
        Student utorid for login to ACORN
    _ut_password:
        Password for login to ACORN
    _email:
        The email address that will send an alert if a space is available
        in the chosen course, currently only supports a valid Gmail address
    _email_pwd:
        The password for the email address that will send an alert if a space
        is available in the chosen course
    _contact:
        The email address that will receive the alert if a space is available
        in the chosen course
    """

    def __init__(self, utorid: str, password: str, email: str, email_pwd: str,
                 contact: str) -> None:
        """
        Initialize a Acorn login session bot using Firefox with Acorn utorid,
        Acorn password, email address, email password using Firefox
        """
        self._utorid = utorid
        self._ut_password = password
        self._email = email
        self._email_pwd = email_pwd
        self._contact = contact
        options = Options()
        options.add_argument('--headless')
        self.bot = webdriver.Firefox(options=options)

    def login(self) -> None:
        """
        Automated a bot to login to ACORN and access the course enrollment page
        """
        login_session = self.bot
        login_session.get('https://acorn.utoronto.ca/')
        time.sleep(4)
        # Enter utorid and password to ACORN
        username = login_session.find_element_by_id('username')
        password = login_session.find_element_by_id('password')
        username.clear()
        password.clear()
        username.send_keys(self._utorid)
        password.send_keys(self._ut_password)
        password.send_keys('\ue006')
        time.sleep(8)
        # Go to course enrollment page in ACORN after logging in
        login_session.get('https://acorn.utoronto.ca/sws/#/courses/0')

    def find_course(self, co: str, term: str, lecture: List[str]) -> \
            Optional[bool]:
        """
        Automated a bot and search if there is available space for lecture
        sections in lecture. Returns True if at least one of the lecture section
        has an available space
        """
        time.sleep(3)
        login_session = self.bot
        # Formulate official course code using co and term
        course_code = co.upper() + ' ' + term.upper()
        # Find where to input course code in course enrollment page
        course = login_session.find_element_by_id('typeaheadInput')
        course.clear()
        course.send_keys(co.upper())
        time.sleep(2)
        course.click()
        # Bot to find and click on the correct on the right course under the
        # javascript course search bar
        login_session.find_element_by_xpath(
            "//*/span[contains(text(),'" + course_code + "')]").click()
        time.sleep(5)
        # Initialized variable "available" to keep track if space is available
        # in any of the chosen lecture sections
        available = False
        # Loop through each lecture section in lecture and determine if free
        # space is available
        for lec in lecture:
            lecture_code = lec[0:3].upper() + '-' + lec[3:].upper()
            # number_of_space is the variable that shows how many space is
            # available at that lecture section currently
            number_of_space = login_session.find_element_by_id(
                lecture_code).find_element_by_css_selector(
                "span[data-ng-bind-html='getSpaceAvailabilityMessage"
                "(currentCourse, info, modalCourse.isPlannedItem)']")
            try:
                # c is a string that displays information regarding space
                c = number_of_space.text
                # n is the first character of the text, if and only if it is an
                # integer that is not 0, it means at least a space is available
                # and will run self.send_email to send an email alert
                n = int(c[0])
                if n != 0:
                    print('ava')
                    self.send_email(co, term, lec, c)
                    # available to set to True and will return True as a space
                    # is available
                    available = True
            # If n is unable to changed from str to int then it is another
            # indication that the lecture section is currently full.
            except ValueError:
                print("FULL")
            # Occasionally a known bug will occur where number_of_space.text
            # is an empty str and therefore IndexError will happen when trying
            # to access index 0 of c.
            except IndexError:
                print(
                    "Unable to check availability due to glitch on webscrapping "
                    "on Acorn, will try again.")
        time.sleep(2)
        # If available is True, whole Firefox browser will close and return True
        if available:
            login_session.close()
            return True
        # If no space is found then bot will close the popup specified course
        # enrollment page and stay IDLE at the general course enrollment ACORN
        # page
        login_session.find_element_by_class_name("close.icon-cancel").click()
        time.sleep(4)

    def send_email(self, co: str, term: str, lecture: str,
                   number_of_space: str) -> None:
        """
        Send an email from self._email to self._contact that alerts that how
        many available space for the lecture section
        """
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self._email, self._email_pwd)
        subject = f"Space is now available for session {lecture.upper()} in " \
                  f"{co.upper()}{term.upper()}! Enroll NOW!"
        body = f"There is {number_of_space} space for session {lecture} in " \
               f"{co}{term}! Enroll now on Acorn to secure your spot!\n" \
               f"Automated Course Search bot will " \
               f"now be disabled."
        msg = f'Subject: {subject}\n\n{body}'
        server.sendmail(self._email, self._contact, msg)
        print('sent!')
        server.quit()
