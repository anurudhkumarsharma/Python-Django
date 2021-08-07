import re
myno='my phone number is 6306188799'
text=re.search(r'\d{10}',myno)
print(text.group())