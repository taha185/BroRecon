"""
Social Recon Pro - Username Search Tool
Created by Taha185
DISCLAIMER: For educational purposes only. Use responsibly.
"""

import requests
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

SITES = {
    'Instagram': 'https://www.instagram.com/{}/',
    'Facebook': 'https://www.facebook.com/{}/',
    'Twitter': 'https://twitter.com/{}',
    'GitHub': 'https://api.github.com/users/{}',
    'Reddit': 'https://www.reddit.com/user/{}/',
    'YouTube': 'https://www.youtube.com/{}',
    'TikTok': 'https://www.tiktok.com/@{}',
    'Pinterest': 'https://www.pinterest.com/{}/',
    'Steam': 'https://steamcommunity.com/id/{}',
    'Spotify': 'https://open.spotify.com/user/{}'
}

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def print_banner():
    print(Fore.CYAN + r"""
    
▓█████▄  ██▀███   ▒█████   ██▓███   ██▀███   ▄████▄  
▒██▀ ██▌▓██ ▒ ██▒▒██▒  ██▒▓██░  ██▒▓██ ▒ ██▒▒██▀ ▀█  
░██   █▌▓██ ░▄█ ▒▒██░  ██▒▓██░ ██▓▒▓██ ░▄█ ▒▒▓█    ▄ 
░▓█▄   ▌▒██▀▀█▄  ▒██   ██░▒██▄█▓▒ ▒▒██▀▀█▄  ▒▓▓▄ ▄██▒
░▒████▓ ░██▓ ▒██▒░ ████▓▒░▒██▒ ░  ░░██▓ ▒██▒▒ ▓███▀ ░
 ▒▒▓  ▒ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ▒▓▒░ ░  ░░ ▒▓ ░▒▓░░ ░▒ ▒  ░
 ░ ▒  ▒   ░▒ ░ ▒░  ░ ▒ ▒░ ░▒ ░       ░▒ ░ ▒░  ░  ▒   
 ░ ░  ░   ░░   ░ ░ ░ ░ ▒  ░░         ░░   ░ ░        
   ░       ░         ░ ░              ░     ░ ░      
 ░                                           ░       
    """)
    print(Fore.LIGHTRED_EX + "Created by Taha185 | Social Recon Pro v1.0\n")
    print(Fore.YELLOW + "DISCLAIMER: Use for educational purposes only. Don't be a skid!\n")

def check_username(username):
    print(Fore.MAGENTA + f"\n[*] Hunting '{username}' across the web... Hold tight bro! 🕵️♂️\n")
    
    for site, url in SITES.items():
        target_url = url.format(username)
        try:
            response = requests.head(target_url, headers=HEADERS, timeout=10)
            
            if site == 'GitHub':
                check = requests.get(target_url).status_code == 200
            else:
                check = response.status_code == 200

            if check:
                print(Fore.GREEN + f"[+] {site}: Noice! 🎉 Profile might exist → {target_url}")
            else:
                print(Fore.RED + f"[-] {site}: Nada! 💀 (Status: {response.status_code})")
                
        except Exception as e:
            print(Fore.YELLOW + f"[!] {site}: Yikes! Error checking → {str(e)}")
        
        print(Style.DIM + "―" * 65)

def main():
    print_banner()
    try:
        username = input(Fore.WHITE + "\n[?] Enter username to hunt: ").strip()
        if not username:
            print(Fore.RED + "\n[!] Bro, enter a username! Don't make me repeat myself... 😤")
            return
            
        check_username(username)
        print(Fore.CYAN + "\n[+] Recon complete! Check results above. Stay ethical! 🦸♂️")
        
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Operation cancelled. Later, bro! 👋")

if __name__ == "__main__":
    main()
