'''
@author: Alex Krepelka
@contact: f4ktu4l@securethemasses.com
'''
__dff_module_browser_forensics_version__ = "1.0.0"

from struct import unpack

from api.vfs import *
from api.module.module import *
from api.types.libtypes import Variant, VList, VMap, Argument, Parameter, typeId, vtime, TIME_UNIX
from api.vfs.libvfs import *
from PyQt4.QtCore import QSize, SIGNAL
from PyQt4.QtGui import QWidget
from ui.gui.utils.utils import Utils

from firefox_forensic import firefox_forensic                                                                                                                                                                      

class browser_forensics(Module):
    
    ''' A Module to extract info from Firefox, Chrome, Safari, or Internet Explorer.'''
    
    def __init__(self):
        Module.__init__(self, "browser_forensics", Browser_Forensics)                                                                                                                                                                             
        self.conf.addArgument({"input": Argument.Optional|Argument.Single|typeId.Node,
                               "name": "profiledir",
                               "description": "Location of your browser's profile directory."
                               })
        self.conf.addArgument({"input" : Argument.Required|Argument.List|typeId.String,
                               "name" : "browser",
                               "description": "Name of browser to analyze",
                               "parameters" : { "type" : Parameter.NotEditable,
                               "predefined" : ["firefox" , "chrome" , "safari", "ie"]}
                               })
        self.conf.addArgument({"input" : Argument.Required|Argument.List|typeId.String,
                               "name" : "extract",
                               "description" : "Type of data to extract from browser.",
                               "parameters" : {"type" : Parameter.NotEditable,
                               "predefined" : ["history", "cookies", "signons", "downloads", "formhistory", "all"]}
                               })
        self.tags = "Browser"

