# Extract emails from the main web page

import re
import aiohttp

pattern = re.compile(rb"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

async def extract_emails(domain):
    url = f"http://{domain}"
    emails = []

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=6) as r:
                html = await r.read()
                found = pattern.findall(html)
                emails = list(set(e.decode() for e in found))

    except Exception:
        pass

    return emails
