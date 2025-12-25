from TTS.api import TTS
import torch

print("Torch version:", torch.__version__)

tts = TTS(
    model_name="tts_models/multilingual/multi-dataset/xtts_v2",
    gpu=False
)

tts.tts_to_file(
    text="Bro finally my voice cloning project is working perfectly",
    speaker_wav="sample1.wav",
    language="en",
    file_path="output.wav"
)

print("✅ Voice generated: output.wav")
