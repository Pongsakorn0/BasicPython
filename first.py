# print("hello Python")
# print(2+3)
# print(2**3)
# # ,end= ไว้สำหรับ ต่อข้อความ จากบรรทัดต่อไป ไม่งั้นจะขึ้นบรรทัดใหม่ เสมอ
# #rint("sss", end="")
# print("note_ZA  "*3)

# print(sum(range(1, 10)))  # rang ไม่เอาตัวท้ายไปนับ มีแค่ 1-9
# print("\t pongsakorn")   # \t = ย่อหน้า
# print("This is = "+"Saturday")
# print("This is = ", "Saturday")  # , เชื่อม ข้อความ และเว้นวรรค

# ---------------------------- ตัวแปร มาใส่ในข้อความ -------------------------------
a = 3
b = 15.50
# วิธีที่ 1
print("ราคาขายต่อชิ้น", b)

# วิธีที่ 2
# %s ข้อความ
# %d  จำนวนเต็ม
# %f  ทศนิยม   .2 = ทศนิยม 2 ตำแหน่ง
print("ราคาขายต่อชิ้น %.2f บาท จำนวน %d ชิ้น " %
      (b, a))  # เอาตัวแปร b เข้าไปใน %f

# วิธีที่ 3 ใส่ f ข้างหน้าข้อความ ใส่ ตัวแปร ไว้ใน {}
print(f"ราคาขายต่อชิ้น {b} บาท จำนวน {a} ชิ้น")

print("สวัสดีไพทอน")
