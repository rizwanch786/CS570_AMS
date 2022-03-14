import tkinter as tk
from tkinter import *
import cv2
import csv
import os
import numpy as np
from PIL import Image,ImageTk
import pyttsx3
#import PIL
#from PIL import ImageTk
# from PIL import Image
import pandas as pd
import datetime
import time

#####Window is our Main frame of system
window = tk.Tk()
window.title("Face Recognition Based Attendance System")

window.geometry('1080x720')
window.configure(background='snow')
# Background image
bg_icon = ImageTk.PhotoImage(file = "bg.jpg")
bg_image = Label(window, image = bg_icon).place(x = 0, y = 0, relheight  = 1, relwidth = 1)


####GUI for manually fill attendance

def manually_fill():
    global sb
    sb = tk.Tk()
    sb.iconbitmap('AMS.ico')
    sb.title("Enter subject name...")
    sb.geometry('450x320')
    sb.resizable(False, False)
    sb.configure(bg = "white")

    def err_screen_for_subject():
        def ec_delete():
            ec.destroy()
        global ec
        ec = tk.Tk()
        ec.geometry('300x100')
        ec.iconbitmap('AMS.ico')
        ec.title('Warning!!')
        ec.configure(background='snow')
        Label(ec, text='Please enter your subject name!!!', fg='black', bg='white', font=('times', 16, ' bold ')).pack()
        Button(ec, text='OK', command=ec_delete, fg="black", bg="lawn green", width=9, height=1, activebackground="Red",
               font=('times', 15, ' bold ')).place(x=90, y=50)

    def fill_attendance():
        ts = time.time()
        Date = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d')
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        Time = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        Hour, Minute, Second = timeStamp.split(":")
        ####Creatting csv of attendance

        ##Create table for Attendance
        date_for_DB = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d')
        global subb
        subb=SUB_ENTRY.get()
        DB_table_name = str(subb + "_" + Date + "_Time_" + Hour + "_" + Minute + "_" + Second)

        import pymysql.connections

        ###Connect to the database
        try:
            global cursor
            connection = pymysql.connect(host='localhost', user='ali', password='123', db='manually_fill_attendance')
            cursor = connection.cursor()
        except Exception as e:
            print(e)

        sql = "CREATE TABLE " + DB_table_name + """
                        (ID INT NOT NULL AUTO_INCREMENT,
                         ENROLLMENT varchar(100) NOT NULL,
                         NAME VARCHAR(50) NOT NULL,
                         DATE VARCHAR(20) NOT NULL,
                         TIME VARCHAR(20) NOT NULL,
                             PRIMARY KEY (ID)
                             );
                        """


        try:
            cursor.execute(sql)  ##for create a table
        except Exception as ex:
            print(ex)  #

        if subb=='':
            err_screen_for_subject()
        else:
            sb.destroy()
            MFW = tk.Tk()
            MFW.iconbitmap('AMS.ico')
            MFW.title("Manually attendance of "+ str(subb))
            MFW.geometry('880x470')
            MFW.configure(background='snow')

            def del_errsc2():
                errsc2.destroy()

            def err_screen1():
                global errsc2
                errsc2 = tk.Tk()
                errsc2.geometry('330x100')
                errsc2.iconbitmap('AMS.ico')
                errsc2.title('Warning!!')
                errsc2.configure(background='snow')
                Label(errsc2, text='Please enter Student & Enrollment!!!', fg='black', bg='white',
                      font=('times', 16, ' bold ')).pack()
                Button(errsc2, text='OK', command=del_errsc2, fg="black", bg="lawn green", width=9, height=1,
                       activebackground="Red", font=('times', 15, ' bold ')).place(x=90, y=50)

            def testVal(inStr, acttyp):
                if acttyp == '1':  # insert
                    if not inStr.isdigit():
                        return False
                return True

            ENR = tk.Label(MFW, text="Enter Enrollment", fg="gray", bg="white",
                           font = ("Goudy old style", 20, "bold"))
            ENR.place(x=30, y=90)

            STU_NAME = tk.Label(MFW, text="Enter Student name", fg="gray", bg="white",
                                font = ("Goudy old style", 20, "bold"))
            STU_NAME.place(x=30, y=180)

            global ENR_ENTRY
            ENR_ENTRY = tk.Entry(MFW, validate='key', bg="lightgray", font=('times new roman', 20, ' bold '))
            ENR_ENTRY['validatecommand'] = (ENR_ENTRY.register(testVal), '%P', '%d')
            ENR_ENTRY.place(x=30, y=130, height = 40, width = 350)

            def remove_enr():
                ENR_ENTRY.delete(first=0, last=22)

            STUDENT_ENTRY = tk.Entry(MFW, bg="lightgray", font=('times new roman', 20, ' bold '))
            STUDENT_ENTRY.place(x=30, y=220, height = 40, width = 350)

            def remove_student():
                STUDENT_ENTRY.delete(first=0, last=22)

            ####get important variable
            def enter_data_DB():
                ENROLLMENT = ENR_ENTRY.get()
                STUDENT = STUDENT_ENTRY.get()
                if ENROLLMENT=='':
                    err_screen1()
                elif STUDENT=='':
                    err_screen1()
                else:
                    import time
                    time = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S')
                    Date = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d')
                    Hour, Minute, Second = time.split(":")
                    Insert_data = "INSERT INTO " + DB_table_name + " (ID,ENROLLMENT,NAME,DATE,TIME) VALUES (0, %s, %s, %s,%s)"
                    VALUES = (str(ENROLLMENT), str(STUDENT), str(Date), str(time))
                    try:
                        cursor.execute(Insert_data, VALUES)
                    except Exception as e:
                        print(e)
                    ENR_ENTRY.delete(first=0, last=22)
                    STUDENT_ENTRY.delete(first=0, last=22)

            def create_csv():
                import csv
                cursor.execute("select * from " + DB_table_name + ";")
                csv_name='C:/Users/Muhammad Rizwan/PycharmProjects/CS570_AMS/Attendance/Manually Attendance/'+DB_table_name+'.csv'
                with open(csv_name, "w") as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow([i[0] for i in cursor.description])  # write headers
                    csv_writer.writerows(cursor)
                    O="CSV created Successfully"
                    Notifi.configure(text=O, bg="lightblue", fg="#d77337", width=33, font=('times new roman', 15, 'bold'))
                    Notifi.place(x=30, y=380)
                import csv
                import tkinter
                root = tkinter.Tk()
                root.title("Attendance of " + subb)
                root.configure(background='snow')
                with open(csv_name, newline="") as file:
                    reader = csv.reader(file)
                    r = 0

                    for col in reader:
                        c = 0
                        for row in col:
                            # i've added some styling
                            # dddddd = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:00')
                            # lst = [str(i*datetime.timedelta(minutes=1)) for i in range(24*60)]
                            # if dddddd in lst[:770]:
                            #     label = tkinter.Label(root, width=15, height=1, fg="black", font=('times new roman', 13, ' bold '),
                            #                         bg="lawn green", text=row, relief=tkinter.RIDGE)
                            #     label.grid(row=r, column=c)
                            #     print('yes')
                            # else:
                            label = tkinter.Label(root, width=15, height=1, fg="black", font=('times new roman', 13, ' bold '),
                                                bg="lawn green", text=row, relief=tkinter.RIDGE)
                            label.grid(row=r, column=c)
                                # print(lst[:750])
                                # print(dddddd)
                            c += 1
                        r += 1
                root.mainloop()

            Notifi = tk.Label(MFW, text="CSV created Successfully", bg="lightblue", fg="#d77337", width=33,
                                height=2, font=('times', 19, 'bold'))

            # titile
            title_manual_att = tk.Label(MFW, text = "Manual Attendance", font="Impact 25", fg="#d77337", bg="white")
            title_manual_att.place(x =30, y = 30)
            c1ear_enroll = tk.Button(MFW, text="Clear", command=remove_enr, fg="#d77337", bg="white",
                                     activebackground="Red",bd = 0, font=('times new roman', 20), cursor = "hand2")
            c1ear_enroll.place(height = 40, width = 100, x=390, y=130)

            c1ear_student = tk.Button(MFW, text="Clear",bd = 0,  command=remove_student, fg="#d77337", bg="white",cursor = "hand2",
                                      activebackground="Red", font=('times new roman', 20))
            c1ear_student.place(x=390, y=220, height = 40, width = 100)

            DATA_SUB = tk.Button(MFW, text="Enter Data",command=enter_data_DB, bg="#d77337", fg="white",cursor = "hand2",
                                 activebackground="Red", font=('times new roman', 20, ' bold '), bd = 2, relief = RIDGE)
            DATA_SUB.place(x=30, y=320, height = 40, width = 200)

            MAKE_CSV = tk.Button(MFW, text="Convert to CSV",command=create_csv, bg="#d77337", fg="white",cursor = "hand2",
                                 activebackground="Red", font=('times', 20, ' bold '), bd = 2, relief = RIDGE)
            MAKE_CSV.place(x=250, y=320, height = 40, width = 200)

            def attf():
                import subprocess
                subprocess.Popen(r'explorer /select,"C:/Users/Muhammad Rizwan/PycharmProjects/CS570_AMS/Attendance/Manually Attendance/-------Check atttendance-------"')
            attf = tk.Button(MFW,  text="Check Sheets",command=attf,fg="#d77337", bd = 0, bg="white", activebackground = "Red" ,font=('times new roman', 20, ' underline '))
            attf.place(x=250, y=270, height = 40, width = 200)

            MFW.mainloop()

    Sub_title = tk.Label(sb, text="Manually Fill Attendance", font="Impact 25", fg="#d77337", bg="white")
    Sub_title.place(x=50, y=30)
    SUB = tk.Label(sb, text="Enter Subject", font = ("Goudy old style", 20, "bold"), fg = "gray", bg = "white")
    SUB.place(x=50, y=90)

    global SUB_ENTRY
    SUB_ENTRY = tk.Entry(sb, width=20, font=("times new roman", 15, "bold"), bg="lightgray")
    SUB_ENTRY.place(x=50, y=130, height = 40, width = 350)

    fill_manual_attendance = tk.Button(sb, text="Fill Attendance",command=fill_attendance, fg="white", bg="#d77337",
                       activebackground="Red", font=('times new roman', 15, ' bold '), cursor = "hand2", bd = 2, relief = RIDGE)
    fill_manual_attendance.place(x=120, y=180, height = 40, width = 200)
    sb.mainloop()

