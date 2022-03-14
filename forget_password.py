from tkinter import *
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox

class Forget:
    def __init__(self, root):
        self.root2 = root
        self.root2.iconbitmap('AMS.ico')
        self.root2.geometry("450x500+500+200")
        self.root2.config(bg = "white")
        self.root2.title("Forget Password Window")
        self.root2.resizable(False, False)
        # create Title labels
        self.fg_title = Label(self.root2, text="Forget Password", font="Impact 35 bold", fg="#d77337", bg="white")
        self.fg_title.place(x=30, y=20)

        # create other labels
        self.fg_user = Label(self.root2, text="Username", bg="white", font=("Goudy old style", 15, "bold"), fg="gray")
        self.fg_question = Label(self.root2, text="Security Quesions", bg="white", font=("Goudy old style", 15, "bold"), fg="gray")
        self.fg_answer = Label(self.root2, text="Security Answer", font=("Goudy old style", 15, "bold"), fg="gray", bg="white")
        self.fg_password = Label(self.root2, text="New Password", bg="white", font=("Goudy old style", 15, "bold"), fg="gray")

        # pack the labels
        self.fg_user.place(x=50, y=100)
        self.fg_question.place(x=50, y=170)
        self.fg_answer.place(x=50, y=240)
        self.fg_password.place(x=50, y=310)

        # Create  the entries
        # 01 username
        self.fp_username = Entry(self.root2, font=("times new roman", 15), bg="lightgray")
        # 02 security questions
        self.fp_sequrityQuestion = ttk.Combobox(self.root2, font=("times new roman", 10), state="readonly", justify=CENTER, cursor="hand2")
        self.fp_sequrityQuestion["values"] = ("Select", "Your Best Teacher Name", "Your Birth Place", "Your Best Friend")
        # 03 security answers
        self.fp_securityAnswer = Entry(self.root2, font=("times new roman", 15), bg="lightgray")
        # New password
        self.fp_newpassword = Entry(self.root2, font=("times new roman", 15), bg="lightgray")

        # pack the entries
        self.fp_username.place(x=50, y=130, height = 35, width = 350)

        self.fp_sequrityQuestion.place(x=50, y=200, height = 35, width = 350)
        self.fp_sequrityQuestion.current(0)

        self.fp_securityAnswer.place(x=50, y=270, height = 35, width = 350)
        self.fp_newpassword.place(x=50, y=340, height = 35, width = 350)

        # button
        self.fg_btn = Button(self.root2, text = "Reset Password", fg = "white", bg = "#d77337", font = ("times new roman", 20), cursor = "hand2", bd = 2, relief = RIDGE, command = self.forget_validation)
        self.fg_btn.place(x = 100, y = 400, width = 200, height = 40)
        # callback the signin splash
        sign_in_button = Button(self.root2, text = "Sign In", bg = "white", fg = "#d77337",bd = 0, font = ("times new roman", 20, "underline"), cursor = "hand2", command = self.sign_in_callback)
        sign_in_button.place(x = 100, y = 450, width = 200, height = 40)
        # callback main/home page mean signin page
    def sign_in_callback(self):
        self.root2.destroy()
        #import login
        import os
        os.system("py setup.py")


        # Validations here
    def forget_validation(self):
        if self.fp_username.get() == "":
            messagebox.showerror("Error", "Please Enter the valid username/email to reset your password", parent = root)
        # elif self.fp_username != "":
        #     f = open ("Data.txt", "r")
        #     lines = f.readline()
        #     if self.fp_username.get() in lines:
        #         pass
        #     else:
        #         messagebox.showerror("Error", "Username is invalid")

root = Tk()
obj = Forget(root)
root.mainloop()