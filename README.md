# 🤖 Moltbot Kimi - Clawdbot Hub

### 🚀 Quick Start
1. **Sync**: `git pull origin main`
2. **Validate**: `python3 check_health.py`
3. **Deploy**: `sudo systemctl restart clawdbot-gateway`

### 🛠️ Estrutura de Pastas
- `/skills`: Scripts funcionais (Python/Bash).
- `/config`: Backups do `clawdbot.json` e `gateway.json`.
- `/docs`: Documentação de arquitetura (Kimi K2 Swarm).
- `.env`: Parâmetros de ambiente (Sensitive).

### 📡 Endpoints
- **API**: http://100.114.222.10:18789
- **Control UI**: Localhost (via Tailscale)