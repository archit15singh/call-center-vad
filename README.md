# call-center-vad
a util to do human speech activity detection and cut all the segments without human speech from audio files (excluding music/tones, robot voice)


thank you snakers4/silero-vad


test input audio: 10 seconds human, 5 seconds music, 10 seconds human, 5 seconds music = 30 seconds
expected output audio: 10 seconds human, 10 seconds human = 20 seconds

30 seconds -> 20 seconds
300 seconds -> 200 seconds
5 mins -> 3.33 mins
