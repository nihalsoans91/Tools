from xml.dom import minidom
import os

f= open("lables.txt","w+")
dir_path = os.path.dirname(os.path.realpath(__file__))
ano=os.path.join(dir_path,"Annotations")
dfiles=os.listdir(os.path.join(dir_path,"Annotations"))
for files in dfiles:
    #print(os.path.join(ano,files))

    mydoc = minidom.parse(os.path.join(ano,files))
    clas=mydoc.getElementsByTagName('name')
    c=clas[0].firstChild.data
    polygon = mydoc.getElementsByTagName('polygon')

    x1=polygon[0].childNodes[1].childNodes[0].firstChild.data
    y1=polygon[0].childNodes[1].childNodes[1].firstChild.data

    x2=polygon[0].childNodes[1].childNodes[0].firstChild.data
    y2=polygon[0].childNodes[1].childNodes[1].firstChild.data
    #print(os.path.join(ano,files)+","+str(x1)+","+str(y2)+","+str(x2)+","+str(y2)+","+c)
    f.write(os.path.join(ano,files)+","+str(x1)+","+str(y2)+","+str(x2)+","+str(y2)+","+c+"\n")

f.close
