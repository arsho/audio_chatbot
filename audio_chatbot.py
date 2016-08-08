from tkinter import *
import os, html
import pyaudio
import speech_recognition as sr
import tkinter.scrolledtext
class App():
    def __init__(self):
        self.doss = os.getcwd()
        self.com_sign = "Bot >> "
        self.user_sign = "You >> "
        self.r = sr.Recognizer()
        
        self.window = Tk()
        self.window.title("ChatBot / arsho")
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        window_height = 600
        window_width = 600
        x_pos = (screen_width - window_width) // 2 
        y_pos = (screen_height - window_height) // 2
        geometry_str = str(window_width)+"x"+\
                       str(window_height)+"+"+str(x_pos)+"+"+\
                       str(y_pos)
        self.window.geometry(geometry_str)

        self.start_btn_str = "Talk with me"
        self.start_btn = Button(self.window,text=self.start_btn_str,\
                                command=self.start_btn_click)
        self.start_btn.pack(padx=10, pady=10,fill=BOTH)

        self.chat = tkinter.scrolledtext.ScrolledText(self.window)
        self.chat.pack(padx=10, pady=10, fill=BOTH, expand=True)
        self.chat.insert(INSERT,"Welcome to chat. ")
        self.window.mainloop()

    def start_btn_click(self):
        print("Btn clicked.")
        self.chat.insert(INSERT,"\n")
        self.chat.insert(INSERT,self.com_sign+"Say something\n")
        
        with sr.Microphone() as source:
            audio = self.r.adjust_for_ambient_noise(source)            
            audio = self.r.listen(source)
                                                      
        try:
            s = (self.r.recognize_google(audio))
            message = (s.lower())        
            self.chat.insert(INSERT,self.user_sign+message+"\n")
            if message == "exit":
                self.chat.insert(INSERT,self.com_sign+"Bye bye\n")
            elif message == "how are you":
                self.chat.insert(INSERT,self.com_sign+"I am fine. What about you?\n")
            elif message == "you are good":
                self.chat.insert(INSERT,self.com_sign+"Thanks for your compliment.\n")
            elif message == "goodbye":
                self.chat.insert(INSERT,self.com_sign+"See you soon.\n")
            else:
                self.chat.insert(INSERT,self.com_sign+"I am listening, ain't I?\n")
                    
        except sr.UnknownValueError:
            self.chat.insert(INSERT,self.com_sign+"could not understand audio\n")
        except sr.RequestError as e:
            self.chat.insert(INSERT,self.com_sign+"Could not request results$; {0}".format(e))
        
app = App()
