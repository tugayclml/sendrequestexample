from flask import Flask,render_template,request
import requests
import json


app = Flask(__name__)

callList = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/callList',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      callList.clear()
      result = request.form.to_dict()

      sd = result['startdate']
      startdate = sd.split(' ')
      sdate = startdate[0]
      stime = startdate[1]


      fd = result['finishdate']
      finishdate = fd.split(' ')
      fdate = finishdate[0]
      ftime = finishdate[1]

      apptoken = "ag9zfnRlbGVmb25pLXRlc3RyHwsSElRlbmFudEFwcGxpY2F0aW9ucxiAgICw46OcCQyiARVzdGFnaW5nMS5hbG8tdGVjaC5jb20"

      url = "http://staging1.alo-tech.com/api/?function=reportsCDRLogs&startdate="+sdate+"%20"+stime+":00&finishdate="+fdate+"%20"+ftime+":00&app_token="+apptoken

      response = requests.get(url)

      loaded_json = json.loads(json.dumps(response.json()))

      newjson = loaded_json["CallList"]




      for x in newjson:
          print("%s : " % (x))
          print(x['callerid'])
          callList.append(x)

   return render_template('list.html',callList = callList)




if __name__ == '__main__':
 app.run(host="127.0.0.1",port=6060,debug=True)