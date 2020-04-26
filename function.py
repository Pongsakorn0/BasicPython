
def hello(name):  # สร้าง Function แบบไม่มีการ รีเทิน
    print(f"Hello {name}")


hello('Note')  # การ Call เรียกใช้ Function


def area(width, height):  # สร้าง Function แบบมีการ รีเทิน Value
    total = width*height
    return total


print("พื้นที่เท่ากับ =", area(5, 8))  # Area = 40

# Function ที่มีค่า เริ่มต้น


def show_info(name="", Salary=0.00, lang="not define"):
    print(f"NAME : {name}")
    print(f"SALARY : {Salary}")
    print(f"LANG : {lang}")


# เรียกใช้งาน show_info()
show_info()
print()
show_info("Pongsakorn", 15000, "PHP")