##For clear textbox
def clear():
    txt.delete(first=0, last=22)

def clear1():
    txt2.delete(first=0, last=22)
def del_sc1():
    sc1.destroy()
def err_screen():
    global sc1
    sc1 = tk.Tk()
    sc1.geometry('300x100')
    sc1.iconbitmap('AMS.ico')
    sc1.title('Warning!!')
    sc1.configure(background='snow')
    Label(sc1,text='Enrollment & Name required!!!',fg='red',bg='white',font=('times new roman', 16, ' bold ')).pack()
    Button(sc1,text='OK',command=del_sc1,fg="black"  ,bg="lawn green"  ,width=9  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold ')).place(x=90,y= 50)

##Error screen2
def del_sc2():
    sc2.destroy()
def err_screen1():
    global sc2
    sc2 = tk.Tk()
    sc2.geometry('300x100')
    sc2.iconbitmap('AMS.ico')
    sc2.title('Warning!!')
    sc2.configure(background='snow')
    Label(sc2,text='Please enter your subject name!!!',fg='red',bg='white',font=('times', 16, ' bold ')).pack()
    Button(sc2,text='OK',command=del_sc2,fg="black"  ,bg="lawn green"  ,width=9  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold ')).place(x=90,y= 50)

###For take images for datasets
def take_img():
    l1 = txt.get()
    l2 = txt2.get()
    if l1 == '':
        err_screen()
    elif l2 == '':
        err_screen()
    else:
        try:
            cam = cv2.VideoCapture(0)
            detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            Enrollment = txt.get()
            Name = txt2.get()
            sampleNum = 0
            while (True):
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    # incrementing sample number
                    sampleNum = sampleNum + 1
                    # saving the captured face in the dataset folder
                    cv2.imwrite("TrainingImage/ " + Name + "." + Enrollment + '.' + str(sampleNum) + ".jpg",
                                gray[y:y + h, x:x + w])
                    cv2.imshow('Frame', img)
                # wait for 100 milliseconds
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                # break if the sample number is more than 100
                elif sampleNum > 70:
                    break
            cam.release()
            cv2.destroyAllWindows()
            ts = time.time()
            Date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
            Time = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
            row = [Enrollment, Name, Date, Time]
            with open('StudentDetails\StudentDetails.csv', 'a+') as csvFile:
                writer = csv.writer(csvFile, delimiter=',')
                writer.writerow(row)
                csvFile.close()
            res = "Images Saved for Enrollment : " + Enrollment + " Name : " + Name
            Notification.configure(text=res, bg="lightblue", fg = "#d77337",font=('times new roman', 15, 'bold'))
            Notification.place(x=20, y=450)
        except FileExistsError as F:
            f = 'Student Data already exists'
            Notification.configure(text=f, bg="Red", fg = "#d77337", font=('times new roman', 15, 'bold'))
            Notification.place(x=20, y=450)


###for choose subject and fill attendance
def subjectchoose():
    def Fillattendances():
        sub=tx.get()
        now = time.time()  ###For calculate seconds of video
        future = now + 20
        if time.time() < future:
            if sub == '':
                err_screen1()
            else:
                recognizer = cv2.face.LBPHFaceRecognizer_create()
                #recognizer = cv2.createLBPHFaceRecognizer()
                try:
                    recognizer.read("TrainingImageLabel/Trainner.yml")
                except:
                    e = 'Model not found,Please train model'
                    Notifica.configure(text=e, bg="red", fg="black", width=33, font=('times', 15, 'bold'))
                    Notifica.place(x=300, y=270)

                harcascadePath = "haarcascade_frontalface_default.xml"
                faceCascade = cv2.CascadeClassifier(harcascadePath)
                df = pd.read_csv("StudentDetails\StudentDetails.csv")
                cam = cv2.VideoCapture(0)
                font = cv2.FONT_HERSHEY_SIMPLEX
                col_names = ['Enrollment', 'Name', 'Date', 'Time']
                attendance = pd.DataFrame(columns=col_names)
                while True:
                    ret, im = cam.read()
                    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                    faces = faceCascade.detectMultiScale(gray, 1.2, 5)
                    for (x, y, w, h) in faces:
                        global Id

                        Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
                        if (conf <70):
                            print(conf)
                            global Subject
                            global aa
                            global date
                            global timeStamp
                            Subject = tx.get()
                            ts = time.time()
                            date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                            timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                            aa = df.loc[df['Enrollment'] == Id]['Name'].values
                            global tt
                            # tt = str(Id) + "-" + aa
                            
                            # En = '15624031' + str(Id)
                            attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 260, 0), 7)
                            cv2.putText(im, str(aa), (x + h, y), font, 1, (255, 255, 0,), 4)
                            

                        else:
                            Id = 'Unknown'
                            tt = str(Id)
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
                            cv2.putText(im, str(tt), (x + h, y), font, 1, (0, 25, 255), 4)
                    if time.time() > future:
                        break

                    attendance = attendance.drop_duplicates(['Enrollment'], keep='first')
                    cv2.imshow('Filling attedance..', im)
                    key = cv2.waitKey(30) & 0xff
                    if key == 27:
                        break

                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                Hour, Minute, Second = timeStamp.split(":")
                fileName = "Attendance/" + Subject + "_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
                attendance = attendance.drop_duplicates(['Enrollment'], keep='first')
                print(attendance)
                attendance.to_csv(fileName, index=False)

                ##Create table for Attendance
                date_for_DB = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d')
                DB_Table_name = str( Subject + "_" + date_for_DB + "_Time_" + Hour + "_" + Minute + "_" + Second)
                import pymysql.connections

                ###Connect to the database
                try:
                    global cursor
                    connection = pymysql.connect(host='localhost', user='ali', password='123', db='Face_reco_DB')
                    cursor = connection.cursor()
                except Exception as e:
                    print(e)

                sql = "CREATE TABLE " + DB_Table_name + """
                (ID INT NOT NULL AUTO_INCREMENT,
                 ENROLLMENT varchar(100) NOT NULL,
                 NAME VARCHAR(50) NOT NULL,
                 DATE VARCHAR(20) NOT NULL,
                 TIME VARCHAR(20) NOT NULL,
                     PRIMARY KEY (ID)
                     );
                """
                ####Now enter attendance in Database
                insert_data =  "INSERT INTO " + DB_Table_name + " (ID,ENROLLMENT,NAME,DATE,TIME) VALUES (0, %s, %s, %s,%s)"
                VALUES = (str(Id), str(aa), str(date), str(timeStamp))
                try:
                    cursor.execute(sql)  ##for create a table
                    cursor.execute(insert_data, VALUES)##For insert data into table
                except Exception as ex:
                    print(ex)  #

                M = 'Attendance filled Successfully'
                Notifica.configure(text=M, bg="lightblue", fg="#d77337", width=33, font=('times', 15, 'bold'))
                Notifica.place(x=30, y=270)
                
                cam.release()
                cv2.destroyAllWindows()
                speaker = pyttsx3.init()
                speaker.say(M)
                speaker.runAndWait()


                import csv
                import tkinter
                root = tkinter.Tk()
                root.title("Attendance of " + Subject)
                root.configure(background='snow')
                cs = 'C:/Users/Muhammad Rizwan/PycharmProjects/CS570_AMS/' + fileName
                with open(cs, newline="") as file:
                    reader = csv.reader(file)
                    r = 0
                    for col in reader:
                        c = 0
                        for row in col:
                            # i've added some styling
                            # dddddd = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:00')
                            # lst = [str(i*datetime.timedelta(minutes=1)) for i in range(24*60)]
                            # if dddddd in lst[:60]:
                            #     label = tkinter.Label(root, width=8, height=1, fg="black", font=('times', 15, ' bold '),
                            #                         bg="red", text=row, relief=tkinter.RIDGE)
                            #     label.grid(row=r, column=c)
                            # else:
                            label = tkinter.Label(root, width=8, height=1, fg="black", font=('times', 15, ' bold '),
                                                bg="lawn green", text=row, relief=tkinter.RIDGE)
                            label.grid(row=r, column=c)
                        
                            c += 1
                        r += 1
                root.mainloop()
                print(attendance)

    ###windo is frame for subject chooser
    windo = tk.Tk()
    windo.iconbitmap('AMS.ico')
    windo.title("Enter subject name...")
    windo.geometry('500x320')
    windo.resizable(False,False)
    windo.configure(bg = "white")
    Notifica = tk.Label(windo, text="Attendance filled Successfully", bg="lightblue", fg="#d77337", width=33,
                            height=2, font=('times new roman', 15, 'bold'))

    def Attf():
        import subprocess
        #Popen with arguments executable , args , cwd , and env . The value for args may be a single string or a list of strings, depending on platform.
        subprocess.Popen(r'explorer /select,"C:/Users/Muhammad Rizwan/PycharmProjects/CS570_AMS/Attendance/Manually Attendance/-------Check atttendance-------"')

    # title
    automatic_title = tk.Label(windo, text = "Automatic Attendace", bg = "white", fg = "#d77337", font="Impact 35", )
    automatic_title.place(x=50, y=20)

    sub = tk.Label(windo, text="Enter Subject", fg="gray", bg="white", font=("Goudy old style", 15, "bold"))
    sub.place(x=50, y=100)

    tx = tk.Entry(windo, bg="lightgray",  font=('times new roman', 15))
    tx.place(x=50, y=130, height = 40, width = 350)

    fill_a = tk.Button(windo, text="Fill Attendance", fg="white", command=Fillattendances, bg="#d77337", cursor = "hand2", bd = 2, relief = RIDGE,
                       activebackground="Red", font=('times new roman', 15, ' bold '))
    fill_a.place(x=120, y=180, width = 200, height = 40)

    attf = tk.Button(windo, text="Check Sheets", command=Attf, fg="#d77337",bd = 0, bg="white", cursor="hand2", activebackground="Red", font=('times new roman', 15, 'underline'))
    attf.place(x=160, y=220)
    windo.mainloop()

