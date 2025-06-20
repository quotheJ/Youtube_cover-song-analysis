import pandas as pd
import csv

df = pd.read_csv('video_informations.csv', header=None)

lines = []
for row in df.itertuples(index=False):
    for cell in row:
        if pd.notnull(cell):
            # セル内の各行をstripして追加
            for line in str(cell).splitlines():
                line = line.strip()
                if line and (len(lines) == 0 or lines[-1] != line):
                    lines.append(line)

# ファイルをテキストとして1行ずつ読み込む
with open('video_informations.csv', encoding='utf-8') as f:
    lines = [line.rstrip('\n') for line in f]

results = []
for idx, line in enumerate(lines):
    if '＜オリジナル＞' in line or '＜Original＞' in line:
        composer_line = None
        # 下の5行以内で「作曲」を探す
        for j in range(idx + 1, min(idx + 6, len(lines))):
            if '作曲' in lines[j]:
                composer_line = lines[j]
                results.append((idx + 1, composer_line))  # 行番号は1始まりに
                break

composers = []
for idx, composer_line in results:
    print(f"オリジナル行番号: {idx}")
    print(f"作曲行: {composer_line}")
    print("-" * 30)

    if "：" in composer_line:
        parts = composer_line.split("：")
    elif " : " in composer_line:
        parts = composer_line.split(" : ")
    else:
        parts = composer_line

    if len(parts) > 1:
        result = parts[1].strip()
    else:
        result = None

    composers.append(result)

print(composers)

with open('comporsers.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for composer in composers:
        # そのまま1セルとして書き込む（Noneは空文字に）
        writer.writerow([composer if composer is not None else ''])

##五行以内