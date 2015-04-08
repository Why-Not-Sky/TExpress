#!/usr/bin/env python
# Encodes/Decodes Qr codes
# Makes use of Googles charts API for encoding
# & Zxings online decoder for decoding
# (c) Lee Caine 2011
# http://cocacoda.com
# MIT License

import os, sys, urlparse
import httplib, mimetypes
from optparse import OptionParser
from urllib import urlencode, urlopen
from BeautifulSoup import BeautifulSoup

# Base URL for Google charts API
GC_URL = "https://chart.googleapis.com/chart"
# Base URL for ZXing decoder
ZX_URL = "http://zxing.org/w/decode"

MSG = "\nqrcode - (c) Lee Caine 2011\n\n"

def decode(input_file):
    data = post_file(ZX_URL, [
        ('f', input_file, open(input_file, 'r').read(),)
    ])
    docSoup = BeautifulSoup(data)
    rtext=docSoup.find('table', attrs = {'id': 'result'})
    return(rtext.find('pre').getText())
    return (data)

def multipart_post(host, selector, fields, files):
    """
    Performs a HTTP multpart POST request
    """
    content_type, body = encode_multipart_data(fields, files)
    h = httplib.HTTP(host)
    h.putrequest('POST', selector)
    h.putheader('content-type', content_type)
    h.putheader('content-length', str(len(body)))
    h.endheaders()
    h.send(body)
    errcode, errmsg, headers = h.getreply()
    return h.file.read()

def encode_multipart_data(fields, files):
    """
    Encodes multipart data
    """
    LIMIT = "--------lImIt_of_THE_fIle_eW_$"
    CRLF = "\r\n"
    L = []
    for (key, val) in fields:
        L.append('--' + LIMIT)
        L.append('Content-Disposition: form-data; name="%s"' % key)
        L.append('')
        L.append(val)
    for (key, filename, val) in files:
        L.append('--' + LIMIT)
        L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, filename,))
        L.append('Content-Type: %s' % get_content_type(filename))
        L.append('')
        L.append(val)
    L.append('--' + LIMIT + '--')
    L.append('')
    body = CRLF.join(L)
    content_type = 'multipart/form-data; boundary=%s' % LIMIT
    return content_type, body

def get_content_type(filename):
    """
    Guesses the content type of a file
    """
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream'

def post_file(url, files):
    """
    Posts a file
    """
    urlparts = urlparse.urlsplit(url)
    return multipart_post(urlparts[1], urlparts[2], {}, files)

###########################################
def get_ticket(rtext):
    docSoup = BeautifulSoup(rtext)
    #print docSoup.previous
    tcode = docSoup.previous
    print 'order no:%s, ticket no:%s' % (tcode[0:13], tcode[13:21])



