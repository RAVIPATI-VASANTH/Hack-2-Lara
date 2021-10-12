class Student:
    def __init__(self,name,regd_num,section,parent_num,student_num):
        self.StudentName=name
        self.SectionName=section
        self.RegdNumber=regd_num
        self.ParentContact=parent_num
        self.StudentContact=student_num
        self.AttendedSessionsList=[]
        self.TotalSessionsList=[]
