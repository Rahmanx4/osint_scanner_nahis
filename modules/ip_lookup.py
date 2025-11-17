import socket
from colorama import Fore, Style
import aiohttp
import os

try:
    import ipinfo # type: ignore
except ImportError:
    ipinfo = None

async def ip_lookup(domain, ipinfo_token=None):
    """
    Resolve the IP of a domain and optionally fetch IP info from ipinfo.io
    """
    result = {"ip": None, "ipinfo": {}}

    # Resolve IP
    try:
        ip = socket.gethostbyname(domain)
        result["ip"] = ip
        print(Fore.CYAN + f"[IP] Resolved → {ip}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"[IP] Failed: {e}" + Style.RESET_ALL)
        return result

    # Optional ipinfo.io lookup
    token = ipinfo_token or os.getenv("IPINFO_TOKEN")
    if ipinfo and token:
        try:
            handler = ipinfo.getHandler(token)
            details = handler.getDetails(ip)
            result["ipinfo"] = details.all
            print(Fore.CYAN + f"[IPinfo] Completed → {ip}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"[IPinfo] Failed: {e}" + Style.RESET_ALL)

    return result
