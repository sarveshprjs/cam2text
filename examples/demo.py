# examples/demo.py

from cam2text import generate_activity_report

if __name__ == "__main__":
    output = generate_activity_report("test_video.mp4")
    print("Activity report saved to:", output)
