def create_muti_data():
    data = [(("wu12345wu" + str(x)), "zhangsan1", "138%08d" % x) for x in range(2)]
    return data