def admin_panel():
    win = tk.Tk()
    win.iconbitmap('AMS.ico') # For Icon 
    win.title("LogIn")
    win.geometry('500x420')
    win.resizable(False, False)
    win.configure(bg = "white")

    def log_in():
        username = un_entr.get()
        password = pw_entr.get()

        if username == 'ali' :
            if password == '123':
                win.destroy()
                import csv
                import tkinter
                root = tkinter.Tk()
                root.title("Student Details")
                root.configure(background='snow')

                cs = 'C:/Users/Muhammad Rizwan/PycharmProjects/CS570_AMS/StudentDetails/StudentDetails.csv'
                with open(cs, newline="") as file:
                    reader = csv.reader(file)
                    r = 0

                    for col in reader:
                        c = 0
                        for row in col:
                            # i've added some styling
                            label = tkinter.Label(root, width=8, height=1, fg="black", font=('times', 15, ' bold '),
                                                  bg="lawn green", text=row, relief=tkinter.RIDGE)
                            label.grid(row=r, column=c)
                            c += 1
                        r += 1
                root.mainloop()
            else:
                valid = 'Incorrect ID or Password'
                Nt.configure(text=valid, bg="lightblue", fg="#d77337", font=('times new roman', 15, 'bold'))
                Nt.place(x=10, y=360)

        else:
            valid ='Incorrect ID or Password'
            Nt.configure(text=valid, bg="lightblue", fg="#d77337", font=('times new roman', 15, 'bold'))
            Nt.place(x=10, y=360)


    Nt = tk.Label(win, text="Attendance filled Successfully", bg="Green", fg="white", width=40,
                  height=2, font=('times', 19, 'bold'))
    # Nt.place(x=120, y=350)

    title_for_check_registration = tk.Label(win, text="Check Register Students", font="Impact 30", fg="#d77337", bg="white")
    title_for_check_registration.place(x = 30, y = 30)
    un = tk.Label(win, text="Enter username", fg="gray", bg="white",
                   font=("Goudy old style", 25, "bold"))
    un.place(x=30, y=100)

    pw = tk.Label(win, text="Enter password", fg="gray", bg="white",
                   font=("Goudy old style", 25, "bold"))
    pw.place(x=30, y=200)

    def c00():
        un_entr.delete(first=0, last=22)

    un_entr = tk.Entry(win, bg="lightgray", font=('times new roman', 15, ' bold '))
    un_entr.place(x=30, y=150, height = 40, width = 350)

    def c11():
        pw_entr.delete(first=0, last=22)

    pw_entr = tk.Entry(win, show="*", bg="lightgray", font=('times new roman', 15, ' bold '))
    pw_entr.place(x=30, y=250, height = 40, width = 350)

    c0 = tk.Button(win, text="Clear", command=c00, fg="#d77337", bg="white",bd = 0, cursor = "hand2",
                            activebackground="Red", font=('times', 20, 'underline'))
    c0.place(x=400, y=145)

    c1 = tk.Button(win, text="Clear", command=c11,fg="#d77337", bg="white",bd = 0, cursor = "hand2",
                   activebackground="Red", font=('times', 20, 'underline'))
    c1.place(x=400, y=245)

    Login = tk.Button(win, text="LogIn", fg="white", bg="#d77337", bd = 2, relief = RIDGE , activebackground="Red",command=log_in, font=('times', 15, ' bold '), cursor = "hand2")
    Login.place(x=100, y=310, height = 40, width = 200)
    win.mainloop()


