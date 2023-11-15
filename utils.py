from pydub import AudioSegment

def repeat_wav(input_file, output_file, num_repeats):
    audio = AudioSegment.from_wav(input_file)

    repeated_audio = audio * num_repeats

    repeated_audio.export(output_file, format="wav")
