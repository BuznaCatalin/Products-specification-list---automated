from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


filename = 'products.csv'
f = open(filename, 'w')

headers = 'brand, stock, price \n'

f.write(headers)


for j in range(2, 12):
    my_url = f'https://www.emag.ro/search/placi+video/p{j}'

    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, 'html.parser')

    containers = page_soup.findAll('div', {'class': 'card-item js-product-data'})


    for i in range(len(containers)):

        div_with_info =  containers[i].find("div","card-section-mid")
        brand = div_with_info.a['title']

        div_with_info2 = containers[i].find("div", 'card-body')
        stock = div_with_info2.p.get_text()

        div_with_info3 = containers[i].find('p', 'product-new-price')
        price = div_with_info3.get_text()

        print('brand: ' + brand)
        print('stock:' + stock)
        print('price:' + price)

        f.write(brand.replace(',','|') + ',' + stock + ',' + price + '\n')


f.close()






