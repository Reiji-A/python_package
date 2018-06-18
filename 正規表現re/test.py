import re

regex = r"ab+"
text = "abbabbabaaabb"
pattern = re.compile(regex)
matchObj = pattern.match(text)

matchObj

matchObj = re.match(regex,text)
matchObj

# matchのサンプルコード

data = "abcdefghijklmn"
# パターン式の定義(aで始まりcで終わる最短の文字列)
pattern = re.compile(r"a.*?c")
match_data = pattern.match(data)

print(match_data.group())

# searchのサンプルコード
# パターン式の定義(dで始まりgで終わる最短の文字列)
pattern = re.compile(r"d.*?g")
match_data = pattern.search(data)

# 一致したデータ
print(match_data.group())
# 一致した開始位置
print(match_data.start())
# 一致した終了位置
print(match_data.end())
# 一致した位置を表示
print(match_data.span())

# findallのサンプルコード
# パターン式の定義(dで始まりgで終わる最短の文字列)
pattern = re.compile(r"d.*?g")
match_data = pattern.findall(data)

print(match_data)

# finditerのサンプルコード
# パターン式の定義(dで始まりgで終わる最短の文字列)
data = "abcdefghijklmnabcdefghijklmn"
pattern = re.compile(r"d.*?g")
match_datas = pattern.finditer(data)

print(match_datas)

for match in match_datas:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())
    
