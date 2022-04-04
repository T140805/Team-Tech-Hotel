
name= input("Mời quý khách nhập Họ và tên: ")
age= input("Mời quý khách nhập Tuổi: ")
CMND= input("Mời quý khách nhập Số CMND: ")
class Person:
  def __init__(self, name, age, CMND):
    self.name = name
    self.age = age
    self.CMND = CMND

p1 = Person(name, age, CMND)

rentdate= input("Mời quý khách nhập Số Ngày Thuê: ")
roomtype= input("Mời quý khách nhập Loại Phòng: ")

class Hotel:
  def __init__(hotel, rentdate, roomtype, p1):
    hotel.rentdate = rentdate
    hotel.roomtype = roomtype
    hotel.p1 = p1

h1 = Hotel(rentdate, roomtype, p1)

print("Vui lòng kiểm tra thông tin cá nhân")
print(p1.name)
print(p1.age)
print(p1.CMND)
print("Vui lòng kiểm tra thông tin đặt phòng")
print(h1.rentdate)
print(h1.roomtype)
print("Chúc một ngày tốt lành! Xin cảm ơn.")
