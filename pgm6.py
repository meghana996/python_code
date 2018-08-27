'''list with 5 branches'''
sois=['ewt','emb','vlsi']


sois.append('vir')
sois.insert(3,'big data')


print("Here is the list after sorting:")
for student in sorted(sois):
    print(student.title())

print("here is the list after reverse sorting")
for student in sorted(sois, reverse=True):
    print(student.title())