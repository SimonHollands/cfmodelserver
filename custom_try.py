from imageai.Detection.Custom import CustomVideoObjectDetection
import os

execution_path = os.getcwd()

video_detector = CustomVideoObjectDetection()
video_detector.setModelTypeAsYOLOv3()
video_detector.setModelPath("hololens-ex-60--loss-2.76.h5")
video_detector.setJsonPath("detection_config.json")
video_detector.loadModel()

video_detector.detectObjectsFromVideo(
    input_file_path="holo1.mp4",
    output_file_path=os.path.join(execution_path, "holo1-detected"),
    frames_per_second=30,
    minimum_percentage_probability=40,
    log_progress=True,
)
