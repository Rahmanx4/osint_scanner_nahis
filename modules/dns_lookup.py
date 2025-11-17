import dns.resolver
from colorama import Fore, Style

# DNS lookup (A, NS, MX, TXT)
async def dns_lookup(domain):
    result = {"A": [], "NS": [], "MX": [], "TXT": []}

    try:
        for record_type in ["A", "NS", "MX", "TXT"]:
            try:
                answers = dns.resolver.resolve(domain, record_type, lifetime=3)
                result[record_type] = [r.to_text() for r in answers]
            except Exception:
                result[record_type] = []
    except Exception:
        pass

    print(Fore.CYAN + f"[DNS] Completed → {domain}" + Style.RESET_ALL)
    return result
