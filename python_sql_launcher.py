#Import libraries:
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import logging
import sys
import csv

#Connect to the database (Oracle):
connection_string = "oracle+cx_oracle://" + sys.argv[1] + ":" + sys.argv[2] + "@(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=" + sys.argv[3] + ")(PORT=1521)))(CONNECT_DATA=(SERVICE_NAME=" + sys.argv[4] + ")(SERVER=DEDICATED)))"
engine = create_engine(connection_string)

#Stream logging on CLI, level "error"
handler = logging.StreamHandler()
handler.setLevel(logging.ERROR)
logging.getLogger('sqlalchemy.engine').addHandler(handler)

#Launch PL/SQL and/or SQL query
with engine.connect() as con:
    rs = con.execute(sys.argv[5])

results = rs.all()[1:100000]

#Print the num of elements and all the elements in the CLI
number_of_elements = len(results)
print("Number of elements in the list: ", number_of_elements)
for x in range(number_of_elements):
    a = str(x)
    print("List element in position: " + a)
    print(results[x])

#Opening the csv file in 'w+' mode
file = open('results.csv', 'w+', newline ='')

# writing the data into the file
with file:
    write = csv.writer(file)
    for x in range(number_of_elements):
        data = [results[x]]
        write.writerows(data)

#Exit Python3
exit()
