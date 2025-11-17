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

Environment File (.env)

This tool uses an API token for the IP information lookup.
You must create a .env file in the project directory.

Steps:

1. Create a new file named .env in the root folder of the project.

2. Add the following line inside the file:

IPINFO_TOKEN=your_api_key_here

Usage
Run the tool:
python main.py

Enter the domain to scan when prompted. Results will be saved automatically in the results/ folder.



