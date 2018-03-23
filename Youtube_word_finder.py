import requests
special=r"""!@#$%'^&*()<>"?:{}|+_/.,;[]"""
phrase=raw_input("Enter phrase you want to search: ")
for i in special:
    phrase=phrase.replace(i," ")
phrase=phrase.split(" ")
y_links = list()
No_links = int(input("Enter how many links you will enter: "))
for i in range(No_links):
    temp_link=raw_input("Enter youtube link: ")
    temp_link=temp_link.split("=")
    link="http://video.google.com/timedtext?lang=en&v="+str(temp_link[1])
    y_links.append(link)

session=requests.Session()
special=r"!@#$%^&*()<>?:{}|+_/.,;[]"
for i in range(No_links):
    try:
        temp_list=list()
        temp=session.get(y_links[i])
        tempo=str(temp.text)
        tempo=tempo.lower()
        tempo=tempo.replace("\n"," ")
        tempo=tempo.split("text")
        for j in tempo:
            if j != "><" and j != '<?xml version="1.0" encoding="utf-8" ?><transcript><' and j != "></transcript>":
                temp_list.append(j)
        for k in phrase:
            k=k.lower()
            if k!='':
                for l in temp_list:
                    time_stamp=l.split(">")
                    for l in special:
                        time_stamp[1].replace(l, "")
                        time_stamp[1] = time_stamp[1].replace(l, "")
                    if(time_stamp[1].find(k)!=-1):
                        print("Word Found:%s, at time stamp %s in video_url %s")  %(k,time_stamp[0],y_links[i])

    except:
        print ("Error: Not a url %s "), y_links[i]
        continue

