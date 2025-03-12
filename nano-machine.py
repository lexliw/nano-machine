
#%%
# lista dos capitulos que srão baixados
mangaList = [
    "https://mugiwarasoficial.com/manga/nano-machine/chap-249/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-248/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-247/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-246/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-245/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-244/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-243/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-242/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-241/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-240/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-239/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-238/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-237/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-236/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-235/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-234_1/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-234/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-233/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-232/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-231/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-230/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-229/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-228/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-227/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-226/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-225/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-224/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-223/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-222/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-221/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-220/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-219/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-218/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-217/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-216/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-215/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-214/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-213/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-212/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-211/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-210/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-209/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-208/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-207/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-206/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-205/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-204/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-203/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-202/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-201/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-200/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-199/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-198/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-197/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-196/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-195/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-194/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-193/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-192/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-191/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-190/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-189/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-188/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-187/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-186/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-185/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-184/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-183/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-182/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-181/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-180/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-179/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-178/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-177/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-176/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-175/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-174/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-173/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-172/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-171/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-170/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-169/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-168/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-167/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-166/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-165/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-164/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-163/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-162/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-161/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-160/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-159/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-158/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-157/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-156/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-155/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-154/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-153/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-152/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-151/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-150/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-149/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-148/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-147/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-146/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-145/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-144/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-143/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-142/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-141/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-140/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-139/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-138/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-137/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-136/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-135/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-134/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-133/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-132/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-131/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-130/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-129/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-128/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-127/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-126/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-125/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-124/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-123/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-122/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-121/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-120/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-119/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-118/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-117/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-116/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-115/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-114/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-113/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-112/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-111/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-110/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-109/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-108/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-107/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-106/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-105/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-104/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-103/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-102/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-101/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-100/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-99/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-98/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-97/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-96/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-95/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-94/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-93/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-92/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-91/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-90/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-89/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-88/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-87/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-86/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-85/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-84/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-83/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-82/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-81/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-80/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-79/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-78/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-77/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-76/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-75/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-74/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-73/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-72/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-71/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-70/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-69/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-68/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-67/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-66/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-65/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-64/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-63/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-62/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-61/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-60/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-59/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-58/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-57/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-56/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-55/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-54/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-53/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-52/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-51/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-50/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-49/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-48/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-47/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-46/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-45/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-44/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-43/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-42/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-41/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-40/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-39/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-38/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-37/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-36/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-35/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-34/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-33/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-32/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-31/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-30/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-29/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-28/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-27/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-26/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-25/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-24/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-23/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-22/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-21/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-20/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-19/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-18/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-17/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-16/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-15/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-14/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-13/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-12/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-11/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-10/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-9/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-8/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-7/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-6/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-5/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-4/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-3/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-2/",
    # "https://mugiwarasoficial.com/manga/nano-machine/chap-1/",
]
#%%
# funções que serão usadas para baixar os mangás
import requests
import os
def folderName(url):
    folder = url.split('/')[5].replace('.html','')
    num = folder.split('-')[1]
    znum = num.zfill(4)
    return folder.replace(f'-{num}',f'-{znum}')

def fileName(url):
    result = url.split('/')[9]
    print(result)
    return result

def getManga(manga):
    url = manga
    folder = folderName(url)
    print(folder)

    # criar pasta
    newpath = f'./{folder}'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        # print('---')
    else:
        print('manga já baixado')
        return
    
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    imagesRaw = response.text.split('data-src="')
    i = 0
    listRawImages = []
    for chunk in imagesRaw:
        if 'https://mugiwarasoficial.com/wp-content/uploads/WP-manga/data' in chunk:
            listRawImages.append(chunk.split('" class="wp')[0])
            print(f'imagens 01: {listRawImages[i]}')
            i += 1
    
    # baixar imagens
    for image in listRawImages:
        img_data = requests.get(image).content
        file = fileName(image)
        with open(f'./{folder}/{file}', 'wb') as handler:
            handler.write(img_data)

    # return listImages
#%%
# lista = getManga('https://mugiwarasoficial.com/manga/nano-machine/chap-1/')
#%%
# loop para baixar os mangás

for manga in mangaList:
    getManga(manga)

# print(response.text) "https://meo.comick.pictures/1-Pt0kp13YjAfKd.jpg",

