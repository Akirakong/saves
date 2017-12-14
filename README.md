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
s = saves.Saves()
s.save('numer',num)
```

load
```
s = saves.Saves()
num = s.load('numer')
print(num)
# 99
```

delete
```
s = saves.Saves()
s.delete('numer')
```

delete all
```
s = saves.Saves()
s.clean()
```

get keys
```
s = saves.Saves()
keys = s.keys()
print(keys)
# ['hoge','fuga']
```