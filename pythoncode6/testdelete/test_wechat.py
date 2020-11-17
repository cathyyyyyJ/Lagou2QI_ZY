from pythoncode6.page.main_page import MainPage
dellist=[] #删除后的成员列表
implist=[]#导入后的成员列表
listname=[]#导入的excel表中的成员列表
import xlrd
class TestDel:
    def setup(self):
        self.main=MainPage()
    #删除成员#
    def test_delmember(self):
        self.main.page_goto_del().del_member(namelist=dellist) #获取删除后的成员列表#
        assert 'test22' not in dellist  #判断成员是否删除成功#
    #导入通讯录#
    def test_importmem(self):
        self.main.page_goto_imp().imp_member(namelist=implist)
        #获取excel表中的数据#
        filename=xlrd.open_workbook("E:/project/pycharm/TASK/pythoncode6/page/addressbook2.xls")
        list1=filename.sheet_by_name("成员列表")
        n1=list1.nrows
        for i in range(9,n1):
            name1=str(list1.cell(i,0))
            name2=name1.lstrip('text:').strip("'")
            print(name2)
            listname.append(name2)
        #断言 判断excel中的成员是否全部加入到通讯录中
        for i in listname:
            assert i in implist  #判断excel中的成员是否全部加入到了企业微信中#

