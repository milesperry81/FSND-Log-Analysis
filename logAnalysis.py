#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 17:19:34 2019

@author: Miles
"""

# import the DB-API module
import psycopg2
import datetime

# connect to the DB
db = psycopg2.connect("dbname=news")

# cursor runs the query and stores the results
c = db.cursor()

# first query
query = '''select
articles.title,
count(*) as views
from articles
join log on substr(log.path,10) = articles.slug
group by articles.title
order by count(*) desc
limit 3;'''
c.execute(query)
rows = c.fetchall()

# print results
print("1. What are the most popular three articles of all time?")
for row in rows:
    print(row[0] + " - " + str(row[1]) + " views")
print("\n")

# second query
query = '''select
authors.name,
count(*) as views
from articles
join log on substr(log.path,10) = articles.slug
join authors on authors.id = articles.author
group by authors.name
order by count(*) desc;'''
c.execute(query)
rows = c.fetchall()

# print results
print("2. Who are the most popular article authors of all time?")
for row in rows:
    print(row[0] + " - " + str(row[1]) + " views")
print("\n")

# third query
query = '''select
sq1.date,
sq1.NotOK*100.00/sq2.All as rate
from (
select date(time) as date, count(*) as NotOK
from log where status != '200 OK'
group by date(time)
) as sq1
join (
select date(time) as date, count(*) as All
from log
group by date(time)
) as sq2 on sq1.date = sq2.date
where (sq1.NotOK*100/sq2.All) > 1;'''
c.execute(query)
rows = c.fetchall()

# print results
print("3. On which days did more than 1% of requests lead to errors?")
for row in rows:
    print(str(row[0].strftime("%d %B %Y ")),
          " - ", str(round(row[1], 2)) + "% errors")
print("\n")

# close DB connection
db.close()
