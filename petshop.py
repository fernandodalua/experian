import threading, time
from bs4 import BeautifulSoup
from selenium import webdriver

class PetShop(threading.Thread):
    def __init__(self, search):
        threading.Thread.__init__(self)
        self.driver = webdriver.Chrome()
        self.search = search
        
    def run(self):        
        try:
            self.driver.get('https://buscando2.extra.com.br/busca?q='+self.search)
            time.sleep(5)
            product = self.driver.find_element_by_class_name('neemu-products-container')
            html = product.get_attribute('innerHTML')
            soup = BeautifulSoup(html, 'html.parser')
            #print(soup)
            tags = soup.find_all('div', {'class': 'nm-product-info'})            
            for tag in tags:
            #    if(len(tag.getText()) > 0):                                       
                 print(tag) #.getText().lstrip('\n')
            
            
            #res = BeautifulSoup(html.read(),"html5lib")
            #tags = res.findAll("h3", {"class": "post-title"})
            #for tag in tags:
            #    print(tag.getText()
                
        except Exception as e:
            print('Erro na aplicação: '+str(e))
    
def main():
    petshop = PetShop('Pet Shop')
    petshop.run()

if __name__ == '__main__':
    main()