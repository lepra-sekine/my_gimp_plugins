#!/usr/bin/python
# -*- coding: utf-8 -*-

from gimpfu import *

def generate_default_guides(image):
    i_w = pdb.gimp_image_width(image)
    i_h = pdb.gimp_image_height(image)

    # 縦ガイド
    pdb.gimp_image_add_vguide(image, 0)              # 左端
    pdb.gimp_image_add_vguide(image, i_w)            # 右端
    pdb.gimp_image_add_vguide(image, int(i_w / 2))   # 中央

    # 横ガイド
    pdb.gimp_image_add_hguide(image, 0)              # 上端
    pdb.gimp_image_add_hguide(image, i_h)            # 下端
    pdb.gimp_image_add_hguide(image, int(i_h / 2))   # 中央

    # 更新して画面に反映
    pdb.gimp_displays_flush()


register(
    "generate_default_guides",
    "画像の両端と中央にガイドを追加",
    "画像全体の両端と中央に縦横のガイドを自動で作成します",
    "SR",
    "SR",
    "Mar 2025",
    "<Image>/Filters/Custom/GenerateDefaultGuides",
    "",
    [
        (PF_IMAGE, "image", "Input Image", None),
    ],
    [],
    generate_default_guides,
    menu="")

main()