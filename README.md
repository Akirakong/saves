# saves


savesはシンプルなデータ永続化機構を提供します。

saves provide you to data persistence.

---

install
```
pip install saves
```

save
```
num = 99
s = saves.saves()
s.save('numer',num)
```

load
```
s = saves.saves()
num = s.load('numer')
print(num)
# 99
```

delete
```
s = saves.saves()
s.delete('numer')
```

delete all
```
s = saves.saves()
s.clean()
```

get keys
```
s = saves.saves()
keys = s.keys('numer')
print(keys)
# ['hoge','fuga']
```