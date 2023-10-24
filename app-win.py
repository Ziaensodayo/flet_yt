import flet as ft
import time
import subprocess

def main(page: ft.Page):
    appname = "yt-dlpGUI-v1.1"
    
    page.title = appname
    page.theme_mode = "SYSTEM"
    page.theme = ft.Theme(use_material3=True)
    page.window_height = 460
    page.window_width = 400
    page.window_resizable = False

    appheader = ft.Text(appname, style=ft.TextThemeStyle.HEADLINE_SMALL)
    progress = ft.ProgressBar(height=5)
    url_input = ft.TextField(hint_text="URLを入力",label="URL",prefix_icon=ft.icons.LINK)
    format_dd = ft.Dropdown(
        label="拡張子",
        hint_text="選択してください",
        icon=ft.icons.AUDIO_FILE,

        options=[
            ft.dropdown.Option("mp4"),
            ft.dropdown.Option("mp3"),
            ft.dropdown.Option("flac"),
            ft.dropdown.Option("wav"),
        ]
    )
    playlist_sw = ft.Switch(label=" プレイリストでフォルダ分け")
    metadata_sw = ft.Switch(label=" メタデータを埋め込む")
    othersite_sw = ft.Switch(label=" YouTube以外からダウンロード(非サポート)")

    def download(e):
        if url_input.value == "" or format_dd.value == "":
            dl_btn.text = "URLを入力して下さい"
            dl_btn.disabled = True;
            dl_btn.icon = ft.icons.CLOSE
            page.update()
            time.sleep(3)
            dl_btn.text = "ダウンロード"
            dl_btn.icon = ft.icons.DOWNLOAD
            dl_btn.disabled = False;
            page.update()
            return
        else:
            dl_btn.text = "ダウンロード中です"
            dl_btn.disabled = True;
            page.add(progress)
            page.update()
            result = video_dl(url_input.value,format_dd.value)
            if result == 0:
                print(f"ダウンロード処理は終了コード{result}で正常に終了しました。")
                dl_btn.text = "ダウンロード完了"
                dl_btn.icon = ft.icons.DONE
                page.remove(progress)
                page.update()
                time.sleep(3)
                dl_btn.text = "ダウンロード"
                dl_btn.disabled = False;
                dl_btn.icon = ft.icons.DOWNLOAD
                page.update()
                return
            elif result == 1:
                print(f"ダウンロード処理は終了コード{result}で正常に終了しませんでした。")
                dl_btn.text = "エラーが発生しました"
                dl_btn.icon = ft.icons.ERROR
                page.remove(progress)
                page.update()
                time.sleep(3)
                dl_btn.text = "ダウンロード"
                dl_btn.disabled = False;
                dl_btn.icon = ft.icons.DOWNLOAD
                page.update()
                return
    
    def video_dl(url, fmt):
        print(f"{url}を,{fmt}でダウンロードします。")

        log_file = open('log.txt','w',encoding="utf-8")

        #mp4

        if fmt == "mp4" and playlist_sw.value == False and metadata_sw.value == False: #ほかのオプションなし
            command = f'yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]" -o "video/%(title)s.%(ext)s" "{url}"'
            p = subprocess.run(command,stdout=log_file,text=True,shell=True)
            return p.returncode

        elif fmt == "mp4" and playlist_sw.value == True and metadata_sw.value == False: #プレイリストのみ
            command = f'yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]" -o "video/%(playlist_title)s/%(title)s.%(ext)s" "{url}"'
            p = subprocess.run(command,stdout=log_file,text=True,shell=True)
            return p.returncode

        elif fmt == "mp4" and playlist_sw.value == True and metadata_sw.value == True: #どちらも有効
            command = f'yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]" --add-metadata -o "video/%(playlist_title)s/%(title)s.%(ext)s" "{url}"'
            subprocess.run(command,stdout=log_file,text=True,shell=True)

        elif fmt == "mp4" and playlist_sw.value == False and metadata_sw.value == True: #メタデータのみ
            command = f'yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]" --add-metadata -o "video/%(title)s.%(ext)s" "{url}"'
            p = subprocess.run(command,stdout=log_file,text=True,shell=True)
            return p.returncode

        #mp3

        elif fmt == "mp3" and playlist_sw.value == False and metadata_sw.value == False: #ほかのオプションなし
            command = f'yt-dlp -f bestaudio -x --audio-format mp3 --audio-quality 256K -o "audio/%(title)s.%(ext)s" "{url}"'
            p = subprocess.run(command,stdout=log_file,text=True,shell=True)
            return p.returncode

        elif fmt == "mp3" and playlist_sw.value == True and metadata_sw.value == False: #プレイリストのみ
            command = f'yt-dlp -f bestaudio -x --audio-format mp3 --audio-quality 256K -o "audio/%(playlist_title)s/%(title)s.%(ext)s" "{url}"'
            p = subprocess.run(command,stdout=log_file,text=True,shell=True)
            return p.returncode

        elif fmt == "mp3" and playlist_sw.value == True and metadata_sw.value == True: #どちらも有効
            command = f'yt-dlp -f bestaudio -x --audio-format mp3 --audio-quality 256K --add-metadata -o "audio/%(playlist_title)s/%(title)s.%(ext)s" "{url}"'
            p = subprocess.run(command,stdout=log_file,text=True,shell=True)
            return p.returncode
        
        elif fmt == "mp3" and playlist_sw.value == False and metadata_sw.value == True: #メタデータのみ
            command = f'yt-dlp -f bestaudio -x --audio-format mp3 --audio-quality 256K --add-metadata -o "audio/%(title)s.%(ext)s" "{url}"'
            p = subprocess.run(command,stdout=log_file,text=True,shell=True)
            return p.returncode

        #flac

        elif fmt == "flac" and playlist_sw.value == False and metadata_sw.value == False: #ほかのオプションなし
            command = f'yt-dlp -f bestaudio -x --audio-format flac -o "audio/%(title)s.%(ext)s" "{url}"'
            p = subprocess.run(command,stdout=log_file,text=True,shell=True)
            return p.returncode

        elif fmt == "flac" and playlist_sw.value == True and metadata_sw.value == False: #プレイリストのみ
            command = f'yt-dlp -f bestaudio -x --audio-format flac -o "audio/%(playlist_title)s/%(title)s.%(ext)s" "{url}"'
            p = subprocess.run(command,stdout=log_file,text=True,shell=True)
            return p.returncode

        elif fmt == "flac" and playlist_sw.value == True and metadata_sw.value == True: #どちらも有効
            command = f'yt-dlp -f bestaudio -x --audio-format flac --add-metadata -o "audio/%(playlist_title)s/%(title)s.%(ext)s" "{url}"'
            p = subprocess.run(command,stdout=log_file,text=True,shell=True)
            return p.returncode

        elif fmt == "flac" and playlist_sw.value == False and metadata_sw.value == True: #メタデータのみ
            command = f'yt-dlp -f bestaudio -x --audio-format flac -o --add-metadata "audio/%(title)s.%(ext)s" "{url}"'
            p = subprocess.run(command,stdout=log_file,text=True,shell=True)
            return p.returncode

        #wav

        elif fmt == "wav" and playlist_sw.value == False and metadata_sw.value == False: #ほかのオプションなし
            command = f'yt-dlp -f bestaudio -x --audio-format wav -o "audio/%(title)s.%(ext)s" "{url}"'
            p = subprocess.run(command,stdout=log_file,text=True,shell=True)
            return p.returncode

        elif fmt == "wav" and playlist_sw.value == True and metadata_sw.value == False: #プレイリストのみ
            command = f'yt-dlp -f bestaudio -x --audio-format wav -o "audio/%(playlist_title)s/%(title)s.%(ext)s" "{url}"'
            p = subprocess.run(command,stdout=log_file,text=True,shell=True)
            return p.returncode

        elif fmt == "wav" and playlist_sw.value == True and metadata_sw.value == True: #どちらも有効
            command = f'yt-dlp -f bestaudio -x --audio-format wav --add-metadata -o "audio/%(playlist_title)s/%(title)s.%(ext)s" "{url}"'
            p = subprocess.run(command,stdout=log_file,text=True,shell=True)
            return p.returncode

        elif fmt == "wav" and playlist_sw.value == False and metadata_sw.value == True: #メタデータのみ
            command = f'yt-dlp -f bestaudio -x --audio-format wav -o "audio/%(title)s.%(ext)s" "{url}"'
            p = subprocess.run(command,stdout=log_file,text=True,shell=True)
            return p.returncode

        #YouTube以外

        elif othersite_sw.value == True: #ほかのオプションなし
            command = f'yt-dlp -f best -o "video/%(title)s.%(ext)s" "{url}"'
            p = subprocess.run(command,stdout=log_file,text=True,shell=True)
            return p.returncode

        log_file.close()
            
    dl_btn = ft.FilledTonalButton("ダウンロード", icon=ft.icons.DOWNLOAD, on_click=download)
    

    page.add(appheader,
             url_input,
             format_dd,
             playlist_sw,
             metadata_sw,
             othersite_sw,
             dl_btn)

ft.app(target=main, assets_dir="assets")