import json
import os

#PARSE netlist

net = os.listdir('./Project Outputs/WireListNetlist/')[0]

with open(f'./Project Outputs/WireListNetlist/{net}') as f:
    lines = f.readlines()
for i in range(lines.__len__()):
    lines[i] = lines[i].strip()
lines = lines[lines.index('<<< Wire List >>>'):]
while '' in lines:
    lines.remove('')

keys = ['net','designator','pinNum','pinName','component']
data = lines[2:]
for i in range(data.__len__()):
    data[i] = data[i].split()
result = []
net = ''
for i in data:
    if i[0][0] == '[':
        net = i[1]
    else:
        result.append({
            'net':net,
            'designator': i[0],
            'pinNum': i[1],
            'pinName': i[2],
            'component': i[-1],
            })

for item in result:
    if 'STM'.lower() in item['component'].lower():
        print(item['pinName'],item['net'])


with open('README.md') as f:
    lines = f.readlines()

for li in lines:
    if '## MCU PINOUT' in li:
        print(li)

'''
with open("netlist.json", 'w', encoding='utf8') as outfile:
    json.dump(result, outfile, indent=4, ensure_ascii=False)
    outfile.close()
'''

#MAKE TRANPARENT pics


#   pip install Pillow
# pip install rembg

from rembg import remove
import numpy as np
import cv2

def alphaAndCut(input_path,output_path):
    src = cv2.imread(input_path)
    tgt = remove(src)
    rows = np.any(tgt, axis=1)
    cols = np.any(tgt, axis=0)
    rmin, rmax = np.where(rows)[0][[0, -1]]
    cmin, cmax = np.where(cols)[0][[0, -1]]
    cv2.imwrite(output_path, tgt[rmin:rmax, cmin:cmax])

alphaAndCut('./doc/view.png','./doc/t-view.png')
alphaAndCut('./doc/view-bottom.png','./doc/t-view-bottom.png')
alphaAndCut('./doc/view-top.png','./doc/t-view-top.png')


def Cut(input_path,output_path):
    src = cv2.imread(input_path)
    tgt = src#remove(src)
    rows = np.any(tgt<255, axis=1)
    cols = np.any(tgt<255, axis=0)
    rmin, rmax = np.where(rows)[0][[0, -1]]
    cmin, cmax = np.where(cols)[0][[0, -1]]
    cv2.imwrite(output_path, tgt[rmin-3:rmax+3, cmin-3:cmax+3])


# GENERATE PNG OF drw

try:
    # pip install pdf2image

    from pdf2image import convert_from_path
    pages = convert_from_path('./doc/doc.pdf', 300)
    pages[-1].save('./doc/drw.png', 'PNG')

    #Cut('./doc/drw.png','./doc/drw.png')
except:
    print('something wrong with pdf2image')




#GET MODEL DIMENSIONS

step_file = ''

for path in os.listdir('./doc'):
    if '.step' in path.lower():
        step_file = path
        break
try:
    # pip install steputils
    from steputils import p21
    file = p21.readfile(f'doc/{step_file}')

    points = [
        file.data[0].instances[x].entity.params[1] for x in [                      # 4 get point by id
            entry.entity.params[1] for entry in                                    # 3 get vertex point id
            sum([list(section.instances.values()) for section in file.data], [])   # 1 gather all sections
            if hasattr(entry, 'entity') and entry.entity.name == 'VERTEX_POINT'    # 2 filter all vertices
        ]
    ]

    min_x = min(points, key=lambda x: x[0])[0]
    max_x = max(points, key=lambda x: x[0])[0]

    min_y = min(points, key=lambda x: x[1])[1]
    max_y = max(points, key=lambda x: x[1])[1]

    min_z = min(points, key=lambda x: x[2])[2]
    max_z = max(points, key=lambda x: x[2])[2]

    bbox = (
        (min_x, min_y, min_z),
        (max_x, max_y, max_z)
    )

    dim = (
        max_x - min_x,
        max_y - min_y,
        max_z - min_z
    )

    #print(bbox)
    print(dim)

    x = round(dim[0]*10)/10.0
    y = round(dim[1]*10)/10.0
    z = round(dim[2]*10)/10.0

    print(x,y,z)
except:
    print("An exception occurred 'pip install steputils' not installed")




# GET GERBER DIMENSIONS

from gerber import load_layer

# Open the gerber files
gm2 = load_layer('./Project Outputs/Gerber/PCB.GM2')

#print(gm2.__dict__)
#print(gm2.bounds)
print(-gm2.bounds[0][0]+gm2.bounds[0][1])
print(-gm2.bounds[1][0]+gm2.bounds[1][1])


# GENERATE BOM file exactly for PCBWay

import openpyxl
import pandas as pd

with open('./Project Outputs/BOM/BOMtxt-BOM.txt') as f:
    lines = f.readlines()
for i in range(lines.__len__()):
    lines[i] = lines[i].strip()
for i in range(lines.__len__()):
    lines[i] = lines[i].split('\t')
for i in range(len(lines)):
    for j in range(len(lines[i])):
        lines[i][j] = lines[i][j].replace('"', '')
