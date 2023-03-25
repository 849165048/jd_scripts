fork： https://github.com/ccwav/QLScript2/blob/main/README.md

sendNotify.js
sendNotify.js
发送通知脚本Pro.

集成自动禁用失效CK功能，当NOTIFY_AUTOCHECKCK=“true”时开启,默认关闭,原理是通过捕获任务脚本发送ck失效实现，

精准操作，支持一对一推送，通知标题还是以前的"京东CK检测",兼容jd_CheckCK.js的分组设定和CHECKCK_ALLNOTIFY设定.

变量列表:

    (1) NOTIFY_SKIP_LIST
    如果通知标题在此变量里面存在(&隔开),则用屏蔽不发送通知.(PS: Ningjia 作者写的功能，继承过来.)	
    例子 :  export NOTIFY_SKIP_LIST="京东CK检测&京东资产变动"
    
    (2) NOTIFY_GROUP2_LIST NOTIFY_GROUP3_LIST NOTIFY_GROUP4_LIST NOTIFY_GROUP5_LIST NOTIFY_GROUP6_LIST
    如果通知标题在此变量里面存在(&隔开),则用第2/3/4/5/6套推送变量进行配置.
    
    (3) NOTIFY_SHOWNAMETYPE
    export NOTIFY_SHOWNAMETYPE="1"    不做任何变动
    export NOTIFY_SHOWNAMETYPE="2"    效果是 :  账号名称：别名(备注)	
    export NOTIFY_SHOWNAMETYPE="3"    效果是 :  账号名称：pin(备注)
    export NOTIFY_SHOWNAMETYPE="4"    效果是 :  账号名称：备注
    
    (4) NOTIFY_SKIP_NAMETYPELIST
    单独指定某些脚本不做NOTIFY_SHOWNAMETYPE变量处理
	  例子 :  export NOTIFY_SKIP_NAMETYPELIST="东东农场&东东工厂"
    
    (5) 特殊标题控制，可以自行加载到第二点的变量中控制
    东东农场领取 东东萌宠领取 京喜工厂领取 汪汪乐园养joy领取 脚本任务更新
    
    (6) NOTIFY_NOREMIND
    对 东东农场领取 东东萌宠领取 京喜工厂领取 汪汪乐园养joy领取 脚本任务更新的通知进行屏蔽,可自行删减.	
    export NOTIFY_NOREMIND="京喜工厂领取&汪汪乐园养joy领取"
    
    (7) NOTIFY_NOCKFALSE
    屏蔽任务脚本的ck失效通知
    export NOTIFY_NOCKFALSE="true"
    
    (8) NOTIFY_AUTHOR
    指定通知底部显示 本通知 By 后面显示的字符,默认是ccwav Mod
    
    (9) NOTIFY_NOLOGINSUCCESS
    屏蔽青龙登陆成功通知，登陆失败不屏蔽(新版貌似可以直接设定了)
    export NOTIFY_NOLOGINSUCCESS="true" 
    
    (10) NOTIFY_CUSTOMNOTIFY
    强大的自定义通知，格式为 脚本名称&推送组别&推送类型 (推送组别总共5组)
    推送类型: Server酱&pushplus&pushplushxtrip&Bark&TG机器人&钉钉&企业微信机器人&企业微信应用消息&iGotNotify&gobotNotify&WxPusher
    export NOTIFY_CUSTOMNOTIFY=["京东资产变动&组1&Server酱&Bark&企业微信应用消息","京东白嫖榜&组2&钉钉&pushplus"] 
    
    (11) NOTIFY_CKTASK
    当接收到发送CK失效通知和Ninja 运行通知时候执行子线程任务,支持js py ts 
    例子: export NOTIFY_CKTASK="jd_CheckCK.js"
	
	(12) PUSH_PLUS_TOKEN_hxtrip 和 PUSH_PLUS_USER_hxtrip
    增加pushplus.hxtrip.com的推送加接口，貌似更稳定,注意这个和PUSHPLUS不是同一家.
    
	(13) 用 WxPusher 进行一对一推送
	新方案;
	填写变量 WP_APP_TOKEN_ONE,按照备注内容@@WxPusherUid的格式修改备注,例子 萌新cc@@UID_AASDADASDQWEQWDADASDADASDASDSA
	旧方案:
	详细教程有人写了，不知道是幸运还是不幸: https://www.kejiwanjia.com/jiaocheng/27909.html
	填写变量 WP_APP_TOKEN_ONE,可在管理台查看: https://wxpusher.zjiecode.com/admin/main/app/appToken
	手动建立CK_WxPusherUid.json，放通知脚本同级文件夹,可以参考CKName_cache.json,只是nickName改成Uid，
	每个用户的uid可在管理台查看: https://wxpusher.zjiecode.com/admin/main/wxuser/list	
	CK_WxPusherUid.json 内容(pt_pin 如果是汉字需要填写转码后的!):
	[
	  {
		"pt_pin": "ccwav",
		"Uid": "UID_AAAAAAAA"
	  },
	  {
		"pt_pin": "中文名",
		"Uid": "BBBBBBBBBB"
	  }
	]
	
	(14) NOTIFY_SKIP_TEXT
    如果此变量(&隔开)的关键字在通知内容里面存在,则屏蔽不发送通知.
    例子 :  export NOTIFY_SKIP_TEXT="忘了种植&异常"
    
	(15) NOTIFY_AUTHOR_BLANK (tcbaby提交)
    控制不显示推送通知的底部信息
    例子 :  export NOTIFY_AUTHOR_BLANK="随便填只要非空即可"
	