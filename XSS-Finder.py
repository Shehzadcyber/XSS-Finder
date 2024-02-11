import argparse
import requests
from urllib.parse import quote
from termcolor import colored

def check_xss_vulnerability(url, parameters, payloads):
    for payload in payloads:
        for parameter in parameters:
            encoded_payload = quote(payload)
            target_url = f"{url}?{parameter}={encoded_payload}"
            response = requests.get(target_url)
            if payload in response.text:
                print(colored(f"Vulnerable XSS URL: {target_url}", 'red'))
                break  # Move to the next payload if vulnerability is found
        else:
            print(f"Not Vulnerable to XSS for payload: {payload}")

def main():
    banner = '''
    ╔══════════════════════════════════════════════════════════╗
    ║                   XSS Finder TOOL                        ║
    ║                    by Shehzad Roy                        ║
    ║                Twitter: @theroyhunter313                 ║
    ╚══════════════════════════════════════════════════════════╝
    '''

    print(banner)

    parser = argparse.ArgumentParser(description='XSS Spray')
    parser.add_argument('-u', '--url', help='Target URL')
    parser.add_argument('-p', '--parameters', nargs='+', help='Parameters')
    parser.add_argument('--payloads', required=True, help='File containing XSS payloads')
    parser.add_argument('-pl', '--parameter-list', help='File containing parameter list')

    args = parser.parse_args()

    with open(args.payloads, 'r') as file:
        payloads = file.read().splitlines()

    if args.parameters:
        parameters = args.parameters
    elif args.parameter_list:
        try:
            with open(args.parameter_list, 'r') as file:
                parameters = file.read().splitlines()
        except FileNotFoundError:
            print(f"Parameter file '{args.parameter_list}' not found.")
            return
    else:
        print("Please provide either -p/--parameters or -pl/--parameter-list argument.")
        return

    check_xss_vulnerability(args.url, parameters, payloads)

if __name__ == '__main__':
    main()
