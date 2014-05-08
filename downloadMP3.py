#!/usr/bin/env python
#-*- coding: utf-8 -*-
#baidu音乐网页架构变了，不好使用了
import sys
import os
import re
import urllib2

cwd = os.getcwd()
lc = sys.getfilesystemencoding()
downdir = cwd+os.sep+'Music_'
print '\n下载目录为：',downdir,'\n'



if not os.path.isdir(downdir):
    print '下载目录不存在，正在创建目录：',downdir
    os.mkdir(downdir)

if os.path.isfile(sys.argv[1]):
    list_file = sys.argv[1]
else:
    list_file = cwd + os.sep + sys.argv[1]

print '歌曲文件路径为',list_file
try:
    f = file(list_file,'r')
    print '打开歌曲列表成功！'
except IOError:
    print '歌典列表打开失败，请检查文件是否存在!'
    sys.exit()

for eachLine in f:
    song = eachLine.strip()
    if not song:
        continue
url="http://music.baidu.com/search?key=%s$$" % urllib2.quote(song.decode(lc).encode('gbk'))

xmlf = urllib2.urlopen(url)
outfile = file('temp.xml','w')
for line in xmlf:
    outfile.write(line)
outfile.close()
in_file = file('temp.xml')
txt = in_file.read()
in_file.close()
os.remove('temp.xml')

rex1 = u'()(http://.+?/.+?\..+?)()'
rex2 = u'()(.+?\..+?)()'
l1 = re.findall(rex1,txt)
l2 = re.findall(rex2,txt)

url_list = []

for i in range(len(l1)):
    temp_list = re.split('/',l1[i][1])
temp_list.pop()
temp_list.append(l2[i][1])
down_url = '/'.join(temp_list)
url_list.append(down_url)

for i in range(len(url_list)):

    extname = url_list[i].split('.')[-1] #跳过非MP3的类型
    if extname.upper() == 'MP3':
        mp3file = downdir+os.sep+song+'.mp3'
    if os.path.isfile(mp3file):
        print '\n文件已经存在，转到下一首\n'
    break
    print '\n正在下载歌曲：',song,'…\n'
    cmd = 'wget %s -c -t 3 -O %s' % (url_list[i],downdir+os.sep+song+'.mp3')
    os.system(cmd)
    if os.path.getsize(mp3file) < 500000L: #小于500K的文件将被删除，并重新下载
        print '\n文件过小，可能是目标网站有限制，将尝试下一个链接\n'
        os.remove(mp3file)
    else:
        print song,'下载完毕！'
    break
    print '下载完毕！'