class Browser_Forensics(mfso):

    def __init__(self):
        mfso.__init__(self, "browser_forensics")
        self.name = "browser_forensics"
        self.__disown__()

    def start(self, args):                                                                                                                                                                                             
        self.vfs = vfs.vfs()
        root = Node("firefox", 0, None, self)
        root.__disown__()
        '''
        try:
            v.getnode(args['profiledir'])
        except IndexError:
                print("Could not find " + args['profiledir'] +  "!")
                
        print("It is working!")
        '''
        
        #places = args['profiledir'] + 'places.sqlite'
        if(str(args['browser']) == '[firefox]'):
            f = firefox_forensic()
            
            
            if(str(args['extract']) == '[history]'):
                historyNode = Node("History", 0, root, self)
                historyNode.__disown__()
                output = f.get_history('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/places.sqlite')
                                 
                for line in output:
                        if(len(line) == 5):
                            
                            temp = BrowserNode(line['url'], 0, historyNode, self, 'firefox', 'history', line['last_visit'], line['visits'],line['typed'])
                                                    
                        else:
                            
                            temp = BrowserNode(line['url'], 0, historyNode, self,'firefox', 'history', 0, line['visits'], line['typed'])
                                        
            elif(str(args['extract']) == '[cookies]'):
                cookiesNode = Node("Cookies", 0, root, self)
                cookiesNode.__disown__()
                output = f.get_cookies('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/cookies.sqlite')
                
                for line in output:
                    temp = BrowserNode(line['website'], 0, cookiesNode, self,'firefox', 'cookies', line['lastAccessed'], 0, 0, line['name'], line['value'] )
            
            elif(str(args['extract']) == '[signons]'):
                signonsNode = Node("Signons", 0, root, self)
                signonsNode.__disown__()
                output = f.get_signons('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/')
               
                for line in output:
                    temp = BrowserNode(line['website'], 0, signonsNode, self, 'firefox', 'signons', 0, 0, 0, line['username'], line['password'])
                    
                    
            elif(str(args['extract']) == '[downloads]'):
                downloadsNode = Node("Downloads", 0 , root, self)
                downloadsNode.__disown__()
                output = f.get_downloads('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/downloads.sqlite')
                
                for line in output:
                    temp = BrowserNode(line['name'], 0, downloadsNode, self,'firefox', 'downloads', line['end'], 0, 0, line['url'],line['location'], line['start'])
            
            elif(str(args['extract']) == '[formhistory]'):
                formhistoryNode = Node("Downloads", 0 , root, self)
                formhistoryNode.__disown__()
                output = f.get_form_history('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/formhistory.sqlite')
                
                for line in output:
                    temp = BrowserNode(line['fieldname'], 0, formhistoryNode, self,'firefox', 'formhistory', line['lastUsed'], 0, 0, line['value'],line['timesUsed'])
            
                
            
            elif(str(args['extract']) == '[all]') :

                historyNode = Node("History", 0, root, self)
                historyNode.__disown__()
                output = f.get_history('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/places.sqlite')
                                 
                for line in output:
                        if(len(line) == 5):
                            
                            temp = BrowserNode(line['url'], 0, historyNode, self, 'firefox', 'history', line['last_visit'], line['visits'],line['typed'])
                                                    
                        else:
                            
                            temp = BrowserNode(line['url'], 0, historyNode, self,'firefox', 'history', 0, line['visits'], line['typed'])
                                        

                cookiesNode = Node("Cookies", 0, root, self)
                cookiesNode.__disown__()
                output = f.get_cookies('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/cookies.sqlite')
                
                for line in output:
                    temp = BrowserNode(line['website'], 0, cookiesNode, self,'firefox', 'cookies', line['lastAccessed'], 0, 0, line['name'], line['value'] )
            

                signonsNode = Node("Signons", 0, root, self)
                signonsNode.__disown__()
                output = f.get_signons('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/')
               
                for line in output:
                    temp = BrowserNode(line['website'], 0, signonsNode, self, 'firefox', 'signons', 0, 0, 0, line['username'], line['password'])
                    
                    

                downloadsNode = Node("Downloads", 0 , root, self)
                downloadsNode.__disown__()
                output = f.get_downloads('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/downloads.sqlite')
                
                for line in output:
                    temp = BrowserNode(line['name'], 0, downloadsNode, self,'firefox', 'downloads', line['end'], 0, 0, line['url'],line['location'], line['start'])
            

                formhistoryNode = Node("Form History", 0 , root, self)
                formhistoryNode.__disown__()
                output = f.get_form_history('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/formhistory.sqlite')
                
                for line in output:
                    temp = BrowserNode(line['fieldname'], 0, formhistoryNode, self,'firefox', 'formhistory', line['lastUsed'], 0, 0, line['value'],line['timesUsed'])
            
        
        elif(str(args['browser']) == 'chrome'):
            pass
            '''    
            if(str(args['extract']) == '[history]'):
                output = f.get_history('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/places.sqlite')
                i = 0
                while i < 20:
                    print(output[i])
                    i = i+1
            
            elif(str(args['extract']) == '[cookies]'):
                output = f.get_cookies('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/cookies.sqlite')
                i = 0
                while i < 20:
                    print(output[i])
                    i = i+1
            
            elif(str(args['extract']) == '[signons]'):
                output = f.get_signons('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/signons.sqlite')
                i = 0
                while i < 20:
                    print(output[i])
                    i = i+1
            elif(str(args['extract']) == '[downloads]'):
                output = f.get_cookies('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/downloads.sqlite')
                i = 0
                while i < 20:
                    print(output[i])
                    i = i+1
            
            elif(str(args['extract']) == '[formhistory]'):
                output = f.get_form_history('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/formhistory.sqlite')
                i = 0
                while i < 20:
                    print(output[i])
                    i = i+1
            else :
                f.get_history('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/places.sqlite')
                f.get_history('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/cookies.sqlite')
                f.get_history('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/signons.sqlite')
                f.get_history('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/downloads.sqlite')
                f.get_history('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/formhistory.sqlite')
            '''
        
        elif(str(args['browser']) == 'safari'):
            pass
            ''' 
            if(str(args['extract']) == '[history]'):
                output = f.get_history('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/places.sqlite')
                i = 0
                while i < 20:
                    print(output[i])
                    i = i+1
            
            elif(str(args['extract']) == '[cookies]'):
                output = f.get_cookies('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/cookies.sqlite')
                i = 0
                while i < 20:
                    print(output[i])
                    i = i+1
            
            elif(str(args['extract']) == '[signons]'):
                output = f.get_signons('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/signons.sqlite')
                i = 0
                while i < 20:
                    print(output[i])
                    i = i+1
            elif(str(args['extract']) == '[downloads]'):
                output = f.get_cookies('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/downloads.sqlite')
                i = 0
                while i < 20:
                    print(output[i])
                    i = i+1
            
            elif(str(args['extract']) == '[formhistory]'):
                output = f.get_form_history('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/formhistory.sqlite')
                i = 0
                while i < 20:
                    print(output[i])
                    i = i+1
            else :
                f.get_history('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/places.sqlite')
                f.get_history('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/cookies.sqlite')
                f.get_history('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/signons.sqlite')
                f.get_history('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/downloads.sqlite')
                f.get_history('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/formhistory.sqlite')
                '''
        elif(str(args['browser']) == 'ie') :
            pass
        
        '''
                        
            if(str(args['extract']) == '[history]'):
                output = f.get_history('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/places.sqlite')
                i = 0
                while i < 20:
                    print(output[i])
                    i = i+1
            
            elif(str(args['extract']) == '[cookies]'):
                output = f.get_cookies('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/cookies.sqlite')
                i = 0
                while i < 20:
                    print(output[i])
                    i = i+1
            
            elif(str(args['extract']) == '[signons]'):
                output = f.get_signons('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/signons.sqlite')
                i = 0
                while i < 20:
                    print(output[i])
                    i = i+1
            elif(str(args['extract']) == '[downloads]'):
                output = f.get_cookies('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/downloads.sqlite')
                i = 0
                while i < 20:
                    print(output[i])
                    i = i+1
            
            elif(str(args['extract']) == '[formhistory]'):
                output = f.get_form_history('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/formhistory.sqlite')
                i = 0
                while i < 20:
                    print(output[i])
                    i = i+1
            else :
                f.get_history('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/places.sqlite')
                f.get_history('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/cookies.sqlite')
                f.get_history('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/signons.sqlite')
                f.get_history('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/downloads.sqlite')
                f.get_history('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/formhistory.sqlite')
                '''
        
        
        rootVfs = self.vfs.getnode('/')
        self.registerTree(rootVfs, root)
        
        
