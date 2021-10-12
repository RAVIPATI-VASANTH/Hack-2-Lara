#Project importation Files
from tkinter import *
from InternalWorking import *
#from twilio.rest import Client
import pickle

#configuration
StudentFile=open("StudentsData.pickle","a")
StudentFile.close()

#twilio setup 
account_sid="ACf8ffa48bbd63dd930bd719c1a3070bc0"
auth_token="a1cc3bf604d415ed0ce05df68759df70"

#Class Definitions in project
class NEWBUTTON():
    def __init__(self,App):
        self.App=App
        self.BuildNewframe()

    def BuildNewframe(self):
        FrameInfo=Label(self.App.WorkingFrameslist[0],text="NEW Module",bg="LightGrey",font=("Arial", 25))
        FrameInfo.grid(row=0,column=0,padx=5,pady=5,ipadx=5,ipady=5,columnspan=2)
        Labelslist=["Student Name","Student RegdNum","StudentSection","Parent Contact","Student Contact"]
        j=1
        for i in Labelslist:
            label=Label(self.App.WorkingFrameslist[0],text=i,width=20,bg="lightgrey",font=("Arial", 10))
            label.grid(row=j,column=0,padx=5,pady=5,ipadx=5,ipady=5)
            j+=1
        self.StudentNameEntry=Entry(self.App.WorkingFrameslist[0],relief=SUNKEN,bd=3,width=30)
        self.StudentNameEntry.grid(row=1,column=1,padx=5,pady=5)
        self.StudentRegdEntry=Entry(self.App.WorkingFrameslist[0],relief=SUNKEN,bd=3,width=30)
        self.StudentRegdEntry.grid(row=2,column=1,padx=5,pady=5)
        self.StudentSectionEntry=Entry(self.App.WorkingFrameslist[0],relief=SUNKEN,bd=3,width=30)
        self.StudentSectionEntry.grid(row=3,column=1,padx=5,pady=5)
        self.StudentParentContactEntry=Entry(self.App.WorkingFrameslist[0],relief=SUNKEN,bd=3,width=30)
        self.StudentParentContactEntry.grid(row=4,column=1,padx=5,pady=5)
        self.StudentContactEntry=Entry(self.App.WorkingFrameslist[0],relief=SUNKEN,bd=3,width=30)
        self.StudentContactEntry.grid(row=5,column=1,padx=5,pady=5)
        saveButton=Button(self.App.WorkingFrameslist[0],text="Save",width=10,command=self.SaveData,font=("Arial", 12))
        saveButton.grid(row=6,column=1,padx=5,pady=5,ipadx=5,ipady=5)
        self.NewframeMessageLabel=Label(self.App.WorkingFrameslist[0],text="Enter required Data to Create New Student Data",bg="lightgrey",font=("Arial", 10))
        self.NewframeMessageLabel.grid(row=0,column=2,padx=5,pady=5,ipadx=5,ipady=5,columnspan=2)

    def SaveData(self):
        signal=True
        if(self.StudentNameEntry.get().strip()=="" or self.StudentRegdEntry.get().strip()=="" or self.StudentParentContactEntry.get().strip()=="" or self.StudentContactEntry.get().strip()=="" or self.StudentSectionEntry.get().strip()==""):
            self.NewframeMessageLabel["text"]="Data Should not be Empty"
            signal=False
        elif(self.StudentParentContactEntry.get().isalpha() or self.StudentContactEntry.get().isalpha()):
            self.NewframeMessageLabel["text"]="Contact Fields Must contain on numbers"
            signal=False
        if(signal):
            for i in self.App.StudentsList:
                if(self.StudentRegdEntry.get().strip().upper()==i.RegdNumber):
                    self.NewframeMessageLabel["text"]="This register number is already Exists"
                    signal=False
                    break
        if(signal):
            self.NewframeMessageLabel["text"]=self.StudentNameEntry.get().strip().upper()+" with Registration id "+self.StudentRegdEntry.get().strip().upper()+" created."
            currentStudent=Student(self.StudentNameEntry.get().strip().upper(),self.StudentRegdEntry.get().strip().upper(),self.StudentSectionEntry.get().strip().upper(),self.StudentParentContactEntry.get().strip().upper(),self.StudentContactEntry.get().strip().upper())
            self.App.StudentsList.append(currentStudent)
            self.App.ModifyData()
            self.App.UpdateWidgets()
            self.StudentNameEntry.delete(0,"end")
            self.StudentRegdEntry.delete(0,"end")
            self.StudentSectionEntry.delete(0,"end")
            self.StudentParentContactEntry.delete(0,"end")
            self.StudentContactEntry.delete(0,"end")

