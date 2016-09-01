#!coding=utf-8

'''
jsp木马判断机制2

'''

import re

keyword_a=r"Runtime\.getRuntime\(\)\.exec"  #关键字匹配 
keyword_b=r"java\.io\.FileOutputStream\(application\.getRealPath\("      #关键字匹配 


def Check(filestr,filepath):

	filestr=filestr.lower()

	a=re.search(keyword_a,filestr)
	b=re.search(keyword_b,filestr)

	if a:
		return ((a.group(),),),'Danger'

	elif b:
		return ((a.group(),),),'Danger'

	return None