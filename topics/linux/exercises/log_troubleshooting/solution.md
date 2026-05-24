# Reverse Proxy Log Diagnostics - Solution

## 1. Extract Connection Refusal Event
To isolate the connection errors in the log file, use `grep`:
```bash
grep -i "error" nginx_error.log
```
Or to specifically isolate connection refusal events targeting upstream port 5000:
```bash
grep "Connection refused" nginx_error.log | grep "127.0.0.1:5000"
```

## 2. Logical Diagnostics and Resolution Workflow (using systemd)
Since the reverse proxy is up but the upstream port `5000` is refusing connections, the backend daemon is likely stopped or hung. Follow this troubleshooting workflow:

1. **Verify Backend Status**: Inspect whether the system service managing the backend daemon is running:
   ```bash
   systemctl status backend
   ```
2. **Start/Restart the Backend**: If it is `inactive (dead)` or `failed`, start the service:
   ```bash
   systemctl start backend
   ```
3. **Verify Sockets**: Inspect active ports to ensure the process successfully bound port 5000:
   ```bash
   ss -tulpn | grep :5000
   ```
4. **Inspect System Logs**: If the service fails to start, review system logs to find the runtime crash reason:
   ```bash
   journalctl -u backend -n 50
   ```
