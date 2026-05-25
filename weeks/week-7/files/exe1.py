import os

# part one 

with open ('diary.txt','w') as file:
    file.write('2024-01-15 | was very busy day\n')
    file.write('2024-01-16 | I learn about file handling in python\n')
    file.write('2024-01-17 | I complited my first exeresize\n')
print('file has created succecfuly')

# part two 

def add_entry(filename:str, date:str, content:str):
    """
    add a new line to the file with date and content

    parms:
        filename: (str) the path to the file
        date: (str) the date to add before the content
        content: (str) the content to add to the file
    

    """

    with open(filename, 'a') as file:
        file.write(date)
        file.write(f' {content} \n')

add_entry(filename='diary.txt', date= '2025-12-8', content='was tribble day')

# part 3

def search_diary(filename:str, keyword:str)->list[str]:
    """
    serch key word in a file and return list of lines with the key word.

    parms:
        filename: (str) the file path
        keyword: (str) the word or prase to search in the file 

    return:
        list: (list[str]) list of lines that the keyword appear in them
                note: in case the files dosen't exists or the key word dosent exists you'll get an empty list

    """
    lines_with_keyword = []
    if not os.path.exists(path= filename):
        return lines_with_keyword
    
    with open(filename, 'r') as file:
        for line in file:
            if keyword in line:
                lines_with_keyword.append(line.strip())

    return lines_with_keyword

print(search_diary(filename='diary.txt',keyword='day'))
