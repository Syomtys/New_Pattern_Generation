from PIL import Image, ImageFont, ImageDraw, ImageFilter
from script.create_html_files import Create_Pats_html
from script.ListUserAgent import RandomUserPC
from script.ListsForPatern import *
from string import ascii_uppercase
from datetime import datetime
from bs4 import BeautifulSoup
from script.Start import *
from random import choice
from ftplib import *
import http.client
import requests
import random
import shutil
import json
import re
import os

#-------------------PARSING JOOM IN LIST--------------------------#
#-----------------------------------------------------------------#

now = datetime.now()
start_time = datetime.now()

def Parsing_JOOM_in_list():
    print('PARSING JOOM')
    list_id_tivar = []
    ok_url = []
    templates_print = 0
    def curl(id_towar):
        cookies = {
            '_gcl_au': '1.1.1002810158.1660711796',
            '_gid': 'GA1.2.146019057.1660711796',
            '_ga': 'GA1.1.11631034314210437782',
            '_ga_5F0JRH5NNP': 'GS1.1.1660796664.5.1.1660803146.0.0.0',
        }

        headers = {
            'authority': 'api.joom.com',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,kk;q=0.6,tr;q=0.5,uz;q=0.4',
            'authorization': 'Bearer SEV0001AHdJrpMIDBe1cZLmdmyapsRgfXKDorM1OKOQEjjDZ4_XlNzIBSgQsAX3s7g3VzA93vZFu_xAVqLmIbpmldNUQXtCX3mxLRHAVzVgMrdcaTDPK1SuFFIi40DDKrgvgVlxss7_AMYv4kHajyehrsqwMis9Zl6zhT5ecR-VqbayYWg_P79M2HGq6XS_n0v0JWwdnlG8EH8mVUp247JPLIYiof_mikypl2j14p3LRFOQu5ySO8z1vXQa4pYssU3nmf9Yskulpmtk3uWTgJnBivGoPlvEuXCfMFgLXJ-Bs1ACbBuubjbQHpY',
            'origin': 'https://www.joom.com',
            'referer': 'https://www.joom.com/',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36',
            'x-api-token': 'si0MhzMZ5GFaE6RECweCUDsfam59dz0t',
            'x-ostype': 'android',
            'x-rendering-id': '62fdd848edbbc76cffaf453d',
            'x-request-path': '/ru/products/6182275c20d7a601dcb04c4d',
            'x-version': '4.8.3-2697',
        }
        params = {
            'language': 'ru-RU',
            '_': 'l6ynbbso',
        }
        json_data = {
            'appearance': {},
            'pageToken': '1-gatjb250ZW50TGlzdIKhZqdyZXZpZXdzom1w0Rdw',
        }
        response = requests.post(f'https://api.joom.com/1.1/products/{id_towar}/contentList/get',
                                 params=params, cookies=cookies, headers=headers, json=json_data).json()
        tovars_id = response.get('contexts')
        final_str = re.findall(r"'id': '(.*?)',", str(tovars_id), flags=re.M)
        for i in final_str:
            list_id_tivar.append(i)
    with open('script/2id_list.json', 'r') as file:
        list_used_noused = json.load(file)

    id_towar = list_used_noused[1][len(list_used_noused[1])-1]
    curl(id_towar)
    ok_url = list_id_tivar
    for i in ok_url:
        if i in list_used_noused[0] or i in list_used_noused[1]:
            pass
            # print('уже есть')
        else:
            list_used_noused[1].append(i)
            templates_print = templates_print+1
            # print(i)
    print('добавлено JOOM ссылок - '+str(templates_print))

    with open('script/2id_list.json', 'w') as f:
        json.dump(list_used_noused,f,indent=4,ensure_ascii=False)

if parsing == 1:
    Parsing_JOOM_in_list()
    print('\n\n' + str(datetime.now() - start_time))


