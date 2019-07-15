import os
import json
import jieba


def iter_files(rootDir):
    fp = open("wiki.txt", 'w', encoding='utf-8')
    for root, dirs, files in os.walk(rootDir):
        for file in files:
            file_name = os.path.join(root, file)
            with open(file_name, 'r', encoding='utf-8') as wiki:
                for line in wiki:
                    text = json.loads(line)['text']
                    seg_list = jieba.cut(text)
                    fp.write(" ".join(seg_list))


iter_files('wiki_zh')
