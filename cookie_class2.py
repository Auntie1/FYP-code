import requests

url = "https://careershub.tarmac.com/members/"
cookies = {'cookie_name': 'cookie_value'}  # Replace with your actual cookies

# Send a GET request to the specified URL with the provided cookies
response = requests.get(url, cookies=cookies)

# Extract and analyze the received cookies from the response
received_cookies = response.cookies

# Extract the domain from the original request URL
request_domain = url.split('//')[1].split('/')[0]

# Print the number of received cookies
num_received_cookies = len(received_cookies)
print(f"Number of Received Cookies: {num_received_cookies}")

# Print details about the received cookies
print("\nReceived Cookies:")
for cookie in received_cookies:
    cookie_name = cookie.name
    cookie_value = cookie.value
    cookie_domain = cookie.domain
    cookie_path = cookie.path
    cookie_secure = cookie.secure
    cookie_http_only = cookie.has_nonstandard_attr('HttpOnly')

    # Determine the cookie type based on attributes
    cookie_type = "Session Cookie" if not cookie.expires else "Persistent Cookie"
    if cookie_secure:
        cookie_type += " (Secure)"
    if cookie_http_only:
        cookie_type += " (HttpOnly)"

    # Determine if the cookie is 3rd party
    is_third_party = cookie_domain != request_domain
    if is_third_party:
        cookie_type += " (3rd Party)"

    # Print detailed information about each received cookie
    print(f"Cookie Name: {cookie_name}")
    print(f"Value: {cookie_value}")
    print(f"Domain: {cookie_domain}")
    print(f"Path: {cookie_path}")
    print(f"Type: {cookie_type}")
    print("------------------------")
