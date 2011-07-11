'''
Created on May 29, 2011

@author: f4ktu4l
'''

import sqlite3,datetime,re

class chrome_forensics(object):

    def __init__(self):
        print("Browser Forensics is fun!")
        
    def get_cookies(self,cookies_file):
        cookies = sqlite3.connect(cookies_file)
        c = cookies.cursor()
        c.execute('select name,value,host,lastAccessed from moz_cookies')
        cookies_container = []
    
def get_history(history_file):
    history = sqlite3.connect(history_file)
    
    h = history.cursor()
    h.execute('select urls.url, urls.title,urls.visit_count,urls.typed_count, urls.last_visit_time,urls.hiddend from urls, visits where urls.id = visits.url')
    
    history_container = []
    
    for row in h:
        '''temp = { 'url' : found[1], 'title' : found[2], 'visit_count' : found[3], 'typed_count' : found[4], 'last_visit_time' : found[5]}
        print(temp)
        print
        history_container.append(temp)'''
        print(row)


    def get_downloads(self,download_file):

        
    def get_form_history(self,form_history):

            
    def get_signons(self,signons_history):
