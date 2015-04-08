#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

line = "Cats are smarter than dogs"

pattern_1 = r'(.*) are (.*?) .*'
pattern_2 = r'(.*) are (.*?) than (.*)'

def test_reg():
    matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

    if matchObj:
        print "matchObj.group() : ", matchObj.group()
        print "matchObj.group(1) : ", matchObj.group(1)
        print "matchObj.group(2) : ", matchObj.group(2)
    else:
        print "No match!!"

# test_reg()

def parse_comparison(pattern, grp_no=1):
    matchObj = re.match( pattern, line, re.M|re.I)
    for idx in range(grp_no): print str(idx) + ':', matchObj.group(idx)

    #for idx, p in enumerate(matchObj.groups()): print ('group(%i): %s' % (idx, p))
    print ('group(%i): %s' % (0, matchObj.group(0)))

    idx = 1
    for p in matchObj.groups():
        print ('group(%i): %s' % (idx, p))
        idx += 1

#parse_comparison(pattern_1, 3)
#parse_comparison(pattern_2, 4)

def find(pattern, string):
    match = re.search(pattern,string)
    if match: return(match) #.group())
    else: print "not find"

def parse_ticket():
    tif = '乘車區間\n\n' + '票款票款\n\n' + '2015-03-13\n\n' + '222\n\n' \
         + '左營 16:54 - 台北 18:30\n\n' + 'NT$ 1630\n\n' \
         + '注意事項：'
    #print(tif)

    search_date  = find(r'(\d{4})-(\d+)-(\d+)', tif) # , re.M|re.I)
    print(search_date.group())
    for g in search_date.groups(): print g
    #search_trip = find(r'(.*) - (.*)', tif) #, re.M|re.I)
    search_trip = find(r'(.*) (\d{2}:\d{2}) - (.*) (\d{2}:\d{2})', tif) #, re.M|re.I)
    print(search_trip.group())
    for g in search_trip.groups(): print g

parse_ticket()
