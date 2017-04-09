from array import array
import os
import sys
import wave

CHUNK = 1024
THRESHOLD = 400
DISTANCE_BEG = 100
DISTANCE_END = 1000
MAX_DISTANCE_BEG = 1000
MAX_DISTANCE_END = 1500

def main():
    wf = wave.open(sys.argv[1], 'r')

    ### detect silences
    cnt = 0;
    silences = []
    while True:
        frames = array('h', wf.readframes(CHUNK))
        if len(frames) == 0:
            break
        maxValue = max(frames)
        silence = maxValue <= THRESHOLD
        if silence:
            silences.append(cnt)

        cnt += 1
    numFramesTotal = cnt

    print("Silences: " + str(silences))
    print("Total number of frames: %d" % numFramesTotal)


    ### detect first relevant silence
    startPoint = 0
    for silence in silences:
        if silence > MAX_DISTANCE_BEG:
            break
        if silence > DISTANCE_BEG:
            startPoint = silence
            break

    ### detect last relevant silence
    endPoint = numFramesTotal
    for silence in reversed(silences):
        if silence < numFramesTotal - MAX_DISTANCE_END:
            break
        if silence < numFramesTotal - DISTANCE_END:
            endPoint = silence
            break

    ### write result
    wf.setpos(0)
    result = wave.open(sys.argv[2], 'w')
    result.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))

    cnt = 0
    while cnt <= endPoint:
        frames = wf.readframes(CHUNK)
        if cnt >= startPoint:
            result.writeframes(frames)
        cnt += 1

if __name__ == "__main__":
    main()
