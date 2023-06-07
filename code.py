# pip install ffmpeg-stream-to-numpy keyboard cv2obs opencv-python kthread-sleep
from ffmpeg_stream_to_numpy import NumpyVideo
import keyboard, cv2
from cv2obs.cv2obscam import start_cv2obs, get_index_of_working_cameras
from kthread_sleep import sleep
show_fake = True
def fake_on_off():
    global show_fake
    show_fake = not show_fake
keyboard.add_hotkey('ctrl+alt+f', fake_on_off)
path_fake_video = r"C:\Users\hansc\Downloads\videofake2.mp4"
vi = NumpyVideo(videofile = path_fake_video, ffmpeg_param=('-re',))
fakevideo = [i for i in vi.play_video_ffmpeg()]
cameras=get_index_of_working_cameras()
camera_verdade = 0
camera_obs = 2
original_vid = cv2.VideoCapture(camera_verdade)
px = start_cv2obs(
    height=480,
    width=640,
    fps=29.97,
    camera=camera_obs,
    killkeys="ctrl+alt+l",
)
while True:
    for i in fakevideo:
        if show_fake:
            px.write_image(
                i
            )
            sleep(1/29.97)
        else:
            ret, frame = original_vid.read()
            px.write_image(
                frame
            )
# original_vid.release()



