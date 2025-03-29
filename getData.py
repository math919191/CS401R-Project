from serpapi import GoogleSearch

from dotenv import load_dotenv
import os
from pathlib import Path
import json    

load_dotenv()
SERP_API_KEY = os.getenv("SERP_API_KEY") 

text = Path('videos.txt').read_text()
videos = []
for line in text.split("\n"):
    title, url = line.split("-")
    _, urlParams = url.split("v=")
    params = urlParams.split("&") 
    videoID = params[0]
    videos.append((title, videoID, params))


all_data = []

for i in range(0,9):
  params = {
    "engine": "youtube_video",
    "v": videos[i][1],
    "api_key": SERP_API_KEY
  }

  print(params)

  search = GoogleSearch(params)
  results = search.get_dict()

  all_data.append(results)
data = {"data": all_data}

# fileName = "results" + "_try2_" + videoID + ".json"
fileName = "video_data" + ".json" 
with open(fileName, "w") as file:
    json.dump(data, file, indent=4)
