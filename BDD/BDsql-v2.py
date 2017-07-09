import sqlite3

Eqpmanager = None

Eqpmanager = sqlite3.connect('test2.db')

cur = Eqpmanager.cursor()

#import time
#start = time.clock()

with Eqpmanager:
    cur.execute("DROP TABLE IF EXISTS eqpm2")
    cur.execute("CREATE TABLE eqpm2(Id INT, CategorieEqpm TEXT, Etatservice TEXT, provenance TEXT, Centreservice TEXT, Etatconservation INT, Marque TEXT, Modèle TEXT, Noserie TEXT, Salle TEXT, Dateaquis TEXT, DateLastEntre TEXT, CodeASSET TEXT)")
#test
    #cur.execute("INSERT INTO eqpm VALUES(2,'Sonde','maintenance','bla','néonatal',1)")
    #cur.execute("INSERT INTO eqpm VALUES(1,'incubateur','maintenance','bla','néonatal',1)")
    #cur.execute("INSERT INTO eqpm VALUES(3,'ECG','rebut','bla','néonatal',1)")
    #cur.execute("INSERT INTO eqpm VALUES(4,'Frigidaire','service','bla','néonatal',2)")
    #cur.execute("INSERT INTO eqpm VALUES(5,'Télévision','rebut','bla','néonatal',1)")

    n=1
    while n<1000:
        r = round(n/7) + round(n/2)
        if round(r) == r/2:
            mes1 = 'aaa222bbb'
            mes2 = '12345678'
        elif round(r) == r/7:
            mes1 = 'bbb666hhh'
        else:
            mes1 = 'ccc555lll'
            mes2 = '99887766'
    request = [n,'Sonde','maintenance','bla','néonatal',r,'bla',mes1,mes2,'bla','bla','bla','bla']
    cur.execute("INSERT INTO eqpm VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)", request)
    n += 1


with Eqpmanager:
    for row in cur.execute('SELECT * FROM eqpm WHERE Id>19000 AND Id<21500 ORDER BY Etatconservation'):
        print(row)


Clock = time.clock() - start
print(Clock)
#cur.execute('INSERT INTO éqpm VALUES(6,?,?,?)', request)

