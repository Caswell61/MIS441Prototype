### Program: 355_cons_pdf_autofill.py
### Class: MIS 441
### Authors: Nick Caswell, Cristian Hernandez, Kyle Zhou, Fares Hayouna
### Description: This program launches a GUI which is used to autofill
###              and organize contracting files for the workers at the
###              355th Contracting Squadron @ DMAFB.

from fillpdf import fillpdfs
# import pypdftk as pdf
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import datetime as dt
import os 

# Constants used for using files within the pdf_autofill package and
# PDF editting/creation
CWD = os.getcwd()
CWD_UTILS = CWD + "\\utils\\"
CWD_TEMPLATES = CWD + "\\templates\\"
CWD_PROJECTS = CWD + "\\Contracting Projects\\"
FORM_TEMPLATES = ['DD2579_Template.pdf', 'J&A_Single_Source_Template.pdf',
                  'Market_Research_Template']

class contractor:
    '''
    This class will be used for further integration with the database. It is currently not used.
    '''
    def __init__(self, name, office, email, telephone):
        self.name = name
        self.officesymbol = office
        self.email = email
        self.telephone = telephone
    # Getters and setters for the contractor class
    def get_name(self):
        return self.name

    def set_officesymbol(self, office):
        self.officesymbol = ""
    def get_officesymbol(self):
        return self.officesymbol

    def set_email(self, email):
        self.email = email
    def get_email(self):
        return self.email

    def set_telephone(self,phone):
        self.telephone = phone
    def get_telephone(self):
        return self.telephone
    
    def export_info(self):
        file = open(CWD_UTILS + "profiles.txt", "w")
        print(self.name, self.officesymbol, self.email, self.telephone)
        file.write(self.name + " " + self.officesymbol + " " + self.email + " " + str(self.telephone))
        file.close()

