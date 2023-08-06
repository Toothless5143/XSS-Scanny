# XSS-Scanny
This tool is a simple XSS (Cross-Site Scripting) scanner using `Selenium`, a popular web automation tool. It's designed to check if a given URL is vulnerable to XSS attacks by injecting different payloads from a wordlist into the URL.

### Installation:
Download all the required files and libraries you need to run the tool: <br>
```shell
git clone https://github.com/Toothless5143/XSS-Scanny.git && cd XSS-Scanny
pip install selenium
```

In order to run the tool prepare the command like this, you need to put a `*` in order to mark the fuzzing point: <br>
```shell
python3 xss_scanner.py -u <URL Containing a get parameter>* -w <wordlist_path>
```

You guys can use any wordlist you want but personally, I prefer [XSS-Jhaddix.txt](https://github.com/danielmiessler/SecLists/blob/master/Fuzzing/XSS/XSS-Jhaddix.txt) by SecLists.

### License:
This tool is open source and available under the [MIT License.](/LICENSE)
