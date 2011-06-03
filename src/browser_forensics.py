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
        root = Node("firefox", 0, None, mfso)
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
                historyNode = Node("History", 0, root, mfso)
                output = f.get_history('/media/A056644956642270/Users/Alex/AppData/Roaming/Mozilla/Firefox/Profiles/dy3zdv2o.default/places.sqlite')
                
                if(len(output) == 4):
                    
                    for line in output:
                        BrowserNode(output('visited'), 0, history, mfso)
                    
            
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
   def __init__(self, name, size, parent, mfso):
      Node.__init__(self, name, size, parent, mfso)
      self.__disown__()

   def _attributes(self):
    return None

   def fileMapping(self, fm):
    pass
 
#    f = firefox_forensic(args.firefox_path)
    '''
    print('\n\nGetting Cookies\n\n')
    f.get_cookies(args.firefox_path + 'cookies.sqlite')
    print('\n\nGetting History\n\n')
    f.get_history(args.firefox_path + 'places.sqlite','count')
    print('\n\nGetting facebook\n\n')
    f.get_facebook(args.firefox_path + 'places.sqlite')
    print('\n\nGetting Downloads\n\n')
    f.get_downloads(args.firefox_path + 'downloads.sqlite')
    print('\n\nGetting Form History\n\n')
    f.get_form_history(args.firefox_path + 'formhistory.sqlite')
    print('\n\nGetting Signons\n\n')
    f.get_signons(args.firefox_path)
    '''