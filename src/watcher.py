#!/usr/bin/env python3
import argparse
import sys
from typing import Optional
import time

import cv2
import framegrab
import yaml

def display_loop(grabber: framegrab.FrameGrabber) -> None:
    window_name = "Camera Feed"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    print("Displaying camera feed...")
    print("Press 'q' to quit")

    while True:
        frame = grabber.grab()
        if frame is None:
            print("Failed to grab frame", file=sys.stderr)
            time.sleep(1)
            continue
        cv2.imshow(window_name, frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def main(config_file: str = "camera.yaml") -> None:
    """
    Main function that loads camera configuration, captures frames and displays them full screen.
    
    Args:
        config_file: Path to the camera configuration YAML file
    """
    grabbers = framegrab.FrameGrabber.from_yaml(config_file)
    grabber = grabbers[0]

    try:
        display_loop(grabber)
    except KeyboardInterrupt:
        print("Keyboard interrupt")
    finally:
        cv2.destroyAllWindows()
        grabber.release()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Display camera feed in fullscreen")
    parser.add_argument(
        "--config",
        type=str,
        default="camera.yaml",
        help="Path to camera configuration YAML file (default: camera.yaml)"
    )
    
    args = parser.parse_args()
    main(args.config)





