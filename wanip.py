##PULL_WAN_IP can include on line one (optional) - #!/usr/bin/env python3

import bs4, os, sys, time
from bs4 import BeautifulSoup

def main(tmp_space, pull_wanip):
    earl_file = open(tmp_space)
    earl_bs4 = BeautifulSoup(earl_file, 'html5lib')
    wanip = earl_bs4.findAll(class_="lookup")
    wanip = (wanip[0].get_text())
    wanip = (str(wanip).split('[')[0])
    return wanip

def rec_data(file_space, wanip):
    persist_file = open(file_space, 'w')
    #persist_file.write('#NEW_RECORD'+'\n') #Uncomment to include New Record REM
    #persist_file.write(('#TIMESTAMP ')+str(time.ctime())+'\n') #Uncomment to include Timestamp
    persist_file.write(wanip) #IP ADDRESS VARIABLE
    persist_file.close()

if __name__ == '__main__':
    pull_wanip = 'http://ip-address.org'
    tmp_space = '/tmp/wanip.tmp' #can remain /tmp/
    file_space = '/tmp/data.ip' #change to desired /dir/space/data.ip
    gets = ('wget -S '+pull_wanip+' -O '+tmp_space)
    os.system(gets)
    wanip = main(tmp_space, pull_wanip)
    rec_data(file_space, wanip)
