import builtwith
from colorama import Fore, Style

def tech_fingerprint(domain):
    """
    Fingerprint target technologies using builtwith.
    Returns dict of categories → technologies.
    """
    print(Fore.CYAN + f"[Tech] Detecting technologies…" + Style.RESET_ALL)

    try:
        tech = builtwith.parse(f"https://{domain}")
        clean = {}

        # Normalize and clean empty entries
        for category, items in tech.items():
            if not items:
                continue
            clean[category] = list(set(items))

        if not clean:
            print(Fore.YELLOW + "[Tech] No technologies detected." + Style.RESET_ALL)
            return None

        print(Fore.GREEN + "[Tech] Technologies found." + Style.RESET_ALL)
        return clean

    except Exception as e:
        print(Fore.RED + f"[Tech] Error: {e}" + Style.RESET_ALL)
        return None
