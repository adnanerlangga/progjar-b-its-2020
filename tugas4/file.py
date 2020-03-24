import os

class File:
    def __init__(self):
        if not os.path.exists('file'):
            os.makedirs('file')

    def uploadFile(self, namaFile = None, isiFile = None):
        tmp = open('file/' + namaFile, 'w')
        tmp.write(isiFile)
        return True

    def downloadFile(self, namaFile = None):
        tmp = open('file/' + namaFile, 'rb')
        isiFile = tmp.read()
        tmp.close()

        isiFile = isiFile.decode()
        return isiFile

    def listFile(self):
        listFile = os.listdir('file')
        tmp = []
        for namaFile in listFile:
            tmp.append(namaFile)
        return tmp

if __name__=='__main__':
    f = File()
