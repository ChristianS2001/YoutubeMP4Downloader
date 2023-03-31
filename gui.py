import os
import flet as ft


#DO NOT RUN THIS FILE, run main.py instead
# These values are set to none here so no errors are done, they are changed in main.py
run_backend_video = None
run_backend_audio = None

def main(page: ft.Page):
    page.title = "Youtube MP3 and MP4 Converter"
    page.vertical_alignment = "center"
    page.window_height = 1000
    page.window_width = 1000


    def pick_file_result(e: ft.FilePickerResultEvent):
        if(radioHead.value == "mp4"):
            print("we are in the mp4 scope")
            selected_path.value = pick_file_dialog.result.path + ".mp4"
        else:
            print("we are in the mp3 scope")
            selected_path.value = pick_file_dialog.result.path + ".mp3"
        page.update()


    def handle_submit(e):
        if not url_input.value:
            url_input.error_text = "Please enter URL"
            page.update()
        if(radioHead.value == "mp4"):
            url_input.error_text = None
            run_backend_video(url_input.value, selected_path.value, in_progress, on_complete, handle_error)
            page.update()
        else:
            url_input.error_text = None
            run_backend_audio(url_input.value, selected_path.value, in_progress, on_complete, handle_error)
            page.update()

    def in_progress(*args):
        download_complete.value = "Download In Progress"
        page.update()
    
    def on_complete(*args):
        download_complete.value = "Download Complete"
        page.update()

    def handle_error(*args):
        download_complete.value = "Something went wrong, try again"
        page.update()
    

    url_input = ft.TextField(label="Video URL")
    pick_file_dialog = ft.FilePicker(on_result=pick_file_result)
    pick_file_button = ft.ElevatedButton(
        "Pick File Name",
        icon=ft.icons.UPLOAD_FILE,
        on_click=lambda _: pick_file_dialog.save_file(
            file_type="video", 
            allowed_extensions=["mp4"])
        )
    page.overlay.append(pick_file_dialog)
    selected_path = ft.Text()
    selected_path.value = "File Save Location"

    #text to tell user what to select and why
    radioHeadText = ft.Text()
    radioHeadText.size = 28
    radioHeadText.value = "Select File Type Below"

    #selection for either mp3 or mp4 (this will be for downloading later)
    radioHead = ft.RadioGroup(content=ft.Row([
        ft.Radio(value="mp3", label="MP3"),
        ft.Radio(value="mp4", label="MP4")]))
    
    radioHead.value = "mp3" #this is to set the defualt value to mp3 for when user goes to download a video

    download_button = ft.TextButton("Download", on_click=handle_submit)
    
    download_complete = ft.Text()


    page.add(
        ft.Column(
            [   
                ft.Row([
                    radioHeadText
                ],
                alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row([
                    radioHead
                ],
                alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row([
                    url_input
                ],
                alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row([
                    pick_file_button,
                    selected_path
                    ]),
                ft.Row([
                    download_button,
                ],
                alignment=ft.MainAxisAlignment.CENTER
                    ),
                ft.Row([
                    download_complete
                ],
                alignment=ft.MainAxisAlignment.CENTER)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=50
        )
    )

def whatOption(option):
    fileType = option
    return fileType #I hope this does not crash the GUI

def run_gui():
    ft.app(target=main)


if __name__ == "__main__":
    run_gui()