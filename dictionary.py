score = {
    "John": 1200,
    "bobby": 2000,
    "Janny": 4200
}

print(score)  # ผล = {'John': 1200, 'bobby': 2000, 'Janny': 4200}
print(score["John"])  # ผล = 1200

# เพิ่มค่าใหม่ เข้าไป

score["Pang"] = 5000
print(score)  # ผล = {'John': 1200, 'bobby': 2000, 'Janny': 4200, 'Pang': 5000}

# การสร้าง Dictionary ว่าง
# points = {}

# kk = input("key = ")
# vv = input("value =")
# points[str(kk)] = vv
# print(points)  # {'team': 'liverpool'}

# การ Loop อ่านสมาชิกของ Dictionary ออกมา
# ตัวแปร k,v  มาเก็บจากตัวแปรก Score
# .item จะได้ทั้ง key+Value
# .key จะได้ key
for k, v in score.items():
    print(k, v)  # John 1200 bobby 2000  Janny 4200  Pang 5000

for k in score.keys():
    print(k)  # John  bobby Janny Pang

for v in score.values():
    print(v)  # 1200 2000 4200 5000
