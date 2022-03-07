#Import libraries:
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import logging
import sys

USER = sys.argv[1],
PWD = sys.argv[2],
IP = sys.argv[3],
SERVICE = sys.argv[4]

#Connect to the database:
connection_string = "oracle+cx_oracle://" + USER + ":" + "@(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=" + IP + ")(PORT=1521)))(CONNECT_DATA=(SERVICE_NAME=" + SERVICE + ")(SERVER=DEDICATED)))"
engine = create_engine(connection_string)

handler = logging.StreamHandler()
handler.setLevel(logging.ERROR)
logging.getLogger('sqlalchemy.engine').addHandler(handler)

#Launch PL/SQL
with engine.connect() as con:
    rs = con.execute('begin drop_ge_temp; end;')

#Exit Python3
exit()
