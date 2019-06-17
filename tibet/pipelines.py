# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

from scrapy.conf import settings



#class TibetPipeline(object):
    #def process_item(self, item, spider):
        #return item


# This pipeline takes the Item and stuffs it into scrapedata.db

import sqlite3
import os
con = None

class TibetPipeline(object):

    def __init__(self):
        self.setupDBCon()
        self.createTables()

    def setupDBCon(self):
        self.con = sqlite3.connect(os.getcwd() + '/test.db')
        self.cur = self.con.cursor()

    def createTables(self):
        self.dropTibetTable()
        self.createTibetTable()

    def dropTibetTable(self):
        #drop tibet table if it exists
        self.cur.execute("DROP TABLE IF EXISTS Tibet")

    def closeDB(self):
        self.con.close()

    def __del__(self):
        self.closeDB()

    #create table

    def createTibetTable(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS Tibet(id INTEGER PRIMARY KEY NOT NULL, \
            title TEXT, \
            url  TEXT \
            )")


    def process_item(self, item, spider):
        self.storeInDb(item)
        return item
   # store information in database
    def storeInDb(self,item):
        self.cur.execute("INSERT INTO Tibet(\
            title, \
            url \
            ) \
        VALUES( ?, ?)", \
        ( \
            item.get('title',''),
            item.get('url',''),
        ))
        print ('#######################')
        print ('Data Stored in Database')
        self.con.commit()
