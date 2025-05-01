import csv 
import os
import random


filename = 'leads-100.csv'


class Csv():
    def __init__(self, filename):
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            self.headers = next(reader)
            self.data = [i for i in reader]


    def Show(self, button='top', count=5, separator=', '):
            if count > len(self.data):
                dt = self.data
            dt = []
            if button == 'top':
                dt = self.data[:count]
            elif button == 'bottom':
                dt = self.data[-count:]
            elif button == 'random':
                for i in range(count):
                    dt.append(self.data[random.randint(0, len(self.data))])

            for i in dt:
                print(*i,sep=separator)
    def Info(self):
        col = len(self.headers)
        row = len(self.data)
        print(f'{row}x{col}')

        # x = 2.333
        # print(f'{x.__class__}'[8:-2])
        column_stats = {col: {'count': 0, 'type': None} for col in self.headers}
        for row in self.data:
            for i, value in enumerate(row):
                if value:
                    column_stats[self.headers[i]]['count'] += 1
                    if column_stats[self.headers[i]]['type'] is None:
                        if value.isdigit():
                            column_stats[self.headers[i]]['type'] = "int"
                        else:
                            column_stats[self.headers[i]]['type'] = "string"
        for col, key in column_stats.items():
            print(f"{col} {key['count']} {key['type']}")
    def DelNaN(self):
        for i in self.data:
            if '' in i:
                self.data.remove(i)
    def MakeDS(self):
        random.shuffle(self.data)
        learn_data = self.data[:int(len(self.data) * 0.7)]
        test_data = self.data[int(len(self.data) * 0.7):]
        os.makedirs('workdata/Learning')
        os.makedirs('workdata/Testing')
        with open('workdata/Learning/train.csv', 'w', newline = '') as f:
            writer = csv.writer(f)
            writer.writerows(learn_data)
        with open('workdata/Testing/test.csv', 'w', newline = '') as f:
            writer = csv.writer(f)
            writer.writerows(test_data)
a = Csv(filename)
#a.Show('top', 5)
# a.DelNaN()
# a.Info()
# a.Show('top',7)
a.MakeDS()