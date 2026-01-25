import wave
import struct
import math

# --- Pomocná funkcia na generovanie WAV ---


def generate_wav(filename, duration, freq_func, volume=0.5, sample_rate=44100):
    wav = wave.open(filename, "w")
    wav.setparams((1, 2, sample_rate, 0, "NONE", "not compressed"))

    for i in range(int(duration * sample_rate)):
        t = i / sample_rate
        freq = freq_func(t)
        sample = int(volume * 32767 * math.sin(2 * math.pi * freq * t))
        wav.writeframes(struct.pack("<h", sample))

    wav.close()


# --- 1. HIT SOUND (krátky pop) ---
def hit_freq(t):
    return 800 + 400 * math.exp(-6 * t)  # rýchly pokles frekvencie


generate_wav("hit.wav", duration=0.12, freq_func=hit_freq, volume=0.7)


# --- 2. FAIL SOUND (nízky buzz) ---
def fail_freq(t):
    return 120 + 20 * math.sin(40 * t)


generate_wav("fail.wav", duration=0.35, freq_func=fail_freq, volume=0.6)


# --- 3. SIMPLE MUSIC LOOP (ambientná syntetická melódia) ---
def music_freq(t):
    # jednoduchý trojtónový pattern
    notes = [440, 554, 659]  # A4, C#5, E5
    index = int(t * 2) % len(notes)
    return notes[index]


generate_wav("music.wav", duration=4.0, freq_func=music_freq, volume=0.3)