class UPDATEBUTTON():
    def __init__(self,App):
        self.App=App
        self.BuildUpdateframe()
        
    def BuildUpdateframe(self):
        FrameInfo=Label(self.App.WorkingFrameslist[1],text="UPDATE Module",bg="LightGrey",font=("Arial", 25))
        FrameInfo.grid(row=0,column=0,padx=5,pady=5,ipadx=5,ipady=5,columnspan=2)
        self.UpdateMessageLabel=Label(self.App.WorkingFrameslist[1],bg="lightgrey",text="",font=("Arial", 12),width=50)
        self.UpdateMessageLabel.grid(row=0,column=2,padx=5,pady=5,ipadx=5,ipady=5,columnspan=2)
        StudentRegdLabel=Label(self.App.WorkingFrameslist[1],text="Student RegdNum",width=20,bg="LightGrey",font=("Arial", 12))
        StudentRegdLabel.grid(row=1,column=0,padx=5,pady=5,ipadx=5,ipady=5)
        self.StudentRegdOptoinValue=StringVar()
        self.StudentRegdOptoinValue.set("Select Register Number")
        stdentlist=[]
        for i in self.App.StudentsList:
            stdentlist.append(i.RegdNumber)
        if(len(stdentlist)==0):
            stdentlist.append("NO DATA") 
        StudentRegdOptionMenu=OptionMenu(self.App.WorkingFrameslist[1],self.StudentRegdOptoinValue,*stdentlist)
        StudentRegdOptionMenu.config(width=25)
        StudentRegdOptionMenu.grid(row=1,column=1,padx=5,pady=5,columnspan=2)
        StudentNextButton=Button(self.App.WorkingFrameslist[1],text="Next->>",width=10,command=self.Check,font=("Arial", 12))
        StudentNextButton.grid(row=2,column=1,padx=5,pady=5)
        self.UpdateWorkingFramesList=["Attendance Frame","Internals Frame"]
        j=0
        for i in self.UpdateWorkingFramesList:
            frame=Frame(self.App.WorkingFrameslist[1],bg="lightgrey",width=500,height=400)
            frame.grid(row=4,column=1)
            frame.grid_propagate(0)
            frame.pack_propagate(0)
            self.UpdateWorkingFramesList[j]=frame
            j+=1
        self.AttendanceButton=Button(self.App.WorkingFrameslist[1],text="Attendance",width=10,font=("Arial", 12),command=lambda : self.ShowFrame(self.UpdateWorkingFramesList[0]))
        self.AttendanceButton.grid(row=3,column=0,padx=5,pady=5)
        self.AttendanceButton["state"]="disabled"
        self.InternalsButton=Button(self.App.WorkingFrameslist[1],text="Internals",width=10,font=("Arial", 12),command=lambda : self.ShowFrame(self.UpdateWorkingFramesList[1]))
        self.InternalsButton.grid(row=3,column=1,padx=5,pady=5)
        self.InternalsButton["state"]="disabled"

    def Check(self):
        signal=True
        if(self.StudentRegdOptoinValue.get()=="Select Register Number"):
            self.UpdateMessageLabel["text"]="Select the Student number"
            signal=False
        elif(self.StudentRegdOptoinValue.get()=="NO DATA"):
            self.UpdateMessageLabel["text"]="No Students are available to Select"
            signal=False
        if(signal):
            self.AttendanceButton["state"]="normal"
            self.InternalsButton["state"]="normal"
            self.BuildAttendanceFrame()
            self.BuildInternalFrame()
            self.UpdateWorkingFramesList[0].tkraise()
    
    def BuildAttendanceFrame(self):
        labels=["Total periods","Attended periods"]
        j=0
        for i in labels:
            label=Label(self.UpdateWorkingFramesList[0],bg="lightgrey",text=i,font=("Arial", 12),width=15)
            label.grid(row=j,column=0,padx=5,pady=5,ipadx=5,ipady=5)
            j+=1
        self.TotalPeriodsEntry=Entry(self.UpdateWorkingFramesList[0],relief=SUNKEN,bd=3,width=30)
        self.TotalPeriodsEntry.grid(row=0,column=1,padx=5,pady=5)
        self.AttendedPeriodsEntry=Entry(self.UpdateWorkingFramesList[0],relief=SUNKEN,bd=3,width=30)
        self.AttendedPeriodsEntry.grid(row=1,column=1,padx=5,pady=5)
        AttendanceUpdateButton=Button(self.UpdateWorkingFramesList[0],text="UPDATE",width=10,font=("Arial", 12),command=self.UpdateAttandence)
        AttendanceUpdateButton.grid(row=3,column=1,padx=5,pady=5,ipadx=5,ipady=5)

    def UpdateAttandence(self):
        signal=True
        if(self.TotalPeriodsEntry.get().strip()=="" or self.AttendedPeriodsEntry.get().strip()==""):
            self.UpdateMessageLabel["text"]="Data Should not be Empty"
            signal=False
        elif(self.TotalPeriodsEntry.get().strip().isalpha() or self.AttendedPeriodsEntry.get().strip().isalpha()):
            self.UpdateMessageLabel["text"]="Data should be Numericals"
            signal=False
        elif(int(self.AttendedPeriodsEntry.get())>int(self.TotalPeriodsEntry.get())):
            self.UpdateMessageLabel["text"]="Attended periods Can't greater than Total Periods"
            signal=False
        if(signal):
            print("here it is")
            for i in self.App.StudentsList:
                if(i.RegdNumber==self.StudentRegdOptoinValue.get()):
                    i.AttendedSessionsList.append(int(self.AttendedPeriodsEntry.get()))
                    i.TotalSessionsList.append(int(self.TotalPeriodsEntry.get()))
                    self.App.ModifyData()
                    self.CalculateAttandance(i)
                    break

    def CalculateAttandance(self,Student):
        Message="Your Ward, "+Student.StudentName+"'s Attandance Percentage is "
        percentage=(sum(Student.AttendedSessionsList)/sum(Student.TotalSessionsList)*100)
        if(percentage<75):
            Message=Message+str(percentage)+".\n"
            Tuple=self.calci(sum(Student.AttendedSessionsList),sum(Student.TotalSessionsList))
            Message=Message+"And need to attend "+str(Tuple[0]-sum(Student.AttendedSessionsList))+" Periods in next "+str(Tuple[1]-sum(Student.TotalSessionsList))+" Periods to reach Minimum Attandence of 75."
            person=Client(account_sid,auth_token)
            sms= person.messages.create(from_="+14158253280",body=Message,to="+91"+Student.ParentContact,)
            print(sms.sid)

    def calci(self,ca,ct):
        cp=(ca/ct)*100
        if(cp<75):
            da=ca
            dt=ct
            count=0
            while(1):
                dt+=8
                signal=False
                for i in range(1,8+1):
                    da+=1
                    dp=(da/dt)*100
                    if(dp>=75):
                        return (da,dt)
                if(signal==True):
                    break
    
    def BuildInternalFrame(self):
        subjectcountlabel=Label(self.UpdateWorkingFramesList[1],text="No of Subjects",width=15,font=("Arial", 12),bg="lightgrey")
        subjectcountlabel.grid(row=0,column=0,padx=5,pady=5,ipadx=5,ipady=5)
        self.subjectCountEntry=Entry(self.UpdateWorkingFramesList[1],relief=SUNKEN,bd=3,width=15)
        self.subjectCountEntry.grid(row=0,column=1,padx=5,pady=5)
        self.subjectNextButton=Button(self.UpdateWorkingFramesList[1],text="Next->>",width=10,command=self.SubjectcountNext)
        self.subjectNextButton.grid(row=0,column=2,padx=5,pady=5)
        
    def SubjectcountNext(self):
        signal=True
        if(self.subjectCountEntry.get().strip()==""):
            self.UpdateMessageLabel["text"]="Data Should Not be Empty"
            signal=False
        elif(self.subjectCountEntry.get().isalpha()):
            self.UpdateMessageLabel["text"]="Data should be Numericals"
            signal=False
        if(signal):
            self.subjectNextButton["state"]="disabled"
            self.SubjectsList=[]
            self.MarksList=[]
            self.labStatusList=[]
            self.currentcount=int(self.subjectCountEntry.get())
            self.UpdateMessageLabel["text"]="Enter "+str(self.currentcount)+" more subjects"
            labels=["subject name","subject marks"]
            j=1
            for i in labels:
                label=Label(self.UpdateWorkingFramesList[1],text=i,width=15,bg="lightgrey",font=("Arial", 12))
                label.grid(row=j,column=0,padx=5,pady=5,ipadx=5,ipady=5)
                j+=1
            self.Entries=["subject name","subject marks"]
            j=1
            for i in self.Entries:
                entry=Entry(self.UpdateWorkingFramesList[1],relief=SUNKEN,bd=3,width=15)
                entry.grid(row=j,column=1,padx=5,pady=5)
                self.Entries[j-1]=entry
                j+=1
            self.statusvalue= BooleanVar()
            self.labstatus=Checkbutton(self.UpdateWorkingFramesList[1],text="Lab Status",font=("Arial", 12),width=10,bg="lightgrey",variable=self.statusvalue,onvalue=True,offvalue=False)
            self.labstatus.grid(row=3,column=0,pady=5,padx=5,ipadx=5,ipady=5)
            self.nextButton=Button(self.UpdateWorkingFramesList[1],text="Next->>",width=10,command=self.CheckSubject)
            self.nextButton.grid(row=3,column=1,padx=5,pady=5)
    
    def CheckSubject(self):
        signal=True
        if(self.Entries[0].get().strip()=="" or self.Entries[1].get().strip()==""):
            self.UpdateMessageLabel["text"]="Data should not be Empty"
            signal=False
        elif(self.Entries[1].get().strip().isalpha()):
            self.UpdateMessageLabel["text"]=" Subjects Marks should be Numerical"
            signal=False
        elif(self.statusvalue.get()==True and int(self.Entries[1].get())>20):
            self.UpdateMessageLabel["text"]="Lab Subject Doesnot Allow greter than 20"
            signal=False
        elif(self.statusvalue.get()==False and int(self.Entries[1].get())>25):
            self.UpdateMessageLabel["text"]="Subject Doesnot Allow greter than 25"
            signal=False
        if(signal):
            self.currentcount-=1
            self.UpdateMessageLabel["text"]="Enter "+str(self.currentcount)+" more subjects"
            self.SubjectsList.append(self.Entries[0].get().strip().upper())
            self.MarksList.append(int(self.Entries[1].get()))
            self.labStatusList.append(self.statusvalue.get())
            self.Entries[0].delete(0,"end")
            self.Entries[1].delete(0,"end")
            if(self.currentcount==0):
                self.nextButton["state"]="disabled"
                self.UpdateMessageLabel["text"]="click on Save to Send Message"
                Student=""
                for i in self.App.StudentsList:
                    if(i.RegdNumber==self.StudentRegdOptoinValue.get()):
                        Student=i
                self.SubmitButton=Button(self.UpdateWorkingFramesList[1],text="Submit",width=10,command=lambda : self.SubmitCall(Student),font=("Arial", 12))
                self.SubmitButton.grid(row=4,column=2,padx=5,pady=5,ipady=5,ipadx=5)

    def SubmitCall(self,Student):
        self.SubmitButton["state"]="disabled"
        print("Sujects : ",self.SubjectsList)
        print("Marks : ",self.MarksList)
        print("Lab status value",self.labStatusList)
        Message="Your Ward, "+Student.StudentName+"'s Internals Marks Are Finalized as below\n"
        for i in range(len(self.SubjectsList)):
            if(self.labStatusList[i]==False):
                Message+=self.SubjectsList[i]+" : "+str(self.MarksList[i])+"/25"+"\n"
                if(self.MarksList[i]<16):
                    Message+="And need to Score "+str(16-self.MarksList[i]+24)+" in External Examinations to get pass in "+self.SubjectsList[i]+"\n"
                else:
                    Message+="And need to Score "+str(24)+" in External Examinations to get pass in "+self.SubjectsList[i]+"\n"
            else:
                Message+=self.SubjectsList[i]+" : "+str(self.MarksList[i])+"/20"+"\n"
                if(self.MarksList[i]<8):
                    Message+="And need to Score "+str(8-self.MarksList[i]+12)+" in External Examinations to get pass in "+self.SubjectsList[i]+"\n"
                else:
                    Message+="And need to Score "+str(12)+" in External Examinations to get pass in "+self.SubjectsList[i]+"\n"
        person=Client(account_sid,auth_token)
        sms= person.messages.create(from_="+14158253280",body=Message,to="+91"+Student.ParentContact,)
        print(sms.sid)
  
    def ShowFrame(self,frame):
        frame.tkraise()

