Youtubeで、再生リスト内の全動画を取得し、その概要欄の内容を分析するプログラムです。  
「歌ってみた動画の、オリジナルの作曲者一覧を取得して分析する」というとてもマイナーな用途に使うために作りました。

# 使用方法
・youtube APIを取得  
・APIキーと取得したいプレイリストのリンクを.envファイルに入れて保存  
・parse.pyの、取得する文字列の形式部分を取得したい内容に合わせていじる  

注意：video_list.py, video_info.py, parse.py　と正しい順番で実行しないとエラーが起きます。

## 処理の流れ:
・全動画を取得し、そのURL一覧を作成(video_list.py)　→ video_urls.csv　に保存  …Youtube APIを使用
・それぞれの動画の情報を取得(video_info.py) → video_informations.csv に保存  …同様
・取得した情報から、概要欄に書かれている内容を取得し、一覧にする(parse.py) → composers.csv に保存  
