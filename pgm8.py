'''program to create list with two tuples'''
tuple_a = ('Apple', 'strawbwerry', 'mango', 'watermelon')
tuple_b = ('carrot', 'Brinjal', 'onion', 'chilli')
my_list = list(zip(tuple_a,tuple_b))

for val in range(len(my_list)):
	print (my_list[val])