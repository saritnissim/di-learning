# Exercise 1 : Family
class Family:
    def __init__(self, last_name):
        self.members = [
        {'name':'Michael','age':35,'gender':'Male','is_child':False},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False}
        ]
        self.last_name = last_name

    def born(self,**kwargs):
        self.members.append(kwargs)
        child_name = kwargs['name']
        print(f"Congratulations! {child_name} has been born into the {self.last_name} family.")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print(f"Family Name: {self.last_name}")
        print(f"Family Members: {', '.join(member['name'] for member in self.members)}")

# Exercise 2 : TheIncredibles Family
class TheIncredibles(Family):
    
    def __init__(self, last_name):
        super().__init__(last_name)
        self.members = [
            {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
            {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
        ]
    
    def use_power(self):
        for member in self.members:
            if self.is_18(member["name"]):
                print(f'{member["power"]}')
            else:
                raise Exception(f"{member['name']} is not over 18 years old.")


    def incredible_presentation(self):
        super().family_presentation()
        incredibles = [x for x in self.members if 'power' in x]        
        names = list(map(lambda x: f"{x['name']} : {x['power']}", incredibles ))
        print(names)

incredible_family = TheIncredibles("The Incredibles")
incredible_family.incredible_presentation()
incredible_family.born(name='Jack', gender='Male', power='Unknown Power', incredible_name='Baby Jack')
incredible_family.incredible_presentation()