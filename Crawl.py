from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import datetime
import time
import json

chrome_path = r"chromedriver.exe"
# firefox_path = r"C:\Users\Asus\Desktop\geckodriver.exe"
seleniumDriver = webdriver.Chrome(chrome_path)
x = 0
seleniumDriver.set_page_load_timeout(30)
data = {}
jData = {'All The News': []}
for i in range(0, 180):
    author = ""
    newsBody = ""
    newsHead = ""
    newsTitle = ""
    date = ""
    emptyComments = []
    emptyCommentsDate = []
    emptyCommentsAuthor = []
    t = datetime.date.today() - datetime.timedelta(6 * 365 / 12 - i)  # +10)#son 6 ayı hesaplıyor
    date = t.strftime('%Y%m%d')
    url = "http://www.hurriyet.com.tr/index/?d=%s" % (date)
    date = t.strftime('%Y/%m/%d')
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    newsTitle = soup.find("div", attrs={"class": "top-line"}).find("h1").text
    print("title :", newsTitle)

    for link in soup.find_all("div", attrs={"class": "news"}):
        try:
            newsBody = link.find('p').text
            newsHead = link.find('a').get('title')
            href = link.find('a').get('href')
            newsLink = "http://www.hurriyet.com.tr" + href
            r4 = requests.get(newsLink)
            data4 = r4.text
            soup4 = BeautifulSoup(data4, "html.parser")
            newsAuthor = soup4.find("div", attrs={"class": "breadcrumb-body clr"})
            if (newsAuthor is not None):
                tag = newsAuthor.findAll('a')[1].get('title')
                print("tag :", tag)
            else:
                print("tag : None")
            print("news date :", date)
            print("news head :", newsHead)
            print("news body :", newsBody)
            r2 = requests.get(newsLink)
            data2 = r2.text
            soup2 = BeautifulSoup(data2, "html.parser")
            newsAuthor = soup2.find("div", attrs={"class": "col-md-5 news-detail-author"})

            r3 = requests.get(newsLink)
            data3 = r3.text
            soup3 = BeautifulSoup(data3, "html.parser")
            newsAuthor2 = soup3.find("div", attrs={"class": "rhd-editor-title"})
            if (newsAuthor is not None):
                author = newsAuthor.find('span').text
                print("news author :", author)
            elif (newsAuthor2 is not None):
                author = newsAuthor2.text
                print("news author :", author)
            else:
                print("news author : None")
        except Exception:
            print("Cannot reach the news (%s)"%date)
            break
        try:
            seleniumDriver.get(newsLink)
            if (x == 0):
                time.sleep(1.5)
                # time.sleep(2)
                x = x + 1
            else:
                time.sleep(1.5)
            # time.sleep(2)
            xpath2 = seleniumDriver.find_elements_by_xpath('//*[@id="yorumlar"]/div[1]/h5[1]')  # yorumlari goster
            if len(xpath2) > 0:
                xpath2[0].click()
                time.sleep(1.5)
            else:
                xpath3 = seleniumDriver.find_elements_by_xpath('//*[@id="yorumlar"]/div[1]')  # yorumlari goster
                if len(xpath3) > 0:
                    xpath3[0].click()
                    time.sleep(1.5)
            xpath1 = seleniumDriver.find_elements_by_xpath('//*[@id="commenty_40696717"]/div/div[3]/div/a[1]')  # diger yorumlari goster
            if len(xpath1) > 0:
                xpath1[0].click()
                time.sleep(1.5)
            xpath4 = seleniumDriver.find_elements_by_xpath('//*[@id="commenty_40696600"]/div/div[3]/div/a[1]')
            if len(xpath4) > 0:
                xpath4[0].click()
                time.sleep(1.5)
            xpath5 = seleniumDriver.find_elements_by_xpath('//*[@id="commenty_40696716"]/div/div[3]/div/a[1]')
            if len(xpath5) > 0:
                xpath5[0].click()
                time.sleep(1.5)
            xpath6 = seleniumDriver.find_elements_by_xpath('//*[@id="commenty_40718721"]/div/div[3]/div/a[1]')
            if len(xpath6) > 0:
                xpath6[0].click()
                time.sleep(1.5)

            #xpath7 = seleniumDriver.find_elements_by_xpath('//*[@id="commenty_40718721"]/div/div[1]/div/div/div[1]')
            #commentCounter = xpath7.text
            #print("commentCounter:",commentCounter)
            newsAuthor5 = seleniumDriver.find_elements_by_class_name("flex-text-wrap")
            try:
                newsAuthor6 = seleniumDriver.find_element_by_xpath('//*[@id="commenty_40718721"]/div/div[1]/div/div/div[1]')
            except Exception:
                time.sleep(0.1)
                ##
            try:
                newsAuthor6 = seleniumDriver.find_element_by_xpath('// *[ @ id = "commenty_40718719"] / div / div[1] / div / div / div[1]')
            except Exception:
                time.sleep(0.1)
                ##
            newsAuthor7 = seleniumDriver.find_element_by_xpath('//*[@id="commentText"]')
            commentCounterStr = newsAuthor6.find_element_by_xpath('//*[@id="commenty_40718721"]/div/div[1]/div/div/div[1]/span').text
            commentCounter = int(commentCounterStr)

            count = 0
            commentCount = 0
            commentsAuthorStr = []
            commentsDateStr = []
            print("Comments")
            print("5 : ",len(newsAuthor5))
            try:
                print("7 : ",len(newsAuthor7))
                if(len(newsAuthor5) < len(newsAuthor7)):
                    newsAuthor5 = newsAuthor7
                else:
                    newsAuthor5 = newsAuthor5
            except Exception:
                newsAuthor5 = newsAuthor5
            for comments in newsAuthor5:
                if (count % 2 == 0):
                    try:
                        commentCount = commentCount + 1
                        if len(comments.text) > 0:
                            commentsAuthor = seleniumDriver.find_elements_by_class_name("comment-box-member-info-title")
                            commentsDate = seleniumDriver.find_elements_by_class_name("comment-box-member-info-date")
                            commentsAuthorStr.append(commentsAuthor[commentCount - 1].text)
                            commentsDateStr.append(commentsDate[commentCount - 1].text)
                            print(commentCount, "\t", commentsAuthorStr[commentCount - 1], " ", commentsDateStr[commentCount - 1])
                            # print("Comment",commentCount,":",comments.text)#emojileri düzelt
                            print("\t\t", comments.text)  # emojileri düzelt
                        else:
                            commentCount = commentCount - 1
                    except UnicodeEncodeError:
                        print("UnicodeEncodeError")
                        commentCount = commentCount - 1
                        count = count + 1
                        pass
                if (commentCount == 10):
                    break
                count = count + 1
                #end for
            time.sleep(1)
            commentsArray = []
            counter = 0
            for i in range(0,len(newsAuthor5)):
                if(counter % 2 == 0):
                    if len(newsAuthor5[i].text) > 0:
                        commentsArray.append(newsAuthor5[i].text)
                counter = counter + 1
            #if (commentCount == 0):
                #print("\tNone")
            if len(commentsArray) > 0:
                news_info = {'News': {
                    'Title': newsTitle,
                    'Date': date,
                    'Head': newsHead,
                    'Body': newsBody,
                    'Author': author,
                    'Comments' : commentsArray,
                    'Comments Date' : commentsDateStr,
                    'Comments Author' : commentsAuthorStr,
                    'Total Comment Count' : commentCounter
                }
                }
            else:
                news_info = {'News': {
                    'Title': newsTitle,
                    'Date': date,
                    'Head': newsHead,
                    'Body': newsBody,
                    'Author': author,
                    'Comments': emptyComments,
                    'Comments Date': emptyCommentsDate,
                    'Comments Author': emptyCommentsAuthor,
                    'Total Comment Count': 0
                }
                }
            jData['All The News'].append(news_info)
            print("")
        except Exception:
            print("\tNone")
            news_info = {'News': {
                'Title': newsTitle,
                'Date': date,
                'Head': newsHead,
                'Body': newsBody,
                'Author': author,
                'Comments': emptyComments,
                'Comments Date': emptyCommentsDate,
                'Comments Author': emptyCommentsAuthor,
                'Total Comment Count': 0
            }
            }
            jData['All The News'].append(news_info)
            pass
with open("deneme.json", 'a', encoding='utf8') as fp:
    json.dump(jData, fp, ensure_ascii=False)
    try:
        seleniumDriver.close()
    except Exception:
        print("end")
# for link in soup.find_all('a'):
# print(link.get('href'))

