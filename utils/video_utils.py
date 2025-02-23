import cv2

def read_video(video_path):
    """
    Reads a video file and returns a list of frames.

    Args:
        video_path (str): Path to the video file.

    Returns:
        list: A list of frames.
    """
    try:
        cap = cv2.VideoCapture(video_path)
        frames = []
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frames.append(frame)
        cap.release()
        return frames
    
    except Exception as e:
        print(f"Error reading video: {e}")
        return []

def save_video(output_video_frames, output_video_path, fps=25):
    """
    Saves a list of frames to a video file.

    Args:
        output_video_frames (list): A list of frames.
        output_video_path (str): Path to the output video file.
        fps (int): Frames per second. Default is 25.

    Returns:
        None
    """
    if not output_video_frames:
        print("No frames to save!")
        return
    
    try:
        fourcc = cv2.VideoWriter_fourcc(*'XVID') 
        height, width = output_video_frames[0].shape[:2]
        out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))
        
        for frame in output_video_frames:
            if frame.shape[:2] != (height, width): 
                frame = cv2.resize(frame, (width, height))
            out.write(frame)
        
        out.release()
        print(f"Video saved to {output_video_path}")
    except Exception as e:
        print(f"Error saving video: {e}")