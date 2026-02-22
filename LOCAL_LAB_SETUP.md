# Local Lab Setup (VirtualBox Host-Only) — Windows + macOS

## Minimum Laptop/VM Requirements (Course Assumption)
We assume each student has a laptop with **at least 8GB RAM**.

Recommended VM (works well on 8GB RAM):
- OS: **Ubuntu Server** (preferred) or Lubuntu
- VM RAM: **1.5 GB** (1 GB minimum; 2 GB if available)
- CPU: **1 vCPU** (2 vCPU if available)
- Disk: **12–20 GB**
- Virtualization: **Intel VT-x / AMD-V enabled**
- VirtualBox installed (Windows/macOS)

Network adapters:
- Adapter 1: **Host-Only** (required)
- Adapter 2: **NAT** (optional, only for downloading packages)

If your laptop cannot run a VM, contact the instructor early.

You will create a **private, isolated** mini-network on your own laptop so this assignment have real targets.
This prevents accidental scanning of the campus/home network.

## Your Team Network (do not change)
- Team CIDR (assignment): **10.50.0.0/29**
- Host-only adapter IP (your laptop on the lab network): **10.50.0.1**
- VM IP (Recon target for assignment): **10.50.0.2**

---

## Prerequisites


See `VM_ACQUISITION.md` and `ISO_INSTALL_GUIDE.md` for getting Ubuntu installed (no OVA needed).


## VM acquisition options (default: ISO install)
- **Fastest:** Import an instructor-provided `.ova` (see `VM_ACQUISITION.md`).
- **Alternative:** Install Ubuntu Server from ISO (also linked in `OVA_OPTION.md`).


- VirtualBox installed (Windows or macOS)
- A Linux VM (recommended: Ubuntu Server or Lubuntu)
  - Best: instructor-provided OVA (import)
  - Otherwise: install Ubuntu Server from ISO

Your host machine (laptop) will run the scanner scripts.
Your VM will run a few services (HTTP/SSH) so your scanner finds open ports.

---

## Step 1 — Create a Host-Only Network (VirtualBox)
1) Open VirtualBox
2) Go to **Tools → Network → Host-only Networks**
3) Click **Create**
4) Select the new host-only network and configure:
   - IPv4 Address: **10.50.0.1**
   - IPv4 Network Mask: **255.255.255.248** (this is /29)
   - **Disable DHCP** (recommended)

> If VirtualBox shows “CIDR”, enter the host IP and set the mask to 255.255.255.248.

---

## Step 2 — Attach the VM to the Host-Only Network
VM → **Settings → Network**
- Adapter 1: Enable
- Attached to: **Host-only Adapter**
- Name: choose the host-only network you created in Step 1

(Optional) You may keep NAT as Adapter 2 if you need the VM to download packages.
If you do, scanning must still only target your assigned CIDR/IP.

---

## Step 3 — Set a Static IP Inside the VM
### Ubuntu (netplan) quick steps
1) Find your interface name:
```bash
ip a
```
Look for something like `enp0s3` or `ens33`.

2) Edit netplan:
```bash
sudo nano /etc/netplan/01-netcfg.yaml
```

3) Use this template (replace interface name as needed):
```yaml
network:
  version: 2
  ethernets:
    <INTERFACE_NAME>:
      dhcp4: no
      addresses:
        - 10.50.0.2/29
```

4) Apply:
```bash
sudo netplan apply
```

5) Test:
```bash
ping -c 2 10.50.0.1
```

> If `ping` fails: check VM is attached to Host-only and the host-only network uses the right IP/mask.

---

## Step 4 — Start Lab Services on the VM

## Optional (Recommended): one-command service startup
Inside your Linux VM, you can use the helper in this zip:
- `vm_tools/START_SERVICES.sh`
See `vm_tools/README_VM_TOOLS.md`.

These services create “open ports” for assignment and data for assignment.

### A) HTTP server on port 80
```bash
sudo python3 -m http.server 80 --bind 0.0.0.0
```

### B) HTTP server on port 8080
Open a second terminal and run:
```bash
python3 -m http.server 8080 --bind 0.0.0.0
```

### C) SSH (port 22)
```bash
sudo apt-get update
sudo apt-get install -y openssh-server
sudo systemctl enable --now ssh
```

### If firewall is enabled on the VM (UFW)
```bash
sudo ufw allow 22
sudo ufw allow 80
sudo ufw allow 8080
```

---

## Step 5 — Verify from your laptop (host)
### Windows (PowerShell)
```powershell
ping 10.50.0.2
Test-NetConnection 10.50.0.2 -Port 80
Test-NetConnection 10.50.0.2 -Port 8080
Test-NetConnection 10.50.0.2 -Port 22
```

### macOS (Terminal)
```bash
ping -c 2 10.50.0.2
nc -vz 10.50.0.2 80
nc -vz 10.50.0.2 8080
nc -vz 10.50.0.2 22
```

> If macOS doesn’t have `nc`, install it via Homebrew or skip port checks and just confirm ping works.

---

## How this maps to your projects
### assignment (Recon)
Use the recon target IP from `LAB_TARGETS.md`:
- `10.50.0.2`

### assignment (Scanner)
Scan your team CIDR:
- `10.50.0.0/29`

### assignment (Findings)
Run your findings engine on the output from assignment.

### assignment (PCAP Hunt)
No network setup needed — use the provided PCAP file.

---

## Troubleshooting (common issues)
- **Virtualization not enabled:** enable Intel VT-x / AMD-V in BIOS/UEFI.
- **No ping to VM:** re-check host-only adapter IP/mask, VM attached to host-only, VM static IP.
- **Ports closed:** ensure the HTTP servers are running; check UFW rules.
- **Windows firewall blocks ping/ports:** temporarily allow VirtualBox host-only traffic or disable firewall for the host-only adapter.

If you cannot run a VM due to hardware limits, contact the instructor early.