###For train the model
def trainimg():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    #recognizer = cv2.LBPHFaceRecognizer_create()
    global detector
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    try:
        global faces,Id
        faces, Id = getImagesAndLabels("TrainingImage")
    except Exception as e:
        l='please make "TrainingImage" folder & put Images'
        Notification.configure(text=l, bg="lightblue", fg = "#d77337", font=('times new roman', 18, 'bold'))
        Notification.place(x=50, y=420)

    recognizer.train(faces, np.array(Id))
    try:
        recognizer.save("TrainingImageLabel\Trainner.yml")
    except Exception as e:
        q='Please make "TrainingImageLabel" folder'
        Notification.configure(text=q, bg="lightblue",fg = "#d77337", font=('times', 18, 'bold'))
        Notification.place(x=50, y=420)

    res = "Model Trained"  # +",".join(str(f) for f in Id)
    Notification.configure(text=res, bg="lightblue",fg = "#d77337", font=('times new roman', 18, 'bold'))
    Notification.place(x=50, y=420)

def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # create empth face list
    faceSamples = []
    # create empty ID list
    Ids = []
    # now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        # loading the image and converting it to gray scale
        pilImage = Image.open(imagePath).convert('L')
        # Now we are converting the PIL image into numpy array
        imageNp = np.array(pilImage, 'uint8')
        # getting the Id from the image

        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces = detector.detectMultiScale(imageNp)
        # If a face is there then append that in the list as well as Id of it
        for (x, y, w, h) in faces:
            faceSamples.append(imageNp[y:y + h, x:x + w])
            Ids.append(Id)
    return faceSamples, Ids

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.iconbitmap('AMS.ico')

