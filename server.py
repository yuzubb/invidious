from flask import Flask, request, jsonify
import yt_dlp
import os

app = Flask(__name__)

@app.route('/download', methods=['GET'])
def download():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400

    ydl_opts = {
        'format': 'best',
        # 保存先を指定（a-Shell内のDocumentsフォルダなど）
        'outtmpl': '~/Documents/%(title)s.%(ext)s',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return jsonify({"status": "success", "message": "Download started/finished"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # a-Shellでアクセス可能なポートを指定
    app.run(host='0.0.0.0', port=8080)
