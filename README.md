# reportingM

reportingM is a program that fetching three informations from database as shown as below
* The most popular three articles of all time.
* The most popular article authors of all time.
* The days more than 1% of requests led to errors

Install
--------
You should install python in order to run this program [Python](https://www.python.org/downloads/)

After you install Python, open your terminal and type:
```shell
python reportingM.py
```
then the instruction is going to show up on your terminal.

More Information
----------------
The newsdata.sql has two views as:
```sql
create view whole_view as select to_char(time, 'Mon DD,YYYY') as wtime, count(*) as cnt from log group by wtime;
```
and
```sql
create view error_view as select to_char(time, 'Mon DD,YYYY') as etime, count(*) as cnt from log where status = '404 NOT FOUND' group by etime;
```

License
-------
reportingM is Copyright © 2019 Daewoong Ko.
It is freeware.
