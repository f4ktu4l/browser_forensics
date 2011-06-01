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

class BROWSER_FORENSICS(Script):
    def __init__(self):
        #Module initialization goes here                                                                                                                                                                            
        Script.__init__(self, "browser_forensics")
        self.vfs = vfs.vfs()
        
    #def c_display(self):
        #print('It is working!')

    def start(self, args):                                                                                                                                                                                             
        try:
            for i in args:
                print(i)
                
            print("It seems to work")
        
        except IndexError:
                print("Could not get 'parent' argument.")
    
#    def browser_forensics


class browser_forensics(Module):
    def __init__(self):
        Module.__init__(self, "browser_forensics", BROWSER_FORENSICS)                                                                                                                                                                             
        self.conf.addArgument({"input": Argument.Required|Argument.Single|typeId.String,
                               "name": "profiledir",
                               "description": "Location of your Firefox profile directory."
                               })
        self.conf.addArgument({"input": Argument.Required|Argument.Single|typeId.String,
                               "name": "browser",
                               "description": "Firefox, Chrome, Safari, IE"
                               })
        self.tags = "Node"



class Browser_Forensics(mfso):

    def __init__(self):
        mfso.__init__(self, "browser_forensics")
        self.name = "browser_forensics"
        self.__disown__()
        print("MFSO is working!")

    def start(self,args):
        print("It is working!")
        f = firefox_forensic(args['profiledir'].value())
        print('\n\nGetting facebook\n\n')
        f.get_facebook(args['profiledir'] + 'places.sqlite')


class Browser_Forensics_Node(Node):
    def __init__(self, name, size, parent, mfso, firefox_profile_dir):
        Node.__init__(self, name, size, parent, mfso)
        print("Node is working!")
 
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