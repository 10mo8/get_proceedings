#スクレイピングしてきたデータの整形を行います
import re

#発言の部分だけを元データから抽出します
with open("original.txt", "r", encoding="utf-8") as fin, open("extract_speech.txt", "w", encoding="utf-8") as fout:
    texts = [text.strip() for text in fin.readlines()]
    for text in texts:
        matchobj = re.search(r"○", text)
        if matchobj is not None:
            fout.write(text)

#発言の中から第1文だけを抽出します
with open("extract_speech.txt", "r", encoding="utf-8") as fin, open("extract_fspeech.txt", "w", encoding="utf-8") as fout:
    texts = fin.read()
    texts = texts.replace("\n", "")
    texts = texts.split("○")
    for text in texts:
        matchobj = re.search(r"。", text)
        if matchobj is not None:
            fout.write(text[:matchobj.start()] + "\n")

#特定の議員の発言とその議員の前の発言を抽出します
with open("extractf_speech.txt", "r", encoding="utf-8") as fin, open("conv.txt", "w", encoding="utf-8") as fout:
    texts = [text.strip() for text in fin.readlines()]
    prevname = ""
    prevtext = ""

    for text in texts:
        matchobj = re.search(r"　", text)
        if matchobj is not None:
            #発言者の名前
            name = text[0:matchobj.start()]
            #発言内容
            sentence = text[matchobj.end():]
            
            #名前が抽出対象なら前のテキストを返す
            #if name == "蓮舫君":
            prevtext = prevtext.replace("、", "")
            prevtext = prevtext.replace("…", "")
            prevtext = re.sub(r"\（.*\）", "", prevtext)

            sentence = sentence.replace("、", "")
            sentence = sentence.replace("…", "")
            sentence = re.sub(r"\（.*\）", "", sentence)
            #特定の人物の応答を抽出します
            fout.write(prevtext+ "," + sentence + "\n")
            prevtext = ""

            prevname = name
            prevtext = sentence