number = (1, 2, 3, 4, 5)
mixed = (10, 20, [5, 4, 3], True, "NOTE")
print(mixed[2])  # ผล = [5, 4, 3]
print(mixed[2][1])  # ผล = 4

# ลองเปลี่ยนแปลง ค่า สมาชิก
number[2] = 10
print(number)

