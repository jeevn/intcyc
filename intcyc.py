# INTERVAL CYCLER # CC BY-NC-SA # http://jeevn.github.io
scale = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
note = lambda x: scale[(x%12)]
def dir (y,x):
    if (abs(y-x))//12>0: o = str(abs(y-x)//12)+' '
    else: o = ' '
    if (y>x): return '^'+o
    elif (y<x): return '_'+o
print '\n*******************\n* INTERVAL CYCLER *\n*******************\n\nEnter pitches as space-separated integers.\nC=0(mod12); 8ves are relative; negatives are fine.\nMIDI note values are compatible.\n\nRead results across rows (not down columns).\nChord voicing: left--right = low--high.\n'
while True:
    print 'INITIAL PITCH ROW:',
    userInput = raw_input()
    try: row = map(int, userInput.split())
    except Exception:
        if userInput in ('Q','q'): break
        else:
            print '\nEnter pitches as numbers.\n'
            continue
    n = len(row)
    intervals = [row[i]-row[i-1] for i in range (n)]
    rows = [[row[0]] for i in range (n)]
    for i in range (n):
        for j in range (1,n): rows[i].append(rows[i][j-1] + intervals[(i+j)%n])
    chords = [ [sorted(set(rows[j]))] + [sorted(set([s[i]-row[j]+row[0] for s in rows])) for i in range (1,n)] for j in range (n)]
    rnotes = [[note(i[0])] + [dir(i[j],i[j-1])+note(i[j]) for j in range (1,n)] for i in rows]
    cnotes = [[[note(z) for z in y] for y in x]for x in chords]
    print '__________\nPITCH ROWS\n'
    for m in rnotes: print ' '.join(m)
    print '\n______\nCHORDS\n'
    for s in cnotes:
        for t in s: print ' '.join(t)
        print
    print 'Go again, or type Q to quit.\n'