data = pd.DataFrame(lines[1:], columns=lines[0])
data = data.drop(0)
columns = ['*Designator', '*Qty', 'Manufacturer', '*Mfg Part #', 'Value / Description', '*Package/Footprint',
           'Mounting Type', 'Your Instructions / Notes', 'Assembly', '*Unit Price(XX sets)', '*Total', '*Delivery Time',
           '*Actual Purchase Mfg Part #', '*PCBWay Note', 'Customer Reply', 'PCBWay Update']
dataxls = pd.DataFrame(columns=columns)
dataxls['*Designator'] = data['Designator']
dataxls['*Qty'] = data['Quantity']
dataxls['Manufacturer'] = data['MF']
dataxls['*Mfg Part #'] = data['MP']
dataxls['Value / Description'] = data['Value'].astype('str') + '; ' + data['Description'].astype('str')
dataxls['*Package/Footprint'] = data['Package']
dataxls['Mounting Type'] = data['Type']
dataxls['Your Instructions / Notes'] = data['Instructions'] + '; ' + data['HelpURL']
dataxls.to_excel('./Project Outputs/BOM/output.xlsx')

book = openpyxl.load_workbook('./Project Outputs/BOM/output.xlsx')
sheet = book['Sheet1']
for col in sheet.columns: # автоматическая ширина ячеек
     max_length = 0
     column = col[0].column_letter # Get the column name
     for cell in col:
         try: # Necessary to avoid error on empty cells
             if len(str(cell.value)) > max_length:
                 max_length = len(str(cell.value))
         except:
             pass
     adjusted_width = max_length * 0.8
     sheet.column_dimensions[column].width = adjusted_width
yellow = openpyxl.styles.PatternFill('solid', fgColor="FFFF00")
grey = openpyxl.styles.PatternFill('solid', fgColor="C0C0C0")
for row in sheet.iter_rows(min_row=1, min_col=1, max_row=1, max_col=sheet.max_column):
    for cell in row:
        cell.fill = grey
sheet['B1'].fill = yellow
sheet['C1'].fill = yellow
sheet['E1'].fill = yellow
sheet['G1'].fill = yellow
sheet['K1'].fill = yellow
sheet['L1'].fill = yellow
sheet['M1'].fill = yellow
sheet['N1'].fill = yellow
sheet['O1'].fill = yellow
sheet['P1'].fill = yellow
sheet['Q1'].fill = yellow
book.save('./Project Outputs/BOM/output.xlsx')


#PCB.xls

# pip install xlrd
data = pd.read_excel('./Project Outputs/Report Board Stack/PCB.xls')
# суммарная толщина всех слоёв
maxvalue = float(list(data[-1:].stack())[0].split()[-1].replace('mm','').replace(',','.')) # Последняя строка из таблицы стакается в одну ячейку, превращается в список, оставшаяся строка делится по пробелам, удаляется mm, запятая меняется на точку, всё это превращается в число float
data = data[4:-3]
layers = data.loc[data.iloc[:,-3] == 'Copper'] #Ищу по столбцу где есть медь - это проводящие слои
listlayers = list(layers.iloc[:,-4]) # Список слоёв
hight = list(layers.iloc[:,-2]) # Список толщин
temp = []
for i in hight:
    temp.append(float(i.replace('mm','').replace(',','.')))
hight = temp.copy()
standrdrow = [0.2, 0.3, 0.4, 0.6, 0.8, 1.0, 1.2, 1.6, 2.0, 2.4, 2.6, 2.8, 3.0, 3.2]
standrdvalue = [abs(i-maxvalue) for i in standrdrow]
standrdvalue = standrdrow[standrdvalue.index(min(standrdvalue))]

#PCB.TXT

with open('./Project Outputs/NC Drill/PCB.TXT') as f:
    lines = f.readlines()
for i in range(lines.__len__()):
    lines[i] = lines[i].strip()
pcbplate = lines[lines.index(';TYPE=PLATED')+1:lines.index('%')] #TODO в цикл его надо пихать шобы по всему файлу пройтись?
tmp = []
for i in pcbplate:
    tmp.append(float(i[i.index('C')+1:]))

#PCB.G1

with open('./Project Outputs/Gerber/PCB.G1') as f:
    lines = f.readlines()
for i in range(lines.__len__()):
    lines[i] = lines[i].strip('*\n')
listfromPCBG1 = []
for i in lines:
    if i.find('%') == False: #TODO поиск строк по % во всём файле вообще корректен?
        i = i.strip('*%')
        if i.find('C') != -1 and i.find(',') != -1:
            listfromPCBG1.append(float(i[i.find(',')+1:]))

result = [layers.shape[0], # Число слоёв
          listlayers, # Названия слоёв
          maxvalue, # Максимальное число
          standrdvalue, # Число приведённое к стандартному значению
          hight, # Высота слоёв
          min(tmp), # Минимальная высота из файла PCB.TXT
          min(listfromPCBG1) # Минимальная высота из файла PCB.G1
          ]
print(result)