from sys import argv, exit
from csv import DictReader


# Check user input
if len(argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit(1)

strs = []
profiles = []

# Open csv data file
with open(argv[1], "r") as datafile:
    
    reader = DictReader(datafile)
    strs = reader.fieldnames[1:]
    
    for row in reader:
        profiles.append(row)

strcount = dict.fromkeys(strs, 0)

# Open sequence file
with open(argv[2], "r") as seqfile:

    sequence = seqfile.readline()

    for STR in strs:

        l = len(STR)
        maximum = 0

        for i in range(len(sequence)):
            repeats = 0

            if sequence[i: i + l] == STR:
                repeats += 1

                while sequence[i: i + l] == sequence[i + l: i + (2 * l)]:
                    repeats += 1
                    i += l

            if repeats > maximum:
                maximum = repeats

        strcount[STR] = maximum

# Compare sequence
for profile in profiles:

    match = 0

    for STR in strs:

        if int(profile[STR]) != strcount[STR]:
            continue

        match += 1

    # Print match
    if match == len(strs):
        print(profile['name'])
        exit(0)

print("No match")

exit(1)
