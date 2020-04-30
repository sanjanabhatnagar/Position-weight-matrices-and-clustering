import json
injected = []
recovered = []
array = []
with open("Barcodes_120", 'r') as handle:
    for a in handle:
        injected.append(a.strip())
with open("Recovered_120", 'r') as handle2:
    for b in handle2:
        recovered.append(b.strip())
score = 0

Comparisons = {}
Temp = {}

for a in injected:
    Array = []
    SCORES = []
    Mismatches = {}
    for b in recovered:
        penalty = 0
        i = 0
        while (i < 10):
            if a[i] == b[i]:
                score += 1
            else:
                penalty += 1
            i += 1
        #if (penalty <3 and penalty != 0):
        Array.append(b)
        SCORES.append(penalty)

    T = len(Array)
    j = 1
    k = 0
    while j < (T+1):
        Mismatches.update({Array[k]: SCORES[k]})
        k = j - 1
        j += 1

    Temp.update({a: Mismatches})

with open("Cis_els_bar_dis1", 'w') as handle:
    json.dump(Mismatches, handle, indent=2)
with open("Cis_els_bar_dis2", 'w') as handle2:
    json.dump(Temp, handle2, indent=2)