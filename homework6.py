# Словарь:
my_dict={'Marina':1963, 'Magda':1994,'Polina':1988,'Aza':2014}
print(my_dict)
print(my_dict['Magda'])
print(my_dict.get('Adam'))
my_dict.update({'Ajza':2017,'Anisa':2019})
print(my_dict)
my_dict.pop('Polina')
print(my_dict)
my_dict.update({'Polina':1988})
a=my_dict.pop('Polina')
print(a)
print(my_dict)
# Множество :
my_set={1,2,2,5,5,9,'job',2.2,2.2,89,90,100,100}
print(my_set)
my_set.add('keys')
my_set.add(505)
print(my_set)
my_set.remove(505,)
my_set.remove(2.2)
print(my_set)