

import sqlite3
import re

connection = sqlite3.connect('drillDB.db')

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg');
fileList2 = list(fileList)



with connection:
    cur = connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_names( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT \
        )")
    for i in fileList2:
        result = re.search('.txt', i)
        if result:
            print(i)
            cur.execute("INSERT INTO tbl_names(col_fname) VALUES (?)",(i,))
    connection.commit()
connection.close()


 
