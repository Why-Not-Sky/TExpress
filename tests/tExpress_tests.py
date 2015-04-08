# -*- coding: utf-8 -*-

from nose.tools import *
import tExpress

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"

def test_decode():
    imgfile = '../data/ticket.png'
    return (decode_qrcode_byWeb(imgfile))

def test_download():
    pnr = '05887138'
    tid = '2900510720726'
    out_file = './' + tid + '.pdf'
    download_ticket_pdf(pnr, tid, out_file)

def test_read_file(txt_file):
    with open(txt_file, 'r') as f: #, encoding = 'UTF-8')
        while True :
            i = f.readline()  #.decode('utf-8')
            if i=='': break
            print(i.decode('utf-8')) #, '')
        f.close()

def test_parse_file():
    tdate, tno, trip, tamount = parse_ticket_file2('../data/2900510720726.txt')
    s = u'<br>order:%s ticket id:%s date:%s trip:%s </br>' % (tdate, tno, trip, tamount )
    print (s) #print (trip)

def test_unit_code():
    pass

def parse_ticket_file2(txt_file):
    def load_file(fname):
        with open(fname, 'r') as fobj:
            data = fobj.read()
            fobj.close()
        return(data)

    data = load_file(txt_file)
    istart =  data.find('票款票款')
    iend =  data.find('注意事項：')
    tinfo = data[istart:iend]

    #tfiso = tinfo.decode('iso-8859-15') #wrong
    #print tinfo
    #print tfutf8

    #points: the process of chinese text
    #tinfo8 = filter(lambda x: x != '', tinfo.split('\n'))  #wrong
    #for t in tinfo8: print t.decode('utf-8')
    #print (tinfo8[3])
    #tdate, tno, trip, tamount = tinfo8[1], tinfo8[2], tinfo8[3], tinfo8[4]
    #print (trip)

    tfutf8 = tinfo.decode('utf-8')
    tf8 = filter(lambda x: x != '', tfutf8.split('\n'))
    #for t in tf8: print t.encode('utf-8')
    #print (tf8[3])
    trip = tf8[3]

    #print (trip)
    #print ([t.encode('utf-8') for t in tf8 if t != ''])  #useless...
    #print (tinfo8, tf8)


    tdate, tno, trip, tamount = tf8[1], tf8[2], tf8[3], tf8[4]
    #(tdate, tno, trip, tamount) = (tf8[1], tf8[2], tf8[3], tf8[4])   #encode translated caused error

    #print tdate, tno, trip, tamount
    return tdate, tno, trip, tamount  #errors occur as tuple translation

def test_get_ticket_info(out_file):
    """
    :param out_file: ticket pdf file
    :return:
    """
    #tdata = load_file(exec_pdf2txt(out_file))
    #tsoup = BeautifulSoup(tdata)
    #todo: use re to get [date, departure-destination, nt$, train number, ticket type]
    import linecache

    txt_file = out_file.replace('.pdf', '.txt')

    LINE_OF_DATE = 23
    LINE_OF_TRAIN_NO = 25
    LINE_OF_TRIP = 27
    LINE_OF_AMOUNT = 29

    tDate = linecache.getline(txt_file, LINE_OF_DATE)
    tTrainNo = linecache.getline(txt_file, LINE_OF_TRAIN_NO)
    tTrip = linecache.getline(txt_file, LINE_OF_TRIP)
    tAmount = linecache.getline(txt_file, LINE_OF_AMOUNT)

    #txt_file = exec_pdf2txt(out_file)
    with open(txt_file) as f:  # , encoding='iso-8859-1'
        lines = f.readlines()
        f.close()
    #print (lines)
    return (lines[LINE_OF_DATE-1], lines[LINE_OF_TRAIN_NO-1], (lines[LINE_OF_TRIP-1]).decode('utf-8') , lines[LINE_OF_AMOUNT-1])

    #import codecs
    #f = codecs.open(txt_file, encoding='utf-8')
    #for line in f:
    #    print repr(line).decode('utf-8')

    #return (tDate, tTrainNo, tTrip.decode('utf-8'), tAmount)

if __name__ == '__main__':
    #test_decode()
    #test_download()
    test_parse_file()