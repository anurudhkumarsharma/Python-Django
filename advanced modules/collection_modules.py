from collections import Counter
mylist = [1,1,1,1,5,5,5,9,9,9,9,9,9,4,4,4,4,'a','a','c','d','e','']
r=Counter(mylist)
print(r)


#and also 

r=Counter('assaaahsdhkjsdjdddddddkkkkkkkkkkkkkkk')
print(r.most_common(2))


#and 

para="A paragraph is a series of related sentences developing a central idea, called the topic. Try to think about paragraphs in terms of thematic unity: a paragraph is a sentence or a group of sentences that supports one central, unified idea."
r=Counter(para.split())
print(r)


