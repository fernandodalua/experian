import threading, time, csv
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from selenium import webdriver

class PetShop(threading.Thread):
    def __init__(self, search):
        threading.Thread.__init__(self)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.search = search
        
    def run(self):        
        try:
            pages = 1
            while(pages <= 20):
                url = 'https://buscando2.extra.com.br/busca?q='+self.search+'&page='+str(pages)
                self.driver.get(url)            
                product = self.driver.find_element_by_class_name('neemu-products-container')
                html = product.get_attribute('innerHTML')
                soup = BeautifulSoup(html, 'html.parser')            
                tags = soup.find_all('div', {'class': 'nm-product-info'})
                nome = ''
                codigo = ''
                preco = ''
                descricao = ''
                fieldnames = ['Nome', 'Cod', 'Preco', 'Detalhes']
                row = {}
                for tag in tags:
                    name = tag.find_all('a')[0].attrs
                    for key, value in name.items():
                        if(key == 'title'):                            
                            nome = value
                        if(key == 'href'):                                                    
                            descricao = value
                            
                            #TRECHO RESPONSÁVEL POR ENTRAR NAS PÁGINAS PARA CAPTURAR OS DETALHES DO PRODUTO
                            
                            #self.driver.get(value)
                            #details = self.driver.find_element_by_class_name('detalhesProduto')
                            #detailsHtml = details.get_attribute('innerHTML')
                            #detailsSoup = BeautifulSoup(detailsHtml, 'html.parser')                        
                            #descriptions = detailsSoup.find_all('div', {'class': 'descricao'})
                            #print(descriptions)
                            #for tag in descriptions:
                            #    p = tag.find_all('p')
                            #    print(p)                        
                        
                    cod = tag.find_all('div', {'class': 'yv-review-quickreview'})[0].attrs                
                    for key, value in cod.items():
                        if(key == 'value'):                            
                            codigo = value
                    price = tag.find_all('span', {'class': 'nm-price-value'})                    
                    preco = price[0].get_text().strip()
                    row = {
                            "Nome": nome,
                            "Cod": int(codigo),
                            "Preco": preco,
                            "Detalhes": descricao.replace('//www', 'http://www')
                        }
                    csvfile = open('petshop.csv', 'a', newline='')
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
                    writer.writerow(row)
                print('Acessando a página: ' + str(pages))
                pages = pages + 1
                
        except Exception as e:
            print('Erro na aplicação: '+str(e))
    
def main():
    petshop = PetShop('Pet Shop')
    petshop.run()

if __name__ == '__main__':
    main()