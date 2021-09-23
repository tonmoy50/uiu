class Compression:
    def __init__(self):
        self.data = "Dummy"

    def DoCompression(self):
        return "Compressed Data" #dummy compressed data

    def SetData(self, string):
        self.data = string

class Application:
    def __init__(self):
        a1 = Compression()
        self.algo_list = [a1]  #adding a dummy compression algorithm into the application initially
        self.id = self.algo_list[0]
        self.filename = ""

    
    def AddCompressionAlgorithm(self, algo):
        self.algo_list.append(algo)

    def SelectCurrentAlgorithm(self, id):
        self.id = id

    def OpenFile(self, filename):
        self.filename = filename

    def Compression(self):
        self.id.data = self.filename
        self.id.DoCompression()

        


        