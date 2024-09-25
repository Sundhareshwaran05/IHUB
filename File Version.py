import re
input1 = input().split()
input2 = int(input())
if input2 == 0:
    print(-1)
maxversion = -1
pattern = r"File_(\d+)"
for file in input1:
    match = re.match(pattern,file.strip())
    if match :
        version = int(match.group(1))
        maxversion = max(maxversion,version)
print(maxversion)