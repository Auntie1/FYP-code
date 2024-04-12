import http.cookiejar
import urllib.request
from urllib.parse import urlparse

def classify_cookie(cookie):
    # Check if the cookie has an expiration time
    if cookie.expires is not None:
        return "3rd Party"  # If it has an expiration, it's likely a 3rd party cookie

    # Check if the cookie is a session cookie
    if cookie.expires == 0:
        return "Session"  # If it expires at the end of the session, it's a session cookie

    # Extract the domain from the cookie
    domain = urlparse(cookie.domain).hostname

    # Check if the cookie domain matches the request domain
    if domain == urlparse(url).hostname:
        return "1st Party"
    else:
        return "3rd Party"

def survey_cookies(url):
    # Create a CookieJar object to store cookies
    cookie_jar = http.cookiejar.CookieJar()

    # Create a handler to manage cookies
    cookie_handler = urllib.request.HTTPCookieProcessor(cookie_jar)

    # Create an opener that will handle HTTP requests
    opener = urllib.request.build_opener(cookie_handler)

    # Make a request to the URL
    with opener.open(url) as response:
        pass  # Open the URL just to collect cookies

    # Analyze and classify the collected cookies
    cookie_types = {"1st Party": 0, "3rd Party": 0, "Session": 0}
    for cookie in cookie_jar:
        classification = classify_cookie(cookie)
        cookie_types[classification] += 1

    return cookie_types

if __name__ == "__main__":
    url = input("Enter the URL to survey cookies: ")
    cookie_counts = survey_cookies(url)

    print("\nCookie Survey Results:")
    print("Total Cookies Collected:", sum(cookie_counts.values()))
    print("Types of Cookies:")
    for cookie_type, count in cookie_counts.items():
        print(f"- {cookie_type}: {count}")