class DELETEBUTTON():
    def __init__(self,App):
        self.App=App
        self.BuildDeleteFrame()
    
    def BuildDeleteFrame(self):
        FrameInfo=Label(self.App.WorkingFrameslist[2],text="DELETE Module",bg="LightGrey",font=("Arial", 25))
        FrameInfo.grid(row=0,column=0,padx=5,pady=5,ipadx=5,ipady=5,columnspan=2)
        self.DeleteMessageLabel=Label(self.App.WorkingFrameslist[2],bg="lightgrey",text="",font=("Arial", 12),width=50)
        self.DeleteMessageLabel.grid(row=0,column=2,padx=5,pady=5,ipadx=5,ipady=5,columnspan=2)
        StudentRegdLabel=Label(self.App.WorkingFrameslist[2],text="Student RegdNum",width=20,bg="LightGrey",font=("Arial", 12))
        StudentRegdLabel.grid(row=1,column=0,padx=5,pady=5,ipadx=5,ipady=5)
        self.StudentRegdOptoinValue=StringVar()
        self.StudentRegdOptoinValue.set("Select Register Number")
        stdentlist=[]
        for i in self.App.StudentsList:
            stdentlist.append(i.RegdNumber)
        if(len(stdentlist)==0):
            stdentlist.append("NO DATA") 
        StudentRegdOptionMenu=OptionMenu(self.App.WorkingFrameslist[2],self.StudentRegdOptoinValue,*stdentlist)
        StudentRegdOptionMenu.config(width=25)
        StudentRegdOptionMenu.grid(row=1,column=1,padx=5,pady=5,columnspan=2)
        self.StudentDeleteButton=Button(self.App.WorkingFrameslist[2],text="Delete",width=10,command=self.Delete,font=("Arial", 12))
        self.StudentDeleteButton.grid(row=2,column=1,padx=5,pady=5)

    def Delete(self):
        signal=True
        if(self.StudentRegdOptoinValue.get()=="Select Register Number"):
            self.DeleteMessageLabel["text"]="Select the Student number"
            signal=False
        elif(self.StudentRegdOptoinValue.get()=="NO DATA"):
            self.DeleteMessageLabel["text"]="No Students are available to Delete"
            signal=False
        if(signal):
            for i in range(len(self.App.StudentsList)):
                if(self.App.StudentsList[i].RegdNumber==self.StudentRegdOptoinValue.get()):
                    self.DeleteMessageLabel["text"]="Register Number with "+self.StudentRegdOptoinValue.get()+" is Sucessfully Deleted\nClick on Delete Button to delete anothor Student"
                    self.App.StudentsList.remove(self.App.StudentsList[i])
                    self.App.ModifyData()
                    self.UpdateWidgets()
                    break

