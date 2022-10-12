#comment: The main program [non-graphical interface] is here..
import moviepy
import moviepy.editor
video = moviepy.editor.VideoFileClip('#')  # - path to video file.
audio = video.audio
audio.write_audiofile('#') # - path to audio file.
