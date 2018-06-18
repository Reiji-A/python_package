import csv
import collections

with open("name.csv","w") as csvfile:
    fieldnames = ["first","last","address"]
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"first":"Mike","last":"Jackson","address":"a"})
    writer.writerow({"first":"Jun","last":"Sakai","address":"b"})
    writer.writerow({"first":"Eron","last":"Mask","address":"c"})

with open("name.csv","r") as f:
    csv_reader = csv.reader(f)
    print(next(csv_reader))
    #Names = collections.namedtuple("Names", next(csv_reader))
    for row in csv_reader:
        print(row)
        #names = Names._make(row)
        #print(names.first, names.last,names.address)

p = (10,20)
print(p[0])

class Point(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y


p = Point(10,20)
print(p.x)

Point = collections.namedtuple("Point","x,y")
p = Point(10,y=20)
print(p.x)
print(p.y)
p.x = 100

pl = Point._make([100,200])
print(pl)
print(pl._asdict())#

pl._replace(x = 500)
print(pl)
p2 = pl._replace(x = 500)
print(p2)

class Sumpoint(collections.namedtuple("Point",["x","y"])):
    @property
    def total(self):
        return self.x + self.y#

p3 = Sumpoint(2,3)
print(p3.x,p3.y,p3.total)
