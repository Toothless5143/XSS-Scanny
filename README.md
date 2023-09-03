
# XSS-Scanny

XSS-Scanny is a Python-based XSS (Cross-Site Scripting) scanner tool that leverages the `Selenium` library for web automation. It is designed to identify potential XSS vulnerabilities in web applications by injecting various payloads from a wordlist into target URLs. By analyzing the website's response, XSS-Scanny helps security professionals and ethical hackers detect and mitigate these security weaknesses before they can be exploited maliciously.

## Features and Benefits
- Uses `Selenium` for web automation, providing a robust and flexible testing environment.
- Utilizes a customizable wordlist for generating diverse XSS payloads to maximize vulnerability coverage.
- Offers detailed reports of identified XSS vulnerabilities, including the affected URLs and injected payloads.
- Facilitates proactive security testing by automating the process of XSS vulnerability detection.
- Assists in identifying and remediating XSS vulnerabilities in web applications, enhancing overall security posture.

## Installation

To install XSS-Scanny, follow these steps:

1. Clone the XSS-Scanny repository and navigate to the project directory:

```shell
git clone https://github.com/Toothless5143/XSS-Scanny.git
cd XSS-Scanny
```

2. Install the required dependencies using pip:

```shell
pip install selenium
```

## Usage

To run XSS-Scanny, use the following command template:

```shell
python3 xss_scanner.py -u <URL Containing a GET parameter>* -w <wordlist_path>
```

Replace `<URL Containing a GET parameter>*` with the target URL that includes a GET parameter you want to test for XSS vulnerabilities. The `*` character indicates the injection point.

Replace `<wordlist_path>` with the path to your desired wordlist file. XSS-Scanny uses this wordlist to generate different XSS payloads for testing. One recommended wordlist is `XSS-Jhaddix.txt` from SecLists.

By executing XSS-Scanny with the specified parameters, the tool systematically injects each payload from the wordlist into the target URL, monitors the website's response, and reports any detected XSS vulnerabilities.

Note: Ensure that you have proper authorization to perform security assessments on the target website. Unauthorized and malicious use of XSS-Scanny or similar tools is strictly prohibited.

## Output and Reporting

XSS-Scanny provides comprehensive reports of identified XSS vulnerabilities. The tool displays the affected URLs along with the injected payloads that triggered the vulnerabilities. This information aids in understanding the extent and severity of the identified issues.

## Limitations and Considerations

- XSS-Scanny primarily focuses on identifying reflected XSS vulnerabilities and may have limitations in detecting stored XSS or DOM-based XSS.
- Manual verification is essential to validate the identified vulnerabilities and eliminate false positives.
- Always obtain proper authorization and adhere to ethical guidelines when using XSS-Scanny or any similar security assessment tools.
- XSS-Scanny should be used responsibly and only on web applications for which you have explicit permission to test.

## License

XSS-Scanny is an open-source tool released under the [MIT License](/LICENSE).

Please note that while XSS-Scanny can be a useful tool for identifying XSS vulnerabilities, it is essential to supplement automated testing with manual verification and follow responsible disclosure practices when reporting any discovered vulnerabilities.

Remember to always obtain proper authorization before conducting security assessments on any web application.
