#!/opt/local/bin/python

# download comic by specify the first and last pages
# individual file could be download by >curl
import urllib
import sys
import numpy as np
from subprocess import call

def getcomic(url,begin,end):
    id = range(begin,end)
    for i in id:
        web = url+'{0:{fill}2}'.format(i,fill='0')+'.jpg'
        out = '{0:{fill}2}'.format(i,fill='0')+'.jpg'
        urllib.urlretrieve(web,out)

if __name__ == '__main__':
    getcomic(sys.argv[1],np.int_(sys.argv[2]),np.int_(sys.argv[3])+1)
    command = 'zip '+sys.argv[4]+' *.jpg'
    call(command,shell=True)