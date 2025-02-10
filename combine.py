import librosa
import os
import soundfile as sf
import numpy as np

def combine_wavs(wav_files, start_times, output_file, sample_rate=44100):
    """
    合并多个 WAV 文件到一个最终音频文件中，每个文件在指定时刻开始出现。

    :param wav_files: 包含所有输入 WAV 文件路径的列表
    :param start_times: 每个 WAV 文件开始出现的时刻（秒）的列表，与 wav_files 对应
    :param output_file: 输出的最终音频文件路径
    :param sample_rate: 输出音频的采样率，默认为 44100 Hz
    """
    # 确定最终音频的总时长
    max_length = 0
    for wav_file, start_time in zip(wav_files, start_times):
        audio, sr = librosa.load(wav_file, sr=sample_rate)
        length = start_time + len(audio) / sr
        if length > max_length:
            max_length = length

    # 创建一个全零的音频数组，用于存储最终的音频
    final_audio = np.zeros(round(max_length * sample_rate))

    # 将每个 WAV 文件的音频数据添加到最终音频数组的指定位置
    for wav_file, start_time in zip(wav_files, start_times):
        audio, sr = librosa.load(wav_file, sr=sample_rate)
        start_index = round(start_time * sample_rate)
        end_index = start_index + len(audio)
        final_audio[start_index:end_index] += audio

    # 保存最终音频文件
    sf.write(output_file, final_audio, sample_rate)

def get_wav(subname, index):
    assert subname in ["to", "ga", "wa", "group"]
    return os.path.join("pitch-split", subname, "%+03d.wav" % index)

def main():
    output_file = "output.wav"
    timeNow = 0
    bpm = 80
    beatlen = 60 / bpm
    wav_files   = []
    start_times = []

    base = 5

    wav_files.append(get_wav("to", base + 4)) # E
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("to", base + 4)) # E
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("ga", base + 0)) # C
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("wa",base + -5)) # G
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("to", base + 4)) # E
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("to", base + 4)) # E
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("ga", base + 0)) # C
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("wa", base + -5)) # G
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("to", base + 5)) # F
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("to", base + 5)) # F
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("to", base + 5)) # F
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("ga", base + 4)) # E
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("wa", base + 2)) # D
    start_times.append(timeNow)
    timeNow += beatlen

    wav_files.append(get_wav("to", base + 2)) # D
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("to", base + 2)) # D
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("ga", base + -1)) # B
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("wa",base + -5)) # G
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("to", base + 2)) # D
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("to", base + 2)) # D
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("ga", base + -1)) # B
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("wa",base + -5)) # G
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("to", base + 5)) # F
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("to", base + 5)) # F
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("ga", base + 5)) # F
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("wa",base + 4)) # E
    start_times.append(timeNow)
    timeNow += beatlen/8

    wav_files.append(get_wav("wa",base + 2)) # D
    start_times.append(timeNow)
    timeNow += beatlen/8

    wav_files.append(get_wav("ga", base + 4)) # E
    start_times.append(timeNow)
    timeNow += beatlen

    wav_files.append(get_wav("to", base + 4)) # E
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("to", base + 4)) # E
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("ga", base + 0)) # C
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("wa",base + -5)) # G
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("to", base + 4)) # E
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("to", base + 4)) # E
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("ga", base + 0)) # C
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("wa", base + -5)) # G
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("to", base + 5)) # F
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("to", base + 5)) # F
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("to", base + 5)) # F
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("ga", base + 4)) # E
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("wa", base + 2)) # D
    start_times.append(timeNow)
    timeNow += beatlen

    wav_files.append(get_wav("to", base + 2)) # D
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("to", base + 2)) # D
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("ga", base + -1)) # B
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("wa",base + -5)) # G
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("to", base + 2)) # D
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("to", base + 2)) # D
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("ga", base + -1)) # B
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("wa",base + -5)) # G
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("to", base + 5)) # F
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("to", base + 5)) # F
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("ga", base + 5)) # F
    start_times.append(timeNow)
    timeNow += beatlen/4

    wav_files.append(get_wav("wa",base + 4)) # E
    start_times.append(timeNow)
    timeNow += beatlen/8

    wav_files.append(get_wav("wa",base + 2)) # D
    start_times.append(timeNow)
    timeNow += beatlen/8

    wav_files.append(get_wav("ga", base + 0)) # C
    start_times.append(timeNow)
    timeNow += beatlen

    combine_wavs(wav_files, start_times, output_file)

if __name__ == "__main__":
    main()