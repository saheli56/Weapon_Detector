# Weapon Detection Using OpenCV and IP Webcam

This project detects weapons (guns) in real-time video streams using OpenCV and a Haar cascade classifier. It is designed to work with an IP Webcam app, allowing you to use your phone as a wireless camera source.

## Features
- Real-time weapon (gun) detection in video streams
- Uses Haar cascade classifier for detection
- Compatible with IP Webcam app (Android)
- Saves frames with detected weapons to a folder
- Headless operation (no GUI required)

## Requirements
- Python 3.x
- OpenCV (`opencv-python`)
- imutils
- numpy
- IP Webcam app (Android)

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/weapon_detection.git
   cd weapon_detection
   ```
2. Install dependencies:
   ```sh
   pip install opencv-python imutils numpy
   ```
3. Download or provide a suitable Haar cascade XML file (e.g., `cascade.xml`).

## Usage
1. Install and start the [IP Webcam app](https://play.google.com/store/apps/details?id=com.pas.webcam) on your Android phone.
2. Start the server in the app and note the IP address and port (e.g., `http://192.168.1.100:8080`).
3. Update the `url` variable in `main.py` with your phone's IP and port (e.g., `http://192.168.1.100:8080/video`).
4. Run the script:
   ```sh
   python main.py
   ```
5. Detected frames will be saved in the `detected_frames` directory.

## Notes
- Ensure your phone and computer are on the same WiFi network.
- The script is designed for headless environments (no display window).
- To stop the script, use `Ctrl+C` in the terminal.

## File Structure
- `main.py` - Main detection script
- `cascade.xml` - Haar cascade classifier for weapon detection
- `detected_frames/` - Saved frames with detected weapons

## License
This project is for educational purposes. Please check the license of the Haar cascade file you use.

## Credits
- OpenCV team
- IP Webcam app by Pavel Khlebovich
- Haar cascade sources

---
Feel free to contribute or open issues for improvements!
