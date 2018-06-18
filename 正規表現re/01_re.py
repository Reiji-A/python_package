import re
"""
regular expresion
match()    文字列の先頭で正規表現とマッチするか判定
search()   文字列を操作して、正規表現がどこにマッチするか調べる
findall()  正規表現にマッチする部分文字列を全て探し出しリストとして返す
finditer() 重複しないマッチオブジェクトのイテレータを返す
"""
m = re.match('a.c',"abc")
m
print(m.group())
m = re.search("a.c","Test abc test abc")
print(m)
print(m.span())
print(m.group())

m = re.findall("a.c", "Tets abc test abc")
print(m)

m = re.finditer("a.c","test abc test abc")
print(m)
print([w.group() for w in m])

m = re.match("ab?","abb")
print(m)

m = re.match("ab*","abbb")
print(m)

m = re.match("ab+","a")
print(m)
m = re.match("ab+","abb")
print(m)

m = re.match("a{2,4}","aaaaaa")
print(m)

m = re.match("[a-zA-Z0-9_]","_")
print(m)

m = re.match("\w","a")
print(m)
m = re.match("\W","a")
print(m)

m = re.match("[^a-zA-Z0-9_]","1")
print(m)

m = re.match("[0-9]","1")
m = re.match("\D","a")
print(m)

m = re.match("a|b","b")
print(m)

m = re.match("(abc)+","abcabcabc")
print(m)

m = re.match("\s"," ")
print(m)

m = re.match("\S"," ")
print(m)

m = re.match("\?","?*")
print(m)

m = re.search("^abc","abc test abc")
print(m)

m = re.search("abc$", "abctest abc")
print(m)



m = re.search('[A-Z]', "Test Abc test abc")
print(m)
print(m.span())
print(m.group())

m = re.findall('[A-Z]',"Test abc test Abc")
print(m)
result =" "
for i in range(0,len(m)):
    result += m[i]
    print(result)



#m = re.finditer('a.c',"test abc test abc")
#print([w.group() for w in m])

m = re.match('ab?',"a")
print(m)
m = re.match('ab*',"abbb")
print(m)
m = re.match('ab+',"abb")
print(m)
m = re.match('a{2,4}',"aaaaa")
print(m)

#m = re.match('[a-zA-Z0-9_]',"a")
m = re.match('[a-zA-Z0-9]',"a")
#m = re.match('\W',"@")
#m = re.match('\w',"a")
print(m)
