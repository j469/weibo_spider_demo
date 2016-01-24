#-*-coding:utf8-*-

import re
import string
import sys
import os
import urllib
import urllib2
from bs4 import BeautifulSoup
import requests
from lxml import etree

reload(sys) 
sys.setdefaultencoding('utf-8')

# cookie for wap version weibo.cn
cookie = {"Cookie": "_T_WM=b23e51ef977dfb74ed77c6a7126a5fbb;SUHB=09Ps4BQvSrXaY8;SUB=_2A257muRvDeTxGeRJ61AV9izFyj2IHXVZZIwnrDV6PUJbrdANLWX_kW1LHesVZzNszhYoDG8x9qha2fZvKB4cUw..;gsid_CTandWM=4ul15a8413ejW78UIGCMFbl26eH"}

# input a file as parameter; or type in the user_id you want in command line
user_id_list = []
if(len(sys.argv)>=2):
  with open(sys.argv[1]) as f:
    for line in f:
      user_id = int(line)
      user_id_list.append(user_id)
else:
    user_id = (int)(raw_input(u"Please inpu the user_id you want: "))
    user_id_list.append(user_id)

# iterate the user_id_list
for user_id in user_id_list:

  # store to local directory
  directory = "./%s"%user_id
  if not os.path.exists(directory):
    os.makedirs(directory)
  else: # if already exist, just ignore this one
    print u'%s already exists.'%user_id
    break

  # Weibo url for this user
  url = 'http://weibo.cn/%d'%user_id

  html = requests.get(url, cookies = cookie).content
  selector = etree.HTML(html)
  pageNum = (int)(selector.xpath('//input[@name="mp"]')[0].attrib['value'])
  if pageNum > 50:
    pageNum = 50

  result = "" 
  urllist_set = set()
  word_count = 1
  image_count = 1

  print u'Launching %s...'%user_id

  # load pages
  for page in range(1,pageNum+1):

    # lxml pages
    url = 'http://weibo.cn/u/%d?filter=1&page=%d'%(user_id,page) 
    lxml = requests.get(url, cookies = cookie).content
    print u'Loading page number%s' %page

    # texts
    selector = etree.HTML(lxml)
    content = selector.xpath('//span[@class="ctt"]')
    for each in content:
      text = each.xpath('string(.)')
      if word_count>=4:
        text = "%d :"%(word_count-3) +text+"\n\n"
      else :
        text = text+"\n\n"
      result = result + text
      word_count += 1

    # images
    soup = BeautifulSoup(lxml, "lxml")
    urllist = soup.find_all('a',href=re.compile(r'^http://weibo.cn/mblog/oripic',re.I))
    first = 0
    for imgurl in urllist:
      urllist_set.add(requests.get(imgurl['href'], cookies = cookie).url)
      image_count +=1

  # write to text file
  fo = open("./%s/text.txt"%user_id, "wb")
  fo.write(result)
  word_path=os.getcwd()+'/%d'%user_id
  # write image url to file
  link = ""
  fo2 = open("./%s/image.txt"%user_id, "wb")
  for eachlink in urllist_set:
    link = link + eachlink +"\n"
  fo2.write(link)

  print u'Searching done. Total: %d records.'%(word_count-4)
  print u'Now saving to local directory...'

  if not urllist_set:
    print u'No downloads'
  else:
    image_path = "./%s/images"%user_id
    if not os.path.exists(image_path):
      os.makedirs(image_path)

    face_image_path = "./%s/face_images"%user_id
    if not os.path.exists(face_image_path):
      os.makedirs(face_image_path)

    x=1
    for imgurl in urllist_set:
      temp= image_path + '/%s.jpg' %x
      try:
        urllib.urlretrieve(urllib2.urlopen(imgurl).geturl(),temp)
      except:
        print u"Download fails: %s" %x
      x+=1
    print u'Downloads done. Total: %d images.'%(image_count-1)