


#Khởi tạo class
class Students:
    aCount = 1 # Bien dung chung static
    def Inputstu(self, idNumber , aName , aClass):
        self.id = Students.aCount
        Students.aCount +=1
        self.idNumber = idNumber
        self.aName = aName
        self.aClass = aClass
    def  Outputstu(self):
         print("STT : ",self.id*2, "| ID Number : ",self.idNumber*2 , "| Name : ",self.aName , "| Class ", self.aClass)


stu2 = Students()
stu2.Inputstu(4,"Manh Quang1","HTTT")
stu2.Outputstu()
