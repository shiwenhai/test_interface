__author__ = 'songqi'

class dataTmp():
    def __init__(self, dataName):
        self.name = dataName
        self.tmp ={}

    def modifyTmp(self, k, v):
        self.tmp[k] = v

    def getTmp(self):
        return self.tmp

if __name__ == '__main__':

    print dataTest.getTmp()

