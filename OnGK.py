#Tạo class Thíinh
class ThiSinh:
    def __init__(self, MaTS, HoTen, NamSinh, Toan, Van, Anh):
        self.MaTS = MaTS
        self.HoTen = HoTen
        self.NamSinh = NamSinh
        self.Toan = Toan
        self.Van = Van
        self.Anh = Anh

    def get_MaTS(self):
        return self.MaTS
    
    def get_HoTen(self):
        return self.HoTen

    def get_NamSinh(self):
        return self.NamSinh

    def get_Toan(self):
        return self.Toan

    def get_Van(self):
        return self.Van

    def get_Anh(self):
        return self.Anh
    
    #Show thông tin thí sinh
    def show_info(self):
        print('****************************************')
        print(f"Mã của thí sinh: {self.get_MaTS()}")
        print(f"Họ tên: {self.get_HoTen()}")
        print(f"Năm sinh: {self.get_NamSinh()}")
        print(f"Điểm toán: {self.get_Toan()}")
        print(f"Diểm văn: {self.get_Van()}")
        print(f"Điểm Anh: {self.get_Anh()}")
        

lt = []
while True :
    print(''' 
    MỜI CHỌN CHỨC NĂNG
    1. Thêm thí sinh
    2. Xem danh sách các thí sinh
    3. Xem thí sinh có điểm toán cao nhất 
    4. Xem danh sách thí sinh theo tổng điểm giảm dần
    5. Thoát chương trình''')
    selection = int(input('Nhập vào một số : '))
    dem = 0
    
    #Thoát chương trình
    if selection == 5:
        print('Bạn đã thoát chương trình!!!')
        break
    #Thêm thí sinh
    elif selection == 1:
        MaTS = int(input('Nhập mã thí sinh: '))
        HoTen = input('Nhập tên thí sinh: ')
        NamSinh = int(input('Nhập năm sinh: '))
        Toan = int(input('Nhập điểm toán: '))
        Van = int(input('Nhập điểm văn: '))
        Anh = int(input('Nhập điểm anh: '))

        sinhvien = ThiSinh(MaTS, HoTen, NamSinh, Toan, Van, Anh)

        lt.append(sinhvien)
        dem +=1
    
    #Danh sách thí sinh
    elif selection == 2:
        if len(lt) == 0:
            print("Hiện có 0 Thí sinh")
        else:
            print(f"Hiện có {len(lt)} Thí sinh")
            for i in lt:
                i.show_info()
            print('************************************')

    #Thí sinh có điểm toán cao nhất
    elif selection == 3:
        maxmath = 0
        a = len(lt)
        for i in range(a):
            if lt[i].Toan > maxmath:
                maxmath = lt[i].Toan
                ts_maxmath = i
        print(lt[ts_maxmath])

    #Danh sách thí sinh giảm dần theo tổng điểm
    elif selection == 4:
        for i in range(a-1):
            for j in range(i + 1, a):
                if lt[i] < lt[j]:
                    lt[i], lt[j] = lt[j], lt[i]