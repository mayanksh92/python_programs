l2 = []
def flatten(l1):
    for i in l1:
        if type(i) is list:
            flatten(i)
        else:
            l2.append(i)

l1 = [1,2,3,[10,20,30,[100,200,300,[1000,2000,3000]], 40,50]]
flatten(l1)
print(l2)
