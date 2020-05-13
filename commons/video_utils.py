from collections import deque
from typing import List

import cv2
import numpy as np


def frames_to_video(sorted_frames_filepath: List[str], output_video_filepath, resize=None, fps=10):
    first_image = cv2.imread(sorted_frames_filepath[0])
    resolution = resize if resize is not None else (first_image.shape[0], first_image.shape[1])
    video_writer = get_video_writer(output_video_filepath, resolution=resolution, fps=10)

    max_buffer_length = 5_000
    precache = len(sorted_frames_filepath) < max_buffer_length

    if precache:
        frames = [cv2.imread(fp) for fp in sorted_frames_filepath]

    for f, frame_filepath in enumerate(sorted_frames_filepath):
        frame = frames[f] if precache else cv2.imread(frame_filepath)
        if resize is not None:
            frame = cv2.resize(frame, resize)

        video_writer.write(frame)

    video_writer.release()


def get_video_writer(path, resolution, fps=10):
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    return cv2.VideoWriter(path, fourcc, fps, resolution)


def count_frames_in_video(video_path):
    for frame_nr, _ in get_frames_of_video(video_path):
        pass

    return frame_nr + 1


def get_frame(video_path, target_frame_nr):
    generator = get_frames_of_video(video_path, start_from_frame=target_frame_nr)

    frame_nr, frame = next(generator)

    deque(generator, maxlen=0)  # exhaust generator to release video
    return frame


def get_frames(video_path, frame_numbers):
    frames = []
    frame_numbers = sorted(frame_numbers)
    generator = get_frames_of_video(video_path, start_from_frame=frame_numbers[0])
    for target_frame_nr in frame_numbers:
        frame_nr, frame = next(generator)
        if frame_nr == target_frame_nr:
            frames.append(frame)

    deque(generator, maxlen=0)  # exhaust generator to release video

    frames = np.array(frames)

    return frames


def load_frames_to_memory(video_path):
    frames = []

    for _, frame in get_frames_of_video(video_path):
        frames.append(frame)

    return frames


def get_frames_of_video(video_path, start_from_frame=0, end_frame=-1):
    cap = cv2.VideoCapture(video_path)

    # Check if camera opened successfully
    if cap.isOpened() == False:
        print(f"Error opening video stream or file with path '{video_path}'")

    frame_nr = 0
    # Read until video is completed
    while cap.isOpened():
        ret, frame = cap.read()

        if ret is not False:
            if frame_nr < start_from_frame:
                frame_nr += 1
                continue

            if end_frame != -1 and frame_nr > end_frame:
                break

            yield frame_nr, frame

            frame_nr += 1

        else:
            break

    cap.release()


def glue_videos(*video_file_paths):
    # does it in memory, need enough RAM
    frames = []
    for video_fp in video_file_paths:
        # extend function takes places on object
        frames.extend(*load_frames_to_memory(video_fp))

    return frames
