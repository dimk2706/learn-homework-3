"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.
Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.
Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.
13. Вывести список отделов со средним налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]

def exercise1():
    print("1. Названия всех отделов:")
    for department in departments:
        print(department["title"])

def exercise2():
    print("2. Имена всех сотрудников компании:")
    for department in departments:
        for employer in department["employers"]:
            print(employer["first_name"])

def exercise3():
    print("3. Имена всех сотрудников с указанием отдела:")
    for department in departments:
        for employer in department["employers"]:
            name = employer["first_name"]
            department_actual =department["title"]
            print(f"{name} отдел: {department_actual}" )

def exercise4():
    print("4. Имена всех сотрудников компании, которые получают больше 100к:")
    for department in departments:
        for employer in department["employers"]:
            if employer["salary_rub"] > 100000:
                print(employer["first_name"])

def exercise5():
    print("5. Позиции, на которых люди получают меньше 80к:")
    positions = set()
    for department in departments:
        for employer in department["employers"]:
            if employer["salary_rub"] < 80000:
                positions.add(employer["position"])
    converted = '\n'.join(positions)
    print(converted)

def exercise6():
    print("6. Сколько денег в месяц уходит на каждый отдел:")
    for department in departments:
        salary_rub_sum = 0
        for employer in department["employers"]:
            salary_rub_sum += employer["salary_rub"]
        department_name = department["title"]
        print(f"Отдел: {department_name} Затраты на зарплаты в месяц: {salary_rub_sum}") 

def exercise7():
    print("7. Названия отделов с указанием минимальной зарплаты в нём:")
    for department in departments:
        salary_rub_min = department["employers"][0]["salary_rub"]
        for employer in department["employers"]:
            if employer["salary_rub"] < salary_rub_min:
                salary_rub_min = employer["salary_rub"]
        department_name = department["title"]
        print(f"Отдел: {department_name} минимальная зарплата: {salary_rub_min}") 

def exercise8():
    print("8. Названия отделов с указанием минимальной, средней и максимальной зарплаты в нём:")
    for department in departments:
        salaries = []
        for employer in department["employers"]:
            salaries.append(employer["salary_rub"])
        department_name = department["title"]
        salary_rub_min = min(salaries)
        salary_rub_max = max(salaries)
        salary_rub_average = int(sum(salaries)/len(salaries))
        print(f"Отдел: {department_name}, минимальная зарплата: {salary_rub_min}, средняя зарплата: {salary_rub_average}, максимальная зарплата: {salary_rub_max}") 


def exercise9():
    salaries = []
    for department in departments:
        for employer in department["employers"]:
            salaries.append(employer["salary_rub"])
    salary_rub_average = int(sum(salaries)/len(salaries))
    print(f"9. Средняя зарплата по компании: {salary_rub_average}") 

def exercise10():
    print("10. Позиции, на которых люди получают больше 90к:")
    positions = set()
    for department in departments:
        for employer in department["employers"]:
            if employer["salary_rub"] > 90000:
                positions.add(employer["position"])
    converted = '\n'.join(positions)
    print(converted)

def exercise11():
    print("11. Средняя зарплата по каждому отделу среди девушек:")
    female_names = ["Michelle", "Nicole", "Christina", "Caitlin"]
    for department in departments:
        salaries = []
        for employer in department["employers"]:
            if employer["first_name"] in female_names:
                salaries.append(employer["salary_rub"])
        department_name = department["title"]
        if salaries:
            salary_rub_average = int(sum(salaries)/len(salaries))
        else:
            salary_rub_average = "в данном отделе нет девушек"
        print(f"Отдел: {department_name}, средняя зарплата среди девушек: {salary_rub_average}")

def exercise12():
    print("12. Имена людей, чьи фамилии заканчиваются на гласную букву:")
    vowels = "aeiouy"
    names = set()
    for department in departments:
        for employer in department["employers"]:
            if employer["last_name"][-1] in vowels:
                names.add(employer["first_name"])
    converted = '\n'.join(names)
    print(converted)        