for ndom in range(len(domlist)):
    DOMAINNAME = domlist[ndom].lower()

    if restart_liv == 1:
        list_restarted_domain = []
        with open('script/pattern_list.json', 'r') as file_restart:
            list_restarted_domain = json.load(file_restart)
        for items_restart in list_restarted_domain:
            if DOMAINNAME in items_restart:
                print(items_restart[1])
                telcomp = items_restart[1]
                print(items_restart[2])
                adress = items_restart[2]
                print(items_restart[4])
                url = items_restart[4]
    DOMAINNAMESPLIT = DOMAINNAME.split('.')[0]
    list_rename_files = {}
    list_rename_files['img'] = {}
    list_rename_files['css'] = {}
    list_rename_files['html'] = {}
    list_font_files = {}
    filelist = []
    l = ''
    listrename = []
    ccscolor = []
    listimgs = []
    prename = DOMAINNAMESPLIT
    chars = '1234567890ABCDEF'
    char_mini = 'FE'
    ip = sph.split(':')[0]
    log = sph.split(':')[1]
    pas = sph.split(':')[2]
    conn = http.client.HTTPConnection("ifconfig.me")
    conn.request("GET", "/ip")
    print(conn.getresponse().read())
    ra = random.randint(1, 6)
    if ra == 1:
        a = '#F1' + ''.join(random.sample(chars, 2)) + '0D'
    if ra == 4:
        a = '#F1' + '0D' + ''.join(random.sample(chars, 2))
    if ra == 2:
        a = '#' + '0D' + 'F1' + ''.join(random.sample(chars, 2))
    if ra == 5:
        a = '#' + ''.join(random.sample(chars, 2)) + 'F1' + '0D'
    if ra == 3:
        a = '#0D' + ''.join(random.sample(chars, 2)) + 'F1'
    if ra == 6:
        a = '#' + ''.join(random.sample(chars, 2)) + '0D' + 'F1'
    col_r = random.randint(235, 255)
    col_g = random.randint(235, 255)
    col_b = random.randint(235, 255)
    print(f"first color - {a}")
    print(f"last color - {col_r}, {col_g}, {col_b}")

    # print('shop url')
    goodurl1 = 'yes'
    if restart_liv == 0:
        while goodurl1 == 'yes':
            with open('script/2id_list.json', 'r') as file:
                list_used_noused = json.load(file)
            url = list_used_noused[1][len(list_used_noused[1]) - 1]
            list_used_noused[1].remove(url)
            list_used_noused[0].append(url)
            with open('script/2id_list.json', 'w') as f:
                json.dump(list_used_noused, f, indent=4, ensure_ascii=False)
            print('остаток JOOM ссылок - ' + str(len(list_used_noused[1]) - 1))
            url1 = 'https://www.joom.com/ru/products/' + url
            if lang_opt == 'br':
                url = f'https://www.joom.com/pt-br/products/' + url
            else:
                url = f'https://www.joom.com/{lang_opt}/products/' + url

            headers = {'user-agent': RandomUserPC}
            Response = requests.get(url1, headers=headers)
            soup = BeautifulSoup(Response.content, 'html.parser')
            NAMETOVAR1 = str(soup.find('title').text).split('–')[0]
            goodurl = []
            for pwords_1 in pwords_title:
                if pwords_1 in NAMETOVAR1.lower():
                    goodurl.append('yes')
                else:
                    goodurl.append('no')
            print(url)
            if 'yes' in goodurl:
                goodurl1 = 'yes'
                print('this joom url - dont ok')
            else:
                goodurl1 = 'no'
                print('this joom url - ok')



    if os.path.exists('newvite'):
        shutil.rmtree('newvite')
    shutil.copytree('patterns/pattern - test', 'newvite')
    os.chdir('newvite')
    list_html_files = Create_Pats_html(lang_opt)
    for file in list_html_files:
        with open(file, 'w') as file_html:
            file_html.write(list_html_files[file])

    os.mkdir(prename+'font')
    css_items = ["font_1","font_2","font_3","font_4","font_5"]
    fonts_list = os.listdir('../font')
    font = ImageFont.truetype(f'../font/{str(random.choice(fonts_list))}', 28)
    with open('css/_style_1.css', 'r') as file:
        css_txt = file.read()
    css_txt = css_txt.replace('f0nt_pth',prename+'font')
    for css_item in css_items:
        css_file_src = random.choice(fonts_list)
        list_font_files[css_item] = css_file_src
        css_file_name = css_file_src.split('.')[0]
        css_txt = css_txt.replace(css_item, css_file_name, 1)
        css_txt = css_txt.replace(css_item, css_file_src, 1)
        css_txt = css_txt.replace(css_item, css_file_name, 1)
        shutil.copyfile(f'../font/{css_file_src}', f'{prename}font/{css_file_src}')
    with open('css/_style_1.css', 'w') as file:
        file.write(css_txt)

    with open('css/_style_2.css', 'r') as file:
        css_txt = file.read()

    css_txt = re.sub(r"#f8d0b2", f'rgb({str(random.randint(190, 240))}, {str(random.randint(190, 240))}, {str(random.randint(190, 240))})', css_txt, flags=re.M)
    css_txt = re.sub(r"#f4ccd6", f'rgb({str(random.randint(190, 240))}, {str(random.randint(190, 240))}, {str(random.randint(190, 240))})', css_txt, flags=re.M)
    with open('css/_style_2.css', 'w') as file:
        file.write(css_txt)

    with open('index.html', 'r') as file:
        htmltxt = file.read()

    with open('../script/language_all_list.json', 'r') as f:
        file = json.load(f)[lang_opt]["text_in_html"]
    for item_text_in_html in file:
        htmltxt = htmltxt.replace(item_text_in_html, file[item_text_in_html])
    # for i in file[f'{lang_opt}'].keys():
    #     htmltxt = htmltxt.replace(i, file[f'{lang_opt}'][i])
        # print(i + ' //// ' + file[f'{lang_opt}'][i])
    htmltxt = htmltxt.replace('DOMAINNAME', DOMAINNAME)
    htmltxt = htmltxt.replace('DOMA1NNAMESPLIT', DOMAINNAMESPLIT)
    if lang_opt == "ru":
        htmltxt = htmltxt.replace('PRISESTISTOVAR', str(random.randint(4000, 20000)))
    else:
        htmltxt = htmltxt.replace('PRISESTISTOVAR', str(random.randint(30, 300)))

    with open('index.html', 'w') as file:
        file.write(htmltxt)

    # ----------  DOWNLOAD IMAGES   -------------

    if url.split('/')[2] == 'aliexpress.ru':
        url = url.split('?')[0]
        # headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; ) AppleWebKit/539.36 (KHTML, like Gecko) Chrome/92.0.4472.77 Safari/538.36'}
        headers = {'user-agent': RandomUserPC}
        # headers = {'user-agent': f'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53{str(random.randint(0,9))}.3{str(random.randint(0,9))} (KHTML, like Gecko) Chrome/9{str(random.randint(0,9))}.0.418{str(random.randint(0,9))}.8{str(random.randint(0,9))} Safari/53{str(random.randint(0,9))}.3{str(random.randint(0,9))}'}
        # print(RandomUserPC)
        Response = requests.get(url, headers=headers)
        # time.sleep(7.5)
        soup = BeautifulSoup(Response.content, 'html.parser')
        html_new = str(soup)
        NAMETOVAR = str(soup.find_all('title')).split(',')[0].split('|')[0].split('>')[1]
        imagelist = soup.find('div', attrs={'style': 'margin:0 0 16px 0;padding:20px;border-radius:0 0 5px 5px'})
        images = imagelist.find_all('img')
    elif url.split('/')[2] == 'www.joom.com':
        headers = {'user-agent': RandomUserPC}
        Response = requests.get(url, headers=headers)
        soup = BeautifulSoup(Response.content, 'html.parser')
        NAMETOVAR = str(soup.find('title').text).split('–')[0]
        if lang_opt == "ru":
            alpha = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890%./,-'
        else:
            alpha = '1234567890%./,-'

        # print(NAMETOVAR)
        for i in range(len(alpha)):
            if alpha[i] in NAMETOVAR:
                # print(alpha[i])
                NAMETOVAR = NAMETOVAR.replace(alpha[i], '')
        for i in pwors:  # replace pWords
            NAMETOVAR = NAMETOVAR.replace(i, '')
        print('pWords cleaninig')
        NAMETOVAR = NAMETOVAR.replace('   ', ' ')
        NAMETOVAR = NAMETOVAR.replace('  ', ' ')
        # print(NAMETOVAR)
        cookies = {
            'sticky_session_id': '1660711793.946.2062.709724',
            'accesstoken': 'SEV0001AHdJrpMIDBe1cZLmdmyapsRgfXKDorM1OKOQEjjDZ4_XlNzIBSgQsAX3s7g3VzA93vZFu_xAVqLmIbpmldNUQXtCX3mxLRHAVzVgMrdcaTDPK1SuFFIi40DDKrgvgVlxss7_AMYv4kHajyehrsqwMis9Zl6zhT5ecR-VqbayYWg_P79M2HGq6XS_n0v0JWwdnlG8EH8mVUp247JPLIYiof_mikypl2j14p3LRFOQu5ySO8z1vXQa4pYssU3nmf9Yskulpmtk3uWTgJnBivGoPlvEuXCfMFgLXJ-Bs1ACbBuubjbQHpY',
            'accesstokenhash': '-1k1qljf',
            'refreshtoken': 'SEV0001AHdKrpMIDBcekBnCKP7UeJ_bRyaAVToSGcPx8AgwJwDXsX5BU0k5visHWC1VjT4clCwV07GPlhPkm4I0NDk0NNS5nYRVmjjOHTGpmaPkH608nsRaF5WBFJq5gI5Ng-a0Yff0-hAVjddHZHE7J0eU6vumwTo-g0yG-R-I5fx9rsjKlmJqt-zOnDahW53uvMTP-piSbpquWVOj',
            'redirectLanguage': 'ru',
            'userhash': '-1e79qji',
            'timezoneName': 'Asia%2FYekaterinburg',
            'timezone': '-300',
            'trc': '%7B%22sent%22%3Atrue%7D',
            '_gcl_au': '1.1.1002810158.1660711796',
            'appPopupShown': '1',
            '_gid': 'GA1.2.146019057.1660711796',
            'ver': '4.8.3-2697',
            'session_id': '99e9b255-7802-4b83-8578-8e10ce3d97d5',
            '_ga_5F0JRH5NNP': 'GS1.1.1660816546.8.1.1660818659.0.0.0',
            '_ga': 'GA1.1.11631034314210437782',
        }

        headers1 = {
            'authority': 'www.joom.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,kk;q=0.6,tr;q=0.5,uz;q=0.4',
            'cache-control': 'no-cache',
            # Requests sorts cookies= alphabetically
            # 'cookie': 'sticky_session_id=1660711793.946.2062.709724; accesstoken=SEV0001AHdJrpMIDBe1cZLmdmyapsRgfXKDorM1OKOQEjjDZ4_XlNzIBSgQsAX3s7g3VzA93vZFu_xAVqLmIbpmldNUQXtCX3mxLRHAVzVgMrdcaTDPK1SuFFIi40DDKrgvgVlxss7_AMYv4kHajyehrsqwMis9Zl6zhT5ecR-VqbayYWg_P79M2HGq6XS_n0v0JWwdnlG8EH8mVUp247JPLIYiof_mikypl2j14p3LRFOQu5ySO8z1vXQa4pYssU3nmf9Yskulpmtk3uWTgJnBivGoPlvEuXCfMFgLXJ-Bs1ACbBuubjbQHpY; accesstokenhash=-1k1qljf; refreshtoken=SEV0001AHdKrpMIDBcekBnCKP7UeJ_bRyaAVToSGcPx8AgwJwDXsX5BU0k5visHWC1VjT4clCwV07GPlhPkm4I0NDk0NNS5nYRVmjjOHTGpmaPkH608nsRaF5WBFJq5gI5Ng-a0Yff0-hAVjddHZHE7J0eU6vumwTo-g0yG-R-I5fx9rsjKlmJqt-zOnDahW53uvMTP-piSbpquWVOj; redirectLanguage=ru; userhash=-1e79qji; timezoneName=Asia%2FYekaterinburg; timezone=-300; trc=%7B%22sent%22%3Atrue%7D; _gcl_au=1.1.1002810158.1660711796; appPopupShown=1; _gid=GA1.2.146019057.1660711796; ver=4.8.3-2697; session_id=99e9b255-7802-4b83-8578-8e10ce3d97d5; _ga_5F0JRH5NNP=GS1.1.1660816546.8.1.1660818659.0.0.0; _ga=GA1.1.11631034314210437782',
            'pragma': 'no-cache',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'service-worker-navigation-preload': 'true',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36',
        }
        json_data = {
            'appearance': {},
            'pageToken': '1-gatjb250ZW50TGlzdIKhZqdyZXZpZXdzom1w0Rdw',
        }
        list_url = []
        response = requests.get(url, cookies=cookies, headers=headers1)
        # print(response.content)
        final_str = re.findall(r"(https:(\w|\\|\.)*original\.jpeg)", str(response.content), flags=re.M)
        # print('---')
        # print(final_str)
        for i in final_str:
            if (str(i[0]).replace('\\', '/').replace('u002F', '').replace('//', '/')) in list_url:
                pass
                # print('данная ссылка уже есть в списке')
            else:
                list_url.append((str(i[0]).replace('\\', '/').replace('u002F', '').replace('//', '/')))
        # print(list_url)
        images = list_url
    numimg = 0
    img_n = 1
    imgpars = 0

    def Mylti_parse(i):
        i = i.split('?')[0]
        r = requests.get(i)
        fileimg = 'parse' + str(numimg) + '.' + i.split('.')[-1]
        with open(fileimg, 'wb') as outfile:
            outfile.write(r.content)
        if fileimg != '.DS_Store':
            im = Image.open(fileimg)
            if im.size[1] >= 380 and im.size[0] >= 380:
                # imgpars = imgpars + 1
                # print(str(im.size[1]) + ' - h: ' + str(im.size[0]) + ' - w  ==' + i)
                if im.mode != 'RGB':
                    im = im.convert('RGB')
                im = im.filter(ImageFilter.EDGE_ENHANCE)
                im = im.filter(ImageFilter.GaussianBlur(radius=1))
                im = im.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
                if im_draw_window == 1:
                    draw = ImageDraw.Draw(im)
                    draw.line([(0, 0), (0, im.size[1]), (im.size[0], im.size[1]), (im.size[1], 0), (0, 0)],
                              fill=(col_r, col_g, col_b), width=150)
                    draw.text((im.size[0] / 2 - 150, 15), DOMAINNAME, font=font, fill=f'{a}')

                im.save('img/image_' + str(random.randint(1, 160)) + '.' + i.split('.')[-1])
            os.remove(fileimg)


    # threads = []
    num_img = 0
    for i in images:
        # i = image.get('src')
        if i[:4] == 'http':
            Mylti_parse(i)
            num_img += 1
        if num_img == 7:
            break
            # t = threading.Thread(target=Mylti_parse, args=(i,))
            # threads.append(t)
            # t.start()
                    # if img_n <= 9:
                    #     im.save('img/image_0' + str(img_n) + '.' + i.split('.')[-1])
                    # else:
                    #     im.save('img/image_' + str(img_n) + '.' + i.split('.')[-1])
                    # img_n += 1

            # numimg = numimg + 1
            # if imgpars >= 8:
            #     break
    # for t in threads:
    #     t.join()

    print('replace')
    all_class_html = {}

    classiki = re.findall(r"class=[\"](.*?)\"", htmltxt, flags=re.M)

    filelist.append('index.html')
    for i in os.listdir('css'):
        if '.DS_Store' not in i:
            filelist.append('css/'+i)

    for repa in classiki:
        if ' ' in repa:
            for i in repa.split(' '):
                newnamec = ''.join(choice(ascii_uppercase) for i in range(random.randint(9, 15)))
                all_class_html[i] = newnamec
        else:
            newnamec = ''.join(choice(ascii_uppercase) for i in range(random.randint(9, 15)))
            all_class_html[repa] = newnamec


    for k in filelist:
        # print(k)
        qw = ''
        with open(k, 'r') as outfile:
            qw = outfile.read()
        for i in all_class_html:
            qw = qw.replace(i, all_class_html[i])
        with open(k, 'w+') as outfile:
            outfile.write(qw)

    # -------------    RENAME FILES     -----------------


    for root, dirs, files in os.walk("."):
        for filename in files:
            if '.DS_Store' not in filename:
                root_n = root[2:]
                if root_n == 'css':
                    # list_rename_files['css'][root_n + '/' + filename] = prename + root_n + '/' + prename + filename
                    list_rename_files['css'][filename] =prename + filename
                elif root_n == 'img':
                    # list_rename_files['img'][root_n + '/' + filename] = prename + root_n + '/' + prename + filename
                    list_rename_files['img'][filename] =prename + filename
                else:
                    if filename.split('.')[1] == 'html':
                        if filename == 'index.html':
                            list_rename_files['html'][filename] = filename
                        else:
                            list_rename_files['html'][filename] = prename + filename


    os.renames('css', prename + 'css')
    os.renames('img', prename + 'img')

    for i1 in list_rename_files:
        # print(f'[{list_rename_files[i1]}]')
        for i in list_rename_files[i1]:
            if i1 != 'html':
                # print(i1+'/'+i + ' - ' + prename + i1 + '/' + list_rename_files[i1][i])
                os.renames(prename + i1 + '/' + i, prename + i1 + '/' + list_rename_files[i1][i])
            else:
                # print(i + ' - ' + list_rename_files[i1][i])
                os.renames(i, list_rename_files[i1][i])

                if i == 'index.html':
                    with open(list_rename_files[i1][i], 'r')as file:
                        html_r = file.read()
                    for dir in list_rename_files:
                        for file_name in list_rename_files[dir]:
                            if dir == 'img':
                                html_r = html_r.replace('imgr/rimage', prename + dir + '/' + list_rename_files[dir][file_name], 1)
                            elif dir == 'css':
                                html_r = html_r.replace(dir+'/'+file_name, prename + dir + '/' + list_rename_files[dir][file_name])
                            else:
                                html_r = html_r.replace(file_name, list_rename_files[dir][file_name])
                    with open(list_rename_files[i1][i], 'w') as file:
                        file.write(html_r)
                else:
                    with open(list_rename_files[i1][i], 'r')as file:
                        html_r = file.read()
                    html_r = html_r.replace('DOMAINNAME', DOMAINNAME)
                    with open(list_rename_files[i1][i], 'w') as file:
                        file.write(html_r)

    with open('index.html', 'r') as file:
        html_r = file.read()

    html_id = re.findall(r"id=[\"](.*?)\"", html_r, flags=re.M)
    for id_h in html_id:
        prename1 = ''.join(choice(ascii_uppercase) for i in range(random.randint(4, 6)))
        html_r = html_r.replace(id_h, f'{prename}-{prename1}-{str(random.randint(1, 50))}')

    html_id_list = re.findall(r"<section.*?id=[\"](.*?)\"", html_r, flags=re.M)
    with open(f'{prename}css/{prename}_style_1.css', 'r') as css_rep_id:
        text_css = css_rep_id.read()
    id_h_items = ''
    for id_h_item in html_id_list:
        id_h_items = f'{id_h_items}\n#{id_h_item}'+'{\n'+f'background-color: rgb({str(random.randint(240, 255))},{str(random.randint(240, 255))},{str(random.randint(240, 255))});'+'}\n'

    text_css = f'{text_css}\n{id_h_items}'
    with open(f'{prename}css/{prename}_style_1.css', 'w') as css_rep_id:
        css_rep_id.write(text_css)

    while 'imgr/rimage' in html_r:
        for dir in list_rename_files:
            for file_name in list_rename_files[dir]:
                html_r = html_r.replace('imgr/rimage', prename + dir + '/' + list_rename_files[dir][file_name], 1)
        # html_r = html_r.replace('imgr/rimage',prename+'img/' + random.choice(os.listdir(prename+'img')), 1)

    section_in_html = re.findall(r"(<section[\s\S]*?>[\s\S]*?<\/section>)", html_r, flags=re.M)
    section_in_html_pat = random.sample(section_in_html, len(section_in_html))
    for section_item in range(len(section_in_html)):
        html_r = html_r.replace(section_in_html[section_item], section_in_html_pat[section_item], 1)
    html_r = html_r.replace('NAMETOVAR', NAMETOVAR)

    # if lang_opt == "ru":
    #     html_r = html_r.replace('F0PR1_OLIC_POCA', random.choice(F0PR1_OLIC_POCA))
    #     html_r = html_r.replace('F0PR2_STAT0S', random.choice(F0PR2_STAT0S))
    #     html_r = html_r.replace('F0PR3_U5PX', random.choice(F0PR3_U5PX))
    #     html_r = html_r.replace('F0PR5_4UVSTV0', random.choice(F0PR5_4UVSTV0))
    #     html_r = html_r.replace('F0PR4_5TY1E', random.choice(F0PR4_5TY1E))
    #     html_r = html_r.replace('F0PR6_0R1GIN4L', random.choice(F0PR6_0R1GIN4L))
    #     html_r = html_r.replace('F0PR7_54MOD0', random.choice(F0PR7_54MOD0))
    #     html_r = html_r.replace('F0PR8_SHED3VR0', random.choice(F0PR8_SHED3VR0))
    #     html_r = html_r.replace('F0PR9_V1SHEDVR', random.choice(F0PR9_V1SHEDVR))
    # if lang_opt == "us":
    #     html_r = html_r.replace('F0PR1_OLIC_POCA', random.choice(F0PR1_ENOLIC_POCA))
    #     html_r = html_r.replace('F0PR2_STAT0S', random.choice(F0PR2_ENSTAT0S))
    #     html_r = html_r.replace('F0PR3_U5PX', random.choice(F0PR3_ENU5PX))
    #     html_r = html_r.replace('F0PR5_4UVSTV0', random.choice(F0PR5_EN4UVSTV0))
    #     html_r = html_r.replace('F0PR4_5TY1E', random.choice(F0PR4_EN5TY1E))
    #     html_r = html_r.replace('F0PR6_0R1GIN4L', random.choice(F0PR6_EN0R1GIN4L))
    #     html_r = html_r.replace('F0PR7_54MOD0', random.choice(F0PR7_EN54MOD0))
    #     html_r = html_r.replace('F0PR8_SHED3VR0', random.choice(F0PR8_ENSHED3VR0))
    #     html_r = html_r.replace('F0PR9_V1SHEDVR', random.choice(F0PR9_ENV1SHEDVR))
    # if lang_opt == "three_lang":
    #     html_r = html_r.replace('F0PR1_OLIC_POCA', random.choice(F0PR1_REOLIC_POCA))
    #     html_r = html_r.replace('F0PR2_STAT0S', random.choice(F0PR2_RESTAT0S))
    #     html_r = html_r.replace('F0PR3_U5PX', random.choice(F0PR3_REU5PX))
    #     html_r = html_r.replace('F0PR5_4UVSTV0', random.choice(F0PR5_RE4UVSTV0))
    #     html_r = html_r.replace('F0PR4_5TY1E', random.choice(F0PR4_RE5TY1E))
    #     html_r = html_r.replace('F0PR6_0R1GIN4L', random.choice(F0PR6_RE0R1GIN4L))
    #     html_r = html_r.replace('F0PR7_54MOD0', random.choice(F0PR7_RE54MOD0))
    #     html_r = html_r.replace('F0PR8_SHED3VR0', random.choice(F0PR8_RESHED3VR0))
    #     html_r = html_r.replace('F0PR9_V1SHEDVR', random.choice(F0PR9_REV1SHEDVR))
    # if lang_opt == "br":
    #     html_r = html_r.replace('F0PR1_OLIC_POCA', random.choice(F0PR1_PROLIC_POCA))
    #     html_r = html_r.replace('F0PR2_STAT0S', random.choice(F0PR2_PRSTAT0S))
    #     html_r = html_r.replace('F0PR3_U5PX', random.choice(F0PR3_PRU5PX))
    #     html_r = html_r.replace('F0PR5_4UVSTV0', random.choice(F0PR5_PR4UVSTV0))
    #     html_r = html_r.replace('F0PR4_5TY1E', random.choice(F0PR4_PR5TY1E))
    #     html_r = html_r.replace('F0PR6_0R1GIN4L', random.choice(F0PR6_PR0R1GIN4L))
    #     html_r = html_r.replace('F0PR7_54MOD0', random.choice(F0PR7_PR54MOD0))
    #     html_r = html_r.replace('F0PR8_SHED3VR0', random.choice(F0PR8_PRSHED3VR0))
    #     html_r = html_r.replace('F0PR9_V1SHEDVR', random.choice(F0PR9_PRV1SHEDVR))
    # if lang_opt == "es":
    #     html_r = html_r.replace('F0PR1_OLIC_POCA', random.choice(F0PR1_ESOLIC_POCA))
    #     html_r = html_r.replace('F0PR2_STAT0S', random.choice(F0PR2_ESSTAT0S))
    #     html_r = html_r.replace('F0PR3_U5PX', random.choice(F0PR3_ESU5PX))
    #     html_r = html_r.replace('F0PR5_4UVSTV0', random.choice(F0PR5_ES4UVSTV0))
    #     html_r = html_r.replace('F0PR4_5TY1E', random.choice(F0PR4_ES5TY1E))
    #     html_r = html_r.replace('F0PR6_0R1GIN4L', random.choice(F0PR6_ES0R1GIN4L))
    #     html_r = html_r.replace('F0PR7_54MOD0', random.choice(F0PR7_ES54MOD0))
    #     html_r = html_r.replace('F0PR8_SHED3VR0', random.choice(F0PR8_ESSHED3VR0))
    #     html_r = html_r.replace('F0PR9_V1SHEDVR', random.choice(F0PR9_ESV1SHEDVR))
    # if lang_opt == "el":
    #     html_r = html_r.replace('F0PR1_OLIC_POCA', random.choice(F0PR1_ELOLIC_POCA))
    #     html_r = html_r.replace('F0PR2_STAT0S', random.choice(F0PR2_ELSTAT0S))
    #     html_r = html_r.replace('F0PR3_U5PX', random.choice(F0PR3_ELU5PX))
    #     html_r = html_r.replace('F0PR5_4UVSTV0', random.choice(F0PR5_EL4UVSTV0))
    #     html_r = html_r.replace('F0PR4_5TY1E', random.choice(F0PR4_EL5TY1E))
    #     html_r = html_r.replace('F0PR6_0R1GIN4L', random.choice(F0PR6_EL0R1GIN4L))
    #     html_r = html_r.replace('F0PR7_54MOD0', random.choice(F0PR7_EL54MOD0))
    #     html_r = html_r.replace('F0PR8_SHED3VR0', random.choice(F0PR8_ELSHED3VR0))
    #     html_r = html_r.replace('F0PR9_V1SHEDVR', random.choice(F0PR9_ELV1SHEDVR))
    # if lang_opt == "de":
    #     html_r = html_r.replace('F0PR1_OLIC_POCA', random.choice(F0PR1_DEOLIC_POCA))
    #     html_r = html_r.replace('F0PR2_STAT0S', random.choice(F0PR2_DESTAT0S))
    #     html_r = html_r.replace('F0PR3_U5PX', random.choice(F0PR3_DEU5PX))
    #     html_r = html_r.replace('F0PR5_4UVSTV0', random.choice(F0PR5_DE4UVSTV0))
    #     html_r = html_r.replace('F0PR4_5TY1E', random.choice(F0PR4_DE5TY1E))
    #     html_r = html_r.replace('F0PR6_0R1GIN4L', random.choice(F0PR6_DE0R1GIN4L))
    #     html_r = html_r.replace('F0PR7_54MOD0', random.choice(F0PR7_DE54MOD0))
    #     html_r = html_r.replace('F0PR8_SHED3VR0', random.choice(F0PR8_DESHED3VR0))
    #     html_r = html_r.replace('F0PR9_V1SHEDVR', random.choice(F0PR9_DEV1SHEDVR))
    # if lang_opt == "tr":
    #     html_r = html_r.replace('F0PR1_OLIC_POCA', random.choice(F0PR1_TROLIC_POCA))
    #     html_r = html_r.replace('F0PR2_STAT0S', random.choice(F0PR2_TRSTAT0S))
    #     html_r = html_r.replace('F0PR3_U5PX', random.choice(F0PR3_TRU5PX))
    #     html_r = html_r.replace('F0PR5_4UVSTV0', random.choice(F0PR5_TR4UVSTV0))
    #     html_r = html_r.replace('F0PR4_5TY1E', random.choice(F0PR4_TR5TY1E))
    #     html_r = html_r.replace('F0PR6_0R1GIN4L', random.choice(F0PR6_TR0R1GIN4L))
    #     html_r = html_r.replace('F0PR7_54MOD0', random.choice(F0PR7_TR54MOD0))
    #     html_r = html_r.replace('F0PR8_SHED3VR0', random.choice(F0PR8_TRSHED3VR0))
    #     html_r = html_r.replace('F0PR9_V1SHEDVR', random.choice(F0PR9_TRV1SHEDVR))
    # if lang_opt == "pl":
    #     html_r = html_r.replace('F0PR1_OLIC_POCA', random.choice(F0PR1_PLOLIC_POCA))
    #     html_r = html_r.replace('F0PR2_STAT0S', random.choice(F0PR2_PLSTAT0S))
    #     html_r = html_r.replace('F0PR3_U5PX', random.choice(F0PR3_PLU5PX))
    #     html_r = html_r.replace('F0PR5_4UVSTV0', random.choice(F0PR5_PL4UVSTV0))
    #     html_r = html_r.replace('F0PR4_5TY1E', random.choice(F0PR4_PL5TY1E))
    #     html_r = html_r.replace('F0PR6_0R1GIN4L', random.choice(F0PR6_PL0R1GIN4L))
    #     html_r = html_r.replace('F0PR7_54MOD0', random.choice(F0PR7_PL54MOD0))
    #     html_r = html_r.replace('F0PR8_SHED3VR0', random.choice(F0PR8_PLSHED3VR0))
    #     html_r = html_r.replace('F0PR9_V1SHEDVR', random.choice(F0PR9_PLV1SHEDVR))
    # if lang_opt == "it":
    #     html_r = html_r.replace('F0PR1_OLIC_POCA', random.choice(F0PR1_ITOLIC_POCA))
    #     html_r = html_r.replace('F0PR2_STAT0S', random.choice(F0PR2_ITSTAT0S))
    #     html_r = html_r.replace('F0PR3_U5PX', random.choice(F0PR3_ITU5PX))
    #     html_r = html_r.replace('F0PR5_4UVSTV0', random.choice(F0PR5_IT4UVSTV0))
    #     html_r = html_r.replace('F0PR4_5TY1E', random.choice(F0PR4_IT5TY1E))
    #     html_r = html_r.replace('F0PR6_0R1GIN4L', random.choice(F0PR6_IT0R1GIN4L))
    #     html_r = html_r.replace('F0PR7_54MOD0', random.choice(F0PR7_IT54MOD0))
    #     html_r = html_r.replace('F0PR8_SHED3VR0', random.choice(F0PR8_ITSHED3VR0))
    #     html_r = html_r.replace('F0PR9_V1SHEDVR', random.choice(F0PR9_ITV1SHEDVR))
    with open('../script/language_all_list.json', 'r') as file_json:
        list_add_text_in_text_in_html = json.load(file_json)[lang_opt]["add_text_in_text_in_html"]
    for item in list_add_text_in_text_in_html:
        html_r = html_r.replace(item, random.choice(list_add_text_in_text_in_html[item]))

    if lang_opt == 'ru':
        ur = "https://www.bestrandoms.com/random-address-in-kz?quantity=1"
    elif lang_opt == 'el':
        ur = "https://www.bestrandoms.com/random-address-in-tr?quantity=1"
    else:
        ur = f"https://www.bestrandoms.com/random-address-in-{lang_opt}?quantity=1"
    # if lang_opt == "four_lang":
    #     ur = "https://www.bestrandoms.com/random-address-in-br?quantity=1"
    # elif lang_opt == "two_lang":
    #     ur = "https://www.bestrandoms.com/random-address-in-us?quantity=1"
    # elif lang_opt == "five_lang":
    #     ur = "https://www.bestrandoms.com/random-address-in-es?quantity=1"
    # elif lang_opt == "six_lang":
    #     ur = "https://www.bestrandoms.com/random-address-in-tr?quantity=1"
    # elif lang_opt == "seven_lang":
    #     ur = "https://www.bestrandoms.com/random-address-in-de?quantity=1"
    # elif lang_opt == "8_lang":
    #     ur = "https://www.bestrandoms.com/random-address-in-tr?quantity=1"
    # elif lang_opt == "9_lang":
    #     ur = "https://www.bestrandoms.com/random-address-in-pl?quantity=1"
    # elif lang_opt == "ten_lang":
    #     ur = "https://www.bestrandoms.com/random-address-in-it?quantity=1"
    # else:
    #     ur = "https://www.bestrandoms.com/random-address-in-kz?quantity=1"
    headers = {'user-agent': RandomUserPC}
    Response = requests.get(ur, headers=headers, verify=False)
    soup = BeautifulSoup(Response.content, 'html.parser')
    html_new = str(soup)
    itemsli = soup.find('div', {'class': 'content'})

    obl = re.findall(r">(.*?)<", str(itemsli), flags=re.M)
    new_list_adpess = []
    for i in obl:
        if len(i) > 2:
            new_list_adpess.append(i.replace(' ', ''))

    for a in new_list_adpess:
        # print(f"[{new_list_adpess.index(a)}] {a}")

        if 'Random address in ' in a:
            country = new_list_adpess[new_list_adpess.index(a) + 1]
            # print(country)
        if 'Street:' in a:
            Street = new_list_adpess[new_list_adpess.index(a) + 1]
            # print(Street)
        if 'City:' in a:
            City = new_list_adpess[new_list_adpess.index(a) + 1]
            # print(City)
        if 'Zip code' in a:
            Zip_code = new_list_adpess[new_list_adpess.index(a) + 1]
            # print(Zip_code)
        else:
            Zip_code = str(random.randint(100000,999999))
        if 'Country calling code' in a:
            Country_calling_code = new_list_adpess[new_list_adpess.index(a) + 1]
            # print(Country_calling_code)
        if 'Phone number' in a:
            Phone_number = new_list_adpess[new_list_adpess.index(a) + 1]
            # print(Phone_number)


    if restart_liv == 0:
        telcomp = f"{Country_calling_code} {Phone_number}"
        adress = f"{country} / [ZIP] {Zip_code} / {City} / {Street}"

    html_r = html_r.replace('COMPANYADRESS', adress)
    html_r = html_r.replace('TELEPHONECOMPANY', telcomp)
    html_r = html_r.replace('Joom', '')
    html_r = html_r.replace('joom', '')
    html_r = html_r.replace('JOOM', '')
    list_rename_files['font'] = list_font_files

    with open('index.html', 'w') as file:
        file.write(html_r)

    def LoadHost():
        ftp = FTP(ip,timeout=85)
        ftp.login(log, pas)

        def deleteAllFiles(ftp):
            for n in ftp.nlst():
                try:
                    if n not in ('.', '..'):
                        print('Working on..' + n)
                        try:
                            ftp.delete(n)
                            print('Deleted...' + n)
                        except Exception:
                            print(n + ' Not deleted, we suspect its a directory, changing to ' + n)
                            ftp.cwd(n)
                            deleteAllFiles(ftp)
                            ftp.cwd('..')
                            print('Trying to remove directory ..' + n)
                            ftp.rmd(n)
                            print('Directory, ' + n + ' Removed')
                except Exception:
                    print('Trying to remove directory ..' + n)
                    ftp.rmd(n)
                    print('Directory, ' + n + ' Removed')

        if hosting == 1:
            ftp.cwd(f'/www/{DOMAINNAME.lower()}')
        elif hosting == 0:
            ftp.cwd(f'/domains/{DOMAINNAME.lower()}/public_html')
        elif hosting == 2:
            ftp.cwd(f'/{DOMAINNAME.lower()}/htdocs/www')
        elif hosting == 3:
            ftp.cwd(f'/web/{DOMAINNAME.lower()}/public_html')
        elif hosting == 4:
            ftp.cwd(f'/public_html/{DOMAINNAME.lower()}')
        elif hosting == 5:
            ftp.cwd(f'/h213456064/{DOMAINNAME.lower()}')



        # if hosting != 2:
        deleteAllFiles(ftp)
        print('Done deleting all Files and Directories')
        for i1 in list_rename_files:
            if i1 != 'html':
                ftp.mkd(prename+i1)


        def Upload_Host(file_path, file):
            # ftp.storbinary('STOR ' + file_path, file)
            if file_path == 'html':
                file_way = file
            else:
                file_way = prename+file_path+'/'+file

            with open(file_way, 'rb') as file_to_upload:
                # file_i1 = file_to_upload.read()
                ftp.storbinary('STOR ' + file_way, file_to_upload)
            print(f'Файл {file} успешно загружен [patch: {file_way}]')



        for i1 in list_rename_files:
            for i in list_rename_files[i1]:
                Upload_Host(i1, list_rename_files[i1][i])


        # threads = []
        # ftp_download = {}
                # if i1 == 'html':
                #     file_way = list_rename_files[i1][i]
                # else:
                #     file_way = prename + i1 + '/' + list_rename_files[i1][i]
                # with open(file_way, 'rb') as file_ftp_download:
                #     ftp_download[file_way] = file_ftp_download

        # for i1 in list_rename_files:
        #     for i in list_rename_files[i1]:
        #         t = threading.Thread(target=Upload_Host, args=(i1, list_rename_files[i1][i]))
        #         threads.append(t)
        #         t.start()
        #
        # for t in threads:
        #     t.join()

        ftp.quit()
        ftp.close()


    if remove_patch == 1:
        LoadHost()


    if restart_liv == 0:
        with open('../script/pattern_list.json', 'r') as file:
            templates = json.load(file)
        load_templates = [
            DOMAINNAME,
            telcomp,
            adress,
            sph,
            url
        ]
        print(load_templates)
        templates.append(load_templates)
        with open('../script/pattern_list.json', 'w') as f:
            json.dump(templates, f, indent=4, ensure_ascii=False)
    os.chdir('../')

print('\n\n' + str(datetime.now() - start_time))

