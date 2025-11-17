import asyncio
import json
import datetime
import os
import csv
from colorama import Fore, Style, init
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Import all modules
from modules.dns_lookup import dns_lookup
from modules.whois_lookup import whois_lookup
from modules.http_info import http_info
from modules.tech_detect import tech_detect
from modules.ip_lookup import ip_lookup
from modules.ssl_info import ssl_info
from modules.subdomains import subdomain_scan
from modules.port_scan import port_scan
from modules.cdn_waf import detect_cdn_waf
from modules.reverse_ip import reverse_ip_lookup
from modules.emails_extract import extract_emails
from modules.metadata import extract_metadata

init(autoreset=True)

async def run_all_checks(domain):
    print(Fore.WHITE + Style.BRIGHT + f"\n[+] Running OSINT scan for: {domain}\n")

    tasks = [
        dns_lookup(domain),
        whois_lookup(domain),
        http_info(domain),
        tech_detect(domain),
        ip_lookup(domain),
        ssl_info(domain),
        subdomain_scan(domain),
        port_scan(domain),
        detect_cdn_waf(domain),
        reverse_ip_lookup(domain),
        extract_emails(domain),
        extract_metadata(domain)
    ]

    results_raw = await asyncio.gather(*tasks)
    results = {
        "domain": domain,
        "timestamp": datetime.datetime.now().isoformat(),
        "dns": results_raw[0],
        "whois": results_raw[1],
        "http_info": results_raw[2],
        "technologies": results_raw[3],
        "ip_info": results_raw[4],
        "ssl_info": results_raw[5],
        "subdomains": results_raw[6],
        "ports": results_raw[7],
        "cdn_waf": results_raw[8],
        "reverse_ip": results_raw[9],
        "emails": results_raw[10],
        "metadata": results_raw[11]
    }
    return results

def save_results(domain, data):
    os.makedirs("results", exist_ok=True)
    safe_domain = domain.replace("://","_").replace(".","_")
    timestamp = int(datetime.datetime.now().timestamp())
    json_filename = f"results/{safe_domain}_{timestamp}.json"
    csv_filename = f"results/{safe_domain}_{timestamp}.csv"

    # Handle non-serializable objects
    def default_serializer(obj):
        try:
            return str(obj)
        except:
            return None

    # Save JSON
    with open(json_filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, default=default_serializer)

    # Save CSV
    with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Category", "Result"])
        for key, value in data.items():
            if isinstance(value, dict) or isinstance(value, list):
                writer.writerow([key, json.dumps(value, default=default_serializer)])
            else:
                writer.writerow([key, value])

    print(Fore.GREEN + f"\n[+] Results saved to {json_filename} and {csv_filename}\n")

async def main():
    # ASCII ART
    print(Fore.RED + Style.BRIGHT + """
⠀⠀⠀⢠⣾⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣰⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢰⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣄⣀⣀⣤⣤⣶⣾⣿⣿⣿⡷
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀
⣿⣿⣿⡇⠀⡾⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀
⣿⣿⣿⣧⡀⠁⣀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⢹⠉⠙⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣀⠀⣀⣼⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⠿⠋⢃⠈⠢⡁⠒⠄⡀⠈⠁⠀⠀⠀⠀⠀⠀⠀
⣿⣿⠟⠁⠀⠀⠈⠉⠉⠁⠀⠀⠀⠀⠈⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")

    print(Fore.WHITE + Style.BRIGHT + """
███▄▄▄▄      ▄████████    ▄█    █▄     ▄█     ▄████████
███▀▀▀██▄   ███    ███   ███    ███   ███    ███    ███
███   ███   ███    ███   ███    ███   ███▌   ███    █▀ 
███   ███   ███    ███  ▄███▄▄▄▄███▄▄ ███▌   ███       
███   ███ ▀███████████ ▀▀███▀▀▀▀███▀  ███▌ ▀███████████
███   ███   ███    ███   ███    ███   ███           ███
███   ███   ███    ███   ███    ███   ███     ▄█    ███
 ▀█   █▀    ███    █▀    ███    █▀    █▀    ▄████████▀ 
""")

    domain = input(Fore.WHITE + Style.BRIGHT + "[?] Enter domain to scan: ").strip()
    print(Fore.RED + "\n[+] Starting scan...\n")

    results = await run_all_checks(domain)
    save_results(domain, results)

    print(Fore.GREEN + "\n[✓] Scan complete!\n")

if __name__ == "__main__":
    asyncio.run(main())
