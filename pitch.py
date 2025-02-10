import os
import librosa
import soundfile as sf

import sounddevice as sd
import soundfile as sf

DIRNOW = os.path.dirname(os.path.abspath(__file__))

def pitch_and_save(input_wav_path, output_wav_path, n_steps):
    audio, sr = librosa.load(input_wav_path)
    pitched_audio = librosa.effects.pitch_shift(audio, sr=sr, n_steps=n_steps)
    sf.write(output_wav_path, pitched_audio, sr)

def play_sound(filepath, wait=True):
    audio, sample_rate = sf.read(filepath)
    sd.play(audio, sample_rate)
    if wait:
        sd.wait()

def pitch_one_tune(filepath):
    assert os.path.isfile(filepath)
    sound_name = os.path.basename(filepath).replace(".wav", "")
    tune_dir   = os.path.join(DIRNOW, "pitch-split", sound_name)
    os.makedirs(tune_dir, exist_ok=True)
    for i in range(-12, 24 + 1):
        pitch_and_save(filepath, os.path.join(tune_dir, "%+03d.wav" % i), i)

def pitch_all_tune():
    tune_split_dir = os.path.join(DIRNOW, "tune-split")
    for file in os.listdir(tune_split_dir):
        filepath = os.path.join(tune_split_dir, file)
        pitch_one_tune(filepath)

if __name__ == "__main__":
    pitch_all_tune()
