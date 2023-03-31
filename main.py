import backend
import gui


gui.run_backend_video = backend.get_video
gui.run_backend_audio = backend.get_audio
gui.run_gui()