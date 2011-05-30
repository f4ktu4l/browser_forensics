'''
Created on May 3, 2011

@author: alex
'''
import sqlite3,datetime,re,base64
from ctypes import *

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
            print('\nWebsite: ' + row[2].encode('utf-8') + '\n' + row[0].encode('utf-8')  + ': '+ row[1].encode('utf-8') + '\n' + str(p))
        c.close()
        
    def get_cache(self,cache_dir):
        pass
    
    def get_history(self,history_file,sort_method = 'date',*keywords):
        history = sqlite3.connect(history_file)
        c = history.cursor()
        c.execute('select title,url,visit_count,typed,last_visit_date from moz_places')
        sorted = []
        
        for row in c:
            if(sort_method == 'count'):
                temp = str(row[2]),row[0],row[1],str(row[3]),row[4]
                sorted.append(temp)
            elif(sort_method == 'date'):
                temp = row[4],row[0],row[1],str(row[3]),str(row[2])
                sorted.append(temp)
        
        sorted.sort()
        sorted.reverse()

        for i in sorted:
                if(sort_method == 'count'):
                    print('Visited: ' + i[2].encode('utf-8'))
                    print('Typed: ' + i[3])
                    print('Number of Visits: ' + i[0])
                                        
                    if(i[4] != None):
                        print('Last Visit Date: ' + str(datetime.datetime.fromtimestamp(i[4]/1e6)))
                    
                    print
                    
                elif(sort_method == 'date'):
                    print('Visited: ' + i[2].encode('utf-8'))
                    print('Typed: ' + i[3])
                    print('Number of Visits: ' + i[4])
                    
                    if(i[0] != None):
                        print('Last Visit Date: ' + str(datetime.datetime.fromtimestamp(i[0]/1e6)))
                    
                    print
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
                print
                
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
            
    def get_signons(self,signons_history):
        #f = open(keyfile,'rb')
        #print(f.read())
        print(signons_history)
        libnss = CDLL('libnss3.so')
        if libnss.NSS_Init(signons_history) != 0:
            print('Total error dude!')
        
        (SECWouldBlock,SECFailure,SECSuccess)=(-2,-1,0)
        (PW_NONE,PW_FROMFILE,PW_PLAINTEXT,PW_EXTERNAL)=(0,1,2,3)
        pwdata = pw_data()
        pwdata.source = PW_NONE
        pwdata.data = 0
        
        decrypted = sec_item()
        signons = sqlite3.connect(signons_history + 'signons.sqlite')
        c = signons.cursor()
        c.execute('Select hostname,httpRealm,formSubmitURL,encryptedUsername,encryptedPassword,guid,encType from moz_logins')
        
        for row in c:
            print('Website: ' + row[0])
            username = sec_item()
            username.data = cast(c_char_p(base64.b64decode(row[3])),c_void_p)
            username.len = len(base64.b64decode(row[3]))
            libnss.PK11SDR_Decrypt(byref(username),byref(decrypted),byref(pwdata))
            print('Username: ' + string_at(decrypted.data,decrypted.len))
            password = sec_item()
            password.data = cast(c_char_p(base64.b64decode(row[4])),c_void_p)
            password.len = len(base64.b64decode(row[4]))
            libnss.PK11SDR_Decrypt(byref(password),byref(decrypted),byref(pwdata))
            print('Password: ' + string_at(decrypted.data, decrypted.len) + '\n')
            
        c.close()
        libnss.NSS_Shutdown()
        
class sec_item(Structure):
    _fields_ = [('type',c_uint),('data',c_void_p),('len',c_uint)]
        
class pw_data(Structure):
    _fields_ = [('source',c_ubyte),('data',c_char_p)]
    
