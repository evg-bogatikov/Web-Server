def getData(request):
    result = parseBody(request.decode())
    return result


def parseBody(request):
    arrayRequest = request.split('\n')
    data = arrayRequest[len(arrayRequest) - 1]
    data = data.split('&')
    result = {}
    for item in data:
        item = item.split('=')
        if len(item) < 0:
            break
        else:
            result[item[0]] = item[1]

    return result
