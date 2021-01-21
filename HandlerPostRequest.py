class HandlerPostRequest:


    def getData(self, request):
        request = request.decode()
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
