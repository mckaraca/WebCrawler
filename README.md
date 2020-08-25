# WebCrawler Ders Projesi

Projenin amacı, Hurriyet.com sitesindeki 6 aylık veriyi Crawl edip JSON formatında saklamak ve analiz etmektir. Bunun için python, BeautifulSoup, <br/>
HTML Parser ve Selenium kütüphaneleri kullanılmıştır. Program, tüm haberleri gezer ve başlık, açıklama, haber tagleri, haber tarihi gibi <br/>
verileri toplayarak JSON dosyasında uygun bir tree formatinda saklar. <br/>

Kurulum:<br/>
download get-pip.py from --> https://bootstrap.pypa.io/get-pip.py<br/>
then open cmd prompt and run --> python get-pip.py<br/>
then run --> pip install BeautifulSoup<br/>
then run --> pip install selenium<br/>
eğer chrome driver dosyasına ulaşamıyorsanız aşağıdaki linkten indirebilirsiniz. <br/>
https://sites.google.com/a/chromium.org/chromedriver/downloads <br/>


Çalıştırma:<br/>
$python Crawl.py<br/>
