from flask import Flask,request,redirect

app = Flask(__name__)

@app.route('/get',methods=['GET'])
def getConfirmation():
    # Design a api to get parameter from url and update meeting room status
    ## This part for parsing the url, which is clicked by user for confirmation
    ### URL form http://127.0.0.1:5000/register?user=anna.z.jin@gmail.com&st=2018-05-29T09:00:00-07:00
    # &et=2018-05-29T10:00:00-07:00&room=PwCsuzhouhe@gmail.com
    # user's mail addr
    user = request.args.get("user")
    #time
    start_time = request.args.get("st")
    end_time = request.args.get("et")
    #meeting room account
    room = request.args.get("room")

    ## Update meeting room's status according to the params above

    ## Optional: Send a email back to user, which contains all details including when, where, who
    return redirect("https://www.baidu.com")


if __name__ == '__main__':
        app.run(host='localhost')