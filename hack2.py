import requests

domain = input("Target domain (e.g facebook.com): ")
subdomains = ["www", "mail", "admin", "api", "test", "dev", "blog"]

print(f"\n[*] Scanning {domain}...\n")

for sub in subdomains:
    url = f"https://{sub}.{domain}"
    try:
        r = requests.get(url, timeout=3)
        if r.status_code < 400:
            print(f"[+] FOUND: {url} -> {r.status_code}")
        else:
            print(f"[-] {url} -> {r.status_code}")
    except:
        print(f"[-] {url} -> DOWN")
