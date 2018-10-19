def camel_to_snake_case(src):

    glue = ' '

    result = ''.join(glue + x if x.isupper() else x for x in src).strip(glue).split(glue)

    word_list=[]

    for word in range(len(result)):
        word = result[word]
        upper_to_lower = word.lower()
        word_list.append(upper_to_lower)
    
    
        snake_case = "_".join(word_list)

    return snake_case

def main():
    src = input('Please enter in a camelCase word eg - PythonProgrammingFall2018: ')
    print(camel_to_snake_case(src))    

main()




# def camel_to_snake_case(src):

#     glue = ' '

#     result = ''.join(glue + x if x.isupper() else x for x in src).strip(glue).split(glue)

#     word_list=[]

#     for word in range(len(result)):
#         word = result[word]
#         upper_to_lower = word.lower()
#         word_list.append(upper_to_lower)
    
    
#         snake_case = "_".join(word_list)

#     return snake_case

# def main():
#     src = 'TheLongAndWindingRoad'
#     print(camel_to_snake_case(src))    

# main()