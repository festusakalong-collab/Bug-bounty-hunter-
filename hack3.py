# hack3.py - Safe Recon v1
import requests

target = input("Enter in-scope domain (e.g. example.com): ").strip()
print(f"[+] Checking {target} - make sure it's IN SCOPE!")

try:
    r = requests.get(f"https://{target}", timeout=5)
    print(f"[+] LIVE -> {target} Status: {r.status_code}")
    print(f"[+] Headers: {r.headers.get('Server', 'unknown server')}")
except Exception as e:
    print(f"[-] Down or blocked: {e}")

print("[+] Done - save this for report")
