'''
@author: Alex Krepelka
@contact: f4ktu4l@securethemasses.com
'''
__dff_module_merge_version__ = "1.0.0"
'''
from struct import unpack

from api.vfs import *
from api.module.module import *
from api.types.libtypes import Variant, VList, VMap, Argument, Parameter, typeId
from api.vfs.libvfs import *
from pyQt4.QtCore import QSize, SIGNAL
from pyQt4.QtCore import QWidget
from ui.gui.utils.utils import Utils
'''
from firefox_forensic import firefox_forensic
import argparse
'''
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
          print "It seems to work"
       except IndexError:
          print "Could not get 'parent' argument."


class browser_forensics(Module):
  def __init__(self):
    Module.__init__(self, "browser_forensics", BROWSER_FORENSICS)

    # Add your argument and tags here
    self.conf.addArgument({"input": Argument.Required|Argument.Single|typeId.Node,
                           "name": "file",
                           "description": "Description of your module"})
    self.tags = "Node" 

'''
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Forensix')
    parser.add_argument('firefox_path', metavar='path',
                        help="The path to your firefox profile.")
    #parser.add_argument('')
    args = parser.parse_args()
    
    
    
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