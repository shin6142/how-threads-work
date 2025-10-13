from flask import Flask
import time
import os

# アプリケーション設定
app = Flask(__name__)
PORT = 3000

@app.route('/<string:value>', methods=['GET'])
def main(value):
    """
    リクエストを受け取り、1秒間ブロッキング処理を行います。
    """
    result = '{0}'.format(value)
    
    # 処理開始ログ (ターミナルに出力)
    print(f'[start] {result} - Process ID: {os.getpid()}')

    # 意図的に1秒間ブロッキング（I/O待ちをシミュレート）
    time.sleep(1)

    # 処理終了ログ
    print(f'[end] {result} - Process ID: {os.getpid()}')
    
    # HTTP応答
    return ""

def single_thread():
    print('=========シングルスレッド=========')
    app.run(host='0.0.0.0', port=PORT, threaded=False, debug=False)

def multi_thread():
    print('=========マルチスレッド=========')
    app.run(host='0.0.0.0', port=PORT, debug=False)


if __name__ == "__main__":
    # single_thread()
    multi_thread()
