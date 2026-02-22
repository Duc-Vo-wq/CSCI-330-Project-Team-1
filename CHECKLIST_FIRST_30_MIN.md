# First 30 Minutes Checklist (Team 1)

This checklist is designed to prevent 95% of common issues.

## A. Before you start (5 minutes)
1) Confirm your laptop has **8GB RAM**.
2) Confirm virtualization is enabled:
   - Windows: Task Manager → Performance → CPU → “Virtualization: Enabled”
   - macOS (Intel): typically enabled by default
3) Install **VirtualBox**.

## B. Build the isolated lab network (10 minutes)
4) Follow `LOCAL_LAB_SETUP.md` to create a **Host-only** network for your team.
5) Confirm your Host-only adapter settings match:
   - IP and mask shown in `LOCAL_LAB_SETUP.md`
   - DHCP disabled (recommended)

## C. Bring the VM online (10 minutes)
6) Attach your Linux VM to the Host-only adapter.
7) Set the VM static IP shown in `LOCAL_LAB_SETUP.md`.
8) From your host laptop, verify:
   - Windows PowerShell: `ping <VM_IP>`
   - macOS: `ping -c 2 <VM_IP>`

## D. Start services on the VM (2 minutes)
9) Inside the VM, run:
```bash
cd vm_tools
chmod +x START_SERVICES.sh
./START_SERVICES.sh
```

## E. Verify ports from the host (3 minutes)
10) Windows PowerShell:
```powershell
Test-NetConnection <VM_IP> -Port 80
Test-NetConnection <VM_IP> -Port 8080
Test-NetConnection <VM_IP> -Port 22
```
macOS:
```bash
nc -vz <VM_IP> 80
nc -vz <VM_IP> 8080
nc -vz <VM_IP> 22
```

If Steps 8–10 pass, you are ready for this assignment.

---

# Where to find everything
- Targets: `LAB_TARGETS.md`
- Setup: `LOCAL_LAB_SETUP.md`
- Start VM services: `vm_tools/START_SERVICES.sh`
- Project instructions: `PROJECTS_OVERVIEW.md`
- Required CLI flags: `CLI_SPEC.md`
- Output templates: `project*/OUTPUT_TEMPLATE_*.json/.md`
- Grading: `RUBRIC_50_POINTS.md`

---

# Hard rules (read)
- Only scan the CIDR in `LAB_TARGETS.md`.
- Do not test/scans outside the lab.
- Outputs must match the provided templates.

Tip: If you don’t have an OVA, install Ubuntu using `ISO_INSTALL_GUIDE.md` first.

