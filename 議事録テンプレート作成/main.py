import os
from parser.docx_parser import parse_docx_structure, get_style_info
from generator.docx_template_builder import extract_common_structure, build_template

INPUT_DIR = "input"
OUTPUT_FILE = "output/template.docx"

def main():
    print("🛠 テンプレート生成開始...")

    structures = []
    style_reference_file = None  # 書式抽出用に先頭ファイル1件を指定

    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".docx"):
            path = os.path.join(INPUT_DIR, filename)
            print(f"📄 処理中: {filename}")
            structure = parse_docx_structure(path)
            structures.append(structure)
            if not style_reference_file:
                style_reference_file = path  # 最初のファイルをベースに書式取得

    if not structures:
        print("⚠ 入力ファイルが見つかりません。")
        return

    common_structure = extract_common_structure(structures)
    if not common_structure:
        print("⚠ 共通構造が見つかりません。")
        return

    style_info = get_style_info(style_reference_file)
    print("🎨 書式情報を取得しました。テンプレートに反映します。")

    build_template(common_structure, OUTPUT_FILE, style_info)
    print(f"✅ テンプレートを {OUTPUT_FILE} に出力しました。")

if __name__ == "__main__":
    main()
