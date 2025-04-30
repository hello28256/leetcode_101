# -*-coding: utf-8 -*-
# @Time    : 2025/4/30 10:02
# @Author  : hello28256@gmail.com
# @FileName: 76_minimum-window-substring.py
# @Software: PyCharm
# @Blog    ：https://github.com/hello28256
import collections

from collections import Counter
def minWindow(s: str, t: str) -> str:
    #统计t中的每一个字符出现的次数
    freq=Counter(t)
    #定义目标字段出现的起始位置和长度
    min_pos,min_lenth= None, None
    #统计字符出现数量
    count=0
    l=0
    for r in range(len(s)):
        if s[r] not in freq:
            continue
        freq[s[r]]-=1
        if freq[s[r]]>=0:
            count+=1
        while count==len(t):
            if min_lenth is None or r-l+1<min_lenth:
                min_pos=l
                min_lenth=r-l+1
            if s[l] in freq:
                freq[s[l]]+=1
                if freq[s[l]]>0:
                    count-=1
            l+=1
    return "" if min_lenth is None else s[min_pos:min_pos+min_lenth]

if __name__=="__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    output=minWindow(s,t)
    print(output)