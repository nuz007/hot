import requests,time
url = 'https://top.baidu.com/api/board?platform=wise&tab=realtime'
header = {
	'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36',
	'Host': 'top.baidu.com',
	'Accept': 'application/json, text/plain, */*',
	'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
	'Accept-Encoding': 'gzip, deflate, br',
	'Referer': 'https://top.baidu.com/board?tab=novel',
}
r = requests.get(url, header)
json_data=r.json()
top_content_list = json_data['data']['cards'][0]['topContent']
content_list = json_data['data']['cards'][0]['content']

sum2=top_content_list+content_list
sum=[]
for i in range(len(sum2)):
	del sum2[i]["appUrl"]
	del sum2[i]["hotChange"]
	try:del sum2[i]["hotTag"]
	except:pass
	try:del sum2[i]["hotTagImg"]
	except:pass
	del sum2[i]["img"]
	del sum2[i]["indexUrl"]
	del sum2[i]["query"]
	del sum2[i]["rawUrl"]
	del sum2[i]["show"]
	del sum2[i]["url"]
for i in sum2:
	tmp=[]
	for j in i:tmp.insert(0,i[j])
	tmp[0]='<a href="https://cn.bing.com/search?q={}">{}</a>'.format(tmp[0],tmp[0])
	sum.append(tmp)

for i in sum:i[1]=int(i[1])+2
sum[0][1]=1
def dict_to_table(ks, vs):
    th = ''
    for name in ks:
        th = th + '<th>' + name + '</th>'
    trth = '<tr>' + th + '</tr>'

    trtd = ''
    for tds in vs:
        tdss = ''
        for td in tds:
            tdss = tdss + '<td>' + str(td) + '</td>'
        tdss = '<tr>' + tdss + '</tr>'
        trtd = trtd + tdss

    return '<table>' + trth + trtd + '</table>'

for i in range(len(sum)):
	pass
	tmp=sum[i][1]
	sum[i][1]=sum[i][0]
	sum[i][0]=tmp

sum.sort(key=lambda x:x[0])
sum=sum[0:-1]
sx=dict_to_table(["排行","热点","热度","详细描述"], sum).replace("\n","").replace("  "," ")
xs="<html><head><title>热搜榜</title><style>@media screen and (max-width: 1024px){td:nth-child(4),th:nth-child(4){display: none}}*{color:#ffffff}body{background-color:#000000}a{color:#ccddff}table{border-collapse:collapse;width:100%;margin-bottom:20px}th{border:0px;background-color:#444444;padding:5px 9px;font-size:14px;font-weight:normal;text-align:center}td{border:0px;padding:5px 9px;font-size:12px;font-weight:normal;text-align:center;word-break:break-all}tr{background-color:#222222}th:nth-child(1),td:nth-child(1),th:nth-child(3),td:nth-child(3){width:60px}</style></head><body><h1>热搜排行榜</h1><br/><span>更新时间: <br/><span id=\"time\"></span></span><br/>"+sx+"</body><footer><script>var time=new Date("+str(int(time.time()*1000))+");document.getElementById(\"time\").innerHTML=time</script></footer></html>"
with open("./index.html","w",encoding="utf-8") as xxxx:xxxx.write(xs)
