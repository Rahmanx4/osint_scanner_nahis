import asyncio
import socket
from colorama import Fore, Style

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP-ALT"
}

async def scan_port(ip, port):
    try:
        conn = asyncio.open_connection(ip, port)
        reader, writer = await asyncio.wait_for(conn, timeout=1)

        service = COMMON_PORTS.get(port, "Unknown")
        writer.close()
        await writer.wait_closed()

        return port, service
    except:
        return None


async def port_scan(ip):
    print(Fore.CYAN + f"[Port Scan] Starting scan… {ip}" + Style.RESET_ALL)

    tasks = []
    for port in range(1, 1025):  # Fast scan (1–1024)
        tasks.append(scan_port(ip, port))

    open_ports = []
    for result in await asyncio.gather(*tasks):
        if result:
            open_ports.append(result)

    print(Fore.CYAN + f"[Port Scan] Completed → {ip}" + Style.RESET_ALL)
    return open_ports
