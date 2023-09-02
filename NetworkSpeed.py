import tkinter as tk
import speedtest
import threading

def run_speed_test():
    check_button.config(state=tk.DISABLED)
    check_button.config(text='Đang kiểm tra . . .')
    
    def run_test():
        speed_test = speedtest.Speedtest()
        speed_test.get_best_server()

        download_speed = speed_test.download() / 1024**2
        upload_speed = speed_test.upload() / 1024**2
        
        download_result.config(text=f'{download_speed:.2f} Mbps')
        upload_result.config(text=f'{upload_speed:.2f} Mbps')
        
        check_button.config(state=tk.NORMAL)
        check_button.config(text='Kiểm tra tốc độ')

    thread = threading.Thread(target=run_test)
    thread.start()
    
    
root = tk.Tk()
root.title("Kiểm tra tốc độ mạng")
root.config(bg='blue')
root.geometry("400x450")

frame = tk.Frame(root, bg='blue')
frame.pack(padx=50, pady=50)

download_label = tk.Label(frame, bg='green', fg='white', text="Tốc độ download", font=("Helvetica", 12), width=40, height=2, highlightthickness=1)
download_label.pack(pady=7)

download_result = tk.Label(frame, bg='cyan', fg='white', text="0 Mbps", font=("Helvetica", 12), width=40, height=2, highlightthickness=1)
download_result.pack(pady=7)

upload_label = tk.Label(frame, bg='purple', fg='white', text="Tốc độ upload", font=("Helvetica", 12), width=40, height=2, highlightthickness=1)
upload_label.pack(pady=7)

upload_result = tk.Label(frame, bg='violet', fg='white', text="0 Mbps", font=("Helvetica", 12), width=40, height=2, highlightthickness=1)
upload_result.pack(pady=7)

check_button = tk.Button(frame, bg='orange', fg='white', text="Kiểm tra tốc độ", font=("Helvetica", 10), width=51, height=2, command=run_speed_test)
check_button.pack(pady=7)

copyright_label = tk.Label(root, bg='blue', fg='white', text="Lê Anh đẹp trai", font=("Helvetica", 12))
copyright_label.pack(pady=7)

root.mainloop()