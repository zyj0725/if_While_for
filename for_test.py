"""
    输出小于20的质数
"""

for num in range(21):
    if num < 2:
        print("质数是大于1的自然数")
    if num >= 2:
        for x in range(2,num):
            if num % x == 0 :
                # print(num,'不是质数')
                break
        else:
            print(num,end=' ')

