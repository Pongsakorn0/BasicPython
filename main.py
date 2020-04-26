
# from number import factorial, fibonacci  # import มาบาง Function
# import number  # import ทั้งหมดทุก Function ใน Module
# from number import *  # import ทั้งหมดทุก Function ใน Module

# call เรียกใช้งาน Function จากไฟล์ number.py ทุก Function
# print(number.factorial(5))
# print(number.fibonacci(100))


# import และเปลี่ยนชื่อ Function (นามแผง = alias)
from number import factorial as fa, fibonacci as fi
# ----------------------------------------------------------------------

print(fa(5))
print(fi(100))
