from auto import Auto
import datetime

cars=[]
f=open('cars.txt')
readcar=f.readlines()
f.close()
for i in range(len(readcar)):
    readcar[i]=readcar[i].replace("\n","")
    readcar[i]=readcar[i].split("@")
    dat=readcar[i][6].split(" ")
    cars.append(Auto(readcar[i][0],readcar[i][1],readcar[i][2],readcar[i][3],readcar[i][4],readcar[i][5],datetime.date(int(dat[0]),int(dat[1]),int(dat[2]))))


print(Auto.get_info(cars,"Grey","Toyota","01"))
