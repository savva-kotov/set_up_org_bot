'''
import pandas as pd
lst = pd.read_csv('vol.csv')
for i in lst[['Фамилия','Имя','Посещение']]:
    print(i)
'''
import csv
lst = []
with open('vol.csv', newline='', encoding='utf-8') as File:  
    reader = csv.reader(File)
    for row in reader:
        if row[1] != '':
            row[2] = '0'
            row[3] = 'no comments'
        lst.append(row)

def s(letter):
    global lst
    print('Участники с фамилией на букву ' + letter)
    for i in lst[1:]:
        if i[0][0] == letter and len(i[0]) > 1:
            print(' '.join(i))
    
