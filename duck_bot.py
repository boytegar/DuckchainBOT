import requests
import time
import json
from colorama import Fore, Style
from fake_useragent import UserAgent

def load_credentials():
    # Membaca token dari file dan mengembalikan daftar token
    try:
        with open('duck_query.txt', 'r') as f:
            queries = [line.strip() for line in f.readlines()]
        # print("Token berhasil dimuat.")
        return queries
    except FileNotFoundError:
        print("File duck_query.txt not found.")
        return 
    except Exception as e:
        print("Terjadi kesalahan saat memuat query:", str(e))
        return 

headers = {
    'accept-language': 'en-US,en;q=0.9',
    'if-none-match': 'W/"129-83t1ejiXqZksI6D5DMDXM+paHE4"',
    'origin': 'https://tgdapp.duckchain.io',
    'priority': 'u=1, i',
    'referer': 'https://tgdapp.duckchain.io/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
}

def userinfo(authorization_data):
    api_url = 'https://preapi.duckchain.io/user/info'
    headers['authorization'] = f'tma {authorization_data}' 

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()

        data = response.json()

        duck_name = data.get('data', {}).get('duckName')
        if duck_name:
            print(Fore.GREEN + "Duck Name:" + Style.RESET_ALL, duck_name)
        else:
            print(Fore.RED + "Duck name not found in response." + Style.RESET_ALL)

    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Terjadi kesalahan saat melakukan permintaan userinfo: {e}" + Style.RESET_ALL)


def quack_execute(authorization_data):
    api_url = 'https://preapi.duckchain.io/quack/execute?'
    headers['authorization'] = f'tma {authorization_data}'

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()

        data = response.json()

        decibel = data.get('data', {}).get('decibel')
        quack_times = data.get('data', {}).get('quackTimes')

        if decibel and quack_times:
            print(Fore.GREEN + "Balance:" + Style.RESET_ALL, decibel)
            print(Fore.GREEN + "Total Click:" + Style.RESET_ALL, quack_times)
        else:
            print(Fore.RED + "Decibel or Quack Times not found in response." + Style.RESET_ALL)

    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Terjadi kesalahan saat melakukan permintaan quack_execute: {e}" + Style.RESET_ALL)

def main():
    ua = UserAgent()
    while True:
        queries = load_credentials()
        for i, query in enumerate(queries):
            headers['user-agent'] = ua.random 
            print(Fore.YELLOW + f"\n=== Akun ke-{i+1} ===" + Style.RESET_ALL) 
            userinfo(query)
            quack_execute(query)
            time.sleep(1)

if __name__ == '__main__':
    main()