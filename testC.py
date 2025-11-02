food = [
    ("pho", 10),
("shusi", 9),
    ("hotdog", 6)
]
print(f"Chung toi dang lam mot list ve cac mon an tren khap the gioi, va hien tai chung toi da lam duoc tung nay mon an: {food}")
print("list tren duoc tao ra de danh gia ve cac mon an tren thang diem 10")
print("Vi vay ban co the giup chung toi danh gia cac mon an ma ban tung an!")
food_name = input("Ten mon ma bon an tuong nhat la:")
rate_food =int(input("Ban danh gia mon nay bao nhieu tren 10 diem: "))
ur_food = (food_name, rate_food)
food.append((ur_food))
print(food)
print("Cam on ban da gop y kien cua minh vao list!")
