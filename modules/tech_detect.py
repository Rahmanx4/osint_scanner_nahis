from colorama import Fore, Style
import aiohttp
import re

# Simple technology detection by keywords in HTML and headers
TECH_KEYWORDS = {
    "WordPress": ["wp-content", "wp-includes"],
    "Joomla": ["content=\"Joomla!"],
    "Drupal": ["Drupal.settings"],
    "React": ["data-reactroot", "react-dom"],
    "Angular": ["ng-app"],
    "Vue": ["vue"],
    "Shopify": ["cdn.shopify.com"],
    "Cloudflare": ["cloudflare"],
}

async def tech_detect(domain):
    result = []
    urls = [f"https://{domain}", f"http://{domain}"]

    async with aiohttp.ClientSession() as session:
        for url in urls:
            try:
                async with session.get(url, timeout=5, ssl=False) as resp:
                    html = await resp.text()
                    # Detect technologies by keywords
                    detected = []
                    for tech, keywords in TECH_KEYWORDS.items():
                        for kw in keywords:
                            if kw.lower() in html.lower():
                                detected.append(tech)
                                break
                    result = list(set(detected))
                    print(Fore.CYAN + f"[Tech] Completed → {domain}" + Style.RESET_ALL)
                    return result
            except Exception:
                continue

    print(Fore.RED + f"[Tech] Failed for {domain}" + Style.RESET_ALL)
    return result
