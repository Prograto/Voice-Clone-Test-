# 🧠🎙 Personal AI Voice Clone (XTTS v2)

A **personal AI voice cloning system** that generates speech in **your own voice** using **Coqui XTTS v2**.  
Built with **Python**, **PyTorch**, and **Transformers**, this project demonstrates real-world AI/ML engineering practices including environment management, strict dependency pinning, and debugging breaking changes.

---

## ✨ Features

- 🎙 Clone your **own voice** from a short audio sample  
- 🌍 Multilingual text-to-speech (XTTS v2)
- 🧠 High-quality neural voice synthesis
- 💻 CPU-only support (no GPU required)
- 📦 Fully reproducible environment
- 🧪 Stable against PyTorch breaking changes

---

## 🧰 Tech Stack

- **Python**: 3.10.11 (mandatory)
- **TTS Engine**: Coqui TTS (XTTS v2)
- **Deep Learning**: PyTorch 2.1.2
- **NLP**: Transformers 4.36.2
- **Audio**: librosa, soundfile, pydub

---

## ⚠️ Important Compatibility Notice

❌ Python 3.12 / 3.13 → NOT supported  
❌ PyTorch 2.6+ → NOT supported  

This project works **ONLY** with the versions listed below.

---

## ✅ Requirements

### Python Version (MANDATORY)

    Python 3.10.11

Verify:

    python --version

---

## 📦 Python Dependencies

Create a file named `requirements.txt`:

    TTS==0.22.0
    transformers==4.36.2
    torch==2.1.2
    torchaudio==2.1.2
    torchvision==0.16.2
    numpy
    scipy
    soundfile
    librosa
    unidecode
    pydub
    tqdm
    typing_extensions

---

## 📁 Project Structure

    MyVoice-Clone/
    ├── app.py
    ├── requirements.txt
    ├── myvoice.wav
    ├── output.wav
    └── myvenv/

---

## 🚀 Installation & Setup

### 1️⃣ Create Virtual Environment (Python 3.10)

    python -m venv myvenv

Activate:

Windows:

    myvenv\Scripts\activate

Linux / macOS:

    source myvenv/bin/activate

---

### 2️⃣ Upgrade pip

    pip install --upgrade pip

---

### 3️⃣ Install Dependencies

    pip install -r requirements.txt

---

## 🎙 Voice Sample Preparation

Add a file named:

    myvoice.wav

Guidelines:
- Duration: 10–30 seconds
- Clear voice, no music or noise
- Normal speaking tone
- WAV format

---

## ▶️ Run the Voice Cloner

### app.py

    from TTS.api import TTS
    import torch

    print("Torch version:", torch.__version__)

    tts = TTS(
        model_name="tts_models/multilingual/multi-dataset/xtts_v2",
        gpu=False
    )

    tts.tts_to_file(
        text="Bro finally my voice cloning project is working perfectly",
        speaker_wav="myvoice.wav",
        language="en",
        file_path="output.wav"
    )

    print("✅ Voice generated: output.wav")

---

### Run

    python app.py

Output file:

    output.wav

---

## 🛠 Troubleshooting

### BeamSearchScorer Import Error
Cause: Incorrect transformers version  
Fix:

    pip install transformers==4.36.2

---

### Weights-only / Unpickling Error
Cause: PyTorch ≥ 2.6  
Fix:

    pip install torch==2.1.2

---

### torchvision image extension warning
Safe to ignore (image features not used).

---

### pkg_resources deprecated warning
Harmless warning from librosa.

---

## 🔒 Ethics & Usage

- Clone **only your own voice**
- Do not impersonate others
- Label audio as AI-generated when shared publicly

---

## 📌 Resume / Portfolio Description

**Personal AI Voice Clone using XTTS v2**  
Built a neural voice cloning system using Coqui XTTS v2 and PyTorch, capable of generating high-quality speech from short voice samples. Implemented a reproducible ML environment with strict dependency pinning to handle breaking changes in modern PyTorch releases.

---

## 🚀 Future Improvements

- Real-time voice chat (Whisper + XTTS)
- Slang/personality-based LLM
- FastAPI backend
- React frontend
- Mobile support

---

## 🤝 Credits

- Coqui TTS
- PyTorch
- Hugging Face Transformers

---

⭐ If you like this project, give it a star on GitHub!
