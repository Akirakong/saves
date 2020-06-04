# saves


savesはシンプルなデータ永続化機構を提供します。  
カレントディレクトリにデータベース(sqlite3)が作成されます。

saves provide you to data persistence.  
A database (sqlite3) will be created in the current directory.
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

change database name
```
Saves.current_dbname = 'fuga'
s = saves.Saves()
```

Change the name of the database used
```
Saves.current_dbname = 'fuga'
s = saves.Saves()
```

Rename the already created database
```
s = saves.Saves()
s.set_db_name('fuga')
```

