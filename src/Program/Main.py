import time

from Object import TrainingData

with open('sample.txt', 'r') as trainingDataFile:
  rawData = trainingDataFile.read()

list = TrainingData.rawDataToList(rawData, " eatshit ")

print(list)
time.sleep(2)
print(TrainingData.getContent(list[0]))
print(TrainingData.getFollowers(list[0]))
print(TrainingData.getPopularity(list[0]))

json = TrainingData.parseTrainingSampleToJson(list[0])

print(json)

jsonlist = TrainingData.parseListToJsonList(list)

print(jsonlist)
time.sleep(2)
print(jsonlist[0])
print(jsonlist[420])
print(jsonlist[69].get("input").get("content"))

def main():
    f = open('sample.txt')
    line_contents = f.read()
    print(line_contents)
    search_phrase = "eatshit"
    for line in f.readlines():
        line.split()
        if line.find(search_phrase) >= 0:
            print(line)
