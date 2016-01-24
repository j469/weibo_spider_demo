# Weibo spider with face detection

----------

## 1. Introduction
This script can automaticlly download all the tweets and images from [Sina Weibo(chinese version of twitter&instagram)][1] of one user or a huge set of users. The searching and downloading process is done in multi-thread way, and it will report if a specific images is not available for downloading. After searching and downloading, there will be a face detection process( using API from service provider [Face++][2]) and put the pictures with faces into another folder, so you don't need the hassle to click next-picture next-picture to see how she/he really looks like. Imagine what you wanna do with this script! :)

I'm currently working on the algorithm to detect what faces I love most, to improve the efficiency of finding cuties. For now, I'm using the relative position of one's eyes, nose abd mouth. Hopefully it will drop some 'less preferred' pictures, but it's hard to tell which one is better from all the 'normal pictures'. If you have any idea about how to improve such an algorithm, please share with me!

**Note:** This program is a free software. It comes without any warranty, to the extent permitted by applicable law. You can redistribute it and/or modify it under the terms of Do Whatever You Want. However, I suggest DON'T save any others' pictures to your own disks or use others' pictures to do something bad, it's your own responsibility for breaking any law.

----------

## 2. Usage

### 2.1. Typical Input
#### 2.1.1 Single user:

    $ python weibo_spider.py

After the promot, type the user_id (int):

    Please type the user_id you want: 


#### 2.1.2 Input file:
You can generate a file with lots of user_ids, one per line. The script will read in the file, and search for all of them.

    $ python weibo_spider.py <FILE, or relative path>

### 2.2 Typical Output
#### 2.2.1 Screen shot of one example

    $ python weibo_spider.py
    Please inpu the user_id you want: 5519184134
    Launching 5519184134...
    Searching done. Total: 171 records.
    Saving images for 5519184134...
    Download fails: 57
    Download fails: 60
    Download fails: 70
    Download fails: 81
    Download fails: 101
    Downloads done. Total: 119 images.

#### 2.2.2 Storage location
This script will generate a folder in the same directory with the script, named after the user_id. In this folder, there's a 'text.txt' consists the plain text of all tweets, a 'image.txt' consists the urls of all images, and two sub folders 'images' and 'face_images' of original size images. 

### 2.3 Screenshot
![Screen shot one][3]

----------

## 3. Some thinking
### 3.1 about efficiency
Since desktop version Weibo and their mobile apps have several anti-scraping mechanism, I grab the page from their wap site, which doesn't have robot_test. However, there's still a limit of how fast you request a new page, which is about one request per second. So unless you have multiple accounts & using different IPs for these accounts, this script will not have a fancy efficiency.

### 3.2 about anti-scraping
Weibo has some pretty solid anti-scraping technics in their website and their APPs, including rate limiting, captcha tests(read text from a picture), blocking IP after too many requests. However, they don't have such many tools used in their 10+ years old WAP site, because of whatever reasons(I think no one still maintains that codes nowadays). As Cannikin Law, the chain is only as strong as the weakest link. Any company including Weibo should imporve all of their products to the same level of security, or shut down the services that too old to be updated.


----------

Last update: 2016/1/24

  [1]: https://en.wikipedia.org/wiki/Sina_Weibo
  [2]: http://www.faceplusplus.com/
  [3]: https://github.com/j469/weibo_spider_demo/blob/master/screenshot_1.png