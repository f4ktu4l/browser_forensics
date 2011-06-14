'''
@author: Alex Krepelka
@contact: f4ktu4l@securethemasses.com
'''
__dff_module_browser_forensics_version__ = "1.0.0"

from struct import unpack

from api.vfs import *
from api.module.module import *
from api.types.libtypes import Variant, VList, VMap, Argument, Parameter, typeId
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
                               "predefined" : ["history", "cookies", "signons", "downloads", "formhistory", "cache", "all"]}
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
                            
                            temp = BrowserNode(line['url'], 0, historyNode, self,line['visits'],line['typed'],line['last_visit'])
                                                    
                        else:
                            
                            temp = BrowserNode(line['url'], 0, historyNode, self,line['visits'], line['typed'])
                                        
            elif(str(args['extract']) == '[cookies]'):
                cookiesNode = Node("Cookies", 0, root, self)
                cookiesNode.__disown__()
                output = f.get_cookies('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/cookies.sqlite')
                
                for line in output:
                    temp = BrowserNode(line['website'], 0, cookiesNode,self)
            
            elif(str(args['extract']) == '[signons]'):
                signonsNode = Node("Signons", 0, root, self)
                signonsNode.__disown__()
                output = f.get_signons('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/signons.sqlite')
               
                for line in output:
                    
                    temp = BrowserNode(line['hostname'], 0, signonsNode, self)
                    
                    
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
            
            elif(str(args['extract']) == '[cache]'):
                output = f.get_cache('/media/be036205-1329-4a4c-b2eb-8bff8ed32a11/home/alex/.mozilla/firefox/vkuuxfit.default/Cache/')
                
            
            else :
                f.get_history('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/places.sqlite')
                f.get_history('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/cookies.sqlite')
                f.get_history('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/signons.sqlite')
                f.get_history('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/downloads.sqlite')
                f.get_history('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/formhistory.sqlite')
        
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
    def __init__(self, name, size, parent, mfso, visit_count = 0, typed = 0 , timestamp = 0, data = 0): # don't forget to add profile_dir
        Node.__init__(self, name, size, parent, mfso)

        #self.profile_dir = profile_dir
        self.data = data
        #self.timestamp = timestamp
        self.visit_count = visit_count
        self.typed = typed
        self.__disown__()
        
    def _attributes(self):
       
               
        #dt = datetime.datetime.fromtimestamp(self.timestamp/1e6)
        #vt = VTime(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
        
        
        #v_vt = Variant(vt)
        #v_profile_dir = Variant(self.profile_dir())
        v_data = Variant(self.data)
        v_visit_count = Variant(self.visit_count)
        v_typed = Variant(self.typed)
        
        #v_vt.thisown = False
        #v_profile_dir.thisown = False
        v_data.thisown = False
        v_visit_count.thisown = False
        v_typed.thisown = False
        
        attr = VMap()
        attr.thisown = False
        
        
        #attr["profile directory"] = v_profile_dir
        attr['data'] = v_data
        #attr['accessed'] = v_vt
        attr['visit count'] = v_visit_count
        attr['typed'] = v_typed
        return attr

    def fileMapping(self, fm):
        pass
