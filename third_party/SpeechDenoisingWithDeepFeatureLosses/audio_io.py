import pyaudio
import wave


class AudioIO():
    def __init__(self, args):
        if args.format == 0:
            self.FORMAT = pyaudio.paInt16
        self.CHANNELS = args.channels
        self.RATE = args.rate
        self.CHUNK = args.chunk
        self.SAVE_AUDIO = args.save_audio
        self.WAVE_OUTPUT_FILENAME =  args.output_filename
        
        self.audio = pyaudio.PyAudio()

        self.stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS,
                            rate=self.RATE, input=True,
                            frames_per_buffer=self.CHUNK)

        self.frames = []

    def get_audio(self):
        audio = self.stream.read(self.CHUNK)
        if self.SAVE_AUDIO:
            self.frames.append(audio)
        return audio        

    def __del__(self):        
        # stop Recording
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()

        if self.SAVE_AUDIO:
            print('Saving audio')
            waveFile = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
            waveFile.setnchannels(self.CHANNELS)
            waveFile.setsampwidth(self.audio.get_sample_size(self.FORMAT))
            waveFile.setframerate(self.RATE)
            waveFile.writeframes(b''.join(self.frames))
            waveFile.close()
