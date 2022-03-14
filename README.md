# python-sql-launcher
A simple Python script that launches an SQL PL/Query directly in a database, shows the results in the terminal and logs them in a .csv file.

### Prerequisites
To have [Python](https://www.python.org/) installed on your machine.

---

### How you should use the program
This script is supposed to be launched from the terminal (CLI), or anything equivalent, for example a Virtual Machine on Google Cloud platform.
```
python3 python-sql-launcher.py [arg1] [arg2] [arg3] [arg4] [arg5] 
```

##### Meaning of the arguments
- ```[arg1]```: Username of the database
- ```[arg2]```: Password of the database
- ```[arg3]```: IP for the connection
- ```[arg4]```: Service name of the connection
- ```[arg5]```: Your query or PL/SQL, ***enclosed between double quotes***

---

### Troubleshooting and personalization
##### I ran a PL/SQL and I received a "xxxx" error, why?
If you want to run only a PL/SQL, you should delete the part of the script where the results of the query are writtend inside the .csv file. (from line xx to line xx)
Leaving the scripts as it is, will return an error because PL/SQL do not return results, unlike a query.

##### test
test

---

### Troubleshooting and personalization
- [x] Write some pretty basic Python code. :snake:
- [x] Write an excessively accurate documentation. 🗒️
- [ ] Add "connection_string" templates of major databases.
- [ ] Add delight to the experience when all tasks are complete :tada:
