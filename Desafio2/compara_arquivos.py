import threading

class Arquivo(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print('oi')






def main():
    arquivo = Arquivo()
    arquivo.run()

if __name__ == '__main__':
    main()