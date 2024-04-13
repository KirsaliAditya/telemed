import tkinter as tk
from pytube import YouTube

def download_video():
    url = url_entry.get()
    choice = int(resolution_var.get())
    
    try:
        yt = YouTube(url)
        info_label.config(text=f"Title: {yt.title}\nViews: {yt.views}")
        
        streams = yt.streams.filter(progressive=True)
        resolutions = {}
        resolution_options = []
        
        for i, stream in enumerate(streams):
            resolution = f"{stream.resolution} - {stream.mime_type}"
            resolutions[i] = stream
            resolution_options.append(resolution)
        
        resolution_menu['values'] = resolution_options
        
        if choice in resolutions:
            selected_stream = resolutions[choice]
            selected_stream.download("E:/coding/python/ytdownloader")
            download_status.config(text="Download complete")
        else:
            download_status.config(text="Invalid choice")
    
    except Exception as e:
        download_status.config(text="Error occurred. Check URL or try again.")

# Create GUI
root = tk.Tk()
root.title("YouTube Downloader")

# URL Entry
url_label = tk.Label(root, text="Enter URL:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# Resolution Selection
resolution_label = tk.Label(root, text="Select Resolution:")
resolution_label.pack()

resolution_var = tk.StringVar(root)
resolution_menu = tk.OptionMenu(root, resolution_var, "")
resolution_menu.pack()

# Download Button
download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack()

# Video Info Display
info_label = tk.Label(root, text="", wraplength=300)
info_label.pack()

# Download Status
download_status = tk.Label(root, text="")
download_status.pack()

root.mainloop()
