import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

audio_file = "audio.wav"    
tsv_file = "s1.tsv"  
tsv_file2 = "s2.tsv"      
os.makedirs("outputs", exist_ok=True)
# loading the audio 
y, sr = librosa.load(audio_file, sr=None)
duration = librosa.get_duration(y=y, sr=sr)

# STFT 
D = np.abs(librosa.stft(y, n_fft=1024, hop_length=256))
S_db = librosa.amplitude_to_db(D, ref=np.max)

plt.figure(figsize=(10, 5))
librosa.display.specshow(S_db, sr=sr, hop_length=256, x_axis="time", y_axis="log", cmap="viridis")
plt.colorbar(format="%+2.0f dB")
plt.title("STFT Magnitude Spectrogram")
plt.tight_layout()
plt.savefig("outputs/spectrogram.png")
plt.show()
plt.close()

rms = librosa.feature.rms(y=y, frame_length=1024, hop_length=256)[0]
rms_db = librosa.amplitude_to_db(rms, ref=np.max)
frames = range(len(rms))
times = librosa.frames_to_time(frames, sr=sr, hop_length=256)
#Frame wise Rms
plt.figure(figsize=(10, 4))
plt.plot(frames, rms_db, label="RMS Energy (dB)")
plt.xlabel("Time (s)")
plt.ylabel("Energy (dB)")
plt.title("RMS Energy Over Frames")
plt.legend()
plt.tight_layout()
plt.show()
plt.savefig("outputs/rms_energy_frame.png")
plt.close()
# time wise rms :
plt.figure(figsize=(10, 4))
plt.plot(times, rms_db, label="RMS Energy (dB)")
plt.xlabel("Time (s)")
plt.ylabel("Energy (dB)")
plt.title("RMS Energy Over Time")
plt.legend()
plt.tight_layout()
plt.savefig("outputs/rms_energy_time.png")
plt.show()
plt.close()


# load tsv 
df = pd.read_csv(tsv_file, sep="\t", header=None, names=["Start", "End", "ASR Output", "Reference"])

plt.figure(figsize=(12, 4))
librosa.display.waveshow(y, sr=sr, alpha=0.7)
plt.title("Waveform with Segment Boundaries")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

#TSV Segment Boundaries
for _, row in df.iterrows():
    start, end = row["Start"], row["End"]
    plt.axvline(x=start, color="red", linestyle="--", alpha=0.6)
    plt.axvline(x=end, color="blue", linestyle="--", alpha=0.6)

plt.tight_layout()
plt.savefig("outputs/waveform_segments.png")
plt.close()

#load tsv 2
df2 = pd.read_csv(tsv_file2, sep="\t", header=None, names=["Start", "End", "ASR Output", "Reference"])

plt.figure(figsize=(12, 4))
librosa.display.waveshow(y, sr=sr, alpha=0.7)
plt.title("Waveform with Segment Boundaries")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")


for _, row in df2.iterrows():
    start, end = row["Start"], row["End"]
    plt.axvline(x=start, color="red", linestyle="--", alpha=0.6)
    plt.axvline(x=end, color="blue", linestyle="--", alpha=0.6)

plt.tight_layout()
plt.savefig("outputs/waveform_segments_2.png")
plt.close()