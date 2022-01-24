
from flask import Flask,request

app=Flask(__name__)

@app.route("/result",methods=["GET"])
def result():
    # output=request.get_json()

    # if len(output.keys())!=1:
    #     return{"Status":"BAD Response"}
    # num1=int(output['num1'])

    cal={"Mirzapur":[
        '"Mata ji yahan hai, Behen yahan hai, Maa-Behen ek karne mein aasani hogi.”--Munna Bhaiyya',
        '“Attack me bhi gun, defense me bhi gun, Hum banayenge Mirzapur ko Amrica!”--Guddu Pandit',
        '“Neta banna hai toh Gundey paalo. Gundey mat bano.”--Kaleen Bhaiyya',
        '“Darr ki yahi dikkat hai, ki kabhi bhi Khatam ho sakta hai.”--Kaleen Bhaiyya',
        '“Suru majboori mein kiye the….. Ab maza aa raha hai.”--Guddu Pandit',
        '“Guns ki maddad se darr nahi badhana hai, Darr ki maddad se guns badhani hai.”--Bablu Pandit',
        '“Izzat nahi karte hain… Darte hain sab.”--Kaleen Bhaiyya',
        '“Ch***ya hain woh important nahi hai. Hamara ladka hai, Woh important hai.”--Kaleen Bhaiyya',
        '“Agli baar Munna Bhaiya ghar aaye… Zinda wapas hi nahi laute toh?”--Guddu Pandit',
        '“Oh Bhos***i waley Chacha. Rest kariye, varna Rest in Peace ho jaoge!”--Munna Bhaiyya'
        ],
        "Sacred Games":[
        ]}
    return (cal)


if __name__=='__main__':
    app.run(debug=True,port=2000)