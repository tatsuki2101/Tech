import whisper
from typing import List

def transcribe_segments(segment_paths: List[str], model_size: str = "base") -> List[str]:
    """
    各セグメントファイルに対してWhisperを用いて文字起こしを行う。
    テキストのリストを返す。
    """
    model = whisper.load_model(model_size)
    results = []

    for path in segment_paths:
        result = model.transcribe(path, language="ja")
        text = result.get("text", "").strip()
        results.append(text)

    return results
