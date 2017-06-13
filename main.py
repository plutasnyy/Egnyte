import json

for j in range(0,34):
    for i in open('out/FSE_'+str(j), 'r'):
        print(json.loads(i)['eventHeader']['workgroupID'])

