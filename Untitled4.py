#!/usr/bin/env python
# coding: utf-8

# In[4]:


from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import xlsxwriter
def scrapwebsite():
    count=0
    workbook = xlsxwriter.Workbook('yoshopimg.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', 'Product_Name')
    worksheet.write('B1', 'Price')
    worksheet.write('C1', 'discounted Price')
    worksheet.write('D1', 'Shiping')
    worksheet.write('E1', 'Product URL')
    worksheet.write('F1', 'Rating')
    for i in range(1,12):
        s="https://yoshops.com/products?page="+str(i)
        html_txt= urllib.request.urlopen(s).read()
        soup=BeautifulSoup(html_txt,"html.parser")
        prod=soup.find_all('div',class_='product-thumb-inner')
        prod1=soup.find_all('div',class_='col-sm-3 col-xs-6')
        for j in range(0,len(prod)):
            if "noimage" in prod1[j].img['src']:
                ship="free"
                price=prod1[j].find_all('span',class_='')[0].text
                dprice=prod1[j].find_all('span',class_='')[1].text
                x=len(prod1[j].find_all('div',class_='free-shipping'))
                if x==0:
                    ship="not free"
                rate=prod1[j].find_all('span',class_="sr-only")
                if len(rate)==0:
                    rate= "None"
                count=count+1
                worksheet.write(count,0,prod[j].img['alt'] )
                worksheet.write(count,4,"https://yoshop.com"+prod1[j].div.a['href'])
                worksheet.write(count,1,price)
                worksheet.write(count,2,dprice)
                worksheet.write(count,3,ship)
                worksheet.write(count,5,rate)
    print("total missing images:    "+str(count))
    workbook.close()

def sw2(a):
    count=0
    workbook = xlsxwriter.Workbook('yoshopimg.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', 'Product_Name')
    worksheet.write('B1', 'Price')
    worksheet.write('C1', 'discounted Price')
    worksheet.write('D1', 'Shiping')
    worksheet.write('E1', 'Product URL')
    worksheet.write('F1', 'Rating')
    s= a
    html_txt= urllib.request.urlopen(s).read()
    soup=BeautifulSoup(html_txt,"html.parser")
    prod=soup.find_all('img',id='product-image')
    if len(prod)==1 and "noimage" in prod[0]['src']:
        worksheet.write(1,0,soup.find('h1',id='product-name').text)
        worksheet.write(1,4,s)
        worksheet.write(1,1,soup.find('span',id='regular-price').text)
        worksheet.write(1,2,soup.find('span',id='sale-price').text)
        worksheet.write(1,3,"not free")
        worksheet.write(1,5,"None")
        print("total missing images:    "+str(1))
    else:
        html_txt= urllib.request.urlopen(s).read()
        soup=BeautifulSoup(html_txt,"html.parser")
        prod=soup.find_all('div',class_='product-thumb-inner')
        prod1=soup.find_all('div',class_='col-sm-3 col-xs-6')
        for j in range(0,len(prod)):
            if "noimage" in prod1[j].img['src']:
                ship="free"
                price=prod1[j].find_all('span',class_='')[0].text
                dprice=prod1[j].find_all('span',class_='')[1].text
                x=len(prod1[j].find_all('div',class_='free-shipping'))
                if x==0:
                    ship="not free"
                rate=prod1[j].find_all('span',class_="sr-only")
                if len(rate)==0:
                    rate= "None"
                count=count+1
                worksheet.write(count,0,prod[j].img['alt'] )
                worksheet.write(count,4,"https://yoshop.com"+prod1[j].div.a['href'])
                worksheet.write(count,1,price)
                worksheet.write(count,2,dprice)
                worksheet.write(count,3,ship)
                worksheet.write(count,5,rate)
        print("total missing images:    "+str(count))
    workbook.close()
    
print("Entre 1 if scrap src is:  Yoshop.com else Entre 2")
i=int(input())
if i==1:
    scrapwebsite()
elif i==2:
    print("Entre web link to be scrapped")
    s=input()
    sw2(s)
print("File saved named yoshopimg.xlsx")


# In[ ]:





# In[ ]:




