# HTTP Info Module
# -------------------------------
# - Fetches HTTP headers
# - Detects server type
# - Detects content-type
# - Extracts redirect chain
# - Basic security-headers detection
# -------------------------------

import aiohttp
import asyncio

async def http_info(target):
    """Return basic HTTP information about the target asynchronously"""

    if not target.startswith("http://") and not target.startswith("https://"):
        target = "http://" + target  # auto-add protocol if missing

    result = {
        "url": target,
        "final_url": None,
        "status_code": None,
        "headers": {},
        "server": None,
        "content_type": None,
        "redirects": [],
        "security_headers": [],
    }

    try:
        timeout = aiohttp.ClientTimeout(total=8)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(target, allow_redirects=True) as response:
                result["final_url"] = str(response.url)
                result["status_code"] = response.status
                result["headers"] = dict(response.headers)

                # server detection
                result["server"] = response.headers.get("Server")

                # content-type detection
                result["content_type"] = response.headers.get("Content-Type")

                # redirect chain
                for r in response.history:
                    result["redirects"].append({
                        "status": r.status,
                        "url": str(r.url)
                    })

                # important security headers
                important_headers = [
                    "Strict-Transport-Security",
                    "Content-Security-Policy",
                    "X-Frame-Options",
                    "X-XSS-Protection",
                    "Referrer-Policy",
                    "Permissions-Policy"
                ]
                for h in important_headers:
                    if h in response.headers:
                        result["security_headers"].append(h)

    except Exception as e:
        result["error"] = str(e)

    return result
