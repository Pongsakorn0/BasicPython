print("-----------------------------------")
print("#Sunnation Program")
print("# Type 'exit' to end the program")
print("-----------------------------------")
print
# ตัวแปรไว้เก็บผลรวม
sumdata = 0
count = 1

while True:
    data = input(f"Enter Number {count}:")
# ตรวจข้อความ data = "Exit" หรือไม่
    if data == "exit":
        break

# การหาผลรวม  +=  บวกแบบสะสมค่า
    sumdata += int(data)
    count = count + 1
print(f"sumdata = {sumdata}")
