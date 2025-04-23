from pydub import AudioSegment

def load_mp3(path: str) -> AudioSegment:
    """
    MP3ファイルを読み込み、AudioSegmentオブジェクトとして返す。
    """
    audio = AudioSegment.from_mp3(path)
    audio = audio.set_channels(1).set_frame_rate(16000)  # Whisper向けに整形
    return audio
