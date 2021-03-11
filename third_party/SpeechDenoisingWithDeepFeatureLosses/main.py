
import argparse
# from speech_denoising import SpeechDenoising
from audio_io import AudioIO
        
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--format", default=0, type=int)
    parser.add_argument("--channels", default=2, type=int)
    parser.add_argument("--rate", default=44100, type=int)
    parser.add_argument("--chunk", default=1024, type=int)
    parser.add_argument("--save_audio", default=False, type=bool)
    parser.add_argument("--output_filename", default='res_audio.wav', type=str)

    args = parser.parse_args()

    # speech_denoising = SpeechDenoising(args)
    audio_io = AudioIO(args)

    while True:
        noisy_audio = audio_io.get_audio()
        # denoised_audio = speech_denoising.get_denoised_audio(noisy_audio)

if __name__ == "__main__":
    main()
