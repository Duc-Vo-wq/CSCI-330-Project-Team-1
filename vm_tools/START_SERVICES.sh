#!/usr/bin/env bash
set -euo pipefail

# Simple lab services for Cybersecurity Scripting & Automation
# Runs:
# - HTTP on 80 (requires sudo)
# - HTTP on 8080
# - SSH service (installs openssh-server if missing)

echo "[*] Starting lab services..."

# Ensure python3 exists
command -v python3 >/dev/null 2>&1 || { echo "[!] python3 not found. Install Python 3."; exit 1; }

# Install SSH server if missing
if ! command -v sshd >/dev/null 2>&1; then
  echo "[*] Installing openssh-server..."
  sudo apt-get update -y
  sudo apt-get install -y openssh-server
fi

echo "[*] Enabling + starting ssh..."
sudo systemctl enable --now ssh || sudo systemctl enable --now sshd || true

# Open firewall ports if ufw exists and is enabled
if command -v ufw >/dev/null 2>&1; then
  if sudo ufw status | grep -qi "Status: active"; then
    echo "[*] UFW active: allowing 22, 80, 8080..."
    sudo ufw allow 22 || true
    sudo ufw allow 80 || true
    sudo ufw allow 8080 || true
  fi
fi

# Start HTTP servers in background using nohup so they keep running after logout
echo "[*] Starting HTTP server on port 80..."
sudo nohup python3 -m http.server 80 --bind 0.0.0.0 >/tmp/http80.log 2>&1 &

echo "[*] Starting HTTP server on port 8080..."
nohup python3 -m http.server 8080 --bind 0.0.0.0 >/tmp/http8080.log 2>&1 &

echo "[+] Done."
echo "    - Port 22 (SSH) should be open"
echo "    - Port 80  (HTTP) log: /tmp/http80.log"
echo "    - Port 8080(HTTP) log: /tmp/http8080.log"
