# import requests

# url = "https://f7f8-202-80-249-133.ap.ngrok.io/api/postdata"


# get = requests.get(url)

# headers = {'Accept': 'application/json',
#         'content-type': 'application/json',
#         'Access-Control_Allow_Origin': '*',}

# myobj = {'license_plate': '01',
#          'name': '02',
#          'date': '03',
#          'timein': '04',
#          'timeout': '05',
#          'city': '06',
#          'vehicle1':'07',
#          'vehicle2':'08',
#          'vehicle3':'09',
#          'vehicle4':'10',
#          'vehicle5':'11',
#          'color': '12'}

# post = requests.post(url,json=myobj,headers=headers)



# print(post.status_code)
# print(post.json())
# print(get.status_code)
# print(get.json())


# import hashlib
# from scipy.misc import imread, imresize, imshow
# import matplotlib.pyplot as plt
# import matplotlib.gridspec as gridspec
# import numpy as np
# import os
# def file_hash(filename):
#     with open(filename,'rb') as f:
#         return hashlib.md5(f.read()).hexdigest()
# os.getcwd()
# os.chdir(r'D:\Develop\Senior_Project\ClarityV\Snapshot-Data')
# os.getcwd()
# files_list = os.listdir('.')
# print (len(files_list))
# duplicates=[]
# hash_keys=dict()
# for index, filename in enumerate(os.listdir('.')):
#     if os.path.isfile(filename):
#         with open(filename, 'rb') as f:
#             filehash = hashlib.md5(f.read()).hexdigest()
#         if filehash not in hash_keys:
#             hash_keys[filehash]=index
#         else:
#             duplicates.append((index,hash_keys[filehash]))
# print(duplicates)
# for file_indexes in duplicates[:30]:
#     try:
#         plt.subplot(121),plt.imshow(imread(files_list[file_indexes[1]]))
#         plt.title(file_indexes[1]),plt.xticks([]),plt.yticks([])
#         plt.subplot(122),plt.imshow(imread(files_list[file_indexes[0]]))
#         plt.title(str(file_indexes[0])+ 'duplicate'),plt.xticks([]),plt.yticks([])
#         plt.show()
#     except OSError as e:
#         continue
# for index in duplicates:
#     os.remove(files_list[index[0]])