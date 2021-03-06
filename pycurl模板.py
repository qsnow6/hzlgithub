#coding:utf-8
#Pycurl通用模板 
import pycurl
import StringIO
import random
#从uaList中随机获取一个ua
def getUA():
    uaList = [
        'Mozilla/4.0+(compatible;+MSIE+6.0;+Windows+NT+5.1;+SV1;+.NET+CLR+1.1.4322;+TencentTraveler)',
        'Mozilla/4.0+(compatible;+MSIE+6.0;+Windows+NT+5.1;+SV1;+.NET+CLR+2.0.50727;+.NET+CLR+3.0.4506.2152;+.NET+CLR+3.5.30729)',
        'Mozilla/5.0+(Windows+NT+5.1)+AppleWebKit/537.1+(KHTML,+like+Gecko)+Chrome/21.0.1180.89+Safari/537.1',
        'Mozilla/4.0+(compatible;+MSIE+6.0;+Windows+NT+5.1;+SV1)',
        'Mozilla/5.0+(Windows+NT+6.1;+rv:11.0)+Gecko/20100101+Firefox/11.0',
        'Mozilla/4.0+(compatible;+MSIE+8.0;+Windows+NT+5.1;+Trident/4.0;+SV1)',
        'Mozilla/4.0+(compatible;+MSIE+8.0;+Windows+NT+5.1;+Trident/4.0;+GTB7.1;+.NET+CLR+2.0.50727)',
        'Mozilla/4.0+(compatible;+MSIE+8.0;+Windows+NT+5.1;+Trident/4.0;+KB974489)',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"
    ]
    newUa = random.choice(uaList)
    return newUa
def getHtml(url,headers):
	c = pycurl.Curl()							#通过curl方法构造一个对象
	c.setopt(pycurl.URL, url)					#设置要访问的URL
	c.setopt(pycurl.FOLLOWLOCATION, True)		#自动进行跳转抓取
	c.setopt(pycurl.MAXREDIRS,5)				#设置最多跳转多少次
	c.setopt(pycurl.CONNECTTIMEOUT, 60)			#设置链接超时
	c.setopt(pycurl.TIMEOUT,120)				#下载超时
	c.setopt(pycurl.ENCODING, 'gzip,deflate')	#处理gzip内容，有些傻逼网站，就算你给的请求没有gzip，它还是会返回一个gzip压缩后的网页
	c.fp = StringIO.StringIO()					#构造StringIO实例
	c.setopt(pycurl.HTTPHEADER,headers)			#传入请求头
	c.setopt(pycurl.POST, 1)					#默认get
	c.setopt(pycurl.POSTFIELDS, data)			#传入POST数据
	c.setopt(c.WRITEFUNCTION, c.fp.write)		#字符串写入缓存
	c.perform()									#完成	
	html = c.fp.getvalue()						#返回源代码
	return html
headers = [
		"Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"Accept-Encoding:gzip, deflate, br",
		"Accept-Language:zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
		"Connection:keep-alive",
		"Host:www.baidu.com",
		"User-Agent:%s"%get getUA()
]
'''
pycurl.NAMELOOKUP_TIME 域名解析时间
pycurl.CONNECT_TIME 远程服务器连接时间
pycurl.PRETRANSFER_TIME 连接上后到开始传输时的时间
pycurl.STARTTRANSFER_TIME 接收到第一个字节的时间
pycurl.TOTAL_TIME 上一请求总的时间
pycurl.REDIRECT_TIME 如果存在转向的话，花费的时间
pycurl.HTTP_CODE HTTP 响应代码
pycurl.REDIRECT_COUNT 重定向的次数
pycurl.SIZE_UPLOAD 上传的数据大小
pycurl.SIZE_DOWNLOAD 下载的数据大小
pycurl.SPEED_UPLOAD 上传速度
pycurl.HEADER_SIZE 头部大小
pycurl.REQUEST_SIZE 请求大小
pycurl.CONTENT_LENGTH_DOWNLOAD 下载内容长度
pycurl.CONTENT_LENGTH_UPLOAD 上传内容长度
pycurl.CONTENT_TYPE 内容的类型
pycurl.RESPONSE_CODE 响应代码
pycurl.SPEED_DOWNLOAD 下载速度
pycurl.INFO_FILETIME 文件的时间信息
pycurl.HTTP_CONNECTCODE HTTP 连接代码
'''