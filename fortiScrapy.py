#參考網站
#https://ithelp.ithome.com.tw/articles/10204709
#https://zx2515296964.medium.com/python-%E6%95%99%E5%AD%B8-%E7%B0%A1%E5%96%AE%E5%B9%BE%E6%AD%A5%E9%A9%9F-%E8%AE%93%E4%BD%A0%E8%BC%95%E9%AC%86%E7%88%AC%E8%9F%B2-928a816051c1
#https://kknews.cc/zh-tw/code/5g2nb22.html
#pip install requests
#pip install bs4
#pip install lxml
import requests
from lxml import etree
import re
FortiVersion = input(
'''
please type in FortiVersion:
example:6.0.11
''')
#totalVersion_Split = FortiVersion.split('.',-1)
#totalVersion = totalVersion_Split[0] + '.' + totalVersion_Split[1]
#url = 'https://docs.fortinet.com/product/fortigate/'+totalVersion
#r = requests.get(url)
release_note = 'https://docs.fortinet.com/document/fortigate/'+FortiVersion+'/fortios-release-notes'
r = requests.get(release_note)
content = r.content.decode()
html = etree.HTML(content)

#know_issue_href = html.xpath('//a[text()="Known Issues"]/@href')
Know_issue_href = html.xpath('//a[contains(@href,"known-issues")]/@href')
Know_issue = Know_issue_href[0]
Know_issue_url = 'https://docs.fortinet.com'+Know_issue
r = requests.get(Know_issue_url)
from lxml import html
tree = html.fromstring(r.content)
trs = tree.xpath('//table[contains(@class,"TableStyle-FortinetTable")]//text()')
x = '\r\n     '
a = []
for i in range(len(trs)):
      if x not in trs[i]:
          a.append(trs[i])

BugID = 'Bug ID'
aa = []
for i in range(len(a)):
      if BugID not in a[i]:
         aa.append(a[i])

a = []
Description = 'Description'
for i in range(len(aa)):
      if Description not in aa[i]:
         a.append(aa[i])

aa = []
y = '\r\n'
for i in range(len(a)):
      if y in a[i]:
            aa.append(''.join(a[i].splitlines()))
      else:
            aa.append(a[i])

a = aa

Bug_ID_list = []
for i in range(len(a)):
      if re.match(r"([1-9][0-9][0-9][0-9][0-9][0-9])" , a[i]):
           Bug_ID_list.append(i)

Bug_ID = []
for i in range(len(a)):
      if re.match(r"([1-9][0-9][0-9][0-9][0-9][0-9])" , a[i]):
           Bug_ID.append(a[i])

BugInformation = []
i = 0
j = 0
while i < (len(Bug_ID_list)-1):
      x = 0
      x = Bug_ID_list[(i+1)] - Bug_ID_list[i]
      j = Bug_ID_list[i]
      if j == 0 and x > 0:
           aString = []
           for j in range(x-1):
                 j += 1
                 aString.append(a[j])
           BugInformation.append(''.join(aString))
      elif i != 0 and x > 0:
           bString = []
           x = Bug_ID_list[i] + x
           while j < (x-1):
                 j += 1
                 bString.append(a[j])
           BugInformation.append(''.join(bString))
      i += 1
