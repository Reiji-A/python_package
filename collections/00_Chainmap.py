import collections

a = {'a':"a",'c':"c","num":0}
b = {'b':"a",'c':"cc"}
c = {'b':"bbb",'c':"ccc"}

class DeepChainMap(collections.ChainMap):
    def __setitem__(self, key, value):
        for mapping in self.maps:
            if key in mapping:
                if type(mapping[key]) is int and mapping[key] < value:
                    mapping[key] = value
                return
        self.maps[0][key] = value

m = DeepChainMap(a,b,c)
m.maps
m["new_num"] = -1
m.maps
print(m['new_num'])
print(m["num"])

print(a)
a.update(b)
print(a)
a.update(c)
print(a)

m = collections.ChainMap(a,b,c)
print(m["b"])
print(m.maps)
m.maps.reverse()
print(m.maps)
m.maps.insert(0,{"c":"CCCCC"})
del m.maps[0]
print(m.maps)
print(m['c'])
m["b"] = "BBBBB"
print(m.maps)