def exercise13():
    print("13. Список отделов со средним налогом на сотрудников этого отдела:")
    names_departments = {}
    for taxe in taxes:
        if taxe["department"]:
            name_department = taxe["department"].capitalize()
        else:
            name_department = taxe["department"]
        names_departments.update({name_department: taxe["value_percents"]})
    for department in departments:
        taxe_average = names_departments[None]
        if department["title"].capitalize() in names_departments.keys():
            name_department1 = department["title"].capitalize()
            taxe_average += names_departments[name_department1]
        salaries = []
        for employer in department["employers"]:
            salaries.append(employer["salary_rub"])
        taxe_department_average = int((sum(salaries)*taxe_average/100)/len(salaries))
        department_name = department["title"]
        print(f"Отдел {department_name}, средний налог: {taxe_department_average}")


def exercise14():
    print("14. Список всех сотрудников с указанием зарплаты на руки и зарплаты с учётом налогов:")
    names_departments = {}
    for taxe in taxes:
        if taxe["department"]:
            name_department = taxe["department"].capitalize()
        else:
            name_department = taxe["department"]
        names_departments.update({name_department: taxe["value_percents"]})
    for department in departments:
        taxe_average = names_departments[None]
        if department["title"].capitalize() in names_departments.keys():
            name_department1 = department["title"].capitalize()
            taxe_average += names_departments[name_department1]
        salary = 0
        salary_with_taxe = 0
        for employer in department["employers"]:
            salary = employer["salary_rub"]
            salary_with_taxe = salary - salary*taxe_average/100
            name = employer["first_name"]
            surname = employer["last_name"]
            print(f"Сотрудник: {name} {surname}, зарплата на руки: {salary}, зарплата с учетом налогов: {salary_with_taxe}")


def exercise15():
    print("15. Cписок отделов, отсортированный по месячной налоговой нагрузки:")
    names_departments = {}
    for taxe in taxes:
        if taxe["department"]:
            name_department = taxe["department"].capitalize()
        else:
            name_department = taxe["department"]
        names_departments.update({name_department: taxe["value_percents"]})
    taxes_and_departments = {}
    for department in departments:
        taxe_department = names_departments[None]
        if department["title"].capitalize() in names_departments.keys():
            name_department1 = department["title"].capitalize()
            taxe_department += names_departments[name_department1]
        salaries = []
        for employer in department["employers"]:
            salaries.append(employer["salary_rub"])
        taxe_department_sum = int((sum(salaries)*taxe_department/100))
        department_name = department["title"]
        taxes_and_departments.update({department_name: taxe_department_sum})
    sorted_departments = sorted(taxes_and_departments.keys(), key=lambda item: item[1])
    converted = '\n'.join(sorted_departments)
    print(converted) 


def exercise16():
    print("16. Все сотрудники, за которых компания платит больше 100к налогов в год.:")
    names_departments = {}
    for taxe in taxes:
        if taxe["department"]:
            name_department = taxe["department"].capitalize()
        else:
            name_department = taxe["department"]
        names_departments.update({name_department: taxe["value_percents"]})
    for department in departments:
        taxe_average = names_departments[None]
        if department["title"].capitalize() in names_departments.keys():
            name_department1 = department["title"].capitalize()
            taxe_average += names_departments[name_department1]
        taxe_year = 0
        for employer in department["employers"]:
            taxe_year = employer["salary_rub"]*taxe_average/100 * 12
            if taxe_year > 100000:
                print(employer["first_name"], employer["last_name"])


def exercise17():
    names_departments = {}
    for taxe in taxes:
        if taxe["department"]:
            name_department = taxe["department"].capitalize()
        else:
            name_department = taxe["department"]
        names_departments.update({name_department: taxe["value_percents"]})
    taxes_and_names_surnames = {}
    for department in departments:
        taxe_average = names_departments[None]
        if department["title"].capitalize() in names_departments.keys():
            name_department1 = department["title"].capitalize()
            taxe_average += names_departments[name_department1]
        for employer in department["employers"]:
            taxe_employer=employer["salary_rub"]*taxe_average/100
            name_surname = str(employer["first_name"]) +" " + str(employer["last_name"])
            taxes_and_names_surnames.update({name_surname: taxe_employer})
    min_employer = min(taxes_and_names_surnames.keys(), key=lambda item: item[1])
    print(f"17. Имя и фамилия сотрудника, за которого компания платит меньше всего налогов: {min_employer}")
        



if __name__ == "__main__":
    exercise1()
    exercise2()
    exercise3()
    exercise4()
    exercise5()
    exercise6()
    exercise7()
    exercise8()
    exercise9()
    exercise10()
    exercise11()
    exercise12()
    exercise13()
    exercise14()
    exercise15()
    exercise16()
    exercise17()