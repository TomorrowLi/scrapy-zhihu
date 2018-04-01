
一、首先在setting.py中修改True改为False

	# Obey robots.txt rules
	#允许爬取robots.txt文件内不能爬取的资源
	ROBOTSTXT_OBEY = True
    #知乎是由反扒措施的必须添加User-agent以及authorization
	DEFAULT_REQUEST_HEADERS = {
	  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	  'Accept-Language': 'en',
	    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36' ,
	    'authorization':'Bearer 2|1:0|10:1521707334|4:z_c0|80:MS4xS1NYS0FnQUFBQUFtQUFBQVlBSlZUVWEzb0Z0ZDl0MGhaa0VJOWM0ODhiejhRenVUd0tURnFnPT0=|98bb6f4900c1b4b52ece0282393ede5e31046c9a90216e69dec1feece8086ee0'
	}

	MONGO_DATABASE='zhihu'

二、最后启动setting.py中的

    ITEM_PIPELINES = {
   		'zhihu.pipelines.MongoPipeline': 300,
	}
	#去掉注释
三、结果展示

![image](https://github.com/TomorrowLi/MarkdownImage/blob/master/zhihuMongodb.PNG?raw=true)

详细描述可以访问我的博客 [TomorrowLi](tomorrowli.github.io)
