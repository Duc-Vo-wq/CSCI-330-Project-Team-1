# Ubuntu VM (ISO Install) — Default Setup (No OVA Needed)

For this course, assume **no OVA is provided**. You will install Ubuntu in VirtualBox from an ISO, then follow the team
zip instructions for Host-only networking and targets.

## What you will do
1) Download Ubuntu Server ISO
2) Create a VirtualBox VM and install Ubuntu
3) Attach the VM to your team Host-only network (see `LOCAL_LAB_SETUP.md`)
4) Set the VM static IP for your team (see `LOCAL_LAB_SETUP.md`)
5) Start lab services in the VM with `vm_tools/START_SERVICES.sh`

---

## Step 1 — Download Ubuntu Server ISO
Download Ubuntu Server (LTS recommended) from Canonical:
- Ubuntu Server download page: https://ubuntu.com/download/server

> If the page offers multiple versions, choose the latest **LTS**.

---

## Step 2 — Create the VM in VirtualBox (Windows/macOS)
VirtualBox → **New**
Recommended settings (works on 8GB laptops):
- Name: `CyberLab-Ubuntu`
- Type: Linux
- Version: Ubuntu (64-bit)
- Memory: **1536 MB** (1.5 GB) (or 2048 MB if available)
- CPU: **1** (2 if available)
- Disk: **12–20 GB** (dynamically allocated)

When prompted for installation media, select the ISO you downloaded.

---

## Step 3 — Install Ubuntu Server (minimal choices)
During the Ubuntu Server installer:
- Create a user (example): `student`
- Set a password you will remember
- Enable OpenSSH server if the installer asks (optional; the script can install it later)
- Use defaults for the rest (no encryption, no special storage)

After installation, reboot into Ubuntu.

---

## Step 4 — Install basics (inside the VM)
Run:
```bash
sudo apt-get update -y
sudo apt-get install -y python3 python3-pip
```

(SSH is optional; `START_SERVICES.sh` will install it if missing.)

---

## Step 5 — Continue with your Team Zip
Now go back to your team pack and follow in this order:
1) `ROOT_README.md`
2) `QUICKSTART.md`
3) `CHECKLIST_FIRST_30_MIN.md`
4) `LOCAL_LAB_SETUP.md`
5) Start services: `vm_tools/START_SERVICES.sh`

---

## Common issues
- VirtualBox says 64-bit not available: enable Intel VT-x / AMD-V in BIOS/UEFI.
- VM has no internet for apt-get: keep Adapter 1 as NAT during install; later add Host-only as shown in `LOCAL_LAB_SETUP.md`.
