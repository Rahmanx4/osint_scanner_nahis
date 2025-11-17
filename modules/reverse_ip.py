# Reverse IP lookup using HackerTarget API

import aiohttp

async def reverse_ip_lookup(domain):
    api_url = f"https://api.hackertarget.com/reverseiplookup/?q={domain}"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(api_url, timeout=6) as response:
                text = await response.text()

                if "error" in text.lower():
                    return []

                domains = text.splitlines()
                return domains

    except Exception:
        return []
