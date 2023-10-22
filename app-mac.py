import flet as ft
import threading
import time
import subprocess

def main(page: ft.Page):
    appname = "yt-dlpGUI"
    
    page.title = appname
    page.theme_mode = "SYSTEM"
    page.theme = ft.Theme(color_scheme_seed='red')
    page.window_height = 450
    page.window_width = 400
    page.window_resizable = False

    appheader = ft.Text(appname, style=ft.TextThemeStyle.HEADLINE_SMALL)
    progress = ft.ProgressBar(height=5)
    url_input = ft.TextField(hint_text="リンクを入力",label="URL",prefix_icon=ft.icons.LINK)
    format_dd = ft.Dropdown(
        label="フォーマット",
        hint_text="選択してください",
        icon=ft.icons.AUDIO_FILE,

        options=[
            ft.dropdown.Option("mp4"),
            ft.dropdown.Option("mp3"),
            ft.dropdown.Option("flac"),
            ft.dropdown.Option("wav"),
        ]
    )
    playlist_sw = ft.Switch(label="プレイリストでフォルダ分け",label_position='left')
    metadata_sw = ft.Switch(label="メタデータを埋め込む", label_position='left')
    othersite_sw = ft.Switch(label="YouTube以外からダウンロード(非サポート)", label_position='left')
    def download(e):
        if url_input.value == "":
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
            page.add(progress)
            page.update()
            t1 = threading.Thread(target=video_dl)
            t1.start()
            t1.join()
            dl_btn.text = "ダウンロード"
            page.remove(progress)
            page.update()
    
    def video_dl():
        url = url_input.value
        fmt = format_dd.value
        print(f"{url},{fmt}")

        #mp4

        if fmt == "mp4" and playlist_sw.value == False and metadata_sw.value == False: #ほかのオプションなし
            command = ["yt-dlp","-f",'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',"-o",'video/%(title)s.%(ext)s',f'{url}']
            command_string = " ".join(command)
            print(command_string)
            subprocess.run(command,stdout=subprocess.PIPE,text=True)

        elif fmt == "mp4" and playlist_sw.value == True and metadata_sw.value == False: #プレイリストのみ
            command = ["yt-dlp","-f",'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',"-o",'video/%(playlist_title)s/%(title)s.%(ext)s',f'{url}']
            command_string = " ".join(command)
            print(command_string)
            subprocess.run(command,stdout=subprocess.PIPE,text=True)

        elif fmt == "mp4" and playlist_sw.value == True and metadata_sw.value == True: #どちらも有効
            command = ["yt-dlp","-f",'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',"-o",'video/%(playlist_title)s/%(title)s.%(ext)s',"--add-metadata",f'{url}']
            command_string = " ".join(command)
            print(command_string)
            subprocess.run(command,stdout=subprocess.PIPE,text=True)

        elif fmt == "mp4" and playlist_sw.value == False and metadata_sw.value == True: #メタデータのみ
            command = ["yt-dlp","-f",'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',"-o",'video/%(title)s.%(ext)s',"--add-metadata",f'{url}']
            command_string = " ".join(command)
            print(command_string)
            subprocess.run(command,stdout=subprocess.PIPE,text=True)

        #mp3

        elif fmt == "mp3" and playlist_sw.value == False and metadata_sw.value == False: #ほかのオプションなし
            command = ["yt-dlp","-f",'bestaudio',"-x","--audio-format","mp3","-o",'audio/%(title)s.%(ext)s',f'{url}']
            command_string = " ".join(command)
            print(command_string)
            subprocess.run(command,stdout=subprocess.PIPE,text=True)

        elif fmt == "mp3" and playlist_sw.value == True and metadata_sw.value == False: #プレイリストのみ
            command = ["yt-dlp","-f",'bestaudio',"-x","--audio-format","mp3","-o",'audio/%(playlist_title)s/%(title)s.%(ext)s',f'{url}']
            command_string = " ".join(command)
            print(command_string)
            subprocess.run(command,stdout=subprocess.PIPE,text=True)

        elif fmt == "mp3" and playlist_sw.value == True and metadata_sw.value == True: #どちらも有効
            command = ["yt-dlp","-f",'bestaudio',"-x","--audio-format","mp3","--add-metadata","-o",'audio/%(playlist_title)s/%(title)s.%(ext)s',f'{url}']
            command_string = " ".join(command)
            print(command_string)
            subprocess.run(command,stdout=subprocess.PIPE,text=True)

        elif fmt == "mp3" and playlist_sw.value == False and metadata_sw.value == True: #メタデータのみ
            command = ["yt-dlp","-f",'bestaudio',"-x","--audio-format","mp3","--add-metadata","-o",'audio/%(title)s.%(ext)s',f'{url}']
            command_string = " ".join(command)
            print(command_string)
            subprocess.run(command,stdout=subprocess.PIPE,text=True)

        #flac

        elif fmt == "flac" and playlist_sw.value == False and metadata_sw.value == False: #ほかのオプションなし
            command = ["yt-dlp","-f",'bestaudio',"-x","--audio-format","flac","-o",'audio/%(title)s.%(ext)s',f'{url}']
            command_string = " ".join(command)
            print(command_string)
            subprocess.run(command,stdout=subprocess.PIPE,text=True)

        elif fmt == "flac" and playlist_sw.value == True and metadata_sw.value == False: #プレイリストのみ
            command = ["yt-dlp","-f",'bestaudio',"-x","--audio-format","flac","-o",'audio/%(playlist_title)s/%(title)s.%(ext)s',f'{url}']
            command_string = " ".join(command)
            print(command_string)
            subprocess.run(command,stdout=subprocess.PIPE,text=True)

        elif fmt == "flac" and playlist_sw.value == True and metadata_sw.value == True: #どちらも有効
            command = ["yt-dlp","-f",'bestaudio',"-x","--audio-format","flac","--add-metadata","-o",'audio/%(playlist_title)s/%(title)s.%(ext)s',f'{url}']
            command_string = " ".join(command)
            print(command_string)
            subprocess.run(command,stdout=subprocess.PIPE,text=True)

        elif fmt == "flac" and playlist_sw.value == False and metadata_sw.value == True: #メタデータのみ
            command = ["yt-dlp","-f",'bestaudio',"-x","--audio-format","flac","--add-metadata","-o",'audio/%(title)s.%(ext)s',f'{url}']
            command_string = " ".join(command)
            print(command_string)
            subprocess.run(command,stdout=subprocess.PIPE,text=True)

        #wav

        elif fmt == "wav" and playlist_sw.value == False and metadata_sw.value == False: #ほかのオプションなし
            command = ["yt-dlp","-f",'bestaudio',"-x","--audio-format","wav","-o",'audio/%(title)s.%(ext)s',f'{url}']
            command_string = " ".join(command)
            print(command_string)
            subprocess.run(command,stdout=subprocess.PIPE,text=True)

        elif fmt == "wav" and playlist_sw.value == True and metadata_sw.value == False: #プレイリストのみ
            command = ["yt-dlp","-f",'bestaudio',"-x","--audio-format","wav","-o",'audio/%(playlist_title)s/%(title)s.%(ext)s',f'{url}']
            command_string = " ".join(command)
            print(command_string)
            subprocess.run(command,stdout=subprocess.PIPE,text=True)

        elif fmt == "wav" and playlist_sw.value == True and metadata_sw.value == True: #どちらも有効
            command = ["yt-dlp","-f",'bestaudio',"-x","--audio-format","wav","--add-metadata","-o",'audio/%(playlist_title)s/%(title)s.%(ext)s',f'{url}']
            command_string = " ".join(command)
            print(command_string)
            subprocess.run(command,stdout=subprocess.PIPE,text=True)

        elif fmt == "wav" and playlist_sw.value == False and metadata_sw.value == True: #メタデータのみ
            command = ["yt-dlp","-f",'bestaudio',"-x","--audio-format","wav","--add-metadata","-o",'audio/%(title)s.%(ext)s',f'{url}']
            command_string = " ".join(command)
            print(command_string)
            subprocess.run(command,stdout=subprocess.PIPE,text=True)

        elif othersite_sw.value == True: #ほかのオプションなし
            command = ["yt-dlp","-f",'best',"-o",'video/%(title)s.%(ext)s',f'{url}']
            command_string = " ".join(command)
            print(command_string)
            subprocess.run(command,stdout=subprocess.PIPE,text=True)
            
    dl_btn = ft.FilledTonalButton("ダウンロード", icon=ft.icons.DOWNLOAD, on_click=download)
    

    page.add(appheader,
             url_input,
             format_dd,
             playlist_sw,
             metadata_sw,
             othersite_sw,
             dl_btn)

ft.app(target=main, assets_dir="assets")