#上述==下面這一大串
#BugInformation = []
#while i < (len(Bug_ID_list)-1):
#      if Bug_ID_list[(i+1)] - Bug_ID_list[i] == 2:
#         BugInformation.append(a[(Bug_ID_list[i]+1)])
#      elif Bug_ID_list[(i+1)] - Bug_ID_list[i] == 3:
#         BugInformation.append(a[(Bug_ID_list[i]+1)]+a[(Bug_ID_list[i]+2)])
#      elif Bug_ID_list[(i+1)] - Bug_ID_list[i] == 4:
#         BugInformation.append(a[(Bug_ID_list[i]+1)]+a[(Bug_ID_list[i]+2)]+a[(Bug_ID_list[i]+3)])
#      elif Bug_ID_list[(i+1)] - Bug_ID_list[i] == 5:
#         BugInformation.append(a[(Bug_ID_list[i]+1)]+a[(Bug_ID_list[i]+2)]+a[(Bug_ID_list[i]+3)]+a[(Bug_ID_list[i]+4)])
#      elif Bug_ID_list[(i+1)] - Bug_ID_list[i] == 6:
#         BugInformation.append(a[(Bug_ID_list[i]+1)]+a[(Bug_ID_list[i]+2)]+a[(Bug_ID_list[i]+3)]+a[(Bug_ID_list[i]+4)]+a[(Bug_ID_list[i]+5)])
#      elif Bug_ID_list[(i+1)] - Bug_ID_list[i] == 7:
#         BugInformation.append(a[(Bug_ID_list[i]+1)]+a[(Bug_ID_list[i]+2)]+a[(Bug_ID_list[i]+3)]+a[(Bug_ID_list[i]+4)]+a[(Bug_ID_list[i]+5)]+a[(Bug_ID_list[i]+6)])
#      elif Bug_ID_list[(i+1)] - Bug_ID_list[i] == 8:
#         BugInformation.append(a[(Bug_ID_list[i]+1)]+a[(Bug_ID_list[i]+2)]+a[(Bug_ID_list[i]+3)]+a[(Bug_ID_list[i]+4)]+a[(Bug_ID_list[i]+5)]+a[(Bug_ID_list[i]+6)]+a[(Bug_ID_list[i]+7)])
#      elif Bug_ID_list[(i+1)] - Bug_ID_list[i] == 9:
#         BugInformation.append(a[(Bug_ID_list[i]+1)]+a[(Bug_ID_list[i]+2)]+a[(Bug_ID_list[i]+3)]+a[(Bug_ID_list[i]+4)]+a[(Bug_ID_list[i]+5)]+a[(Bug_ID_list[i]+6)]+a[(Bug_ID_list[i]+7)]+a[(Bug_ID_list[i]+8)])
#      elif Bug_ID_list[(i+1)] - Bug_ID_list[i] == 10:
#         BugInformation.append(a[(Bug_ID_list[i]+1)]+a[(Bug_ID_list[i]+2)]+a[(Bug_ID_list[i]+3)]+a[(Bug_ID_list[i]+4)]+a[(Bug_ID_list[i]+5)]+a[(Bug_ID_list[i]+6)]+a[(Bug_ID_list[i]+7)]+a[(Bug_ID_list[i]+8)]+a[(Bug_ID_list[i]+9)])
#      i += 1


v = Bug_ID_list[len(Bug_ID_list)-1]
EndString = []
while v < len(a) - 1:
      v += 1
      EndString.append(a[v])


BugInformation.append(''.join(EndString))

for i in range(len(Bug_ID_list) // int(2) ):
      print('BugID:', Bug_ID[i])
      print('BugDescription:', BugInformation[i])






#if (len(a)) - max(Bug_ID_list) == 2:
#      BugInformation.append(a[(Bug_ID_list[(len(Bug_ID_list)-1)])+1])
#elif (len(a)) - max(Bug_ID_list) == 3:
#      BugInformation.append(a[(Bug_ID_list[(len(Bug_ID_list)-1)])+1] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+2])
#elif (len(a)) - max(Bug_ID_list) == 4:
#      BugInformation.append(a[(Bug_ID_list[(len(Bug_ID_list)-1)])+1] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+2] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+3])
#elif (len(a)) - max(Bug_ID_list) == 5:
#      BugInformation.append(a[(Bug_ID_list[(len(Bug_ID_list)-1)])+1] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+2] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+3] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+4])
#elif (len(a)) - max(Bug_ID_list) == 6:
#      BugInformation.append(a[(Bug_ID_list[(len(Bug_ID_list)-1)])+1] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+2] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+3] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+4] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+5])
#elif (len(a)) - max(Bug_ID_list) == 7:
#      BugInformation.append(a[(Bug_ID_list[(len(Bug_ID_list)-1)])+1] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+2] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+3] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+4] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+5] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+6])
#elif (len(a)) - max(Bug_ID_list) == 8:
#      BugInformation.append(a[(Bug_ID_list[(len(Bug_ID_list)-1)])+1] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+2] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+3] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+4] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+5] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+6] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+7])
#elif (len(a)) - max(Bug_ID_list) == 9:
#      BugInformation.append(a[(Bug_ID_list[(len(Bug_ID_list)-1)])+1] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+2] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+3] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+4] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+5] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+6] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+7] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+8])
#elif (len(a)) - max(Bug_ID_list) == 10:
#     BugInformation.append(a[(Bug_ID_list[(len(Bug_ID_list)-1)])+1] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+2] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+3] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+4] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+5] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+6] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+7] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+8] + a[(Bug_ID_list[(len(Bug_ID_list)-1)])+9])
