class Person:
    name = ""
    age = 0
    sex = "male"
    account_type = "new"
    tags = "aaa"

    def __init__(self, name, age, sex, account_type, tags):
        self.name = name
        self.age = age
        self.sex = sex
        self.account_type = account_type
        self.tags = tags