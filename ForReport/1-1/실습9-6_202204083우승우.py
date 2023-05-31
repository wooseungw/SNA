from xml.dom.minidom import Element


mixlist = ['apple', 5, 'banana', 'grape', 3, 8, 6, 'melon'] 


for element in mixlist:
    if type(element) == str:
        print(element)
        print("type is string\n")
    else:
        print(element)
        print("type is integer\n")