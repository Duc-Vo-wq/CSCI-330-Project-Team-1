# VM helper: Start Lab Services

This folder contains a helper script for your **Linux VM** (not your host laptop).

## What it does
- Ensures SSH server is installed/enabled (port 22)
- Starts a Python HTTP server on port 80 (requires sudo)
- Starts a Python HTTP server on port 8080
- If UFW firewall is active, opens ports 22/80/8080

## How to use (inside the VM)
1) Copy the `vm_tools/` folder from your team zip into your VM (any location), or recreate the files.
2) Run:
```bash
cd vm_tools
chmod +x START_SERVICES.sh
./START_SERVICES.sh
```

## How to verify from host
Windows PowerShell:
```powershell
Test-NetConnection <VM_IP> -Port 22
Test-NetConnection <VM_IP> -Port 80
Test-NetConnection <VM_IP> -Port 8080
```

macOS:
```bash
nc -vz <VM_IP> 22
nc -vz <VM_IP> 80
nc -vz <VM_IP> 8080
```
