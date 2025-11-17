import whois
from colorama import Fore, Style

# WHOIS lookup
async def whois_lookup(domain):
    result = {}
    try:
        w = whois.whois(domain)
        # convert all fields to string
        for key, value in w.items():
            if value is None:
                continue
            if isinstance(value, (list, tuple)):
                value = ", ".join(map(str, value))
            result[key] = str(value)
    except Exception as e:
        print(Fore.RED + f"[WHOIS] Failed: {e}" + Style.RESET_ALL)
        return {}

    print(Fore.CYAN + f"[WHOIS] Completed → {domain}" + Style.RESET_ALL)
    return result
