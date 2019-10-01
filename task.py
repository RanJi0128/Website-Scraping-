import xlwt
from xlwt import Workbook
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys


url = "https://www.bluenile.com/diamond-search"
driver = webdriver.Chrome()
driver.implicitly_wait(150)
driver.get(url)
#element = WebDriverWait(driver, 10).until(
#time.sleep(15)

driver.find_element_by_xpath('//*[@id="react-app"]/div/div/div/section[1]/div[1]/div[2]/div[3]/div[4]/div[2]/div/div/div[1]/div/div/label').click()
count = 2
while (count <= 10):
    filter_xpath = "//*[@id='react-app']/div/div/div/section[1]/div[1]/div[2]/div[3]/div[6]/div[2]/div/div["
    filter_xpath += str(count)
    filter_xpath += "]/div[3]";
    driver.find_element_by_xpath(filter_xpath).click()
    count = count + 1
driver.find_element_by_xpath('//*[@id="react-app"]/div/div/div/section[1]/div[1]/div[2]/div[3]/div[13]').click()

#driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)

driver.find_element_by_xpath('//*[@id="react-app"]/div/div/div/section[1]/div[1]/div[2]/div[3]/div[7]/div[2]/div/div[1]/input[1]').clear()
driver.find_element_by_xpath('//*[@id="react-app"]/div/div/div/section[1]/div[1]/div[2]/div[3]/div[7]/div[2]/div/div[1]/input[1]').send_keys("695")
driver.find_element_by_xpath('//*[@id="react-app"]/div/div/div/section[1]/div[1]/div[2]/div[3]/div[4]/div[2]/div/div/div[1]/div/div/label').click()
driver.find_element_by_xpath('//*[@id="react-app"]/div/div/div/section[1]/div[1]/div[2]/div[3]/div[4]/div[2]/div/div/div[1]/div/div/label').click()
#driver.find_element_by_tag_name('body').send_keys(Keys.END)
time.sleep(7)
count = 1
while (count <= 6):
    filter_xpath = '//*[@id="react-app"]/div/div/div/section[1]/div[1]/div[2]/div[3]/div[12]/div['
    filter_xpath += str(count)
    filter_xpath += ']/div[1]/div/div/div/div';
    driver.find_element_by_xpath(filter_xpath).click()
    count = count + 1
#driver.find_element_by_tag_name('body').send_keys(Keys.END)
#time.sleep(15)



wb = Workbook()
sheet1 = wb.add_sheet('diamond')
#sheet1.write(0, 0, 'No')
sheet1.write(0, 1, 'Shape')
sheet1.write(0, 2, 'Price')
sheet1.write(0, 3, 'Carat')
sheet1.write(0, 4, 'Clarity')
sheet1.write(0, 5, 'Cut')
sheet1.write(0, 6, 'Color')
sheet1.write(0, 7, 'Url to diamond')
sheet1.write(0, 8, 'Fluorescence')
sheet1.write(0, 9, 'Table')
sheet1.write(0, 10, 'Polish')
sheet1.write(0, 11, 'L/W Ratio')
sheet1.write(0, 12, 'Depth')
sheet1.write(0, 13, 'Symmetry')
wb.save('diamond.xls')

row = 2
#ttt = 1009
list = ['','',0,'',0.0,0.0,'','','','','',0.0,'',0.0,0.0,'']
#list = []
while (row <=1000):
    #column = 1
    path_row = '//*[@id="react-app"]/div/div/div/section[1]/section/div/div/div[2]/a['
    path_row += str(row)
    path_row += ']'

    col = 2
    while (col <= 13):
        flag = 0
        temp = path_row
        path_col = '/div['
        path_col += str(col)
        path_col += ']'
        temp += path_col
        if(col == 2):
            temp += '/div/span[2]'
            flag = 1
        if(col == 5):
            temp += '/div/span[1]'
            flag = 1
        if(flag == 0):
            temp += '/span'
        list[col] = driver.find_element_by_xpath(temp).text
        #print (temp)
        col = col + 1

    #print ('\n')
#    sheet1.write(row, 0, row)
    sheet1.write(row, 1, list[2])
    sheet1.write(row, 2, list[3])
    sheet1.write(row, 3, list[4])
    sheet1.write(row, 4, list[7])
    sheet1.write(row, 5, list[5])
    sheet1.write(row, 6, list[6])
    sheet1.write(row, 7, driver.find_element_by_xpath(path_row).get_attribute("href"))
    sheet1.write(row, 8, list[10])
    sheet1.write(row, 9, list[12])
    sheet1.write(row, 10, list[8])
    sheet1.write(row, 11, list[13])
    sheet1.write(row, 12, list[11])
    sheet1.write(row, 13, list[9])
    wb.save('diamond.xls')
    row = row + 1
    if row%15 == 0:
        if row < 1002:
            driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        #sheet1.write(row, col, driver.find_element_by_xpath(path).text)





#output = driver.find_element_by_xpath('//*[@id="react-app"]/div/div/div/section[1]/section/div/div/div[2]/a[1000]/div[2]').text
#print (output)

#python_div = driver.find_element_by_class_name('grid-body') #FHSU
#print (strdriver.find_element_by_xpath("//*[@id='react-app']/div/div/div/section[1]/section/div/div/div[2]/a[1]/div[3]/span").text())

"""
//*[@id="react-app"]/div/div/div/section[1]/section/div/div/div[2]/a[1]
    //*[@id="react-app"]/div/div/div/section[1]/section/div/div/div[2]/a[1]/div[2]/div/span[2]
    //*[@id="react-app"]/div/div/div/section[1]/section/div/div/div[2]/a[10]/div[2]/div/span[2]
    //*[@id="react-app"]/div/div/div/section[1]/section/div/div/div[2]/a[1]/div[2]/div/span[2]
    //*[@id="react-app"]/div/div/div/section[1]/section/div/div/div[2]/a[1]/div[3]/span
    //*[@id="react-app"]/div/div/div/section[1]/section/div/div/div[2]/a[1]/div[4]/span
    //*[@id="react-app"]/div/div/div/section[1]/section/div/div/div[2]/a[1]/div[5]/div/span[1]
    //*[@id="react-app"]/div/div/div/section[1]/section/div/div/div[2]/a[1]/div[6]
    //*[@id="react-app"]/div/div/div/section[1]/section/div/div/div[2]/a[1]/div[7]/span
    //*[@id="react-app"]/div/div/div/section[1]/section/div/div/div[2]/a[1]/div[8]/span
    //*[@id="react-app"]/div/div/div/section[1]/section/div/div/div[2]/a[1]/div[9]/span
    //*[@id="react-app"]/div/div/div/section[1]/section/div/div/div[2]/a[1]/div[10]/span
    //*[@id="react-app"]/div/div/div/section[1]/section/div/div/div[2]/a[1]/div[11]/span
    //*[@id="react-app"]/div/div/div/section[1]/section/div/div/div[2]/a[1]/div[12]/span
    //*[@id="react-app"]/div/div/div/section[1]/section/div/div/div[2]/a[1]/div[13]/span

//*[@id="react-app"]/div/div/div/section[1]/section/div/div/div[2]/a[2]
    //*[@id="react-app"]/div/div/div/section[1]/section/div/div/div[2]/a[2]/div[2]/div/span[2]
    //*[@id="react-app"]/div/div/div/section[1]/section/div/div/div[2]/a[2]/div[3]/span

//*[@id="react-app"]/div/div/div/section[1]/section/div/div/div[2]/a[1]
//*[@id="react-app"]/div/div/div/section[1]/section/div/div/div[2]/a[2]
"""
