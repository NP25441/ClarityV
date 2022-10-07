import os

index = [1,2,3,4]
for i ,t in enumerate(index):
    directory = f'{t}'
    parent_dir = "Snapshot_Car"

    path = os.path.join(parent_dir, directory)

    os.mkdir(path)
    
    print(path)