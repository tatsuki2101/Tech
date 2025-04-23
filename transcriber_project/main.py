from audio_utils.converter import load_mp3
from audio_utils.segmenter import split_by_silence
from transcriber.whisper_transcriber import transcribe_segments
from formatter.bullet_formatter import format_bullet_text
import os

TEMP_DIR = "temp"
OUTPUT_DIR = "output"
INPUT_FILE = "input.mp3"

def ensure_dirs():
    os.makedirs(TEMP_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    ensure_dirs()

    print("🎧 音声ファイルの読み込み中...")
    audio = load_mp3(INPUT_FILE)

    print("🔇 無音区間の検出と分割...")
    segments = split_by_silence(audio, temp_dir=TEMP_DIR)

    print("🗣️ 音声認識（Whisper）中...")
    texts = transcribe_segments(segments)

    print("📝 テキスト整形中（箇条書き＋空白行）...")
    formatted = format_bullet_text(texts)

    output_path = os.path.join(OUTPUT_DIR, "output.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(formatted)

    print(f"✅ 完了！出力ファイル: {output_path}")

if __name__ == "__main__":
    main()
