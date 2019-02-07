# mysql-funk

Querying and updating a MySQL database in Python doesn't get any easier than this. This package was created because the mysql-connector is too convoluted to use on the fly. For a quick data recording job, I didn't want to worry about openning and closing connections and cursors. Other packages like SQLAlchemy were not my preference because I'm comfortable with SQL. Some packages try to get rid of the SQL which just isn't a problem for me.

So to put a fine point on it - this package is created for one who knows SQL.

I maintain my DB on the server and just want python to add records periodically or post results to a web app/report. This package works great as a simple solution to do just that. I call it funk because it's care free, smooth, and relaxed. The learning curve is small.

Step 1: Enter the DB connection info

```
dbconfig = {
        'user': 'main',
        'password': '',
        'host': '127.0.0.1',
        'database': 'army_knife'
            }
```

Step 2: Startup the MysqlFunk class
```
from MysqlFunk import MysqlFunk
my_db = MysqlFunk(**dbconfig)
```
Step 3: Update or insert
```
insert = "insert into test (date_time,text,text2) values (now(),'test','test')"
my_db.query_statement(insert)
```
Step 4: Query away
```
select = "select * from test"
results = my_db.commit_statement(select)
```
Results always come back as a list of tuples. Each tuple is a row from the DB.

