import requests,json


def stream_price():
    f=open('api_key.txt','r')
    api_key=json.loads(f.read())
    url='https://stream-fxpractice.oanda.com'
    header='Authorization: Bearer %s' % api_key['key_prac']
    print(header)
if __name__ == "__main__":
    stream_price()
    
