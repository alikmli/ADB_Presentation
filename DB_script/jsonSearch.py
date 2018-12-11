
import  query


db=input()
db=db.split()
db=db.pop()
db.strip()


que=input('>> ')
tbl_name="/home/ali/NKDBMS/"+db+"/"+query.query_table_name(que) + ".json"
select_part=query.query_style_select(que)
where_part=query.query_style_where(que)
#print(tbl_name,select_part,where_part)

list_result=list()
with open(tbl_name) as f:
    for line in f:
         line=line.strip()
         line=line[1:len(line)-1]
         line=line.split(",",2)
         for i in range(0,len(line)):
             line[i]=line[i].split(":")
             line[i][0]=line[i][0][1:len(line[i][0])-1]

         for item in where_part.keys():
             if item == line[0][0]:
                 if where_part[item]==line[0][1]:
                     list_result.append(line)
             elif item == line[1][0]:
                 if where_part[item]==line[1][1]:
                     list_result.append(line)



print("The results are : ")

for item in select_part:
    for res in list_result:
        if item==res[0][0]:
            print(res[0][1])
        elif item == res[1][0]:
            print(res[1][1])

