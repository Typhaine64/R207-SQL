import sqlite3 as sql

con = sql.connect("magasin.sqlite")
cur = con.cursor()

cur.execute("SELECT nomProd FROM Produit WHERE numProd = 'p1' or numProd = 'p2' or numProd = 'p3' or numProd = 'p4'")
res = cur.fetchall()

column_names = [description[0] for description in cur.description]

# code html

print("<!Doctype html>")
print("<html>")

print("<head>")
print("<title> sql en python </title>")
print("<style>table{border-collapse:collapse;}td{text-align:center;border:1px solid black;}th{text-align:center;border:1px solid black;}</style>")
# ^ défini le style du tableau
print("</head>")

print("<body>")
print("<center>") # permet centrer le tableau
print("<table>")

print("<tr>")
#print les noms de chaque colonne en faisant un th par colonne
for col_name in column_names :
    print("<th>", col_name,"</th>")
print("<tr>")

for row in res: #pour toute ligne/paramètre dans le résultat de la requete 
    print("<tr>")
    for column in row:
        if column is None: # tiret si pas de colone 
            print("<td>-</td>")
        else:
            print('<td>' + str(column) + "</td> </font>") #sinon on print l'intérieur de la collone
    print("</tr>")

print("</table>")
print("</center>")
print("</body>")
print("</html>")

con.close()
