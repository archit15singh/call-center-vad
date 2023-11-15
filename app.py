import time
import torch
from pydub import AudioSegment

torch.set_num_threads(1)

SAMPLING_RATE = 16000

def main():
    s = time.time()

    model, utils = torch.hub.load(repo_or_dir='snakers4/silero-vad',
                                  model='silero_vad',
                                  force_reload=True,
                                  onnx=False)

    (get_speech_timestamps,
     save_audio,
     read_audio,
     VADIterator,
     collect_chunks) = utils

    input_file = '10_input.wav'
    output_file = 'human_speech_extracted.wav'

    wav = read_audio(input_file, sampling_rate=SAMPLING_RATE)
    speech_timestamps = get_speech_timestamps(wav, model, sampling_rate=SAMPLING_RATE)

    save_audio(output_file, collect_chunks(speech_timestamps, wav), sampling_rate=SAMPLING_RATE)

    e = time.time()
    print(f"Execution time: {e - s} seconds")

if __name__ == "__main__":
    main()
