import webview

def main():
    webview.create_window(
        'Qwilight Seed Finder', 
        'resource/index.html', 
        width=1024, 
        height=768, 
        resizable=False
    )
    webview.start()
if __name__ == "__main__":
    main()
