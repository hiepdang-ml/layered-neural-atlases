import os
import cv2
# from madgrad import MADGRAD

def video_to_images(video_path: os.PathLike, output_dir: os.PathLike, num_frames: int = None) -> None:
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Open the video file
    vidcap = cv2.VideoCapture(str(video_path))

    # Get the total number of frames in the video
    total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"The input video has: {total_frames} frames")

    # Calculate the number of frames to skip to get the desired number of frames
    frame_skip = 1 if num_frames is None else total_frames // num_frames

    success, image = vidcap.read()
    write_count = 0
    read_count = 0
    while success and write_count < num_frames:
        # Save frame as JPEG file only if it's the right frame according to the frame_skip
        if read_count % frame_skip == 0:
            n_digits = len(str(write_count))
            n_zeros = 5 - n_digits
            name = '0' * n_zeros + str(write_count)
            cv2.imwrite(os.path.join(output_dir, f"{name}.jpg"), image)
            write_count += 1

        success, image = vidcap.read()
        read_count += 1




