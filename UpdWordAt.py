# -*- coding: utf-8 -*-

import psycopg2

def insert(word_attribute_list):
    try:
        connector = psycopg2.connect(host="localhost",database="android",user="general",password="Szbysadmin01")
        cursor    = connector.cursor()
        
        for wat in word_attribute_list:
            cursor.execute("insert into random_disp.words values(%d,%s,%s,%s)",("1","test","test","テスト")

        connector.commit()

        cursor.close()
        connector.close()
    except:
        print "失敗"
    finally:
        print "終了〜"