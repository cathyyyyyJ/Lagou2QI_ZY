import yaml
from pythoncode2.main import cat, dog

if __name__ == "__main__":
    print("----------")
    cat1 = cat("小猫","白蓝色","2个月","女","短毛")
    print(f"猫猫的姓名：{cat1.name},颜色：{cat1.color},年龄：{cat1.age},性别：{cat1.sex},毛发：{cat1.hair}")
    cat1.catch()
    print("----------")
    dog1 = dog("小狗","白色","3个月","男","短毛")
    print(f"狗狗的姓名：{dog1.name},颜色：{dog1.color},年龄：{dog1.age},性别：{dog1.sex},毛发：{dog1.hair}")
    dog1.watch()
    print("----------")

    with open("animal.yaml", encoding="utf-8") as f:
        datas=yaml.safe_load(f)
        cat2 = cat(datas["猫猫"]['name'], datas["猫猫"]['color'], datas["猫猫"]['age'], datas["猫猫"]['sex'])
        print(f"猫猫的姓名：{cat2.name},颜色：{cat2.color},年龄：{cat2.age},性别：{cat2.sex},毛发：{cat2.hair}")
        print("----------")
        dog2 = dog(datas["狗狗"]['name'], datas["狗狗"]['color'], datas["狗狗"]['age'], datas["狗狗"]['sex'])
        print(f"狗狗的姓名：{dog2.name},颜色：{dog2.color},年龄：{dog2.age},性别：{dog2.sex},毛发：{dog2.hair}")
        print("----------")





