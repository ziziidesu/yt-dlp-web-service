import subprocess
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        # yt-dlpを使って動画をダウンロード
        result = subprocess.run(['yt-dlp', url], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