def gui():

    def form_fill(data):
        #test_doc = CWD_TEMPLATES + FORM_TEMPLATES[2]
        #test_doc = FORM_TEMPLATES[1]
        print(data)
        #pdf_dict = pdf.dump_data_fields(test_doc)
        print('DONE')

    def profileBtn():

        def getProfName():
            userInput = prof_name.get()
            print(userInput)
            return userInput

        def getProfOffice():
            userInput = prof_office.get()
            return userInput

        def getProfEmail():
            userInput = prof_email.get()
            return userInput

        def getProfTelephone():
            userInput = prof_telephone.get()
            return userInput

        def saveProf():
            file = open(CWD_UTILS + "profiles.txt", "w")
            file.write(getProfName() + "; " + getProfOffice() + "; " +
                       getProfEmail() + "; "  + getProfTelephone() + "\n")
            file.close()
            #new_contractor.export_info()

        # GUI settings for Add Profile Mapping.
        root = Tk()
        root.geometry('300x300')
        root.configure(background='#F0F8FF')
        root.title('Input Mapper v1 - Add Profile')
        Button(root, text='Save Profile', bg='#FFFAFA', font=('arial', 12, 'normal'),command=saveProf).place(x=110, y=220)
        Label(root, text='Name (Last, First, Middle Initial)', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=20, y=10)
        Label(root, text='Office Symbol', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=20, y=58)
        Label(root, text='Email', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=20, y=106)
        Label(root, text='Telephone', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=20, y=154)
        # Text Field Creation
        prof_name=Entry(root)
        prof_name.place(x=25, y=35)
        prof_office=Entry(root)
        prof_office.place(x=25, y=83)
        prof_email=Entry(root)
        prof_email.place(x=25, y=131)
        prof_telephone=Entry(root)
        prof_telephone.place(x=25, y=179)
        root.mainloop()

    #def chgprof():
        # Will be implemented in the future, will be used to add a change profile button.
        #print('clicked')
    def exitprogram():
        exit()

    def getConActivity():
        userInput = con_activity.get()
        return userInput

    def getPurReqid():
        userInput = pur_reqid.get()
        return userInput

    def getProjectName():
        userInput = project_name.get()
        return userInput

    def getEstCost():
        userInput = est_cost.get()
        return userInput

    def getPiiNum():
        userInput = pii_num.get()
        return userInput

    def getNaics():
        userInput = NAICS.get()
        return userInput

    def curr_profile_data():
        file = open(CWD_UTILS + 'profiles.txt','r')
        data = file.readline()
        data = data.split(';')
        for x in range(len(data)):
            data[x] = data[x].strip()
        return data

    def formgen():
        '''
        This function compiles data entered by the user into a single
        list, from both the user profile as well as the form entry.
        '''
        profile = curr_profile_data()
        data = []
        data.append(getProjectName())
        data.append(getConActivity())
        data.append(getPurReqid())
        data.append(getPiiNum())
        data.append(getEstCost())
        data.append(getNaics())
        data = data + profile 
        #print(data)
        os.mkdir(CWD_PROJECTS + data[2] + " Contracting Documents\\")
        form_fill(data)
    
    # The building of the primary GUI begins here, functions above are used to interact with the
    # buttons created below.
    date = dt.datetime.now()  
    root = Tk()
    root.geometry('581x400')
    root.configure(background='#F0F8FF')
    root.title('Input Mapper v1')
    curr_prof = curr_profile_data()
    img1 = Image.open(CWD_UTILS+ "CONS.jpg")
    img2 = ImageTk.PhotoImage(img1)
    panel = tk.Label(root, image = img2)
    panel.pack(side = TOP, anchor=NW)
    canvas = tk.Canvas()
    canvas.create_line(20,20,600,20)
    canvas.pack()

    # Button Creation
    Button(root, text='Add Profile', bg='#FFFAFA',
           font=('arial', 12, 'normal'),command=profileBtn).place(x=170, y=100)
    # Button(root, text='Change Profile', bg='#FFFAFA', 
    #        font=('arial', 12, 'normal'),command=chgprof).place(x=140, y=100)
    Button(root, text='Exit', bg='#FFFAFA', 
           font=('arial', 12, 'normal'),command=exitprogram).place(x=520, y=15)
    Button(root, text='Generate Forms', bg='#FFFAFA', 
           font=('arial', 12, 'normal'),command=formgen).place(x=205, y=350)

    # Label Creation
    Label(root, text='Project/Program Name', bg='#F0F8FF',
          font=('arial', 12, 'normal')).place(x=20, y=190)
    Label(root, text='Contracting Activity/Organization', bg='#F0F8FF',
          font=('arial', 12, 'normal')).place(x=20, y=238)
    Label(root, text='NAICS Code', bg='#F0F8FF',
          font=('arial', 12, 'normal')).place(x=20, y=286)
    Label(root, text='Purchase Request/ID Number', bg='#F0F8FF', 
          font=('arial', 12, 'normal')).place(x=340, y=190)
    Label(root, text='Estimated Cost', bg='#F0F8FF', 
          font=('arial', 12, 'normal')).place(x=340, y=238)
    Label(root, text='PII Number', bg='#F0F8FF', 
          font=('arial', 12, 'normal')).place(x=340, y=286)
    Label(root, text='Current Profile', bg='#F0F8FF', 
          font=('arial', 12, 'normal')).place(x=140, y=8)
    Label(root, text='Date', bg='#F0F8FF', 
          font=('arial', 12, 'normal')).place(x=370, y=8)
    Label(root, text="Data Input", bg="#F0F8FF", 
          font=('arial', 16, 'bold')).place(x=10, y=160)
    Label(root, text="Profile Map", bg="#F0F8FF", 
          font=('arial', 16, 'bold')).place(x=400, y=100)
    Label(root, text=curr_prof[0], bg='#F0F8FF', 
          font=('arial', 12, 'normal')).place(x=140, y=30)
    Label(root, text=f"{date:%B %d, %Y}", bg="#F0F8FF", 
          font=('arial', 12, 'normal')).place(x=370, y=30)

    # Text Field Creation
    pur_reqid=Entry(root)
    pur_reqid.place(x=345, y=215)
    con_activity=Entry(root)
    con_activity.place(x=25, y=263)
    project_name=Entry(root)
    project_name.place(x=25, y=215)
    est_cost=Entry(root)
    est_cost.place(x=345, y=263)
    pii_num=Entry(root)
    pii_num.place(x=345, y=311)
    NAICS=Entry(root)
    NAICS.place(x=25, y=311)

    root.mainloop()



def main():
    gui()
    pass

if __name__ == "__main__":
    main()
