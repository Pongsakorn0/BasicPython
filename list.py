# การสร้างข้อมูลแบบ List
number = [1, 2]
name = ["john", "Note", "Pang"]
mixed = [10, 25.75, True, "Samit"]

# การเข้าถึงสมาชิกใน List
print(number[0])  # ผลลัพท์ ได้ 1
print(name[1])  # ผลลัพท์ ได้ Note
print(name[1], name[2])  # ผลลัพท์ ได้ Note Pang
print(mixed[1], mixed[2], mixed[3])  # ผลลัพท์ ได้  25.75 True Samit

# การนับจำนวนสมาชิกใน list
# len คือการนับ
# ผลลัพท์ ได้  สมาชิกทั้งหมดของ list =  4
print("สมาชิกทั้งหมดของ list = ", len(mixed))

# สร้าง List แบบว่าง (empty list)
data = []

# การเพิ่มสมาชิกใน list เข้าไปใน list ว่าง ใช้คำสั่ง append ในการเพิ่ม
data.append("NP")
data.append(15)
print(data)

# การอัพเดต สมาชิกใน List
data[1] = 20
print(data)

# ฟังชั่นวนลูปอ่านค่าสมาชิกทั้งหมด
# ตัวแปร n ไว้รับค่า  number คือชื่อ List
for n in number:
    print("n =", n)

# Loop แล้วหาผลรวม
sum = 0
for num in number:
    sum += num
    print(sum)
