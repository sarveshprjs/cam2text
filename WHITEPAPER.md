# Cam2Text: Real-Time Camera-to-Text Conversion Using AI

## Abstract

Cam2Text is an AI-driven application designed to convert real-time camera input into textual information. It leverages Optical Character Recognition (OCR) and image processing to extract readable text from video frames, making it useful in fields like assistive technology, automation, education, and surveillance.

---

## Problem Statement

Extracting meaningful text from live camera feeds remains a challenging task due to varying lighting conditions, motion blur, fonts, and languages. Traditional OCR tools are optimized for static images and often struggle in dynamic real-time environments.

---

## Objectives

- Real-time video-to-text conversion.
- High accuracy under varied lighting and motion.
- Lightweight and easy to deploy.
- Support for multiple languages (future scope).

---

## System Architecture

```
[Camera Feed] --> [Frame Capture] --> [Preprocessing] --> [OCR Engine] --> [Text Output]
```

- **Frame Capture**: Captures frames at regular intervals.
- **Preprocessing**: Applies filters like grayscale, thresholding, or blurring.
- **OCR Engine**: Uses models like Tesseract or EasyOCR.
- **Output**: Displays or saves recognized text.

---

## Technologies Used

- **Python**
- **OpenCV** – for frame capturing and processing.
- **Tesseract / EasyOCR** – for text recognition.
- **Tkinter / Streamlit (optional)** – for GUI.

---

## Applications

- Assistive reading for visually impaired users.
- Text extraction from physical documents on the go.
- Real-time subtitle generation.
- Number plate recognition in surveillance.

---

## Limitations

- Accuracy depends on camera quality and text clarity.
- Performance may vary under poor lighting or motion.

---

## Future Scope

- Integrate with translation APIs.
- Enable handwriting recognition.
- Use deep learning models like CRNN for better accuracy.
- Mobile app deployment (Android/iOS).

---

## Authors & Contributors

- [Sarvesh](https://github.com/sarveshprjs) – Creator
- [Diksha](https://github.com/Diksha-3905) – Contributor

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

- OpenCV Team
- Tesseract OCR
- EasyOCR contributors
