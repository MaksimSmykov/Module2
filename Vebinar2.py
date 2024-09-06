# Картотека сотрудников (список сотрудников)
employees = [
    {"name": "Валерий", "position": "Менеджер", "department": "Продажи"},
    {"name": "Олег", "position": "Менеджер", "department": "Продажи"},
    {"name": "Ольга", "position": "Разработчик", "department": "ИТ"},
    {"name": "Владислав", "position": "Менеджер", "department": "Продажи"},
    {"name": "Владимир", "position": "Разработчик", "department": "ИТ"},
    {"name": "Анна", "position": "Бухгалтер", "department": "Финансы"},
]


def find_name(name):
    '''Функция для поиска сотрудника в картотеке'''
    for emp in employees:
        if emp["name"].lower() == name.lower():
            return emp
    return None


def filtred_emp(position):
    '''Функция фильтрует по должности и распечатывает сотрудника'''
    filter_emp = []
    for emp in employees:
        if emp["position"].lower() == position.lower():
            filter_emp.append(emp)
    return filter_emp


def add_emp(name, position, department):
    new_emp = {"name": name.capitalize(), "position": position.capitalize(), "department": department.capitalize()}
    employees.append(new_emp)
    return new_emp


def delete_emp(name, position, department):
    del_emp = {"name": name.capitalize(), "position": position.capitalize(), "department": department.capitalize()}
    for emp in employees:
        if (del_emp["name"].lower() == emp["name"].lower()
                and del_emp["position"].lower() == emp["position"].lower()
                and del_emp["department"].lower() == emp["department"].lower()):
            employees.remove(emp)
            return del_emp
    return None


def printing_emp_list():
    print(f'\nСписок сотрудников:')
    for emp in employees:
        print(emp)


def main():
    while True:
        print(f'\nMenu')
        print(f'1. Поиск сотрудника по имени')
        print(f'2. Фильтровать сотрудников по должности')
        print(f'3. Добавить нового сотрудника')
        print(f'4. Удалить сотрудника')
        print(f'5. Показать список сотрудников')
        print(f'6. Выход из программы\n')
        choice = input('Введите  пункт меню: ')

        if choice == '1':
            name = input('Введите имя сотрудника: ')
            employee = find_name(name)
            if employee:
                print(f'\nСотрудник: {employee["name"]}\n'
                      f'Должность: {employee["position"]}\n'
                      f'Работает в отделе: {employee["department"]}')
            else:
                print('Сотрудник не найден')

        elif choice == '2':
            position = input('Введите должность: ')
            filtered_emp = filtred_emp(position)
            if filtered_emp:
                print('\nСотрудники с данной должностью:')
                for emp in filtered_emp:
                    print(f'Имя: {emp["name"]}, Отдел: {emp["department"]}')
            else:
                print(f'Сотрудников с такой должностью нет')

        elif choice == '3':
            new_name = input('\nВведите имя нового сотрудника: ')
            new_position = input('Введите должность нового сотрудника: ')
            new_department = input('Введите отдел нового сотрудника: ')
            new_emp_dict = add_emp(new_name, new_position, new_department)
            if new_name and new_position and new_department:
                print(f'\nНовый сотрудник: {new_emp_dict["name"]} зачислен в отдел: {new_emp_dict["department"]} '
                      f'на должность: {new_emp_dict["position"]}\n')
            else:
                print('\nВведены не все данные')

        elif choice == '4':
            del_name = input('\nВведите имя увольняемого сотрудника: ')
            del_position = input('Введите должность увольняемого сотрудника: ')
            del_department = input('Введите отдел увольняемого сотрудника: ')
            if del_name and del_position and del_department:
                for emp in employees:
                    if (del_name.lower() == emp['name'].lower() and
                            del_position.lower() == emp['position'].lower() and
                            del_department.lower() == emp['department'].lower()):
                        del_emp_dict = delete_emp(del_name, del_position, del_department)
                        print(
                            f'\nСотрудник по имени: {del_emp_dict["name"]} уволен из отдела: {del_emp_dict["department"]} '
                            f'с должности: {del_emp_dict["position"]}\n')
                    else:
                        print('\nДанные введены с ошибками! Такого сотрудника нет.')
                        break
            else:
                print('\nВведены не все данные')

        elif choice == '5':
            printing_emp_list()

        elif choice == '6':
            print('EXIT')
            break


if __name__ == "__main__":
    main()
