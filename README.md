# OSINT Scanner

NAHIS OSINT Scanner is a Python tool for performing OSINT (Open Source Intelligence) on websites. It collects information such as DNS records, WHOIS data, IP details, SSL certificates, subdomains, open ports, emails, and metadata.

## Features
- DNS Lookup  
- WHOIS Lookup  
- IP Lookup  
- SSL Certificate Analysis  
- Technology Detection  
- Port Scanning  
- Subdomain Discovery  
- Email Extraction  
- Reverse IP Lookup  
- Metadata Extraction  
- Save results in JSON & CSV formats  

## Requirements
Install the Python dependencies:

```bash
pip install -r requirements.txt
Environment File
Store sensitive tokens in a .env file:

ini
Copy code
IPINFO_TOKEN=your_api_key_here
Do not commit .env to public repositories.

Usage
Run the tool:

bash
Copy code
python main.py
Enter the domain to scan when prompted. Results will be saved automatically in the results/ folder.

License

This project is free to use, modify, and redistribute.
