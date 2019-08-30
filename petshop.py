import threading, time
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from selenium import webdriver

class PetShop(threading.Thread):
    def __init__(self, search):
        threading.Thread.__init__(self)
        self.driver = webdriver.Chrome('/home/fernando/experian/chromedriver')
        self.driver.maximize_window()
        self.search = search
        
    def run(self):        
        try:
            self.driver.get('https://buscando2.extra.com.br/busca?q='+self.search)            
            product = self.driver.find_element_by_class_name('neemu-products-container')
            html = product.get_attribute('innerHTML')
            soup = BeautifulSoup(html, 'html.parser')            
            tags = soup.find_all('div', {'class': 'nm-product-info'})
            interador = 1
            for tag in tags:
                name = tag.find_all('a')[0].attrs
                for key, value in name.items():
                    if(key == 'href'):
                        if(interador > 5):
                            print(value)
                            quote_page = Request('http:'+value, headers={'User-Agent': 'Chrome/76.0.3809.68'})
                            page = urlopen(quote_page, timeout=10).read()
                            soup = BeautifulSoup(page, 'html.parser')
                            print(soup)
                        interador = interador + 1
                        #details = self.driver.find_element_by_class_name('detalhesProduto')
                        #detailsHtml = details.get_attribute('innerHTML')
                        #detailsSoup = BeautifulSoup(detailsHtml, 'html.parser')
                        ##print(detailsSoup)
                        #descriptions = detailsSoup.find_all('div', {'class': 'descricao'})
                        #print(descriptions)
                        #for tag in descriptions:
                        #    p = tag.find_all('p')
                        #    print(p)
                        #self.driver.back()
                    #if(key == 'title'):
                    #    print('Nome: ' + value)
                #cod = tag.find_all('div', {'class': 'yv-review-quickreview'})[0].attrs                
                #for key, value in cod.items():
                #    if(key == 'value'):
                #        print('Cód. Item: ' + value)
                #price = tag.find_all('span', {'class': 'nm-price-value'})
                #print('Preço: ' + price[0].get_text().strip())
                
            
                
        except Exception as e:
            print('Erro na aplicação: '+str(e))
    
def main():
    petshop = PetShop('Pet Shop')
    petshop.run()

if __name__ == '__main__':
    main()