class APPLICATION:
    def __init__(self):
        #required Data
        self.StudentsList=[]
        #Data Manipulation
        self.RetrieveData()
        self.ModifyData()
        #methods and members
        self.BuildMenuFrame()
        self.MakeWorkingFrame()
        self.MakeSubFramesOfWorkingFrame()
        self.MakeMenuButtons()
        #making Button attributes
        self.New=NEWBUTTON(self)
        self.Update=UPDATEBUTTON(self)
        self.Delete=DELETEBUTTON(self)
        print()
        for i in self.StudentsList:
            print(i.StudentName)
            print(i.AttendedSessionsList)
            print(i.TotalSessionsList)
            print("#########")

    def RetrieveData(self):
        try:
            StudentFile=open("StudentsData.pickle","rb")
            self.StudentsList=pickle.load(StudentFile)
            StudentFile.close()
        except:
            print("hai")

    def ModifyData(self):
        StudentFile=open("StudentsData.pickle","wb")
        pickle.dump(self.StudentsList,StudentFile)
        StudentFile.close()
        print("called")
    
    def BuildMenuFrame(self):
        self.MenuFrame=Frame(MainWindow,bg="lightblue",bd=3,relief=GROOVE)
        self.MenuFrame.pack(side=TOP,expand=False,fill=BOTH)

    def MakeWorkingFrame(self):
        self.WorkingFrame=Frame(MainWindow,bg="lightgreen",bd=3,relief=GROOVE)
        self.WorkingFrame.pack(side=TOP,expand=True,fill=BOTH)

    def MakeSubFramesOfWorkingFrame(self):
        self.WorkingFrameslist=["NEW","UPDATE","DELETE"]
        colors=["lightgrey","lightgrey","lightgrey"]
        j=0
        for i in self.WorkingFrameslist:
            i=Frame(self.WorkingFrame,bg=colors[j],bd=3,relief=GROOVE,width=1200,height=600)
            i.grid(row=0,column=0,padx=15,pady=15,ipadx=5,ipady=5)
            i.grid_propagate(0)
            i.pack_propagate(0)
            self.WorkingFrameslist[j]=i
            j+=1
        self.WorkingFrameslist[0].tkraise()
        self.title=Label(self.WorkingFrame,text="Parent Intimation System",bg="lightgreen",font=("Arial", 45))
        self.title.grid(sticky=S)
        
    def MakeMenuButtons(self):
        self.NewButton=Button(self.MenuFrame,text="NEW",width=10,relief=RAISED,command= lambda : self.showframe(self.WorkingFrameslist[0],0),font=("Arial", 10))
        self.NewButton.grid(row=0,column=0,padx=5,pady=5,ipadx=5,ipady=5)
        self.UpdateButton=Button(self.MenuFrame,text="UPDATE",width=10,relief=RAISED,command= lambda : self.showframe(self.WorkingFrameslist[1],1),font=("Arial", 10))
        self.UpdateButton.grid(row=0,column=1,padx=5,pady=5,ipadx=5,ipady=5)
        self.DeleteButton=Button(self.MenuFrame,text="DELETE",width=10,relief=RAISED,command= lambda : self.showframe(self.WorkingFrameslist[2],2),font=("Arial", 10))
        self.DeleteButton.grid(row=0,column=2,padx=5,pady=5,ipadx=5,ipady=5)

    def UpdateWidgets(self):
        for widget in self.WorkingFrameslist[1].winfo_children():
            widget.destroy()
        self.Update.BuildUpdateframe()
        for widget in self.WorkingFrameslist[2].winfo_children():
            widget.destroy()
        self.Delete.BuildDeleteFrame()

    def showframe(self,frame,index):
        if(index==0):
            for widget in frame.winfo_children():
                widget.destroy()
            self.New.BuildNewframe()
        if(index==1):
            for widget in frame.winfo_children():
                widget.destroy()
            self.Update.BuildUpdateframe()
        if(index==2):
            for widget in frame.winfo_children():
                widget.destroy()
            self.Delete.BuildDeleteFrame()
        frame.tkraise()

#window creation
MainWindow=Tk()
APP=APPLICATION()
MainWindow.title("Parent Intimation System")
MainWindow.mainloop()