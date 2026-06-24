from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    # 讀取環境變數，展示 K8s 的動態配置能力
    env_msg = os.getenv("ENV_MSG", "這是 Python CI/CD 預設文字")
    pod_name = socket.gethostname()
    return f"""
    <h1>🐍 碼叔的第一個 Python 專業 CI/CD 網頁！!!!!!!!!!!!</h1>
    <p>目前環境變數：<b>{env_msg}</b></p>
    <p>提供服務的 Pod 節點：<span style="color:blue">{pod_name}</span></p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