class BrowserNode(Node):
    def __init__(self, name, size, parent, mfso, browser, extract, timestamp = 0, data = 0, data1 = 0 , data2 = 0, data3 = 0, data4 = 0): # don't forget to add profile_dir
        Node.__init__(self, name, size, parent, mfso)

        #self.profile_dir = profile_dir
        self.data = data
        self.data1 = data1
        self.data2 = data2
        self.data3 = data3
        self.data4 = data4
        self.timestamp = long(timestamp)
        self.extract = extract
        self.browser = browser
        self.__disown__()
        
        
        
    def _attributes(self):
        
        vt = vtime(long(self.timestamp/1e6), TIME_UNIX)
        vt.thisown = False
        
        v_vt = Variant(vt)
        #v_profile_dir = Variant(self.profile_dir())
        v_data = Variant(self.data)
        v_data1 = Variant(self.data1)
        v_data2 = Variant(self.data2)
        v_data3 = Variant(self.data3)
        v_data4 = Variant(self.data4)
                
        v_vt.thisown = False
        #v_profile_dir.thisown = False
        v_data.thisown = False
        v_data1.thisown = False
        v_data2.thisown = False
        v_data3.thisown = False
        v_data4.thisown = False
        
        attr = VMap()
        attr.thisown = False
        
        
        #attr["profile directory"] = v_profile_dir
        if (self.browser == 'firefox'):
            
            if(self.extract == 'history'):
                attr['accessed'] = v_vt
                attr['visit count'] = v_data
                attr['typed'] = v_data1
                return attr
            
            elif(self.extract == 'cookies'):
                attr['name'] = v_data2
                attr['cookie'] = v_data3
                attr['accessed'] = v_vt
                return attr
            
            elif(self.extract == 'downloads'):
                attr['url'] = v_data2
                attr['location'] = v_data3
                #attr['start'] = v_data2
                attr['finished'] = v_vt
                return attr
            
            elif(self.extract == 'signons'):
                attr['username'] = v_data2
                attr['password'] = v_data3
                return attr
            
            elif(self.extract == 'formhistory'):
                attr['input'] = v_data2
                attr['times used'] = v_data3
                attr['last used'] = v_vt
                return attr
            
                
    def fileMapping(self, fm):
        pass
