# import function as func
# func.PowerInt(30)

def PowerInt(max,num = 2):
    res = num
    while res <= max:
        print(res)
        res = res * num

try:
    num = int(input("Введите число для возведения в степень: "))
    max = int(input("Введите число N (предел степени):" ))
    PowerInt(max,num)
except:
    print("По условиям задачи требуется число")