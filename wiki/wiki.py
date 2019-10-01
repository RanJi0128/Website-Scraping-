
from time      import sleep
import xlwt 
from xlwt import Workbook

from bs4 import BeautifulSoup
import requests
from datetime import date
def write_xls_header(filename):
    wb = Workbook() 
    sheet1 = wb.add_sheet('Sheet 1')
    sheet1.write(0, 0, 'Surname/Name')
    sheet1.write(0, 1, 'Language Link Name') 
    sheet1.write(0, 2, 'Link example') 
    wb.save(filename+'.xls')
    return wb,sheet1


def write_xlsx(wb,sheet1,data,index,file):  
  sheet1.write(index, 0, data[0])
  sheet1.write(index, 1, data[1]) 
  sheet1.write(index, 2, data[2]) 
  wb.save(file+'.xls') 

def main(url):
    index = 1
    wb, sheet1 = write_xls_header("surnames")
    response = requests.get(url, timeout = 5)
    soup = BeautifulSoup(response.text, 'lxml')
    As = soup.find_all('a',{'class', 'CategoryTreeLabelNs14'})
    for a in As:        
        sub_url = "https://en.wikipedia.org"+a['href']
        name = a.text
        print("***********************"+name)
        print(index)
        index = recurrent(sub_url, name, index,wb, sheet1)
        
        # print(sub_url)
def recurrent(url, name, index, wb, sheet1):
    val = ''
    response = requests.get(url, timeout = 5)
    soup = BeautifulSoup(response.text, 'lxml')
    divs = soup.find_all('div',{'class', "mw-category-group"})
    for div in divs:
        lis = div.find_all('li')
        for li in lis:
            a = li.find('a')
            if  a.text.find("surnames") > -1 or a.text.find("Surnames") > -1 or a.text.find("names") > -1:
                index = sub_getdata("https://en.wikipedia.org"+a['href'], a.text,index, wb, sheet1)
            else:
                if len(li.text.split(" ")) <= 2 and len(li.text) > 2:
                    write_xlsx(wb, sheet1, [name,li.text,response.url], index,"surnames")
                    index = index + 1
    sub_divs = soup.find_all('div',{'class':'mw-content-ltr'})
    for sub_div in sub_divs:
        lis = sub_div.find_all('li')
        for li in lis:           
            if  li.text.find("surnames") > -1 or li.text.find("Surnames") > -1 or li.text.find("names") > -1:
                pass
            else:
                if len(li.text.split(" ")) <= 2 and len(li.text) > 2:
                    write_xlsx(wb, sheet1, [name,li.text,response.url], index,"surnames")
                    index = index + 1
                    print("-----------------"+li.text)
    return index
def sub_getdata(url, name,index, wb, sheet1):
    val = ''
    print("*************************"+name)
    response = requests.get(url, timeout = 5)
    soup = BeautifulSoup(response.text, 'lxml')
    divs = soup.find_all('div',{'class', "mw-category-group"})
    for div in divs:
        lis = div.find_all('li')
        for li in lis:
            a = li.find('a')
            if  a.text.find("surnames") > -1 or a.text.find("Surnames") > -1 or a.text.find("names") > -1:
                index = sub_getdatas("https://en.wikipedia.org"+a['href'],a.text, index ,wb, sheet1)
                
            else:
                if len(li.text.split(" ")) <= 2 and len(li.text) > 2:
                    write_xlsx(wb, sheet1, [name,a.text,response.url], index,"surnames")
                    index = index + 1
    sub_divs = soup.find_all('div',{'class':'mw-content-ltr'})
    for sub_div in sub_divs:
        lis = sub_div.find_all('li')
        for li in lis:           
            if  li.text.find("surnames") > -1 or li.text.find("Surnames") > -1 or li.text.find("names") > -1:
                pass
            else:
                if len(li.text.split(" ")) <= 2 and len(li.text) > 2:
                    write_xlsx(wb, sheet1, [name,li.text,response.url], index,"surnames")
                    index = index + 1
    return index
def sub_getdatas(url, name,index, wb, sheet1):
    val = ''
    print(name)
    response = requests.get(url, timeout = 5)
    soup = BeautifulSoup(response.text, 'lxml')
    divs = soup.find_all('div',{'class', "mw-category-group"})
    for div in divs:
        lis = div.find_all('li')
        for li in lis:
            a = li.find('a')
            if  a.text.find("surnames") > -1 or a.text.find("Surnames") > -1 or a.text.find("names") > -1:
                # sub_getdata("https://en.wikipedia.org"+a['href'],index, a.text,wb, sheet1)
                pass
            else:
                if len(li.text.split(" ")) <= 2 and len(li.text) > 2:
                    write_xlsx(wb, sheet1, [name,a.text,response.url], index,"surnames")
                    index = index + 1
    sub_divs = soup.find_all('div',{'class':'mw-content-ltr'})
    for sub_div in sub_divs:
        lis = sub_div.find_all('li')
        for li in lis:           
            if  li.text.find("surnames") > -1 or li.text.find("Surnames") > -1 or li.text.find("names") > -1:
                pass
            else:
                if len(li.text.split(" ")) <= 2 and len(li.text) > 2:
                    write_xlsx(wb, sheet1, [name,li.text,response.url], index,"surnames")
                    index = index + 1
    return index
    # As = soup.find_all("a",{"class":"CategoryTreeLabelNs14"})
    # if len(As)  ==  0:
    #     for a in As:
    #         print("***********************************"+a.text)
            # get_data("https://en.wikipedia.org"+a['href'])
    

    #     get_data(divs)
    # except Exception as e:
    #     divs = soup.find_all('div',{'class', 'CategoryTreeItem'})
    #     for div in divs:
    #         sub_url = "https://en.wikipedia.org"+div.find('a')['href']
    #         recurrent(sub_url)







if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Category:Surnames_by_language"
    main(url)