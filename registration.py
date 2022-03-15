from tkinter import*
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
import pymysql

class Registration:
    lst = []
    def __init__(self, root):
        self.root = root
        self.root.geometry("1080x720")
        self.root.iconbitmap('AMS.ico')
        self.root.title("Registration Window")
        self.root.config(bg = "white")

        # Set background Image
        self.bg_icon = ImageTk.PhotoImage(file = "bg4.jpg")
        self.bg_image = Label(self.root, image = self.bg_icon)
        self.bg_image.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        # left side  image
        self.left_icon = ImageTk.PhotoImage(file = "left.jpg")
        self.left_image = Label(self.root, image = self.left_icon)
        self.left_image.place(x = 50, y = 100, height = 500, width = 400)

        # Set Frame
        self.frame_registration = Frame(self.root, bg = "white", bd = 2, relief = RIDGE)
        self.frame_registration.place(x = 220, y = 100, height = 500, width = 530)

        # Set title on the frame
        self.title = Label(self.frame_registration, text = "Register Here", font = "Impact 35 bold", fg = "#d77337", bg = "white")
        self.title.place(x = 70, y = 20)

        self.Admin_login = Label(self.frame_registration, text="Admin Registration Area", font=("Goudy old style", 15, "bold"), fg="#d25d17", bg="white")
        self.Admin_login.place(x=70, y=80)

        # Creat Labels
        self.first_name = Label(self.frame_registration, text = "First Name", bg = "white", font = ("Goudy old style", 12, "bold"), fg = "gray")
        self.last_name = Label(self.frame_registration, text = "Last Name", bg = "white", font = ("Goudy old style", 12, "bold"), fg = "gray")
        self.contact_no = Label(self.frame_registration, text = "Contact No.", bg = "white", font = ("Goudy old style", 12, "bold"), fg = "gray")
        self.email = Label(self.frame_registration, text = "Email", bg = "white", font = ("Goudy old style", 12, "bold"), fg = "gray")
        self.select_security_question = Label(self.frame_registration, text = "Security Quesions", bg = "white", font = ("Goudy old style", 12, "bold"), fg = "gray")
        self.security_answer = Label(self.frame_registration, text = "Security Answer", font = ("Goudy old style", 12, "bold"), fg = "gray", bg = "white")
        self.password_0 = Label(self.frame_registration, text = "Password", bg = "white", font = ("Goudy old style", 12, "bold"), fg = "gray")
        self.password_1 = Label(self.frame_registration, text = "Confirm Password", bg = "white", font = ("Goudy old style", 12, "bold"), fg = "gray")

        # Pack the Labels
        self.first_name.place(x = 60, y = 150)
        self.last_name.place(x = 310, y = 150)
        self.contact_no.place(x = 60, y = 220)
        self.email.place(x = 310, y = 220)
        self.select_security_question.place(x = 60, y = 290)
        self.security_answer.place(x = 310, y = 290)
        self.password_0.place(x = 60, y = 360)
        self.password_1.place(x = 310, y = 360)

        # Create the Entries
        self.txt_firstname = Entry(self.frame_registration, font=("times new roman", 15), bg="lightgray")
        self.txt_lastname = Entry(self.frame_registration, font=("times new roman", 15), bg="lightgray")
        self.txt_contact = Entry(self.frame_registration, font=("times new roman", 15), bg="lightgray")
        self.txt_email = Entry(self.frame_registration, font=("times new roman", 15), bg="lightgray")

        self.txt_sequrityQuestion = ttk.Combobox(self.frame_registration, font=("times new roman", 10),state = "readonly", justify= CENTER, cursor = "hand2")
        self.txt_sequrityQuestion["values"] = ("Select", "Your Best Teacher Name", "Your Birth Place", "Your Best Friend")

        self.txt_securityAnswer = Entry(self.frame_registration, font=("times new roman", 15), bg="lightgray")
        self.txt_password = Entry(self.frame_registration, font=("times new roman", 15), bg="lightgray",  show = "*")
        self.txt_confirmPassword = Entry(self.frame_registration, font=("times new roman", 15), bg="lightgray",  show = "*")

        # Pack the Entries
        self.txt_firstname.place(x=60, y=180, height=25, width=160)
        self.txt_lastname.place(x=310, y=180, height=25, width=160)
        self.txt_contact.place(x=60, y=250, height=25, width=160)
        self.txt_email.place(x=310, y=250, height=25, width=160)

        self.txt_sequrityQuestion.place(x=60, y=320, height=25, width=160)
        self.txt_sequrityQuestion.current(0)

        self.txt_securityAnswer.place(x=310, y=320, height=25, width=160)
        self.txt_password.place(x=60, y=390, height=25, width=160)
        self.txt_confirmPassword.place(x=310, y=390, height=25, width=160)

        # CheckBox for TERMS AND CONDITIONS
        self.checkbox_var = IntVar()
        self.check = Checkbutton(self.frame_registration, text = "I agree the terms and conditions", bg = "white", font=("times new roman", 12), cursor = "hand2", variable = self.checkbox_var)
        self.check.place(x = 60, y = 430)

        # Button for registration
        self.btn = Button(self.root, text = "Register Now", fg = "white", bg = "#d77337", font = ("times new roman", 20), cursor = "hand2", command = self.register_function, bd = 2, relief = RIDGE)
        self.btn.place(x = 380, y = 580, width = 200, height = 40)

        # Button for sign in
        self.btn_signin = Button(self.root, text = "Sign In", fg = "black", bg = "white", font = ("times new roman", 20), cursor = "hand2", bd = 2, relief = RIDGE, command = self.sign_in)
        self.btn_signin.place(x = 60, y = 550, width = 150, height = 40)

    #     validation
    def register_function(self):
        if self.txt_firstname.get() == "" or self.txt_lastname.get() == "" or self.txt_contact.get() == "" or self.txt_email.get() == "" or self.txt_password.get() == "" or self.txt_confirmPassword.get() == "":
            messagebox.showerror("Error", "All fields are required", parent = self.root)
        elif self.txt_password.get() != self.txt_confirmPassword.get():
            messagebox.showerror("Error", "Passwords are different", parent = self.root)
        else:
            messagebox.showinfo("Welcome", f"Thanks for Registration {self.txt_firstname.get()} {self.txt_lastname.get()}")
            f = open("Data.txt", "w")
            f.write(f"{self.txt_firstname.get()}\t{self.txt_lastname.get()}\t{self.txt_contact.get()}\t{self.txt_email.get()}\t{self.txt_sequrityQuestion.get()}\t{self.txt_securityAnswer.get()}\t{self.txt_password.get()}\t{self.checkbox_var.get()}")
            f.close()

        # First_Name = self.txt_firstname.get()
        # Last_Name = self.txt_lastname.get()
        # Contact = self.txt_contact.get()
        # Email = self.txt_email.get()
        # Sequrity_Q = self.txt_sequrityQuestion.get()
        # Sequrity_A = self.txt_securityAnswer.get()
        # Password = self.txt_password.get()
        # Confirm_Pass = self.txt_confirmPassword.get()
        # Agreed = self.checkbox_var.get()
        # try:
        #     global cursor
        #     connection = pymysql.connect(host='localhost', user='ali', password='123', db='Registration')
        #     cursor = connection.cursor()
        # except Exception as e:
        #     messagebox.showerror('', e) 
        # DB_Table_Name = str(self.txt_email.get())
        # sql = "CREATE TABLE " + DB_Table_Name + """
        #                 (FIRST_NAME VARCHAR(20) NOT NULL,
        #                  LAST_NAME VARCHAR(20) NOT NULL,
        #                  CONTACT VARCHAR(20) NOT NULL,
        #                  EMAIL VARCHAR(20) NOT NULL,
        #                  SQ VARCHAR(20) NOT NULL,
        #                  SA VARCHAR(20) NOT NULL,
        #                  PASSWORD VARCHAR(20) NOT NULL,
        #                  CPASS VARCHAR(20) NOT NULL,
        #                  AGREE CHAR(1),
        #                     );
        #                 """
        # try:
        #     cursor.execute(sql)  ##for create a table
        # except Exception as e:
        #     messagebox.showerror('', e)  #

        # check_counter=0
        # warn = ""
        # if self.txt_firstname.get() == "":
        #     warn = "First Name can't be empty"
        # else:
        #     check_counter += 1
        # check_counter=0 
        
        # if self.txt_lastname.get() == "":
        #     warn = "Last Name can't be empty"
        # else:
        #     check_counter += 1
        
        # if self.txt_contact.get() == "":
        #     warn = "Contact can't be empty"
        # else:
        #     check_counter += 1
        
        # if self.txt_email.get() == "":
        #     warn = "Email can't be empty"
        # else:
        #     check_counter += 1
        # if self.txt_sequrityQuestion.get() == 'Select':
        #     warn = "Please Select Security Question"
        # else:
        #     check_counter += 1
        
        # if self.txt_securityAnswer.get() == "":
        #     warn = "Sequrity Answer can't be empty"
        # else:
        #     check_counter += 1

        # if self.txt_password.get() == "":
        #     warn = "Password can't be empty"
        # else:
        #     check_counter += 1
        
        # if self.txt_confirmPassword.get() == "":
        #     warn = "Confirm Password can't be empty"
        # else:
        #     check_counter += 1
        
        # if self.txt_password.get() != self.txt_confirmPassword.get():
        #     warn = "Passwords didn't match!"
        # else:
        #     check_counter += 1
        
        # if self.checkbox_var.get() != 1:
        #     warn = 'Agree checkbox not checked'
        # else:
        #     check_counter  += 1
        
        # print("heloooooooooooooo        ",check_counter)
        # if check_counter == 9:
        #     try:
        #         Insert_data = "INSERT INTO " + DB_Table_Name
        #         VALUES = (str(First_Name), str(Last_Name), str(Contact), str(Email), str(Sequrity_Q), str(Sequrity_A), str(Password), str(Confirm_Pass), Agreed)
        #         cursor.execute(Insert_data, VALUES)
        #         messagebox.showinfo('Info', 'Successfully Registered')
        #         cursor.close()
        #     except Exception as e:
        #         messagebox.showerror('Error', e)
        # else:
        #     messagebox.showerror('Error', warn)
        
    # function for callback signin/login page
    def sign_in(self):
        self.root.destroy()
        import setup
        import os
        os.system("py setup.py")



root = Tk()
obj = Registration(root)
root.mainloop()