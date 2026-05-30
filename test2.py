class Parent():
    def test():
        print("parent instance method called")
        
class child(Parent):
    def do():
        super().test()
        

obj = child()

child.do()