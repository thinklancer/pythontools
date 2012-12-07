# download comic by specify the first and last pages
import urllib

def getcomic(url,begin,end):
    id = range(begin,end)
    for i in id:
        web = url+'{0:{fill}3}'.format(i,fill='0')+'.jpg'
        out = '{0:{fill}3}'.format(i,fill='0')+'.jpg'
        urllib.urlretrieve(web,out)

if __name__ == '__main__':
    getcomic('http://imgfast.manhua.178.com/i/Is/Vol_01/',1,97)
