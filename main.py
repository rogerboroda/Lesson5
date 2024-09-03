immutable_var = ('vodka', 'herring', [3, 2, 1])
print(immutable_var)
#immutable_var[1] = 5
immutable_var[2][2] = 5
print(immutable_var)
mutable_list = ['vodka','beer']
print(mutable_list)
mutable_list[0] = 'coffee'
mutable_list[1] = 'croissant'
print(mutable_list)
mutable_list.append('interlocutor')
print(mutable_list)
mutable_list.remove('croissant')
print(mutable_list)