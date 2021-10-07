# 使用者輸入攝氏溫度，程式轉換為華氏溫度

c_temp = input("請輸入溫度：")
c_temp = int(c_temp)
f_temp = c_temp * 9/5 +32
print("華氏溫度為", f_temp)