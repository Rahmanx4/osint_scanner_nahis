import ssl
import socket
from datetime import datetime
from colorama import Fore, Style

# SSL certificate info
async def ssl_info(domain):
    result = {"issuer": None, "subject": None, "valid_from": None, "valid_to": None}

    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=domain) as s:
            s.settimeout(5)
            s.connect((domain, 443))
            cert = s.getpeercert()

            result["issuer"] = dict(x[0] for x in cert.get("issuer", []))
            result["subject"] = dict(x[0] for x in cert.get("subject", []))
            result["valid_from"] = cert.get("notBefore")
            result["valid_to"] = cert.get("notAfter")

        print(Fore.CYAN + f"[SSL] Completed → {domain}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"[SSL] Failed: {e}" + Style.RESET_ALL)

    return result
