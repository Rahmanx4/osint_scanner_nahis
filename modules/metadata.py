# Extract metadata from media files (images, pdf) found on homepage

import aiohttp
import re
import PyPDF2
from PIL import Image
from io import BytesIO

async def extract_metadata(domain):
    results = {
        "images": [],
        "pdf": []
    }

    try:
        homepage = f"http://{domain}"

        async with aiohttp.ClientSession() as session:
            async with session.get(homepage, timeout=6) as r:
                html = await r.text()

        # Find images
        img_urls = re.findall(r'src="([^"]+\.(?:png|jpg|jpeg))"', html)

        async with aiohttp.ClientSession() as session:
            for img in img_urls[:5]:
                try:
                    async with session.get(f"http://{domain}/{img.lstrip('/')}", timeout=6) as r:
                        data = await r.read()
                        img_obj = Image.open(BytesIO(data))
                        results["images"].append(img_obj.getexif())
                except:
                    pass

        # Find PDFs
        pdf_urls = re.findall(r'href="([^"]+\.pdf)"', html)

        async with aiohttp.ClientSession() as session:
            for pdf in pdf_urls[:5]:
                try:
                    async with session.get(f"http://{domain}/{pdf.lstrip('/')}", timeout=6) as r:
                        data = await r.read()
                        pdf_reader = PyPDF2.PdfReader(BytesIO(data))
                        results["pdf"].append(pdf_reader.metadata)
                except:
                    pass

    except Exception:
        pass

    return results
