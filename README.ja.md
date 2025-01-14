# Mosffel

[English Ver.](https://github.com/takty/edgeknock/blob/main/README.md)

## 概要

**Mosffel**は、日本の小中学生が学校で慣れ親しんだブロック体をもとにした等幅フォントです。英語の学習とプログラミングを結びつける目的でデザインされており、特に日本で英語を学ぶ子どもたちが、学習した書き方でプログラミングに親しめるように考案されました。ブロック体でかつ等幅なフォントは、他にないと考えられ、プログラミングやテキストエディタでの使用に適しています。

## インストール方法

**Mosffel**フォントは、ZIP形式で配布されています。以下の手順に従って、OpenTypeフォントをインストールしてください。

### Windows

1. ZIPファイルを解凍します。
1. フォントファイル（`.otf`）を右クリックし、「インストール」を選択します。

### macOS

1. ZIPファイルを解凍します。
1. フォントファイル（`.otf`）をダブルクリックし、フォントブックを開きます。
1. 「フォントをインストール」をクリックします。

### Linux

1. ZIPファイルを解凍します。
1. フォントファイル（`.otf`）をホームディレクトリ内の`.fonts`フォルダにコピーします。
1. ターミナルで`fc-cache -fv`コマンドを実行してフォントキャッシュを更新します。

### Webフォントとしての利用

Webフォントとして利用する場合は、`.otf`ファイルを`.woff`または`.woff2`形式に変換し、CSSで指定して使用します。

## 使用方法

**Mosffel**は、現在のところASCIIコードの範囲内の文字のみを含んでおり、主にプログラミング言語で使用される英数字や記号に対応しています。そのため、このフォントを利用する際は、他のフォントと組み合わせて使用することを推奨します。

### CSSでの使用例

以下は、WebフォントとしてMosffelを他のフォントと組み合わせて使用する際のCSSのサンプルコードです。

```css
body {
    font-family: 'Mosffel', 'Courier New', monospace;
}
```

この例では、Mosffelが指定された範囲の文字に適用され、それ以外の文字はCourier Newやシステムのデフォルトモノスペースフォントが使用されます。

### ライセンス

**Mosffel**は、[SIL Open Font License 1.1](https://scripts.sil.org/OFL)のもとでライセンスされています。このライセンスにより、フォントは自由に使用、修正、再配布が可能です。また、商用利用も許可されています。

改変されたフォントを再配布する場合は、元のフォントとは別の名前を使用してください。

もしこのフォントを使ったり、使う場面があれば、ぜひ何かしらの方法で教えていただけると嬉しいです。

## 著作権とクレジット

**Mosffel**フォントの著作権は、**Takuto Yanagida**に帰属します。

## 更新履歴

- **バージョン 1.0** - 初版リリース（2024年9月5日）
