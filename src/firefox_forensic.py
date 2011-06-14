'''
Created on May 3, 2011

@author: alex
'''
import sqlite3,datetime,re,base64,struct
from ctypes import *

class firefox_forensic(object):

    def __init__(self):
        print("Browser Forensics is fun!")
        
    def get_cookies(self,cookies_file):
        cookies = sqlite3.connect(cookies_file)
        c = cookies.cursor()
        c.execute('select name,value,host,lastAccessed from moz_cookies')
        cookies_container = []
        for row in c:
            temp = {'website' :  row[2].encode('utf-8'), 'name' : row[0].encode('utf-8'), 'value' : row[1].encode('utf-8'), 'lastAccessed' : row[3]}
            cookies_container.append(temp)
        c.close()
        return cookies_container
        
    def get_cache(self,cache_dir):
        pass
        '''cache_map = open(cache_dir + '_CACHE_MAP_', 'rb')
        #get the header of the _CACHE_MAP_ file
        header = cache_map.read(20)
        ver,data_size,entry_count,is_dirty,record_count = struct.unpack('>5l',header)
        
        print('Version: %d' % ver)
        print('Data Size: %d' % data_size)
        print('Entry Count: %d' % entry_count)
        print('Dirty: %d' % is_dirty)
        print('Record Count: %d' % record_count)
        '''
    
    def get_history(self,history_file,sort_method = 'date',*keywords):
        history = sqlite3.connect(history_file)
        c = history.cursor()
        c.execute('select title,url,visit_count,typed,last_visit_date from moz_places')
        sorted = []
        history_container = []
        
        for row in c:
                temp = str(row[2]),row[0],row[1],str(row[3]),row[4]
                sorted.append(temp)
            
        sorted.sort()
        sorted.reverse()

        for i in sorted:
            if(i[4] != None):
                temp = {'name' : i[1].encode('utf-8'),'url' : i[2].encode('utf-8') , 'typed' : i[3] , 'visits' : i[0], 'last_visit' : i[4]}
                    
            else:
                
                temp = {'name' : i[1].encode('utf-8'), 'url' : i[2].encode('utf-8') , 'typed' : i[3] ,'visits' : i[0]}
                    
            history_container.append(temp)
            
        c.close()
        return history_container
    
    def get_downloads(self,download_file):
        downloads = sqlite3.connect(download_file)
        c = downloads.cursor()
        c.execute('select name,source,target,startTime,endTime from moz_downloads')
        downloads_container = []
        
        for row in c:
                temp = 'Download Name: ' + row[0].encode('utf-8') + '\n' + 'URL: ' + row[1].encode('utf-8') + '\n' + 'Location: ' + row[2].encode('utf-8') + '\n' + 'Start: ' + str(datetime.datetime.fromtimestamp(row[3]/1e6)) + ' End: ' + str(datetime.datetime.fromtimestamp(row[4]/1e6)) + '\n'
                downloads_container.append(temp)
        c.close()
        return downloads_container
    
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
        
        return sorted
            
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
        signons_container = []
        
        for row in c:
            temp = 'Website: ' + row[0] + '\n'
            username = sec_item()
            username.data = cast(c_char_p(base64.b64decode(row[3])),c_void_p)
            username.len = len(base64.b64decode(row[3]))
            libnss.PK11SDR_Decrypt(byref(username),byref(decrypted),byref(pwdata))
            temp += 'Username: ' + string_at(decrypted.data,decrypted.len) + '\n'
            password = sec_item()
            password.data = cast(c_char_p(base64.b64decode(row[4])),c_void_p)
            password.len = len(base64.b64decode(row[4]))
            libnss.PK11SDR_Decrypt(byref(password),byref(decrypted),byref(pwdata))
            temp += 'Password: ' + string_at(decrypted.data, decrypted.len) + '\n'
            signons_container.append(temp)
        
        c.close()
        libnss.NSS_Shutdown()
        return signons_container
    
class sec_item(Structure):
    _fields_ = [('type',c_uint),('data',c_void_p),('len',c_uint)]
        
class pw_data(Structure):
    _fields_ = [('source',c_ubyte),('data',c_char_p)]
    