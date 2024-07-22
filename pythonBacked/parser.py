import requests
from bs4 import BeautifulSoup
import json


# rs = requests.get('http://www.7english.ru/dictionary.php?id=2000&letter=all')
# root = BeautifulSoup(rs.content, 'html.parser')

# en_ru_items = []

# for tr in root.select('tr[onmouseover]'):
#     td_list = [td.text.strip() for td in tr.select('td')]

#     # Количество ячеек в таблице со словами -- 9
#     if len(td_list) != 9 or not td_list[1] or not td_list[5]:
#         continue

#     en = td_list[1]

#     # Русские слова могут быть перечислены через запятую 'ты, вы',
#     # а нам достаточно одного слова
#     # 'ты, вы' -> 'ты'
#     ru = td_list[5].split(', ')[0]

#     en_ru_items.append((en, ru))

# print(dict(en_ru_items)['a'])


# with open('JSONdict.txt', 'r') as file:
#     with open('dict2.json', 'w', encoding='utf-8') as f:
#         json.dump(dict(file), f, indent=4, ensure_ascii=False)



with open('JSONdict.txt', 'r') as file:
    print(file)