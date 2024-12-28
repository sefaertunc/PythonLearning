import requests
import requests as rq


urls = {
        "post": "https://httpbin.org/post",
        "get": "https://httpbin.org/get",
        "200": "https://httpbin.org/status/200",
        "300": "https://httpbin.org/status/300",
        "404": "https://httpbin.org/status/404",
        "500": "https://httpbin.org/status/500",
        "delay": "https://httpbin.org/delay/5",
        "basic_auth": "https://httpbin.org//basic-auth/user/passwd",
        "ip": "https://httpbin.org/image/webp"
}

# for url in urls:
#     response = rq.Request("GET", urls[url])
#     rep = response.prepare()
#     res = rq.Session()
#     if input("y or n? ") == "y":
#         message = res.send(rep)
#         print(message)

response = rq.get(urls["ip"])
print(response.text)

try:
    sample = rq.get(urls["basic_auth"], auth=("user", "passwd"))
    print(sample)
except requests.exceptions.RequestException as e:
    print(e)