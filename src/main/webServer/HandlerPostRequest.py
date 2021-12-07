class HandlerPostRequest:


    def getData(self, request):
        data = request[len(request) - 1]
        data = data.split('&')
        result = {}
        for item in data:
            item = item.split('=')
            if len(item) < 0:
                break
            else:
                result[item[0]] = item[1]

        return result
