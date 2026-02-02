import subprocess
import sys
import json

def get_sys_info():
    try:
        # Comando inteligente para status rápido
        cmd = "uptime -p && free -h | grep Mem | awk '{print \"Memoria: \" $3 \"/\" $2}'"
        output = subprocess.check_output(cmd, shell=True).decode().strip()
        return {"status": "success", "output": output}
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    result = get_sys_info()
    print(json.dumps(result))

