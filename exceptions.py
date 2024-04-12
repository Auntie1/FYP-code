import requests
from bs4 import BeautifulSoup

class WebsiteChecker:
    def check_exemptions(self, website_url):
        print("Checking exemptions for", website_url)
        
        # Make a request to the website
        response = requests.get(website_url)
        if response.status_code == 200:
            # Parse HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Search for exemption keywords
            exemption_keywords = ['_ea_clicked', 'accessKey', 'align']
            for keyword in exemption_keywords:
                if soup.find(string=keyword):
                    print("Exemption keyword '{}' found.".format(keyword))
            
            # Search for exemption classes
            exemption_classes = ['communication-exemption', 'necessary-exemption', 'analytics-exemption', 'personalization-exemption']
            for class_name in exemption_classes:
                if soup.find(class_=class_name):
                    print("Exemption class '{}' found.".format(class_name))
            
            # If no exemptions found, print a message
            if not (any(soup.find(string=keyword) for keyword in exemption_keywords) or
                    any(soup.find(class_=class_name) for class_name in exemption_classes)):
                print("No exemptions found.")
        else:
            print("Failed to fetch website content.")

# Create an instance of the WebsiteChecker class
checker = WebsiteChecker()

# Call the check_exemptions method with the website URL
checker.check_exemptions("https://www.ebay.co.uk/gdpr")
