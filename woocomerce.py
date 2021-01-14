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

# wcapi = API(
#     url="https://ecommerce-2.apps.com.pe",
#     consumer_key="ck_cc366d471878d25a89e7ccb0433ce5e4d9fe6faa",
#     consumer_secret="cs_d5d87ee68630c3ca7abd3ceb8d5e18ee6301bc1e",
#     wp_api=True, # Enable the WP REST API integration
#     version="wc/v3"
# )

wcapi = API(
    url="https://sgsacademy.pe/",
    consumer_key="ck_8837e4e56a60e6d3040375f6e7e9c0ba2e6ed8d0",
    consumer_secret="cs_d2ebcbb32460abe15dc08a86ff77a340cc5ba825",
    wp_api=True, # Enable the WP REST API integration
    version="wc/v3",
    verify_ssl=False,
    timeout=20,
    query_string_auth=False,

)

# print(wcapi.get("settings").json())

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
