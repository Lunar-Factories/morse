# Client test application
import time
import requests

requestType = 'get'
url = 'http://localhost:8080'


def getresponse():
    return requests.request(requestType, url)


if __name__ == '__main__':
    i = 0
    while i != 100:
        response = getresponse()
        print(response.text)
        time.sleep(5)
