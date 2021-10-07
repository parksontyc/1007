# 使用者輸入攝氏溫度，程式轉換為華氏溫度

c_temp = input("請輸入溫度：")
c_temp = int(c_temp)
f_temp = c_temp * 9/5 +32
print("華氏溫度為", f_temp)

# input、casting、 if else

age = input("請輸入年齡： ")
age = int(age)

if age >= 18:
    print("可以投票")
else:
    print("不能投票")

# else if
age = input("請輸入年紀： ")
age = int(age)
if age < 13:
    print('去國小')
elif age >= 13 and age < 17:
    print("去國中")
elif age >= 17 and age < 22:
    print("去大學")
else:
    print("去出社會")