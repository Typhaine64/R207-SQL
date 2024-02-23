import json
import sqlite3 as sql

con = sql.connect("magasin.sqlite")
cur = con.cursor()

cur.execute("SELECT * FROM Produit")
res = cur.fetchall()

# en python
print('Données en python : ', res)


# en json
json_string = json.dumps(res)
print("Données en json : ", json_string)

# faire en sorte que ça soit pretty UWU
json_pretty_string = json.dumps(res, indent=4)
print('Données en json (pretty) : \n',json_pretty_string)
