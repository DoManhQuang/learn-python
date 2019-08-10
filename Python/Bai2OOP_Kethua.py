def Bai2Kethua():
	class Nhanvien:
		aCount = 1
		def InputNV(self, idNumber, aName , phoneNumber):
			self.id = Nhanvien.aCount
			Nhanvien.aCount +=1
			self.idNumber = idNumber
			self.aName = aName
			self.phoneNumber = phoneNumber
		def OutputNV(self):
			print("STT : ",self.id , "| ID Number : ",self.idNumber , "| Name : ",self.aName , "| Telephone : ",self.phoneNumber)

	class NhanvienParttime(Nhanvien):
		def Timework(self ,aTime):
			self.aTime = aTime
			self.tienLuong = aTime * 20000
		def OutputPT(self):
			print("| Time : ",self.aTime, "| Tien Luong : ",self.tienLuong)

	Nvpt1 = NhanvienParttime()
	Nvpt1.InputNV("123","Quang","191")
	Nvpt1.Timework(9)
	Nvpt1.OutputNV()
	Nvpt1.OutputPT()

Bai2Kethua()
