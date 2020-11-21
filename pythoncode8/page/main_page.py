from pythoncode8.page.add_member import AddMember
from pythoncode8.page.base_page import BasePage
from pythoncode8.page.del_member import DelMember


class MainPage(BasePage):
    #1-添加成员#
    def page_add(self):
        return AddMember(self.driver)
    #2-删除成员#
    def page_del(self):
        return DelMember(self.driver)