def on_closing():
    from tkinter import messagebox
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()
window.protocol("WM_DELETE_WINDOW", on_closing)


#Frame in home page
home_frame = Frame(window, bg = "white", bd = 2, relief = RIDGE)
home_frame.place(x = 50, y = 100, height =  500, width = 500)

Notification = tk.Label(home_frame, text="All things good", bg="white", fg="#d77337", font=('times new roman', 13, 'bold'))
Notification.place(x = 50, y = 410)

# home title
home_title = tk.Label(home_frame, text = "Face Recoginzation Based Attendance System", font = "Impact 18", fg = "#d77337", bg = "white")
home_title.place(x=20, y=20)


lbl = tk.Label(home_frame, text="Enter Enrollment", fg="gray",bg = "white", font=("Goudy old style", 20, "bold"))
lbl.place(x=50, y=80)



def testVal(inStr,acttyp):
    if acttyp == '1': #insert
        if not inStr.isdigit():
            return False
    return True



txt = tk.Entry(home_frame, validate="key", bg="lightgray", font=('times new roman', 20, ' bold '))
txt['validatecommand'] = (txt.register(testVal),'%P','%d')
txt.place(x=50, y=120, height = 40, width = 350)

lbl2 = tk.Label(home_frame, text="Enter Name", fg="gray",bg = "white", font=("Goudy old style", 20, "bold"))
lbl2.place(x=50, y=160)

