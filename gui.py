from main import *
from tkinter import *
import webbrowser
import threading


def open_github_site():
    webbrowser.open_new('https://github.com/calvinhychu/UofT-Lecture-Space-'
                        'Alert-Bot#university-of-toronto-course-enrollment-'
                        'alert')


class BotGUI:
    def __init__(self, win):
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
        self.l13.bind("<Button-1>", lambda e: open_github_site())
        self.utorid = Entry()
        self.ut_password = Entry(show="*")
        self.course = Entry()
        self.lecture_code = Entry()
        self.email = Entry()
        self.email_password = Entry(show="*")
        self.contact = Entry()
        v1 = StringVar()
        r1 = Radiobutton(bot, text="F", variable=v1, value='F')
        r2 = Radiobutton(bot, text="S", variable=v1, value='S')
        r3 = Radiobutton(bot, text="Y", variable=v1, value='Y')
        self.session_code = v1.get()
        self.l1.place(x=20, y=50)
        self.utorid.place(x=80, y=50)
        self.l2.place(x=20, y=80)
        self.ut_password.place(x=80, y=80)
        self.l3.place(x=20, y=110)
        self.course.place(x=80, y=110)
        self.l4.place(x=210, y=110)
        self.l5.place(x=20, y=140)
        r1.place(x=75, y=140)
        r2.place(x=115, y=140)
        r3.place(x=155, y=140)
        self.l6.place(x=20, y=170)
        self.lecture_code.place(x=80, y=170)
        self.l7.place(x=210, y=170)
        self.l8.place(x=20, y=200)
        self.email.place(x=80, y=200)
        self.l9.place(x=20, y=230)
        self.l10.place(x=20, y=260)
        self.l11.place(x=210, y=200)
        self.l12.place(x=210, y=260)
        self.l13.place(x=30, y=8)
        self.email_password.place(x=80, y=230)
        self.contact.place(x=80, y=260)
        self.b1 = Button(win, text='Start Bot', command = lambda:threading.Thread(target = self.start_bot()).start())
        self.b1.place(x=200, y=300)
        self.status_text = StringVar()
        self.status_text.set('Current Status: IDLE')
        self.l14 = Label(win, textvariable=self.status_text)
        self.l14.place(x=20, y=320)

    def start_bot(self):
        self.status_text.set('Current Status: Running...')
        section = Acorn(self.utorid.get(), self.ut_password.get(),
                            self.email.get(),
                            self.email_password.get(), self.contact.get())
        section.login()
        while True:
            if section.find_course(self.course.get(), self.session_code,
                                   self.lecture_code.get().split()):
                print("FINISHED!")
                break
        self.status_text.set('Current Status: DONE! Email sent!')


bot = Tk()
mywin = BotGUI(bot)
bot.title('UofT Lecture Space Alert Bot')
bot.geometry("450x350")
bot.mainloop()
