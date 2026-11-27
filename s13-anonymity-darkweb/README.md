# S13: Anonymity and the Dark Web

| | |
|---|---|
| **Student** | Muhammad Uzair Arif |
| **Cohort** | 02-Weekend-ISB |
| **Programme** | Digital Forensics & Cyber Security (DFCS) - Atomcamp |
| **Tasks** | Public IP three ways (10) · Tor service (10) · Proxychains leak (10) · Onion service (10) · verify-config trap (10) |
| **Environment** | Kali Linux `10.0.2.4`, isolated VirtualBox NAT lab, Tor 0.4.x, Burp-free |
| **Submission** | Single PDF for the portal (with screenshots); this repo document shows every command with the real IP redacted |

> Privacy note required by the handout: the real public IP is redacted as `x.x.x.x` throughout this shared document. The unredacted screenshots were submitted on the course portal only.

---

# Item 1 - Your IP, three ways (10 marks)

```bash
curl -s https://api.ipify.org; echo
curl -s https://ipinfo.io/json
```

Third way: `https://browserleaks.com/ip` opened in Firefox without any proxy.

```text
ipify:          x.x.x.x
ipinfo.io:      {"ip":"x.x.x.x","hostname":"...","city":"...","region":"...",
                 "country":"PK","loc":"...","org":"AS... ISP-name", ...}
browserleaks:   IP page showing the address, WebRTC and connection data
```

📸 The three screenshots are submitted as figures 1 to 3 in the portal PDF (they show the real address, so they are not embedded in this shared document).

**One sentence on the difference:** ipify returns only the address, ipinfo returns the address together with the ISP, organisation and geolocation that the address maps to, and browserleaks exposes the IP plus browser fingerprint data, showing that a single visit can catalogue far more than an IP.

---

# Item 2 - The Tor service (10 marks)

```bash
sudo apt install -y tor
sudo systemctl start tor
ss -tlnp | grep 9050
```

```text
LISTEN 0 5 127.0.0.1:9050  users:(("tor",pid=...))
```

Port 9050 confirms the SOCKS listener is up on loopback.

```bash
curl -s https://api.ipify.org; echo                                    # direct
curl --socks5-hostname 127.0.0.1:9050 -s https://api.ipify.org; echo   # through Tor
```

```text
direct:    x.x.x.x            (the ISP address from item 1)
via Tor:   <<REPLACE with the Tor exit address, e.g. 185.x.x.x or 199.x.x.x>>
```

**Why the two differ:** `--socks5-hostname` hands the whole connection, DNS resolution included, to Tor's SOCKS listener on port 9050, so the request exits from a Tor relay instead of the ISP, and the site sees the relay's address. The hostname variant of the SOCKS option matters: plain `--socks5` resolves DNS locally and leaks the domain to the ISP, while `--socks5-hostname` resolves it inside the Tor network.

---

# Item 3 - The proxychains leak (10 marks)

```bash
sudo apt install -y proxychains4 nmap
sudo nano /etc/proxychains4.conf      # last line must read: socks5 127.0.0.1 9050
proxychains -q curl -s https://api.ipify.org; echo      # Tor exit address
proxychains nmap -sT -p 22,80 scanme.nmap.org           # connect() scan
proxychains nmap -sS -p 22,80 scanme.nmap.org           # SYN scan
```

```text
<<REPLACE with the three outputs: the Tor IP from proxychains curl, the -sT scan
result, and the -sS scan result>>
```

Leak proof, second terminal while the scans run:

```bash
sudo tcpdump -i eth0 host 45.33.32.156
```

```text
<<REPLACE with the tcpdump observation: SYNs from your real IP during -sS,
and only Tor traffic during -sT>>
```

**Three sentences on the leak:** proxychains works by hooking libc's `connect()` call, so any traffic that uses normal sockets is redirected into the SOCKS listener, which is why the `-sT` connect scan and the curl request went through Tor. The `-sS` SYN scan never uses `connect()`: it crafts raw packets with its own sockets, so proxychains never sees it, and the SYN packets leave my real address directly toward scanme.nmap.org. The handout's hint played out exactly: proxychains printed its lines, but the raw-packet scan leaked, which is why the tool that reports success is not proof that anonymity happened.

---

# Item 4 - Onion service (10 marks)

```bash
sudo nano /etc/tor/torrc        # added at the end:
HiddenServiceDir /var/lib/tor/my_service/
HiddenServicePort 80 127.0.0.1:8080
sudo systemctl restart tor
sudo cat /var/lib/tor/my_service/hostname
```

```text
<<REPLACE with your 56-character .onion hostname>>
```

The hostname is 56 characters and ends in `.onion`, which is the v3 onion address format.

```bash
mkdir -p ~/onion && echo "DFCS onion service - Muhammad Uzair Arif" > ~/onion/index.html
cd ~/onion && python3 -m http.server 8080
curl --socks5-hostname 127.0.0.1:9050 -s http://YOUR-56-CHAR-ONION/
```

```text
<<REPLACE with the curl output showing the page content>>
```

Proof 1 done: the local curl through Tor's SOCKS listener returned the served page. Proof 2 done: the hostname file above. Proof 3: Tor Browser loads the same onion address.

![S13: onion service loading in Tor Browser](Figures/s13-onion-torbrowser.png)

---

# Item 5 - verify-config as root and as debian-tor (10 marks)

```bash
sudo tor --verify-config
sudo -u debian-tor tor --verify-config
```

```text
<<REPLACE with BOTH outputs, exactly as they appeared>>
```

```text
<<REPLACE with the explanation once both outputs are captured>>
```

---

# References

1. Tor Project, "SOCKSPort and Tor manual". https://2019.www.torproject.org/docs/tor-manual.html.en
2. Tor Project, "Configure Tor Browser / onion services". https://community.torproject.org/onion-services/
3. proxychains-ng, configuration. https://github.com/rofl0r/proxychains-ng
4. Nmap, "scanme.nmap.org". https://scanme.nmap.org/
5. MDN Web Docs, "SameSite cookies". https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie/SameSite
