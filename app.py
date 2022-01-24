
from flask import Flask

app=flask.Flask(__name__)

@app.route("/",methods=["GET"])
def home():
    try:
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
            "Jab desh ke PM ka imaan nahin toh apun sidhe raaste chal ke kya karega",
            "Bhagwan ko maante ho? Bhagwan ko l*nd farak nahi padta.",
            "Hindustan jab Hindustan nahin bana tha tab se politics ki macchi ko dharam ke tel mein fry karte hue aaye hain.",
            "Bhagwan aadmi se kahani me baat karta hai. Hum sab ka life ek kahani hai.",
            "Dharmon ka roop yahi hai. Rahgeer ko prem se ghar bulao. Aadar samit bhojan grahan karo. Phir uski aatma pe kabza kar lo.",
            "Gareeb logon ka entry sirf mandir me free hai.",
            "Duniya ke bazaar mein sabse bada dhanda hai dharam. Bhagwan se dara ke chutiya banate hain public ko.",
            "Hindu hotel se apun seekha ki dharam ke naam pe janta ka kitna chutiya banaya ja sakta hai.",
            "Tum mardon ko aisa kyun lagta hain ki har aurat ko tumhe hi bachana hai.",
            "Guns, drugs, property sab chota dhandha hai. Asli dhanda hai politics.",
            ],
            "Family Man":[
            "Privacy is a myth, just like democracy.",
            "Bhai Tu Kuch Ulta-Seedha Mat Karna!",
            "P.T. Usha ke Bhatije!",
            "Kabhi Kabhi Jeetne Ke Liye Haarna Padta Hai",
            "Ab Zinda Rehne Ke Liye Bacha Hi Kya Hai?",
            "Don't be a Minimum Guy",
            "Yeh Quote Bhi Google Pe Mil Jaega Tumhe",
            " We lost the battle, but we won the war",
            "Main Desh Ke Liye Mar Sakta Hoon… Magar Politics Ke Liye Nahi Yaar",
            "Aa Raha Hun Bhench#d G#nd Mei Ghus Jao Insaan Ke.",
            ],
            "Scam 1992":[
            "Jab jeb mein money ho na toh kundli mein shani hone se koi fark nahi padta.",
            "Risk hai toh ishq hai!",
            "Dekho mein Cigarette Nahi Peeta, par jeb mein lighter zarur rakhta hoon, Dhamaka karne ke liye.",
            "Profit Dikhta hai, toh har koi jhukta hai.",
            "Success kya hai? Failure ke baad ka chapter.",
            "Emotion mein insaan hamesa galti karta hai.",
            "Locha, lafda aur jalebi fafda, isko gujarati ki life se koi nikaal nahi sakta.",
            "Old school ho ya new school, sabke syllabus mein ek subject common hota hai--profit aur woh mera favorite subject hai.",
            "Business mein saturation aata hai, dimag mein thodi? Woh chalta rehta hai na!",
            "Share Market Itna Gehra KuaaN Hai Jo Poore DesH Ki Paise Ki Pyaas BujHa Sakta Hai."
            ],
            "Kota Factory":[
            "Galat dikhate hain filmon mein, ki ratt ratt ke kisi ka ho raha hai selection. IIT mein chatur nahi jaate, sirf Rancho jaate hain! 3 idiots dekhi hai na?",
            "Ek baat toh hai Sir ji, Yahaan aake kisi student ka selection ho na ho, par yahaan aake bhi jiska nahi hua uska toh hona hi nahi tha",
            "A1 stuents are my rankers. The rest are my bankers.",
            "Tum Ameer log kisi bhi din cake khaa lete ho kya?",
            "21 din mein koi bhi aadat lag jaati hai, koi bhi aadat chhoot jaati hai. Toh yehi karna hai.",
            "Bhai sahab confidence gir jaata hai, phir jitna duniya nahi samjti na utna aadmi khud ko loser samajhne lagta hai ",
            "If you are the smartest person in the room, you are in the wrong class.",
            "Seedha padhne mat lago, pehle chitra dekho.",
            "Kabhi kabhi cheating chalti hai, bas aadat nahi padi chahiye",
            "Bheek mangne mein jyaada maza aata hai? Dekho, bheek toh maang mat, kucch chahiye toh mehnat kar lo or cheen lo!",
            ]}
        return (cal)
    except KeyError:
        return f'Invalid'


# if __name__=='__main__':
#     app.run(debug=True)