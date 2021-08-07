import re
text = 'my name is rajat and my friends name is hagga and one more name is bihari '
match=re.findall('name',text)
print(match)
r=len(match)
print(r)

for i in re.findall('name',text):
    print('found!')
