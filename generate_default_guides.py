#!/usr/bin/python
# -*- coding: utf-8 -*-

from gimpfu import *

def generate_default_guides(image):
    # 画像の幅と高さを取得
    i_w = pdb.gimp_image_width(image)
    i_h = pdb.gimp_image_height(image)

    # ガイドを追加
    pdb.gimp_image_add_vguide(image, 0)
    pdb.gimp_image_add_hguide(image, 0)
    pdb.gimp_image_add_vguide(image, int(i_w))
    pdb.gimp_image_add_hguide(image, int(i_h))
    pdb.gimp_image_add_vguide(image, int(i_w * 0.5))
    pdb.gimp_image_add_hguide(image, int(i_h * 0.5))

register(
    "generate_default_guides",
    "自動でガイドを生成します",
    "選択レイヤーに関係なく、画像全体にガイドを追加します",
    "作者名",
    "作者名",
    "Mar 2025",
    "<Image>/Filters/Custom/GenerateDefaultGuids",
    "RGB*, GRAY*",   # 適用可能な画像タイプ
    [
        (PF_IMAGE, "image", "Input Image", None),
    ],
    [], 
    generate_default_guides
)

main()