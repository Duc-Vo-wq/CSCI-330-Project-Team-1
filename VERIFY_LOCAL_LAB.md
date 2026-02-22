# Verify Your Local Lab (assignment)

From your host laptop, you should be able to:
- Ping the VM: `ping 10.50.0.2`
- Confirm ports (recommended): 22, 80, 8080 on `10.50.0.2`

If ports are closed, run inside the VM:
```bash
cd vm_tools
chmod +x START_SERVICES.sh
./START_SERVICES.sh
```
