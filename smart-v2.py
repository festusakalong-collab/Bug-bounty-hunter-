# smart-v2.py - BASIC + SMART UPGRADE
import requests

def check_live(target):
    """Function - checks 1 domain"""
    try:
        r = requests.get(f"https://{target}", timeout=5)
        print(f"[+] LIVE {target} -> {r.status_code} | Server: {r.headers.get('Server','?')}")
        return True
    except:
        print(f"[-] DOWN {target}")
        return False

# List - many targets
targets = ["example.com", "google.com", "facebook.com", "github.com"]

print("[*] Starting Smart Recon V2...")
# Loop - check each one
live_count = 0
for site in targets:
    if check_live(site):
        live_count += 1

print(f"\n[+] Done! {live_count}/{len(targets)} live")
print("[+] Save this output for your bug bounty report")
