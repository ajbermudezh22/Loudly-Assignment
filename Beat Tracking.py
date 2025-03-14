import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Load Audio File
audio_file = "loudly.mp3"
y, sr = librosa.load(audio_file)

# Perform Beat Tracking
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
print(f"Estimated tempo: {tempo.item():.2f} beats per minute")

# Convert beat frames to Time in seconds
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

# Display the waveform
plt.figure(figsize=(12, 6))
librosa.display.waveshow(y, sr=sr, alpha=0.6, color="orange", label="Audio Signal")
plt.vlines(beat_times, ymin=-1, ymax=1, color='r', alpha=0.7, linestyle='dashed', label='Beats')

# Add Title and Labels (Fixed Tempo Display)
plt.title(f"Waveform of Audio Signal with Beat Positions\nTempo: {tempo.item():.2f} BPM")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (Normalized)")
plt.legend()
plt.show()
