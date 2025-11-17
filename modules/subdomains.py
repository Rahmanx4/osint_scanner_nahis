import aiohttp
from colorama import Fore, Style

# Simple subdomain scanner (lightweight)
COMMON_SUBDOMAINS = [
    "www", "mail", "ftp", "ns1", "ns2", "blog", "dev", "api", "shop", "test"
]

async def subdomain_scan(domain):
    found = []

    async with aiohttp.ClientSession() as session:
        for sub in COMMON_SUBDOMAINS:
            url = f"http://{sub}.{domain}"
            try:
                async with session.get(url, timeout=3) as resp:
                    if resp.status < 400:
                        found.append(url)
            except Exception:
                continue

    print(Fore.CYAN + f"[Subdomains] Completed → {domain}" + Style.RESET_ALL)
    return found
