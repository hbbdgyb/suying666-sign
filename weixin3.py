#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#GuoYabin

import requests,json,sys,importlib
importlib.reload(sys)

class WeChat(object):
	def __init__(self,corpsecret=None):
		self.url='https://qyapi.weixin.qq.com/cgi-bin/gettoken'
		self.corpid = 'ww0cb105d1003bf9c1'
		self.corpsecret = corpsecret

	def auth(self):
		params={'corpid':self.corpid,'corpsecret':self.corpsecret}
		try:
			rs=requests.get(self.url,params=params)
			return(rs.json()['access_token'])
			rs.close()
		except:
			print('get access_token error!')


	def message(self,touser,subject,message):
		data=json.dumps({
			'touser':touser,
			'msgtype':'news',
			'agentid':'1000007',
			'news':{
				'articles': [{
					'title':subject,
					'description':message,}
							 ]
			},
			'enable_id_trans': 0,
			'enable_duplicate_check': 0,
			'duplicate_check_interval': 1800
		},ensure_ascii=True)
		return(data)

	def send(self,touser,subject,neirong):
		url='https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='+self.auth()
		date = self.message(touser,subject,neirong)
		res=requests.post(url,data=date)
		print(res.json())
		res.close()

			
if __name__ == '__main__':
	weixin=WeChat()
	weixin.send(sys.argv[1],sys.argv[2],sys.argv[3])