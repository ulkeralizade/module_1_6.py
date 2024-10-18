#dictionary
my_dict={"andrey":2001,"max":1999,"dasha":2004}
print(my_dict)
print(my_dict["andrey"])
print(my_dict.get("danya"))
my_dict.update({"masha":2005,"lera":2007})
a=my_dict.pop('masha')
print(a)
print(my_dict)
#set
my_set={5,'peach',5,'true','peach',7.7,'true',7.7}
print(my_set)
my_set.add('apple')
my_set.add('strawberry')
(my_set.discard('true'))
print(my_set)

