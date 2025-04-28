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


    def Show(self, button='top', count=5, separator=','):
        if count > len(self.data):
            count = len(self.data)
        dt = []
        if button == 'top':
            dt = self.data[:count]
        elif button == 'bottom':
            dt = self.data[-count:]
        elif button == 'random':
            for i in range(count):
                dt.append(self.data[random.randint(0, len(self.data))])

        for i in dt:
            print('\t'.join(i))
                
                

a = Csv(filename)
a.Show('top', 5)