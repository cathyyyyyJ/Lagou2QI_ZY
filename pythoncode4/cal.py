class calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add_ca(self):
        return self.a + self.b
    def sub_ca(self):
        return self.a - self.b
    def mul_ca(self):
        return self.a * self.b
    def div_ca(self):
         if self.b==0:
             return 0
         else:
             return self.a / self.b