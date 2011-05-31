'''
@author: Alex Krepelka
@contact: f4ktu4l@securethemasses.com
__dff_browser_forensics_version__ = "0.0.1"

from struct import unpack

from api.vfs import *
from api.module.module import *
from api.types.libtypes import Variant, VList, VMap, Argument, Parameter, typeId
from api.vfs.libvfs import *
from PyQt4.QtCore import QSize, SIGNAL
from PyQt4.QtGui import QWidget
from ui.gui.utils.utils import Utils

#from firefox_forensic import firefox_forensic                                                                                                                                                                      

class BROWSER_FORENSICS(Script):
    def __init__(self):
        #Module initialization goes here                                                                                                                                                                            
        Script.__init__(self, "browser_forensics")

    def c_display(self):
        print('It is working!')

    def start(self, args):
        # get your arguments here.                                                                                                                                                                                  
        # Do soemthing.                                                                                                                                                                                             
        try:
            self.parent = args["parent"].value()
            print("It seems to work")
        except IndexError:
                print("Could not get 'parent' argument.")


class browser_forensics(Module):
    def __init__(self):
        Module.__init__(self, "browser_forensics", Browser_Forensics)

    # Add your argument and tags here                                                                                                                                                                               
        self.conf.addArgument({"input": Argument.Required|Argument.Single|typeId.Node,
                               "name": "Firefox Profile Directory",
                               "description": "Location of your Firefox profile directory.",
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


class Browser_Forensics_Node(Node):
    def __init__(self, name, size, parent, mfso, firefox_profile_dir):
        Node.__init__(self, name, size, parent, mfso)
        print("Node is working!")
    
    f = firefox_forensic(args.firefox_path)
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
    '''
    print('\n\nGetting Signons\n\n')
    f.get_signons(args.firefox_path)