


def getResponse(method, url):
    headers, code = generate_headers(method, url)

    content_status = generate_content_status(code, url)
    if content_status == 200:
        formatUrl = url.split('.')
        if formatUrl[formatUrl.__len__() - 1] == 'jpg' or formatUrl[formatUrl.__len__() - 1] == 'png' or formatUrl[formatUrl.__len__() - 1] == 'gif':
            additional_header, r = pictureResponse(url)
            return (headers + additional_header).encode() + r
        else:
            body = readView(url)
            return (headers + '\n' + body).encode()

    return (headers + '\n' + content_status).encode()