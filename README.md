# reportingM

reportingM is a program that fetching three informations from database as shown as below
* The most popular three articles of all time.
* The most popular article authors of all time.
* The days more than 1% of requests led to errors

Install
--------
You should install python2 in order to run this program, click this: [Python](https://www.python.org/downloads/release/python-2715/)

Also you should install VirtualBox and Vagrant, click the links to download: [VirtualBox](https://www.virtualbox.org) and [Vagrant](https://www.vagrantup.com/downloads.html)

The database file is included with this repository. However, if you want to download original database, follow this link: [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

After you install the all programs above, the first thing you should do is setting up Vagrant with VirtualBox.

Open your terminal and type following codes:
```shell
vagrant up
```
After that type:
```shell
vagrant ssh
```
Then your virtual machine(VM) is set up successfully.

Running
-------
On your terminal with VM environment, go to the directory that include the files(reportingM.py, DB file and etc) is cloned from my repository.

Type the commend to run the program.
```shell
python reportingM.py
```
If you run the program successfully, the further instruction is going to show up on your terminal.

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
