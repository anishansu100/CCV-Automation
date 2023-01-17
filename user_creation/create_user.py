import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grouper import add_user 
from listserv import add_listserv
from chrome import driver
url2 = "https://listserv.brown.edu/cgi-bin/wa?INDEX&X=OEBE49007A9D16C77D2&Y=anish_pradhan%40brown.edu"     
    
def main():
    add_listserv("Anishansu Pradhan", "anish_pradhan@brown.edu")
main()