from main import *
from tkinter import *
import webbrowser
import threading


def open_github_site() -> None:
    """
    Open up Github website for this project for instruction
    """
    webbrowser.open_new('https://github.com/calvinhychu/UofT-Lecture-Space-'
                        'Alert-Bot#university-of-toronto-course-enrollment-'
                        'alert')


class BotGUI:
    """
    A GUI that let user input and submit information to run main.py or automated
    bot

    === Private Attributes ===
    _utorid:
        Student utorid for login to ACORN
    _ut_password:
        Password for login to ACORN
    _course:
        Course code for U of T. e.g. CSC148H1
    _lecture_code:
        A list of lecture section for _course. e.g. LEC0101
    _session_code:
        Sectional code to represent Fall, Winter or Summer section for _course
    _email:
        The email address that will send an alert if a space is available
        in the chosen course, currently only supports a valid Gmail address
    _email_password:
        The password for the email address that will send an alert if a space
        is available in the chosen course
    _contact:
        The email address that will receive the alert if a space is available
        in the chosen course
    """
    def __init__(self, win) -> None:
        """
        Initialize the GUI with labels, entries, submit button and functions
        corresponds to each entry.
        """
        # Initializing all labels shown in GUI
        self.l1 = Label(win, text='UTORid:')
        self.l2 = Label(win, text='Password:')
        self.l3 = Label(win, text='Course:')
        self.l4 = Label(win, text='e.g. CSC148H1 or MAT137Y1')
        self.l5 = Label(win, text='Section:')
        self.l6 = Label(win, text='Lecture:')
        self.l7 = Label(win, text='e.g. LEC0101')
        self.l8 = Label(win, text='Email:')
        self.l9 = Label(win, text='Email pwd:')
        self.l10 = Label(win, text='Send To:')
        self.l11 = Label(win, text='Currently only supports Gmail')
        self.l12 = Label(win, text='e.g. test@mail.utoronto.ca')
        self.l13 = Label(win,
                         text='Welcome! This is an automated bot for checking '
                              'availability of\n lecture sections for '
                              'courses at UofT. Please '
                              'click here for instruction.',
                         cursor="hand2")
        # Binding l13 to left click where clicking it would open GitHub site
        # for this project for instruction
        self.l13.bind("<Button-1>", lambda e: open_github_site())
        # Initialize every entry box for user to input information
        self._utorid = Entry()
        self._ut_password = Entry(show="*")
        self._course = Entry()
        self._lecture_code = Entry()
        self._email = Entry()
        self._email_password = Entry(show="*")
        self._contact = Entry()
        # Create radio button to choose sectional code for chosen course
        v1 = StringVar()
        r1 = Radiobutton(bot, text="F", variable=v1, value='F')
        r2 = Radiobutton(bot, text="S", variable=v1, value='S')
        r3 = Radiobutton(bot, text="Y", variable=v1, value='Y')
        self._session_code = v1.get()
        # Placing each label, radio button and entry box to its respective
        # spot in GUI
        self.l1.place(x=20, y=50)
        self._utorid.place(x=80, y=50)
        self.l2.place(x=20, y=80)
        self._ut_password.place(x=80, y=80)
        self.l3.place(x=20, y=110)
        self._course.place(x=80, y=110)
        self.l4.place(x=210, y=110)
        self.l5.place(x=20, y=140)
        r1.place(x=75, y=140)
        r2.place(x=115, y=140)
        r3.place(x=155, y=140)
        self.l6.place(x=20, y=170)
        self._lecture_code.place(x=80, y=170)
        self.l7.place(x=210, y=170)
        self.l8.place(x=20, y=200)
        self._email.place(x=80, y=200)
        self.l9.place(x=20, y=230)
        self.l10.place(x=20, y=260)
        self.l11.place(x=210, y=200)
        self.l12.place(x=210, y=260)
        self.l13.place(x=30, y=8)
        self._email_password.place(x=80, y=230)
        self._contact.place(x=80, y=260)
        # Create a button to submit all information entered in entry box
        # and run self._start_bot()
        self.b1 = Button(win, text='Start Bot', command = lambda:threading.Thread(target = self._start_bot()).start())
        self.b1.place(x=200, y=300)
        # Displaying current status text as a label
        self.status_text = StringVar()
        self.status_text.set('Current Status: IDLE')
        self.l14 = Label(win, textvariable=self.status_text)
        self.l14.place(x=20, y=320)

    def _start_bot(self) -> None:
        """
        Initialized an Acorn using information from input from GUI. Acorn will
        then login and run Acorn.find_course to continually search for available
        space for course info from input from GUI until an available space is
        found and an email alert will be sent.
        """
        self.status_text.set('Current Status: Running...')
        section = Acorn(self._utorid.get(), self._ut_password.get(),
                            self._email.get(),
                            self._email_password.get(), self._contact.get())
        section.login()
        while True:
            if section.find_course(self._course.get(), self._session_code,
                                   self._lecture_code.get().split()):
                print("FINISHED!")
                break
        self.status_text.set('Current Status: DONE! Email sent!')


bot = Tk()
mywin = BotGUI(bot)
bot.title('UofT Lecture Space Alert Bot')
bot.geometry("450x350")
bot.mainloop()
