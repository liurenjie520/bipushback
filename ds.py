import sys
import time
import ifzf
import requests
import re
import os
import json
from datetime import datetime, timedelta


url='https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history?host_uid=19241861&offset_dynamic_id=0&need_top=1&platform=web'
imgpost = 'https://push.bot.qw360.cn/send/e54011f0-f9aa-11eb-806f-9354f453c154'
headers = {'Content-Type': 'application/json'}

response=requests.get(url=url)
result = json.loads(str(response.content, 'utf-8'))
# dt=html.json()['data']['cards'][0]
data = result['data']
# item = data['cards'][0]['card']
# item = data['cards'][0]
# dynamic_id = item['desc']['dynamic_id']
#
# uname = item['desc']['user_profile']['info']['uname']

# dynamic_id=str(dynamic_id)
# print(item)
if os.path.getsize('wbIds.txt') > 0:
    print("no initialization")
else:
    with open('wbIds.txt', 'a') as f:
        for i in data['cards']:
            jk = i['desc']['dynamic_id']
            f.write(str(jk) + '\n')

        print("Initialization succeeded")




itemIds = []
with open('wbIds.txt','r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        itemIds.append(line)
    for i in data['cards']:
        dk=i['desc']
        cardss=i['card']

        jk = i['desc']['dynamic_id']


        if str(jk) not in itemIds:
            print("New data, start writing")
            with open('wbIds.txt', 'a') as f:
                f.write(str(jk) + '\n')
                print(jk)
                uname = dk['user_profile']['info']['uname']
                dynamic_type = dk['type']
                timestamp = dk['timestamp']
                dynamic_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
                print(uname)
                print(dynamic_type)
                print(dynamic_time)
                dynamic_id = dk['dynamic_id']
                lj = 'https://m.bilibili.com/dynamic/' + str(dynamic_id)
                now = datetime.now() + timedelta(hours=8)

                dc = now.strftime("%H:%M:%S")
                tzshj = dc
                print("github通知时间是：" + tzshj)
                d1 = now.strftime('%Y-%m-%d %H:%M:%S')
                print("github时间d1是：" + d1)
                d3 = datetime.strptime(d1, '%Y-%m-%d %H:%M:%S')
                print(d3)

                d2 = datetime.strptime(dynamic_time, "%Y-%m-%d %H:%M:%S")

                timedelay = d3 - d2

                timedelay = str(timedelay)
                print(timedelay)



                # print(type(content))
                # print(content)
                if dynamic_type == 1:
                    # 转发动态
                    content = json.loads(cardss)
                    content = content['item']
                    zfnr = content['content']
                    zfnr=str(zfnr)
                    orig_dy_id=content['orig_dy_id']


                    lj = 'https://m.bilibili.com/dynamic/' + str(orig_dy_id)

                    diaoifzf = ifzf.ifzf(orig_dy_id)
                    diaoifzf = str(diaoifzf)


                    fasongneir = '@' + uname + '\n' + dynamic_time + ' ' + '\n' + '▷' +'类型'+ str(dynamic_type) + ' ' + '\n' +  '▷' + '推送时间：' + tzshj + ' ' + '\n' + '▷' + '延时推送：' + timedelay + ' ' + '\n' + '▷' + '原博链接：' + lj+ ' ' + '\n' + '------------------------' + '\n' + zfnr + '\n' + '------------------------'+ '\n' + '------------------------' + '\n' + diaoifzf + '\n' + '------------------------'
                    print(fasongneir)
                    postdata = json.dumps({"msg": fasongneir})
                    time.sleep(2)
                    repp = requests.post(url=imgpost, data=postdata, headers=headers)
                    print(repp)











                elif dynamic_type == 2:
                    # 图文动态

                    content = json.loads(cardss)
                    content = content['item']
                    neirong = content['description']
                    pic_url = content['pictures']
                    pictures_count=content['pictures_count']

                    print(pictures_count)
                    print(dynamic_id)

                    fasongneir = '@' + uname + '\n' + dynamic_time + ' ' + '\n' + '▷' + '类型' + str(
                        dynamic_type) + ' ' + '\n' + '▷' + '推送时间：' + tzshj + ' ' + '\n' + '▷' + '延时推送：' + timedelay + ' ' + '\n' + '▷' + '图片数量：' + str(pictures_count) + ' '+'张' + '\n'+'▷' + '原博链接：' + lj + ' ' + '\n' + '------------------------' + '\n' + str(neirong) + '\n'
                    print(fasongneir)
                    postdata = json.dumps({"msg": fasongneir})
                    time.sleep(2)
                    repp = requests.post(url=imgpost, data=postdata, headers=headers)
                    print(repp)


                    for pic in pic_url:
                        zlpic_url=pic['img_src']

                        print(pic['img_src'])
                        postdata = json.dumps({"msg": {"type": "image", "url": "%s" % zlpic_url}})
                        repp = requests.post(url=imgpost, data=postdata, headers=headers)
                        print(repp)


                elif dynamic_type == 4:
                    # 文字动态
                    content = json.loads(cardss)
                    content = content['item']

                    wenzi = content['content']

                    print(wenzi)
                    fasongneir = '@' + uname + '\n' + dynamic_time + ' ' + '\n' + '▷' + '类型' + str(
                        dynamic_type) + ' ' + '\n' + '▷' + '推送时间：' + tzshj + ' ' + '\n' + '▷' + '延时推送：' + timedelay + ' ' + '\n'+ '▷' + '原博链接：' + lj + ' ' + '\n' + '------------------------' + '\n' + str(wenzi) + '\n'
                    print(fasongneir)
                    postdata = json.dumps({"msg": fasongneir})
                    time.sleep(2)
                    repp = requests.post(url=imgpost, data=postdata, headers=headers)
                    print(repp)

                elif dynamic_type == 8:
                    # 投稿动态
                    content = json.loads(cardss)
                    tgtlttle = content['title']
                    tgpic_url = content['pic']
                    tgpic_url=str(tgpic_url)
                    av=dk['rid_str']
                    av='av'+str(av)
                    lj='https://www.bilibili.com/video/'+av
                    print(tgtlttle)
                    print(tgpic_url)
                    fasongneir = '@' + uname + '\n' + dynamic_time + ' ' + '\n' + '▷' + '类型' + str(dynamic_type) + ' ' + '\n' + '▷' + '推送时间：' + tzshj + ' ' + '\n' + '▷' + '延时推送：' + timedelay + ' ' + '\n'  + '▷' + '原博链接：' + lj + ' ' + '\n' + '------------------------' + '\n' + str(tgtlttle) + '\n'
                    print(fasongneir)
                    postdata = json.dumps({"msg": fasongneir})
                    time.sleep(2)
                    repp = requests.post(url=imgpost, data=postdata, headers=headers)
                    print(repp)
                    time.sleep(2)
                    # zlpic_url = pic['img_src']

                    # print(pic['img_src'])
                    postdata = json.dumps({"msg": {"type": "image", "url": "%s" % tgpic_url}})
                    repp2 = requests.post(url=imgpost, data=postdata, headers=headers)
                    print(repp2)


                elif dynamic_type == 64:
                    # 专栏动态
                    content = json.loads(cardss)
                    zltitle = content['title']
                    zlpic_url = content['image_urls'][0]
                    zlpic_url=str(zlpic_url)
                    print(zltitle)
                    print(zlpic_url)
                    fasongneir = '@' + uname + '\n' + dynamic_time + ' ' + '\n' + '▷' + '类型' + str(
                        dynamic_type) + ' ' + '\n' + '▷' + '推送时间：' + tzshj + ' ' + '\n' + '▷' + '延时推送：' + timedelay + ' ' + '\n' + '▷' + '原博链接：' + lj + ' ' + '\n' + '------------------------' + '\n' + str(
                        zltitle) + '\n'
                    print(fasongneir)
                    postdata = json.dumps({"msg": fasongneir})
                    time.sleep(2)
                    repp = requests.post(url=imgpost, data=postdata, headers=headers)
                    print(repp)
                    time.sleep(2)
                    # zlpic_url = pic['img_src']

                    # print(pic['img_src'])
                    postdata = json.dumps({"msg": {"type": "image", "url": "%s" % zlpic_url}})
                    repp2 = requests.post(url=imgpost, data=postdata, headers=headers)
                    print(repp2)
                print("Write OK")







# with open('wbIds.txt', 'a') as f:
#     f.write(dynamic_id+ '\n')
