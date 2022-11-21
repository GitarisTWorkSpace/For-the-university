import csv
import re
from datetime import datetime
from var_dump import var_dump

class DataSet:
    def __init__(self, file_name, vacancies_objects):
        self.file_name = file_name
        self.vacancies_objects = vacancies_objects

class Vacancy:
    def __init__(self, name, description, key_skills, experience_id, premium, employer_name, salary, area_name, published_at):
        self.name = name
        self.description = description
        self.key_skills = key_skills
        self.experience_id = experience_id
        self.premium = premium
        self.employer_name = employer_name
        self.salary = salary
        self.area_name = area_name
        self.published_at = published_at

class Salary:
    def __init__(self, salary_from, salary_to, salary_gross, salary_currency):
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.salary_gross = salary_gross
        self.salary_currency = salary_currency

name_keys = {"name":"Название", "description":"Описание", "key_skills":"Навыки", "experience_id":"Опыт", "premium":"Премиум",
             "employer_name": "Компания", "salary_from":"Нижняя граница оклада", "salary_to":"Верхняя граница оклада",
             "salary_gross":"Оклад указан до вычета налога", "salary_currency":"Идентификатор валюты оклада", "area_name":"Город",
             "published_at":"Дата и время публикации вакансии"}

experiense = {"noExperience":"Нет опыта", "between1And3":"От 1 года до 3 лет", "between3And6":"От 3 лет до 6 лет", "moreThan6":"Более 6 лет"}

currency = {"AZN":"Манаты",
            "BYR":"Белорусские рубли",
            "EUR":"Евро",
            "GEL":"Грузинский лари",
            "KGS":"Киргизский сом",
            "KZT":"Тенге",
            "RUR":"Рубли",
            "UAH":"Гривны",
            "USD":"Доллары",
            "UZS":"Узбекский сум"}

def make_parse(file_name):
    result = []
    with open(file_name, encoding="utf_8_sig") as result_file:
        file_reader = csv.reader(result_file, delimiter=",")
        for line in file_reader:
            result.append(line)

    if len(result) != 0:
        row_name = result.pop(0)
    else:
        return "Пустой файл"

    vacancies_all = []

    for line in result:
        if len(row_name) == len(line) and '' not in line:
            vacancies_all.append(line)

    vacancies = []

    for line in vacancies_all:
        dict_result = {}
        for i in range(0, len(row_name)):
            list_values = []
            if line[i].find("\n") != -1:
                for j in line[i].split("\n"):
                    lines = " ".join(re.sub(r"<[^>]+>", "", j).split())
                    list_values.append(lines)
            else:
                list_values = " ".join(re.sub(r"<[^>]+>", "", line[i]).split())
            dict_result[row_name[i]] = list_values
        vacancies.append(dict_result)
    return vacancies

def input_correst():
    file_name = input("Введите название файла: ")
    filtr_p = input("Введите параметр фильтрации: ")
    sort_p = input("Введите параметр сортировки: ")
    sort_rev = input("Обратный порядок сортировки (Да / Нет): ")
    count_v = input("Введите диапазон вывода: ")
    coluns = input("Введите требуемые столбцы: ")
    return file_name, filtr_p, sort_p, sort_rev, count_v, coluns

file_name, filtr_p, sort_p, sort_rev, count_v, coluns = input_correst()
data_vac = make_parse(file_name)
result = []
for vac in data_vac:
    salary = Salary(vac["salary_from"], vac["salary_to"], vac["salary_gross"], vac["salary_currency"])
    vacancy = Vacancy(vac["name"], vac["description"], vac["key_skills"], vac["experience_id"], vac["premium"], vac["employer_name"], salary, vac["area_name"], vac["published_at"])
    result.append(vacancy)
var_dump(DataSet(file_name, result))