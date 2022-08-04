'''
Создать информационную систему позволяющую работать с сотрудниками
некой компании \ студентами вуза \ учениками школы
'''
database = {}
db = {'parents': 1, 'children': 2, 'position': 3, 'salary': 4}


def reading_file_to_dict(number_file):
    with open(f'{number_file}.txt', 'r', encoding='utf-8') as file_1:
        data = [i.split('\n')[0] for i in file_1.readlines()]
        print(*data)
        print()
        database[number_file] = []
        for i in data:
            database[number_file].append(tuple(i.split(';')))


def print_children(second_name):
    id = [i[0] for i in database[db['parents']] if second_name in i][0]
    deti = [i for i in database[db['children']] if id == i[1]]
    print(f'{second_name} child(ren):',*[' '.join(i[2:4]) + '\n' for i in deti])


def print_position(pos):
    id = [i[0] for i in database[db['parents']] if pos in i][0]
    position = [i for i in database[db['position']] if id == i[0]]
    print(f'{pos} position:',*[' '.join(i[1:]) + '\n' for i in position])


def print_salary(name):
    id = [i[0] for i in database[db['parents']] if name in i][0]
    slry = [i for i in database[db['salary']] if id == i[0]]
    print(f'{name} salary:',*[' '.join(i[1:]) + '\n' for i in slry])


reading_file_to_dict(1)
reading_file_to_dict(2)
reading_file_to_dict(3)
reading_file_to_dict(4)
print(database)
print()
print_children('Ivanov')
print_children('Petrov')
print_position('Petrov')
print_position('Pupkin')
print_salary('Pupkin')