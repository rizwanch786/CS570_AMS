from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
import os
from tkinter import ttk
root = Tk()
#from AMS_Run import window
class Login:
    def __init__(self, root):
        self.root = root
        self.root.iconbitmap('AMS.ico')
        self.root.title("Login Window")
        self.root.geometry("1080x720")
        # self.root.resizable(False,False)
#        Background Image
        self.bg_icon =ImageTk.PhotoImage(file = "bg.jpg")
        bg_image = Label(self.root,image = self.bg_icon).place(x = 0, y = 0, relwidth = 1, relheight = 1)
# or
#         self.bg_image = Label(self.root,image = self.bg).pack()

#         login_frame
        frame_login = Frame(self.root, bg="white", bd = 2, relief = RIDGE)
        frame_login.place(x = 80, y = 150, height = 500, width = 500)
        title = Label(frame_login, text = "Login Here", font = "Impact 35 bold", fg = "#d77337", bg = "white").place(x = 80, y = 20)
        Admin_login = Label(frame_login, text = "Admin Login Area", font = ("Goudy old style", 15, "bold"), fg = "#d25d17", bg = "white").place(x = 80, y = 80)
        user_name = Label(frame_login, text = "Username/Email", font = ("Goudy old style", 12, "bold"), fg = "gray", bg = "white").place(x = 80, y = 120)
        self.txt_username = Entry(frame_login, font = ("times new roman", 15), bg = "lightgray")
        self.txt_username.place(x = 80, y = 150, height = 35, width = 350)

        pass_word = Label(frame_login, text = "Password", font = ("Goudy old style", 12, "bold"), fg = "gray", bg = "white").place(x = 80, y = 200)
        self.txt_password = Entry(frame_login, font = ("times new roman", 15), bg = "lightgray", show = "*")
        self.txt_password.place(x = 80, y = 230, height = 35, width = 350)

        forget = Button(frame_login, text = "Forget Password?", bg = "white", fg = "#d77337",bd = 0, font = ("times new roman", 12), cursor = "hand2", command = self.forget_password_callback)
        forget.place(x = 80, y = 280)

        # Create login Button
        login_button = Button(self.root, text = "Login", command = self.login_function, fg = "white", bg = "#d77337", font = ("times new roman", 20), cursor = "hand2", bd = 2, relief = RIDGE)
        login_button.place(x = 250, y = 470, width = 200, height = 40)


        # Label
        not_have_account = Label(frame_login, text = "Don't have account?", bg = "white", fg = "gray", font = ("times new roman", 12))
        not_have_account.place(x = 80, y = 370)

        create_account_button = Button(frame_login, text = "Create one", bg = "white", fg = "#d77337",bd = 0, font = ("times new roman", 12, "underline"), cursor = "hand2", command = self.sign_up)
        create_account_button.place(x = 80, y = 400)

    def login_function(self):
        if self.txt_password.get() == "" or self.txt_username.get() == "":
            messagebox.showerror("Error", "All fields are required", parent = self.root)
        elif self.txt_username.get() != "ali" or self.txt_password.get() != "123":
            messagebox.showerror("Error", "Invalid username/password", parent = self.root)
        else:
            #messagebox.showinfo("Welcome", f"Welcome {self.txt_username.get()}\nYour Password: {self.txt_password.get()}")
            root.destroy()
            os.system("py AMS_Run.py")


    def sign_up(self):
        self.root.destroy()
        #import registration
        os.system("py registration.py")

    def forget_password_callback(self):
        self.root.destroy()
        #import forget_password
        os.system("py forget_password.py")
        

    



# ------------------------------------------------------------------------------------------------------------------------------
obj = Login(root)
root.mainloop()