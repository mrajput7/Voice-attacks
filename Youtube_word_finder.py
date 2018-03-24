import requests
special=r"""!@#$%'^&*()<>"?:{}|+_/.,;[]"""
phrase=raw_input("Enter phrase you want to search in a single line: ")
for i in special:
    phrase=phrase.replace(i," ")
phrase=phrase.split(" ")
y_links = list()
response=int(input("Enter 1 to give path of a file or Enter 2 to manually enter links: "))

if(response==1):
    file_name = raw_input("Enter txt file path: ")
    f = open(file_name, "r")
    No_links=0
    for elements in f:
        No_links = No_links+1
        elements = elements.split("=")
        link = "http://video.google.com/timedtext?lang=en&v=" + str(elements[1])
        link= link.replace("\n", "")
        y_links.append(link)
elif(response==2):
    No_links = int(input("Enter how many links you will enter: "))
    for i in range(No_links):
        temp_link = raw_input("Enter youtube link: ")
        temp_link = temp_link.split("?v=")
        link = "http://video.google.com/timedtext?lang=en&v=" + str(temp_link[1])
        y_links.append(link)
else:
    print("Wrong choise: Code will exit...")
    exit(1)


session=requests.Session()
special=r"!@#$%^&*()<>?:{}|+_/.,;[]"


for i in range(No_links):
    try:
        temp=session.get(y_links[i])
    except:
        err=y_links[i].split("&v=")
        out="https://www.youtube.com/watch?v=" + str(err[1])
        print ("Error: Not a url %s ")% out
        continue
    temp_list = list()
    tempo = str(temp.text)
    if (tempo.find("<title>Error 404 (Not Found)!!1</title>") != -1):
        err = y_links[i].split("&v=")
        out = "https://www.youtube.com/watch?v=" + str(err[1])
        print("Youtube link: %s is not valid. Moving to next link.") % out
        continue
    tempo = tempo.lower()
    tempo = tempo.replace("\n", " ")
    tempo = tempo.replace("</text><text","</#@@@@@@@@@#><#@@@@@@@@@#")
    tempo = tempo.split("#@@@@@@@@@#")
    for j in tempo:
        if j != "><" and j != '<?xml version="1.0" encoding="utf-8" ?><transcript><' and j != "></transcript>":
            temp_list.append(j)
    for k in phrase:
        k = k.lower()
        if k != '':
            for l in temp_list:
                time_stamp = l.split(">")
                for l in special:
                    time_stamp[1].replace(l, "")
                    time_stamp[1] = time_stamp[1].replace(l, "")
                if (time_stamp[1].find(k) != -1):
                    err = y_links[i].split("&v=")
                    out = "https://www.youtube.com/watch?v=" + str(err[1])
                    print("Word Found: %s, at time stamp %s in video_url %s") % (k, time_stamp[0], out)
