import temp

class Profile():
    
    def method1(self):
        print("method1")
    
    def method2(self):
        print("method2")
    
    @classmethod    
    def get_object(cls)-> temp.User:
        return cls.__new__(cls)