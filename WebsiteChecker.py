#from bs4 import BeautifulSoup
#import requests
#class WebsiteChecker:
    #def __init__(self, website):
     #   self.website = website

    #def check_consent_mechanism(self):
       # print("Checking cookie consent mechanism...")
        # Make a request to the website
        #response = requests.get(self.website)
        #if response.status_code == 200:
            # Parse HTML content
          #  soup = BeautifulSoup(response.content, 'html.parser')
            # Search for elements containing common keywords related to cookie consent
         #   cookie_consent_keywords = ['cookie', 'consent', 'privacy', 'accept', 'reject']
       ##     cookie_consent_banner = soup.find('div', string=lambda text: text and any(keyword in text.lower() for keyword in cookie_consent_keywords))
      #      if cookie_consent_banner:
     #           print("Cookie consent mechanism found.")
    #        else:
   #             print("Cookie consent mechanism not found.")
  #      else:
 #           print("Failed to fetch website content.")

# Example usage:
#checker = WebsiteChecker("https://www.google.co.uk/")
#checker.check_consent_mechanism()

#from bs4 import BeautifulSoup
#import requests

#class WebsiteChecker:
   # def __init__(self, website):
    #    self.website = website

   # def check_consent_mechanism(self):
      #  print("Checking cookie consent mechanism...")
        # Make a request to the website
      #  response = requests.get(self.website)
       # if response.status_code == 200:
            # Parse HTML content
       #     soup = BeautifulSoup(response.content, 'html.parser')
            # Search for elements containing common classes or IDs related to cookie consent
         #   cookie_consent_selectors = ['.cookie-consent', '#cookie-banner', '.privacy-policy-banner']
        #    for selector in cookie_consent_selectors:
       #         cookie_consent_banner = soup.select_one(selector)
      #          if cookie_consent_banner:
     #               print("Cookie consent mechanism found.")
    #                return
   #         print("Cookie consent mechanism not found.")
  #      else:
 #           print("Failed to fetch website content.")

# Example usage:
#checker = WebsiteChecker("https://www.google.co.uk/")
#checker.check_consent_mechanism()


# NEED TO INSTALL SELENIUM SEE IF THAT HELPS


from bs4 import BeautifulSoup
import requests

class WebsiteChecker:
    def __init__(self, website):
        self.website = website

    def check_consent_mechanism(self):
        print(f"Checking cookie consent mechanism for {self.website}...")
        # Make a request to the website
        response = requests.get(self.website)
        if response.status_code == 200:
            # Parse HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            # Search for elements containing common classes, IDs, or attributes related to cookie consent
            cookie_consent_selectors = [
                '.cookie-consent', '#cookie-banner', '.privacy-policy-banner',
                '[id*="cookie"]', '[id*="consent"]', '[class*="cookie"]', '[class*="consent"]',
                '[data-cookie]', '[data-consent]', '[data-privacy-policy]',
                'div:-soup-contains("cookie")', 'div:-soup-contains("consent")', 'div:-soup-contains("privacy policy")',
                'span:-soup-contains("cookie")', 'span:-soup-contains("consent")', 'span:-soup-contains("privacy policy")',
                'p:-soup-contains("cookie")', 'p:-soup-contains("consent")', 'p:-soup-contains("privacy policy")'
            ]
            for selector in cookie_consent_selectors:
                cookie_consent_banner = soup.select_one(selector)
                if cookie_consent_banner:
                    print("Cookie consent mechanism found.")
                    return
            print("Cookie consent mechanism not found.")
        else:
            print("Failed to fetch website content.")

# Example usage:
urls = [
    "https://www.ebay.co.uk/",
    "https://www.bbc.com",
    "https://www.nytimes.com",
    "https://www.amazon.com",
    "https://www.netflix.com",
    "https://www.reddit.com",
    "https://www.youtube.com/"
]

for url in urls:
    checker = WebsiteChecker(url)
    checker.check_consent_mechanism()


