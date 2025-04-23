from typing import List

def format_bullet_text(lines: List[str]) -> str:
    """
    テキストリストを箇条書き＋空白行で整形して1つの文字列にする。
    空の文やノイズ行はスキップする。
    """
    formatted = []

    for line in lines:
        clean_line = line.strip()
        if clean_line:
            formatted.append(f"・{clean_line}")
            formatted.append("")  # 空白行を追加

    return "\n".join(formatted).strip()
