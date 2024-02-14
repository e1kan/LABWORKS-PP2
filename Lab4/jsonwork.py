import json

print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

with open(r"C:\Users\Eva\Desktop\hello\University\LabWorks\Lab4\sample-data.json") as file:
    data = json.load(file)

for item in data['imdata']:
    attributes = item['l1PhysIf']['attributes']
    dn = attributes['dn']
    speed = attributes['speed']
    mtu = attributes['mtu']
    print(f"{dn:<50} {'':<20} {speed:<9} {mtu:<6}")
