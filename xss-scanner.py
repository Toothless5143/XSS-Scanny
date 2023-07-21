from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import warnings
import argparse
import sys

# Hide unnecessary warnings
warnings.filterwarnings('ignore')

def get_user_input():
    """Ask user for target URL and wordlist path."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--wordlist', required=True, help='Path to the wordlist containing XSS payloads')
    args = parser.parse_args()

    target_url = input('Enter the target URL (with * as a placeholder): ')
    return target_url, args.wordlist

def main():
    # Get user input for target URL and wordlist
    target_url, wordlist_path = get_user_input()

    # Configure Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-xss-auditor')
    options.add_argument('--disable-web-security')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--no-sandbox')
    options.add_argument('--log-level=3')
    options.add_argument('--disable-notifications')
    
    # Create Chrome WebDriver Change the path according to your own need
    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=options)

    try:
        # Check if the "*" parameter exists in the target URL
        if '*' not in target_url:
            sys.exit("Need * parameter in the target URL!")

        for payload in open(wordlist_path, "r").readlines():
            # Replace "*" with the current payload in the target URL
            url = target_url.replace('*', payload.strip())

            # Navigate to the URL using the WebDriver
            driver.get(url)

            try:
                # Wait for 3 seconds to see if an XSS alert appears
                WebDriverWait(driver, 3).until(EC.alert_is_present())
                alert = driver.switch_to.alert
                alert.accept()
                print("XSS alert accepted with payload:", payload)
            except TimeoutException:
                print("XSS doesn't work with payload:", payload)

    except KeyboardInterrupt:
        print("Scan interrupted by the user.")
    finally:
        # Close the WebDriver when done
        driver.quit()

if __name__ == "__main__":
    main()
