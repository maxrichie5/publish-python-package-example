import requests

def run():
    resp = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
    print(resp)


if __name__ == "__main__":
    run()
