import threading, sys

class Arquivo(threading.Thread):
    def __init__(self, param):
        threading.Thread.__init__(self)
        self.param = param

    def run(self):
        with open(self.param[1], 'r') as t1, open(self.param[2], 'r') as t2:
            fileOne = t1.readlines()
            fileTwo = t2.readlines()

        with open('saida.csv', 'w') as outFile:
            for line in fileTwo:
                if line in fileOne:
                    outFile.write(line)

        t1.close()
        t2.close()
        outFile.close()
        print('Arquivos comparados com sucesso')


def main():
    param = []    
    for parametro in sys.argv:
        print(parametro)        
        param.append(parametro)                
        
    arquivo = Arquivo(param)
    arquivo.run()

if __name__ == '__main__':
    main()