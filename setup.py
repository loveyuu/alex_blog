print("program start.....")

class Student(object):
    def __init__(self, name):
        self.name = name

if __name__ == "__main__":
    stu = Student("linbin")
    print(stu.name)

