# my_gimp_plugins
自分で使う用に、GIMPのプラグインをpythonで作成する為のリポジトリ。

## 導入方法

- TODO 後で書く

`（cloneして、使いたいファイルだけGIMPのplug-insに置く。）`

## 各プラグインの解説・使用例

### ExpandBlurFill
`expand_blur_fill.py`

- 選択範囲を拡張し周囲をぼかし、塗りつぶしたレイヤーを下に生成する。単色のピクトグラムや文字の縁取り等に使用。

1. フリーハンドで単色の画像や文字を、色域選択もしくはファジー選択する。<img width="1881" height="861" alt="blur1" src="https://github.com/user-attachments/assets/6fe725c6-83aa-4964-acfa-99fce096f35e" />

2. 「フィルター」 > 「Custom」 > 「ExpandBlurFill」を選択する。<img width="1351" height="888" alt="blur2" src="https://github.com/user-attachments/assets/24766ef5-6dd3-4387-8100-a5009d26e632" />

3. ダイアログが表示されるので、拡大量、ぼかし量、塗りつぶし色を指定する。<img width="1596" height="765" alt="blur3" src="https://github.com/user-attachments/assets/9f0ffb1f-ef8f-499f-af02-5103a75608a3" />

4. OKを押すと対象のレイヤーの下に黒塗りレイヤーが作られる。<img width="1604" height="782" alt="blur4" src="https://github.com/user-attachments/assets/b307608e-41a7-42d4-bf3f-f174cf3955bc" />

### GenerateDefaultGuids
`generate_default_guides.py`

- キャンバスの上底下底・両端・中央にガイドを表示する。

1. 「フィルター」 > 「Custom」 > 「GenerateDefaultGuids」を選択する。<img width="1639" height="911" alt="guide1" src="https://github.com/user-attachments/assets/65b7d58b-d43e-461f-b6bf-cde3bdb9517e" />

2. 固定位置のガイドが引かれる。<img width="1393" height="822" alt="guide2" src="https://github.com/user-attachments/assets/7df714d5-56e4-40c9-b1f1-51b42cf7bc77" />
