# スパムメール分類プロジェクト
## 概要

スパムメールと通常メールを分類するNLP分類コンペの練習プロジェクトです。
メール本文のテキストデータを前処理し、ナイーブベイズモデルで分類しています。

## モデル改善結果

チュートリアルの基本モデルではF1スコア0.9486486486486485でしたが、
ステミングやStratifiedKFoldを導入した結果、最終モデルではF1スコア0.9515477792732167に向上しました。

## データ
- train.zip：学習用テキストデータ
- test.zip/：評価用テキストデータ
- train_master.csv：学習用テキストデータとラベルの対応表
- sample_submit.csv：応募用サンプルファイル

## 前処理
- 小文字化、ストップワード除去、記号削除
- 単語のステミング（SnowballStemmer）
- 作成した特徴量：text_length, num_words

## 特徴量
- CountVectorizerで text_remove をベクトル化
- 数値特徴量は使用せず（正規化・標準化してもスコアは向上せず）

## モデル
- GaussianNB, MultinomialNB
- StratifiedKFoldによる交差検証で評価
- 最終モデルは MultinomialNB で学習し提出用データを生成

## 改善ポイント
- ホールドアウト→StratifiedKFoldに変更 → 安定したスコア向上
- ステミングで同義語をまとめて学習 → 精度向上
- TF-IDFやSMOTE等を試したが、過学習でスコア低下 → 採用せず

## 今後の改善点
- 分類に使われていない単語を削減し、学習効率向上
- 外部データの利用による新たな特徴量作成
- 数値特徴量の有効活用
- 他のモデルを用いた分類手法の検討

## 提出
- submission_tutorial.csv に予測結果を保存

## 使用ライブラリ
- pandas, numpy, matplotlib, seaborn, japanize_matplotlib, wordcloud, nltk, scikit-learn

## 参考文献
- signate、【練習問題】スパムメール分類 チュートリアル
https://user.competition.signate.jp/ja/competition/detail/?competition=e5e60bbebefd4226b7a77859080a50f6&task=3bf33745e55b4a589077dfda87962ab5&tab=knowledge&knowledge=8dda9b630e5843d8a7c4bb02111a0745
参照(2025/12/1/01:21)
- IBM、ステミングとレマタイゼーションとは
https://www.ibm.com/jp-ja/think/topics/stemming-lemmatization
参照(2025/12/1/01:00)
- Qiita(@citrus-soke)、不均衡データ処理【オーバーサンプリング】
https://qiita.com/citrus-soke/items/18a87eb506b0f6d0c6d2
参照(2025/12/1/01:04)
- Qiita(@masayuki-sera(sera masayuki))、GCI優秀生・SIGNATE MASTERが考えるコンペのスコア向上Tips
https://qiita.com/masayuki-sera/items/8c330887f957642a3915
参照(2025/12/1/01:05)
