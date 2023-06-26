def find_common_elemets(ls1, ls2):
    common_elements = []
    for element in ls1:
        if element in ls2 :
            common_elements.append(element)

    return common_elements



ls1 = [1, 2, 3,'hello', 45, 62 ]
ls2 = [1, 7, 8,'hello', 19, 62 ]
result = find_common_elemets(ls1, ls2)
print(result) 

# [1, 'hello', 62]