import cv2
from ultralytics import YOLO
from tkinter import Tk, Label, Entry, Button, filedialog
from PIL import Image, ImageTk
import threading

# Initialize YOLO model
yolo = YOLO('yolov8s.pt')

# Define a function to get unique colors for each class
def getColours(cls_num):
    base_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    color_index = cls_num % len(base_colors)
    increments = [(1, -2, 1), (-2, 1, -1), (1, -1, 2)]
    color = [base_colors[color_index][i] + increments[color_index][i] * (cls_num // len(base_colors)) % 256 for i in range(3)]
    return tuple(color)

# Global variables
stop_video = False
videoCap = None
class_to_detect = ""
video_path = ""  # To store selected video path

# Function to select video file
def select_video():
    global video_path
    video_path = filedialog.askopenfilename(title="Select Video File", filetypes=(("MP4 files", "*.mp4"), ("All files", "*.*")))
    if video_path:
        video_label.config(text=f"Selected Video: {video_path.split('/')[-1]}")

# Function to start video processing
def start_detection():
    global videoCap, stop_video, class_to_detect, video_path
    if not video_path:
        video_label.config(text="Please select a video file first.")
        return

    stop_video = False
    videoCap = cv2.VideoCapture(video_path)
    threading.Thread(target=process_video).start()

# Function to process video frames and perform object detection
def process_video():
    global videoCap, stop_video, class_to_detect

    while videoCap.isOpened() and not stop_video:
        ret, frame = videoCap.read()
        if not ret:
            break

        results = yolo.track(frame, stream=True)

        for result in results:
            classes_names = result.names
            for box in result.boxes:
                if box.conf[0] > 0.4:
                    [x1, y1, x2, y2] = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    cls = int(box.cls[0])
                    class_name = classes_names[cls]

                    if class_to_detect.lower() == class_name.lower():
                        colour = getColours(cls)
                        cv2.rectangle(frame, (x1, y1), (x2, y2), colour, 2)
                        cv2.putText(frame, f'{class_name} {box.conf[0]:.2f}', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.6, colour, 2)

        # Convert frame for Tkinter display
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_rgb)
        img = img.resize((800, 500))
        imgtk = ImageTk.PhotoImage(image=img)
        video_display.imgtk = imgtk
        video_display.configure(image=imgtk)

        if stop_video:
            break

    videoCap.release()

# Function to stop video processing
def stop_detection():
    global stop_video
    stop_video = True
    video_display.config(image='')

# GUI setup
root = Tk()
root.title("YOLO Object Detection")
root.geometry("1000x700")
root.configure(bg="light blue")

# Title label
title_label = Label(root, text="YOLO Object Detection", bg="light blue", fg="dark red", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Video selection label and button
video_label = Label(root, text="No video selected", bg="light blue", font=("Arial", 12))
video_label.pack(pady=5)
select_button = Button(root, text="Select Video", bg="blue", fg="white", font=("Arial", 12, "bold"), command=select_video)
select_button.pack(pady=5)

# Entry field for class name
class_label = Label(root, text="Enter Class to Detect:", bg="light blue", font=("Arial", 12))
class_label.pack(pady=5)
class_entry = Entry(root, font=("Arial", 12), width=20)
class_entry.pack()

# Start and stop buttons
start_button = Button(root, text="Start Detection", bg="green", fg="white", font=("Arial", 12, "bold"), command=lambda: set_class_and_start())
start_button.pack(pady=5)
stop_button = Button(root, text="Stop Detection", bg="red", fg="white", font=("Arial", 12, "bold"), command=stop_detection)
stop_button.pack(pady=5)

# Video display label
video_display = Label(root, bg="light blue")
video_display.pack(pady=10)

# Function to set the class name and start detection
def set_class_and_start():
    global class_to_detect
    class_to_detect = class_entry.get().strip()
    start_detection()

# Start the GUI
root.mainloop()
