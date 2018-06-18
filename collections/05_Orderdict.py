import collections

#od = collections.OrderedDict({"banana":3,"apple":4,"pear":1,"orange":2})
#od_2 = collections.OrderedDict({"apple":3,"banana":4,"pear":1,"orange":2})
#print(od==od_2)



d = {"banana":3,"apple":4,"pear":1,"orange":2}

od = collections.OrderedDict(
    #sorted(d.items(),key=lambda t: t[1]) # valueをsort
    sorted(d.items(), key=lambda t: t[0]) # keyをsort
    #sorted(d.items(),key=lambda t: len(t[0])) # 文字の長さでsort
    )
#od = collections.OrderedDict(d)
print(od)
od["cc"] = 100
print(od)
od = collections.OrderedDict(
    sorted(od.items(), key=lambda t: t[0])
)
print(od)
