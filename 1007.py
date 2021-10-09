# # 使用者輸入攝氏溫度，程式轉換為華氏溫度

# c_temp = input("請輸入溫度：")
# c_temp = int(c_temp)
# f_temp = c_temp * 9/5 +32
# print("華氏溫度為", f_temp)

# # input、casting、 if else

# age = input("請輸入年齡： ")
# age = int(age)

# if age >= 18:
#     print("可以投票")
# else:
#     print("不能投票")

# # else if
# age = input("請輸入年紀： ")
# age = int(age)
# if age < 13:
#     print('去國小')
# elif age >= 13 and age < 17:
#     print("去國中")
# elif age >= 17 and age < 22:
#     print("去大學")
# else:
#     print("去出社會")

# # loop
# # while loop 什麼時後要用到while loop

# x = 5
# while x < 10:
#     print("is loop")
#     x += 1
#     print(x)
# print('出來了')

# # while True

# y = 10
# while True:
#     print('無限')
#     y += 1
#     if y > 15:
#         break
# print('我出來了')

# while True:
#     main = input('請輸入模式: ')
#     if main == "q":
#         break
#     elif main == "1":
#         print('module1')
#     elif main == '2':
#         print('module2')
#     else:
#         print('請選擇1或2')

# 密碼重試程式
# 設定密碼
# 使用者『最多』輸入三次
# 不對的話，印出"密碼錯誤，還有__次機會"
# 對的話，印出"登入成功"

# password = "cc1234"
# x = 3 # 可以試試以x當while條件
# while True:
#     password = input("請輸入密碼：")
#     if password == "cc1234":
#         print("登入成功！")
#         break
#     else:
#         x = x - 1
#         print("密碼錯誤，你還有", x, "次的機會")
#         if x == 0:
#             print("你沒有機會了")
#             break

# import

import random
num = random.randint(1, 100)
x = 5
while True:
    your_num = input("請輸入密碼: ")
    x -= 1
    your_num = int(your_num)
    if your_num == num:
        print("答對")
        break
    elif your_num < num:
        print("比答案小")
        if x < 0:
            print("是要猜多久啦")
    elif your_num > num:
        print("比答案大")
        if x < 0:
            print("啊是好了沒")