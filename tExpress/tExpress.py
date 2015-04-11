# -*- coding: utf-8 -*-
# encoding: utf-8

from urllib import urlencode, urlopen
from bs4 import BeautifulSoup

import zxcode

THSRC = 'http://www4.thsrc.com.tw/tc/TExp/page_print.asp?lang=tc'
OUTPUT_PATH = './data/'
IMG_FILE = OUTPUT_PATH + 'ticket.png'
TXT_FILE = OUTPUT_PATH + '2900510720726.txt'
QR_CODE = '290051072072605887138000022201220150313165400002201503131830000100000010000002018001000000163000600100000000002015031310A89C'
WEBQR = OUTPUT_PATH + 'webqr.txt'
ZXING = OUTPUT_PATH + 'zxing.org.txt'

def download_ticket_pdf(ord_no, tid, fname):
    url = (THSRC + "&pnr=%s&tid=%s") % (ord_no, tid)
    response = urlopen(url)
    data = response.read()

    with open(fname, 'w') as fd:
      fd.write(data)
      fd.close()

def upload_ticket_image():
    pass

def get_ticket_id(imgfile):
    tcode = decode_qrcode(imgfile)
    ord_no, tid = tcode[13:21], tcode[0:13]
    return ord_no, tid

def decode_qrcode(imgfile):
    return (decode_qrcode_byWeb(imgfile))

def decode_qrcode_byWeb(imgfile):
    def get_response_html(imgfile):
        return(load_file(imgfile))

    def decode_byWebQR(imgfile):
        data = get_response_html(WEBQR)
        docSoup = BeautifulSoup(data)
        rtext=docSoup.find('div', attrs = {'id': 'result'})
        return(rtext.find('b').getText())

    def decode_byZxing(imgfile):
        return(zxcode.decode(imgfile))

    return (decode_byZxing(imgfile))

def load_file(fname):
    with open(fname, 'r') as fobj:
        data = fobj.read()
        fobj.close()
    return(data)

def exec_pdf2txt(pdf_file):
    # pdf2txt.py -t text -o 2900510720726.txt 2900510720726.pdf
    #subprocess.call([cmd, '-t', 'text', '-o', txt_file, pdf_file])
    import pdf2txt

    txt_file = pdf_file.replace('.pdf', '.txt')
    args = ['pdf2txt.py', '-t', 'text', '-o', txt_file, pdf_file]
    pdf2txt.main(args)
    return(txt_file)

def get_ticket_info(imgfile):
    import collections

    #for testing not to download again
    #return (TXT_FILE, parse_ticket_by_find(TXT_FILE))

    ord_no, tid = get_ticket_id(imgfile)
    out_file = OUTPUT_PATH + tid + '.pdf'
    download_ticket_pdf(ord_no, tid, out_file)
    out_txt_file = exec_pdf2txt(out_file)

    return (out_file, parse_ticket_by_find(out_txt_file))

    #not used
    #tdate, trip = parse_ticket (out_txt_file) #translate to unicode
    #utrip = trip.encode('utf-8')
    utrip = unicode(trip)
    #utrip = trip.decode('utf-8')
    #udate = tdate.encode('utf-8')  #unicode(tdate)
    udate = unicode(tdate)

    result = collections.defaultdict(list)
    result['order no'].append(ord_no)
    result['ticket id'].append(tid)
    result['date'].append(tdate)
    result['journey'].append(trip)

    #return result
    #return ord_no, tid, udate, utrip

def parse_ticket_by_find(txt_file):
    ticket_keys = ['1-乘車日期', '2-車次', '3-乘車區間', '4-票款', '5-訂位代號', '6-票號']
    #ticket_dict = {'date', 'drive', 'journey', 'amount', 'order no', 'ticket id'}
    # ['2015-03-13', '222', '\xe5\xb7\xa6\xe7\x87\x9f 16:54 - \xe5\x8f\xb0\xe5\x8c\x97 18:30', 'NT$ 1630']
    ORDER_NO_KEYWORD = '訂位代號：'  #05887138
    TICKET_ID_KEYWORD = '票號：票號：' #2900510720726

    data = load_file(txt_file)
    iorder_no_begin = data.find(ORDER_NO_KEYWORD)+len(ORDER_NO_KEYWORD)
    iorder_no_end = iorder_no_begin + 8
    order_no = data[iorder_no_begin:iorder_no_end]

    itid_begin = data.find(TICKET_ID_KEYWORD)+len(TICKET_ID_KEYWORD)
    itid_end = itid_begin + 13
    tid = data[itid_begin:itid_end]

    istart =  data.find('票款票款')
    iend =  data.find('注意事項：')
    tinfo = data[istart:iend]

    tf8 = filter(lambda x: x != '', tinfo.split('\n'))
    tf8.append(order_no); tf8.append(tid)

    ticket_dict = dict(zip(ticket_keys, tf8[1:]))

    return (ticket_dict)
    #tdate, tno, trip, tamount = tf8[1], tf8[2], tf8[3], tf8[4]
    #return tdate, tno, trip, tamount  #errors occur as tuple translation

def parse_ticket_by_regular_expression(txt_file):
    tif = '乘車區間\n\n' + '票款票款\n\n' + '2015-03-13\n\n' + '222\n\n' \
          + '左營 16:54 - 台北 18:30\n\n' + 'NT$ 1630\n\n' \
          + '注意事項：'
    #print(tif)
    import re
    def find(pattern, string):
        match = re.search(pattern,string)
        if match: return(match) #.group())
        else: print "not find"

    tif = load_file(txt_file)

    search_date  = find(r'(\d{4})-(\d+)-(\d+)', tif) # , re.M|re.I)
    #print(search_date.group())
    #for g in search_date.groups(): print g
    search_trip = find(r'(.*) (\d{2}:\d{2}) - (.*) (\d{2}:\d{2})', tif) #, re.M|re.I)
    #print(search_trip.group())
    #for g in search_trip.groups(): print g
    #return ({'date':search_date.group(), 'trip': search_trip.group(1) +' - '+ search_trip.group(3)})
    return search_date.group(), search_trip.group()

if __name__ == '__main__':
    # 05887138 2900510720726 2015-03-13 左營 16:54 - 台北 18:30
    pdf_file, tinfo = get_ticket_info(IMG_FILE)
    #tinfo = parse_ticket_by_find(TXT_FILE)
    print pdf_file
    for t in sorted(tinfo.items()): print (t[0] + ':' + t[1])




