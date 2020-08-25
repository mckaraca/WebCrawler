# WebCrawler Ders Projesi

Projenin amacı, Hurriyet.com sitesindeki 6 aylık veriyi Crawl edip JSON formatında saklamak ve analiz etmektir. Bunun için python, BeautifulSoup, 
HTML Parser ve Selenium kütüphaneleri kullanılmıştır. Program, tüm haberleri gezer ve başlık, açıklama, haber tagleri, haber tarihi gibi 
verileri toplayarak JSON dosyasında uygun bir tree formatinda saklar. 

Kurulum:
download get-pip.py from --> https://bootstrap.pypa.io/get-pip.py
then open cmd prompt and run --> python get-pip.py
then run --> pip install BeautifulSoup
then run --> pip install selenium

eğer chrome driver dosyasına ulaşamıyorsanız aşağıdaki linkten indirebilirsiniz. 
https://sites.google.com/a/chromium.org/chromedriver/downloads 



Çalıştırma:
$python Crawl.py