txt2 = tk.Entry(home_frame, bg="lightgray", font=('times new roman', 20, ' bold '), bd = 1)
txt2.place(x=50, y=200, height = 40, width = 350)

clearButton = tk.Button(home_frame, text="Clear",bd = 0, command=clear, fg="#d77337",bg="white", activebackground = "Red",font=('times new roman', 15, ' bold '))
clearButton.place(x=420, y=105)

clearButton1 = tk.Button(home_frame, text="Clear",command=clear1, fg="#d77337",bg="white", activebackground = "Red",font=('times new roman', 15, ' bold '), bd = 0)
clearButton1.place(x=420, y=175)

AP = tk.Button(home_frame, bd = 0, text="Check Register students",command=admin_panel, fg="#d77337",bg="white" , activebackground = "Red" ,font=('times new roman', 15, ' underline '))
AP.place(x=100, y=240)

takeImg = tk.Button(home_frame, text="Take Images",command=take_img, fg="white"  ,bg="#d77337", activebackground = "Red" ,font=('times new roman', 15, ' bold '))
takeImg.place(x=20, y=280, height = 40, width = 220)

trainImg = tk.Button(home_frame, text="Train Images", fg="white",command=trainimg ,bg="#d77337", activebackground = "Red" ,font=('times new roman', 15, ' bold '))
trainImg.place(x=260, y=280, height = 40, width = 220)

FA = tk.Button(home_frame, text="Automatic Attendace",fg="white",command=subjectchoose  ,bg="#d77337", activebackground = "Red" ,font=('times new roman', 15, ' bold '))
FA.place(x=20, y=350, height = 40, width = 220)

quitWindow = tk.Button(home_frame, text="Manually Fill Attendance", command=manually_fill  ,fg="white"  ,bg="#d77337", activebackground = "Red" ,font=('times new roman', 15, ' bold '))
quitWindow.place(x=260, y=350, height = 40, width = 220)

window.mainloop()
