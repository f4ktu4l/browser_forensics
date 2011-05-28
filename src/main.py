'''
Created on May 3, 2011

@author: alex
'''
from firefox_forensic import firefox_forensic
import argparse

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Forensix')
    parser.add_argument('firefox_path', metavar='path',
                        help="The path to your firefox profile.")
    args = parser.parse_args()
    f = firefox_forensic(args.firefox_path)
    #f.get_cookies(args.firefox_path + 'cookies.sqlite')
    #f.get_history(args.firefox_path + 'places.sqlite')
    #f.get_facebook(args.firefox_path + 'places.sqlite')
    #f.get_downloads(args.firefox_path + 'downloads.sqlite')
    f.get_form_history(args.firefox_path + 'formhistory.sqlite')