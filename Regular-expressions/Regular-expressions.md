# Regular expressions

[正则表达式HOWTO](https://docs.python.org/zh-cn/3/howto/regex.html#)

## 1.匹配字符
```txt
元字符
. ^ $ * + ? { } [ ] \ | ( )
```
```txt
[ ] 指定字符类，希望匹配的字符的一个集合
元字符（除了 \ ）在字符类中是不起作用的
[abc] 字符可以单独列出
[a-c] 字符可以用字符范围来表示
^ 放在字符类开头，可以取反字符类，即匹配除给出的字符类之外的任何字符
```