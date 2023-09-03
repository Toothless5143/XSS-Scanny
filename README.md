# XSS-Scanny
XSS-Scanny is a Python-based XSS (Cross-Site Scripting) scanner tool that leverages the `Selenium` library for web automation. It is designed to identify potential XSS vulnerabilities in web applications by injecting various payloads from a wordlist into target URLs. By analyzing the website's response, XSS-Scanny helps security professionals and ethical hackers detect and mitigate these security weaknesses before they can be exploited maliciously.

**Installation:**

To install XSS-Scanny, follow these steps:

1. Clone the XSS-Scanny repository and navigate to the project directory:
   ```
   git clone https://github.com/Toothless5143/XSS-Scanny.git
   cd XSS-Scanny
   ```

2. Install the required dependencies using pip:
   ````
   pip install selenium
   ````

**Usage:**

To run XSS-Scanny, use the following command template:

```
python3 xss_scanner.py -u <URL Containing a GET parameter>* -w <wordlist_path>
```

- Replace `<URL Containing a GET parameter>*` with the target URL that includes a GET parameter you want to test for XSS vulnerabilities. The `*` character indicates the injection point.

- Replace `<wordlist_path>` with the path to your desired wordlist file. XSS-Scanny uses this wordlist to generate different XSS payloads for testing. One recommended wordlist is XSS-Jhaddix.txt from SecLists.

By executing XSS-Scanny with the specified parameters, the tool systematically injects each payload from the wordlist into the target URL, monitors the website's response, and reports any detected XSS vulnerabilities.

**Note:**
Ensure that you have proper authorization to perform security assessments on the target website. Unauthorized and malicious use of XSS-Scanny or similar tools is strictly prohibited.

### License:
XSS-Scanny is an open-source tool released under the [MIT License.](/LICENSE)
