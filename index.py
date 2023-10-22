import flet as ft

def main(page:ft.Page):
    appname = "yt-dlpGUI"
    page.title = appname
    page.theme = ft.Theme(color_scheme_seed="green",use_material3=True)
    page.theme_mode = "DARK"
    page.window_height = 500
    page.window_width = 300
    page.window_resizable = False
    hello = ft.Text(appname,style=ft.TextThemeStyle.HEADLINE_SMALL)
    url_input = ft.TextField(label="URL", hint_text="リンクを入力", autofocus=True)
    dl_btn = ft.FilledTonalButton("ダウンロード", icon=ft.icons.DOWNLOAD, width=300)
    quality_dd = ft.Dropdown(
        label="拡張子",
        options=[
            ft.dropdown.Option("mp4"),
            ft.dropdown.Option("mp3"),
            ft.dropdown.Option("wav"),
            ft.dropdown.Option("opus"),
            ft.dropdown.Option("flac"),
        ]
    )

    page.add(hello,url_input,quality_dd,dl_btn)

ft.app(target=main)