# %%
# trata o nome das imagens
from os import listdir
from os.path import isfile, isdir, join

mypath = './'

onlyfolders = [f for f in listdir(mypath) if isdir(join(mypath, f))]
onlyfolders.sort()
print(onlyfolders)

for folder in onlyfolders:
    chapterFolder = f'./{folder}/'
    onlyfiles = [f for f in listdir(chapterFolder) if isfile(join(chapterFolder, f))]
    onlyfiles.sort()
    for file in onlyfiles:
        if len(file.split('.')[0]) <= 2:
            newfilename= file.replace(file.split('.')[0], file.split('.')[0].zfill(3))            
            os.rename(f'{chapterFolder}{file}', f'{chapterFolder}{newfilename}')
        if 'pagina_' in file or '-optimized' in file  or '-copiar' in file or '411409_' in file or '409788_' in file  or '430151_' in file:
            newfilename= file.replace('pagina_','').replace('-optimized','').replace('-copiar','').replace('411409_','').replace('409788_','').replace('430151_','')
            newfilename= newfilename.replace(newfilename.split('.')[0], newfilename.split('.')[0].zfill(3))            
            os.rename(f'{chapterFolder}{file}', f'{chapterFolder}{newfilename}')
    
    onlyfiles = [f for f in listdir(chapterFolder) if isfile(join(chapterFolder, f))]
    onlyfiles.sort()
    print(f'{folder}:{onlyfiles}')


# %%
# cria os readme.md
from os import listdir
from os.path import isfile, isdir, join

mypath = './'

onlyfolders = [f for f in listdir(mypath) if isdir(join(mypath, f))]
onlyfolders.sort()
onlyfolders.remove('.git')
print(onlyfolders)

conteudo = '# Nano Machine\n'
for folder in onlyfolders:
    #- [teste](/chap-0001/readme.md)
    conteudo += f'- [{folder}](/{folder}/readme.md)\n'
    # conteudo += f'<p style="text-align: center;"><button name="menu" onclick="/{folder}/readme.md">{folder}</button></p>'


print('./readme.md')
f = open('./readme.md', 'w')
f.write(conteudo)
f.close()

for i in range(len(onlyfolders)):
    chapterFolder = f'./{onlyfolders[i]}/'
    anterior = '/nano-machine/'
    proximo = '/nano-machine/'
    menu = '/nano-machine/'
    if i - 1 >= 0: 
        anterior = f'/nano-machine/{onlyfolders[i-1]}/'
    if i + 1 <= len(onlyfolders)-1: 
        proximo = f'/nano-machine/{onlyfolders[i+1]}/'

    onlyfiles = [f for f in listdir(chapterFolder) if isfile(join(chapterFolder, f))]
    onlyfiles.sort()
    onlyfiles.remove('readme.md')
    # print(f'{onlyfolders[i]}:{onlyfiles}')
    navegacao = f'##### [ANTERIOR]({anterior})&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MENU]({menu})&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PRÓXIMO]({proximo})\n'
    conteudo = f'# {onlyfolders[i]}\n{navegacao}'

    for file in onlyfiles:
        conteudo += f'![{file}]({file})\n\n'
    
    conteudo += f'{navegacao}'

    print(f'{chapterFolder}readme.md')
    f = open(f'{chapterFolder}readme.md', 'w')
    f.write(conteudo)
    f.close()
# %%
# %%
# valida imagens
from os import listdir, lstat
from os.path import isfile, isdir, join

mypath = './'

onlyfolders = [f for f in listdir(mypath) if isdir(join(mypath, f))]
onlyfolders.sort()
print(onlyfolders)

for folder in onlyfolders:
    chapterFolder = f'./{folder}/'
    onlyfiles = [f for f in listdir(chapterFolder) if isfile(join(chapterFolder, f))]
    onlyfiles.sort()
    for file in onlyfiles:
        size = lstat(f'./{folder}/{file}').st_size
        if size == 0:
            # onlyfiles.remove(file)
            print(f'./{folder}/{file} size {size}')

    # print(f'{folder}:{onlyfiles}')

# %%
from os import lstat
print (lstat("./chap-0248/001__001.jpg").st_size)
# %%

print(str(int('001')))
# %%
