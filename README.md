# XSS-Finder
The XSS-Finder,  I created for my bug bounty hunting process. It helps me quickly find Cross-Site Scripting (XSS) vulnerabilities by trying different inputs with a variety of XSS attack codes. It has a simple command-line interface that makes it easy to use, allowing me to test web applications for XSS vulnerabilities efficiently and automatically.

## Usage
1. Clone the repository:
     ```git clone https://github.com/Shehzadcyber/XSS-Finder.git```
2. Navigate to the project directory:
    ```cd XSS-Finder```

3. Run the following command
    ``` python xss-spray.py -u http://target.com/page.php -p param1 param2 -pl params.txt --payloads xss-payloads.txt ```

    - -u or --url: Specify the target URL.
    - -p or --parameters: Specify the parameters to be tested (separated by spaces).
    - -pl or --parameter-list: Specify a file with a list of parameters (one per line).
    - --payloads: Specify the file with XSS attack codes.

![image](https://github.com/Shehzadcyber/XSS-Finder/assets/65858237/eec5e9c8-739f-4408-9ab5-72b582b2a2e1)


## Disclaimer
This script is intended for legal and authorized security testing purposes only. I am not responsible for any unauthorized use or consequences resulting from the use of this tool.

# ================================
Feel free to customize this description further if needed. Happy bug bounty hunting!
