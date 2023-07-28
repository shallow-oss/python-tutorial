import re

p = re.compile('[A-Za-z]+')
print(p.match(""))
print(p.match("1121212;';';';';"))
m = p.match("Hello,Regular-Expression")
print(m.group())
print(m.start())
print(m.end())
print(m.span())

p = re.compile(r'\d+')
print(p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping'))

iterator = p.finditer('12 drummers drumming, 11 ... 10 ...')
print(iterator)
for match in iterator:
    print(match)
