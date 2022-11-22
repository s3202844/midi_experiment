import mido
import numpy as np

def sort_diff(l):
    l = sorted(l)
    min_l = min(l)
    print(min_l)
    diff = [n - min_l for n in l]
    # print(l)
    print(diff)

mid = mido.MidiFile("Move Along (Drumless) - The All-American Rejects.mid")
print(len(mid.tracks[1]))
print(mid.tracks[1].name)
note_list = []
for i in mid.tracks[1][:-1]:
    j = i.dict()
    
    n = list(j.values())[2]
    if n == 0:
        print(i)
    if n not in note_list and n != 0:
        note_list += [n]
sort_diff(note_list)

tmp = [3*12+7, 3*12+3, 2*12+2, 5*12+5, 4*12+11, 4*12+9, 4*12+5, 5*12+7, 5*12+9, 3*12]
sort_diff(tmp)

tmp = [0, 2, 12+3, 3*12+7, 3*12+5, 3*12+9, 2*12+11, 2*12+9, 2*12+5]
sort_diff(tmp)
