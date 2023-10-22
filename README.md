# flet_yt
fletで再構築されたyt-dlpGUI  
## これはなに？
fletで再構築されたyt-dlpGUIです。  
## 使い方
まずパソコンにpythonとyt-dlp,ffmpegをインストールしてください。    
yt-dlpはpipでインストール可能です。 `pip install yt-dlp`  

![image](https://github.com/Ziaensodayo/flet_yt/assets/122286711/e186eb80-b68a-4f59-970c-d4b89caebe5c)  
使い方は画像を見ればわかると思います。  
URLというボックスに動画のリンクを、  
![image](https://github.com/Ziaensodayo/flet_yt/assets/122286711/3a0a25f0-1db6-4906-9491-84268fc6f1b2)  
フォーマットはmp4,mp3,flac,wavから選択可能です。  

![image](https://github.com/Ziaensodayo/flet_yt/assets/122286711/a94fbfda-f3f3-4f36-8d1e-a7a032e3a873)  
プレイリストでフォルダ分けはプレイリスト毎にフォルダ分けされます。そのまんまですね。プレイリストのリンクからダウンロードしない場合は/NAになります。  
メタデータを埋め込むもその名の通りファイルにメタデータを埋め込みます。  
YouTube以外からダウンロードはYouTube以外のサイトからダウンロードする際に使用します。標準で動かない場合はこれを試してください。  
なおYouTube以外からのダウンロードではフォーマット選択などできませんので注意してください。  

## インストール
Windowsで開発しましたので基本的にはWindowsしかサポートしません。  
Releaseページから最新のzipファイルをダウンロードしてください。  
MacOSやそのほかのOSはリポジトリをクローンしてpyファイルを実行するなり実行ファイルに変換してお使いください。  
