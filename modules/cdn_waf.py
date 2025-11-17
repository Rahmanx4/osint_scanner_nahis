# Detect CDN and WAF based on headers and IP patterns

import aiohttp
from colorama import Fore

async def detect_cdn_waf(domain):
    result = {
        "cdn": None,
        "waf": None,
        "raw_headers": {}
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"http://{domain}", timeout=6) as r:
                headers = {k.lower(): v.lower() for k, v in r.headers.items()}
                result["raw_headers"] = headers

                # CDN detection
                cdn_signatures = {
                    "cloudflare": ["cf-ray", "cf-cache-status"],
                    "akamai": ["akamai"],
                    "fastly": ["fastly"],
                    "cloudfront": ["x-amz-cf-id"]
                }

                for cdn, sigs in cdn_signatures.items():
                    if any(sig in headers for sig in sigs):
                        result["cdn"] = cdn
                        break

                # WAF detection
                waf_signatures = {
                    "cloudflare": ["cf-ray"],
                    "sucuri": ["x-sucuri-id"],
                    "imperva": ["x-iinfo", "x-cdn"],
                    "f5": ["bigip"]
                }

                for waf, sigs in waf_signatures.items():
                    if any(sig in headers for sig in sigs):
                        result["waf"] = waf
                        break

    except Exception:
        return result

    return result
