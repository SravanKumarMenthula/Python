import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1,100)
    full_name = str(name)+'.jpg'
    urllib.request.urlretrieve(url,full_name)

download_web_image("https://www.google.co.in/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjPl4_v8vTXAhWCWLwKHSOABC0QjRwIBw&url=https%3A%2F%2Fsports.ndtv.com%2Fcricket%2Fms-dhoni-is-goat-says-this-pakistani-cricketer-1750792&psig=AOvVaw3w39kHD_SQJbLcZF8P7ZSq&ust=1512632900071057")