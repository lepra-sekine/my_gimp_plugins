#!/usr/bin/python
# -*- coding: utf-8 -*-

from gimpfu import *

def expand_blur_fill(img, drawable, expand_px=20, feather_px=30, fill_color = (0, 0, 0)):
    # Undo グループ開始
    pdb.gimp_image_undo_group_start(img)

    try:
        # 選択範囲を拡大
        pdb.gimp_selection_grow(img, expand_px)

        # 新規レイヤーを作成（透明）
        new_layer = gimp.Layer(img, "黒塗りレイヤー", 
                               img.width, img.height, 
                               RGBA_IMAGE, 100, NORMAL_MODE)

        # 親グループを取得
        parent = pdb.gimp_item_get_parent(drawable)

        # drawable の位置を取得
        pos = pdb.gimp_image_get_item_position(img, drawable)

        # 新規レイヤーを parent の子として挿入
        pdb.gimp_image_insert_layer(img, new_layer, parent, pos + 1)

        # 新レイヤーをアクティブに
        pdb.gimp_image_set_active_layer(img, new_layer)

        # 選択範囲をぼかす
        pdb.gimp_selection_feather(img, feather_px)

        # 黒で塗りつぶす
        pdb.gimp_context_set_foreground(fill_color)
        pdb.gimp_edit_fill(new_layer, FOREGROUND_FILL)

    except Exception as e:
        pdb.gimp_message("エラー: %s" % str(e))

    # Undo グループ終了
    pdb.gimp_image_undo_group_end(img)

    # 更新
    pdb.gimp_displays_flush()

register(
    "expand_blur_fill",
    "選択範囲を拡大して、下に黒塗りぼかしレイヤーを作成",
    "選択範囲を拡大 → 下にレイヤー作成 → 選択範囲をぼかす → 黒で塗りつぶす",
    "",
    "",
    "Sep 2025",
    "<Image>/Filters/Custom/ExpandBlurFill",  # メニューの場所
    "RGB*, GRAY*",  # 適用可能な画像タイプ
    [
        (PF_INT, "expand_px", "拡大量(px)", 20),
        (PF_INT, "feather_px", "ぼかし量(px)", 30),
        (PF_COLOR, "fill_color", "塗りつぶし色", (0,0,0)),
    ],
    [],
    expand_blur_fill)

main()