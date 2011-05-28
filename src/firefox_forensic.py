'''
Created on May 3, 2011

@author: alex
'''
import sqlite3,datetime,re

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
    
    def get_downloads(self,download_file):
        downloads = sqlite3.connect(download_file)
        c = downloads.cursor()
        c.execute('select name,source,target,startTime,endTime from moz_downloads')
        for row in c:
                print('Download Name: ' + row[0].encode('utf-8'))
                print('URL: ' + row[1].encode('utf-8'))
                print('Location: ' + row[2].encode('utf-8'))
                print('Start: ' + str(datetime.datetime.fromtimestamp(row[3]/1e6)) + ' End: ' + str(datetime.datetime.fromtimestamp(row[4]/1e6)))
                print()
                
    def get_facebook(self,history_file):
        history = sqlite3.connect(history_file)
        c = history.cursor()
        c.execute('select url from moz_places')
        pat = re.compile('facebook.com\/profile.php\?id\=')
        for row in c:
            if pat.search(''.join(row)):
                print(pat.search(''.join(row))).string
        print("Ending Facebook!")
        c.close()
            
    def get_form_history(self,form_history):
        forms = sqlite3.connect(form_history)
        c = forms.cursor()
        c.execute('select fieldname,value,timesUsed from moz_formhistory')
        sorted = []
        
        for row in c:
            temp = str(row[2]),row[0].encode('utf-8'),row[1].encode('utf-8')
            sorted.append(temp)
        
        sorted.sort()    
        sorted.reverse()
        for i in sorted:
            print(i)
    
    def get_bookmarks(self,bookmarks_folder):
        pass
    
    def get_signons(self,signons_history):
        signons = sqlite3.connect(signons_history)
        c = signons.cursor()
        c.execute()