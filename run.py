from pathlib import Path
import json

path_to_dir = Path("address")
files = [ file for file in path_to_dir.iterdir() if not file.is_dir()]

end = {}
for i in files:
    with open(i,"r") as f:
        file =  json.load(f)
        end.update({file["address"]:file})
with open("address.json","w") as f:
    json.dump(end,f)
