import psycopg2
import random as rd
from datas import logins1,domains,professions,countries,pswd_symbols,logins
# num=rd.randint(0,10)
# print(num)
conn=psycopg2.connect(
    database='citizens',
    user='postgres',
    password='postgres',
    host='localhost',
    port='5432'
    )
cur=conn.cursor()

passwords=[]
emails=[]
phone_numbers=[]
addresses=[]
followers=tuple(rd.randint(1,10000000)for i in range(5000))
print(followers)

for name in logins:
    email=name+domains[rd.randint(0,len(domains)-1)]
    emails.append(email)
print(emails)

for i in  range(5000):
    pswrd=''
    for p in range(rd.randint(8,15)):
        pswrd+=pswd_symbols[rd.randint(0,len(pswd_symbols)-1)]
    passwords.append(pswrd)

# print(passwords)

code=('7','2','4','0','7','2','5','3')

for number in range(5000):
    numbers='+996'
    for p in range(0,10):
        numbers+=code[rd.randint(0, len(code)-1)]
    phone_numbers.append(numbers)
# print(phone_numbers)

while len(addresses)<5000:
    for addres in logins:
        d=addres
        d+='ov'
        d+=' '
        d+=str(rd.randint(100,1000))
        addresses.append(d)
print(len(addresses))

cur.execute("""CREATE TABLE users(user_id SERIAL PRIMARY KEY,login VARCHAR(20) NOT NULL,password VARCHAR(100) NOT NULL,
email VARCHAR(100) NOT NULL,
phone_number VARCHAR(20) NOT NULL,
country VARCHAR(50) NOT NULL,
address VARCHAR(50) NOT NULL,
profession VARCHAR(50) NOT NULL,
followers INT NOT NULL
)""")

query='''INSERT INTO users(login,password,email,phone_number,country,address,profession,followers)VALUES'''

for i in range(10000):
    query+=f"""(
        '{logins[rd.randint(0,len(logins)-1)]}',
        '{passwords[rd.randint(0,len(passwords)-1)]}',
        '{emails[rd.randint(0,len(emails)-1)]}',
        '{phone_numbers[rd.randint(0,len(phone_numbers)-1)]}',
        '{countries[rd.randint(0,len(countries)-1)]}',
        '{addresses[rd.randint(0,len(addresses)-1)]}',
        '{professions[rd.randint(0,len(professions)-1)]}',
        {followers[rd.randint(0,len(followers)-1)]}),"""
sql_query=query[:-1]+';'

cur.execute(sql_query)
conn.commit()

cur.close()
conn.close()
