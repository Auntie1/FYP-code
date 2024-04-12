import requests

url = "https://www.ebay.co.uk/"
cookies = {'cookie_name': 'cookie_value'}  # Replace with your actual cookies

response = requests.get(url, cookies=cookies)

# Check the cookies in the response
received_cookies = response.cookies

# Print the received cookies
print("Received Cookies:", received_cookies)

# You can also access individual cookies
for cookie_name, cookie_value in received_cookies.items():
    print(f"Cookie Name: {cookie_name}, Cookie Value: {cookie_value}")

#This code sends a GET request to "https://example.com" and checks the response headers for the presence of "Set-Cookie" headers. 
#If the server responds by setting cookies, those cookies are printed to the console. 
#This is a way to inspect the cookies that the server is setting.