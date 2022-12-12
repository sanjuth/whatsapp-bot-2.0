from __future__ import unicode_literals
import requests
from src.netra_id import get_netra_id


def get_student_details(id):
    id=get_netra_id(id)
    url = 'http://teleuniv.in/netra/api.php'
    myobj = {"method":"318",
            "rollno":id}
    x = requests.post(url, json = myobj)
    ans=''
    ans=x.json()['name'][0:-4]+"\n"+x.json()['currentyear']+"rd year"+'\n'+x.json()['branch']+'-'+x.json()['section']
    return ans


def get_student_overall_att(id):
    id=get_netra_id(id)
    url = 'http://teleuniv.in/netra/api.php'
    myobj = {"method":"314",
            "rollno":id}
    x = requests.post(url, json = myobj)
    overall_att="\nOverall Attendence %: "+x.json()["overallattperformance"]["totalpercentage"]+"%"
    sub_att="\nSubject wise Attendence :\n"
    for sub in x.json()["overallattperformance"]["overall"]:
        sub_att+=sub['subjectname']+" : "
        if sub['percentage']=="--":
            sub_att+=str(sub['practical'])+'%'+'\n'
        else:
            sub_att+=str(sub['percentage'])+'%'+'\n'
    today_att=""
    lis=dict(x.json()["attandance"]["dayobjects"][0]['sessions'])
    print(lis)
    for i,b in lis.items():
        #print(i,b)
        if b=='2' or b==2:
            today_att+="\u26AA"+' '
        elif b=='0' or b==0:
            today_att+="\U0001f534"+" "
        elif b=='1' or b==1:
            today_att+="\U0001f7e2"+" "
    print("today",today_att)
    return overall_att,sub_att,today_att


def student_info_att(id):
    res=get_student_details(id)+"\n"
    att=get_student_overall_att(id)
    res+=att[0]+'\n'
    res+=att[1]+'\n'
    res+="Todays Attendance:"+'\n'
    res+=att[2]
    print(att[2])
    print("to",res)
    return res


