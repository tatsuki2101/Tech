import os
from typing import List
from pydub import AudioSegment
from pydub.silence import detect_nonsilent

def split_by_silence(audio: AudioSegment, temp_dir: str, min_silence_len: int = 1000, silence_thresh: int = -40) -> List[str]:
    """
    音声を無音区間で分割し、各セグメントをWAVファイルとして保存。
    保存されたファイルのパスのリストを返す。
    """
    nonsilent_ranges = detect_nonsilent(audio, min_silence_len=min_silence_len, silence_thresh=silence_thresh)

    segment_paths = []

    for i, (start, end) in enumerate(nonsilent_ranges):
        chunk = audio[start:end]
        segment_path = os.path.join(temp_dir, f"segment_{i:03}.wav")
        chunk.export(segment_path, format="wav")
        segment_paths.append(segment_path)

    return segment_paths
