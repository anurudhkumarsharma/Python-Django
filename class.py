class Rajat():
    print("\n"*10)
    def __init__(self,name,hair_color,height,married):
        self.name=name
        self.hair_color=hair_color
        self.height=height
        self.married=married
my_details=Rajat(name='rajat',hair_color='black',height="5'6",married=True)
print('My name is:       ',my_details.name)
print('My hairs color is:',my_details.hair_color)
print('My height is:     ',my_details.height)
print('Am i married?\n',my_details.married)

        
