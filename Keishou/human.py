class Human:
    def __init__(self, name:str='匿名さん', age:int=0) -> None:
        self.name:str = name
        self.age:int = age

    def introduce(self) -> None:
        msg:str = f'\n私の名前は{self.name}です\n年齢は{self.age}歳です'
        print(msg)

class Student(Human):
    last_st_num = 0
    def __init__(self, name:str = '匿名さん', age:int = 0) -> None:
        super().__init__(name, age)
        Student.last_st_num += 1
        self.number:int = Student.last_st_num

    def introduce(self) -> None:
        super().introduce()
        msg:str = f'出席番号{Student.last_st_num}番です'
        print(msg)