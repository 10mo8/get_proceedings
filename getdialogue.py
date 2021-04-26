#国会会議録のデータを記録します16to19ori.txtというファイルに保存します
import urllib
import untangle
import urllib.parse

if __name__ == '__main__':
    start='1'#発言の通し番号
    while start!=None:
        startdate='2016-01-01'
        enddate= '2019-12-31'
        #meeting='本会議'
        #urllib.parse.quoteが日本語をコーディングしてくれる
        url = 'http://kokkai.ndl.go.jp/api/speech?'+urllib.parse.quote('startRecord='+ start
        + '&maximumRecords=100'
        #+ '&nameOfMeeting='+ meeting
        + '&from=' + startdate
        + '&until='+ enddate)
        #Get信号のリクエストの検索結果（XML）
        obj = untangle.parse(url)

        for record in obj.data.records.record:
            speechrecord = record.recordData.speechRecord
            print(speechrecord.date.cdata,
                speechrecord.speech.cdata)

            file=open('16to19ori.txt','a', encoding="utf-8")
            file.write(speechrecord.speech.cdata)
            file.close()
            #一度に１００件しか帰ってこないので、開始位置を変更して繰り返しGET関数を送信
        start=obj.data.nextRecordPosition.cdata