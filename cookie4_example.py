import requests

url = "https://www.bbc.co.uk/news"
cookies = {'cookie_name': 'cookie_value'} 

response = requests.get(url, cookies=cookies)

# Check the cookies in the response
received_cookies = response.cookies

# Print the number of received cookies
num_received_cookies = len(received_cookies)
print(f"Number of Received Cookies: {num_received_cookies}")

# Print the received cookies
print("\nReceived Cookies:")
for cookie_name, cookie_value in received_cookies.items():
    print(f"Cookie Name: {cookie_name}, Cookie Value: {cookie_value}")
