
import json
import matplotlib.pyplot as plt

with open('video_data.json', 'r') as openfile:
    json_object = json.load(openfile)

dataEntries = json_object["data"]

likes = [videoEntry["extracted_likes"] if "extracted_likes" in videoEntry else 0 for videoEntry in dataEntries ]
descriptionLen = [len(videoEntry["description"]["content"]) for videoEntry in dataEntries]
views = [videoEntry["extracted_views"] for videoEntry in dataEntries]
# for videoEntry in dataEntries:
#     print(videoEntry["title"])
#     print(videoEntry["extracted_likes"])
#     print(videoEntry["published_date"])
#     print("description len", len(videoEntry["description"]["content"]))


# plotting the points   
plt.scatter(likes, views)  
plt.xlabel('Likes')  
plt.ylabel('Views')  
plt.title('Video Analysis')  
plt.show()  
