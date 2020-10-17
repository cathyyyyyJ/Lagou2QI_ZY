#1、有参数
def sweetness(level):
    print(f"1、奶茶的甜度：{level}分糖")

#2、无参数
def tem():
    print(f"2、奶茶的温度：去冰")

#3、无返回值，返回 None
#4、有返回值
def demand():
    print("3、今日奶茶数量：")
    return "5杯黑糖奶茶"


if __name__ == "__main__":
    sweetness(3)
    tem()
    print(demand())



