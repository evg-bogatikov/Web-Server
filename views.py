import binascii
import os

def searchView(url):
    for root, directories, file in os.walk("templates"):
        if file == url:
            with open(f'templates/{url}') as template:
                return template.read()




def index():
    return searchView()

def blog():
    with open('templates/blog.html') as template:
        return template.read()

def parsePost(request):
    parsed = request.split(' ')
    webkit = parsed[10]
    result = webkit.split('boundary=----WebKitFormBoundary')
    webkit = result[1]
    print(webkit)
    return webkit


def handlerPostRequest(request):
    return 'Hi'