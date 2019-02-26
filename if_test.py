"""
    根据人体BMI指数来衡量胖瘦程度以及人体健康程度
    过轻：低于18.5
    正常：18.5-23.9
    过重：24-27
    肥胖：28-32
    非常肥胖, 高于32
"""

while True:
    weight = float(input("请输入你的体重(kg):"))
    height = float(input("请输入你的身高(m):"))
    BMI = weight / height ** 2

    if BMI < 18.5:
        print("你的BMI指数是:",BMI,"你得多吃点了，老铁")
    elif 18.5 <= BMI <= 23.9:
        print("你的BMI指数是:",BMI,"你很健康，继续保持吧")
    elif 24 <= BMI <= 27:
        print("你的BMI指数是:",BMI,"你该控制一下体重了")
    elif 28 <= BMI <= 32:
        print("你的BMI指数是:",BMI,"你有点偏重了")
    else:
        print("你的BMI指数是:",BMI,"你该减肥了")