"""
arn:aws:cloudformation:us-east-1:123456789012:stack/
MyProductionStack/9f960720-b397-11e3-bb75-a5b75389b02d
# この文字列から摘出する
"""
import re

RE_STACK_ID = re.compile(r"""
    arn:aws:cloudformation:
    (?P<region>[\w-]+):                   # region
    (?P<account_id>[\d]+)                 # account_id
    :stack/
    (?P<stack_name>[\w-]+)/               # stack_name
    [\w-]+""", re.VERBOSE)

s1 = ("arn:aws:cloudformation:us-east-1:123456789012:stack/"
     "MyProductionStack/9f960720-b397-11e3-bb75-a5b75389b02d")
s2 = ("arn:aws:cloudformation:us-east-2:566232123231:stack/"
     "MyProductionStack/9f960720-b397-11e3-bb75-a5b75389b02d")

for s in [s1,s2]:
    #m = re.match(
    #    (r'arn:aws:cloudformation:(?P<region>[\w-]+):(?P<account_id>[\d]+)'
    #     r':stack/(?P<stack_name>[\w-]+)/[\w-]+'),s)
    m = RE_STACK_ID.match(s)
    if m:
        print(m.group("region"))
        print(m.group("account_id"))
        print(m.group("stack_name"))
