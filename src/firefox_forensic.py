'''
Created on May 3, 2011

@author: alex
'''
import sqlite3,datetime

class firefox_forensic(object):

    def __init__(self,firefox_directory):
        print(firefox_directory)
        
    def get_cookies(self,cookies_file):
        cookies = sqlite3.connect(cookies_file)
        c = cookies.cursor()
        c.execute('select name,value,host,lastAccessed from moz_cookies')
        for row in c:
            t = row[3]
            t /= 1e6
            p = datetime.datetime.fromtimestamp(t)
            print('\nWebSite: ' + row[2].encode('utf-8') + '\n' + row[0].encode('utf-8')  + ': '+ row[1].encode('utf-8') + '\n' + str(p))
        c.close()
        
    def get_cache(self,cache_dir):
        pass
    
    def get_history(self,history_file):
        history = sqlite3.connect(history_file)
        c = history.cursor()
        c.execute('select title,url from moz_places')
        for row in c:
            print('Visited: ' + row[1].encode('utf-8'))
        c.close()
        