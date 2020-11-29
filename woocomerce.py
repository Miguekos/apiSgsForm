from woocommerce import API
import json

# wcapi = API(
#     url="https://ecommerce-2.apps.com.pe",
#     consumer_key="ck_2956dcbaab2fafcffaf2c57134fea7bef119fe96",
#     consumer_secret="cs_446466432ccda985ceafa968b4eb59c19ad08c4c",
#     version="wc/v3"
# )


#wcapi = API(
#    url="https://euphoria.pe",
#    consumer_key="ck_24372cd19576ca2dacd27540ce4d88f391d2f9dd",
#    consumer_secret="cs_ac4f95f51cc9db55cf7cdb78a7facb0f82bb4329",
#    version="wc/v3",
#    timeout=20
#)

wcapi = API(
    url="https://ecommerce-2.apps.com.pe",
    consumer_key="ck_cc366d471878d25a89e7ccb0433ce5e4d9fe6faa",
    consumer_secret="cs_d5d87ee68630c3ca7abd3ceb8d5e18ee6301bc1e",
    version="wc/v3",
    timeout=20
)

# print(wcapi.get("products").json())

# try:
#     asd = wcapi.get("customers").json()
#     print(asd)
#     print(len(asd))
# except NameError:
#     print("qwe")
#     print(NameError)
# r = wcapi.get("products/24965").json()
# r = wcapi.get("orders").json()
# r = wcapi.get("orders")
# asd = json.loads(r.text)
# print(type(asd))
# print(r)
# print(len(r))
# print(type(r))
# print(r.status_code)
# print(r.text)
