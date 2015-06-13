#!/usr/bin/python
# -*- coding: utf-8 -*-

# Project Apricot
# Copyright (c) 2015 daiz, mathharachan, risingsun_33178.

import sys
import os.path
import commands

DIR_ORIGINAL = 'original'
DIR_WWW ='www'

def loadRecipeFile(recipefile):
    parts = []
    f = open(recipefile, 'r')
    for line in f:
        line = line.split(';')[0]
        if len(line) > 1:
            parts.append(line.strip())
    f.close()
    return parts

def exeCommand(command_str):
    commands.getoutput(command_str)

if __name__ == '__main__':
    # レシピファイルの名前
    recipefilename = sys.argv[1]
    # レシピファイルのパス
    recipefile = '{}/{}'.format(DIR_ORIGINAL, recipefilename)
    # ビルドターゲットの画像名（拡張子なし）をレシピファイルから読み込む
    targets = loadRecipeFile(recipefile)

    # パーツファイル（divファイル）を生成する
    for target in targets:
        if target[-1] == '*': target = target[:-1].strip()

        exeCommand('./build {}'.format(target))

    # レシピファイルに基いて、パーツファイルを実行ファイル（index.html）に統合する
    exeCommand('python make_index_html.py {} > {}/index.html'.format(recipefilename, DIR_WWW))

    # Chrome アプリを起動する(for mac)
    exeCommand('python lib/launch_chrome_app.py run {}'.format(DIR_WWW))
