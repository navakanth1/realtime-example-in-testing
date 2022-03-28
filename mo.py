import sqlite3
from prettytable import PrettyTable
data = sqlite3.connect("mobile.db")
table = data.execute("select name from sqlite_master where type='table' and name='smartphones'").fetchall()
if table!=[]:
    print("Table already created.")
else:
    data.execute('''create table smartphones(
                            name text,
                            brand text,
                            sno integer,
                            myear integer,
                            mmonth text,
                            price integer );''')
    print("Table created")
while True:
    print("Select an option from the list")
    print("1.Add mobile")
    print("2.Search mobile using Serial number")
    print("3.View all mobile phones")
    print("4.update mobile phones using serial number")
    print("5.Delete mobile using serial number")
    print("6.Exit")

    a = int(input("Enter the choice to be executed"))

    if a ==1:
        getMname = input("Enter the mobile name:")
        getMbrand = input("Enter the mobile brand:")
        getSno = input("Enter the serial number:")
        getMyear = input("Enter the manufacturing year:")
        getMmonth = input("Enter the manufactured month:")
        getPrice = input("Enter the price of the mobile:")
        data.execute("insert into smartphones (name,brand,sno,myear,mmonth,price) values('"+getMname+"','"+getMbrand+"',\
        "+getSno+",'"+getMmonth+"','"+getMmonth+"',"+getPrice+")")
        data.commit()
        print("Added mobile phone successfully")

    elif a==2:
        data = sqlite3.connect("mobile.db")
        getSno = input("Enter the serial number of mobile to be searched:")
        result = data.execute("select * from smartphones where sno="+getSno)
        for i in result:
            print("Mobile name",i[0])
            print("Mobile Brand",i[1])
            print("Mobile serial number",i[2])
            print("Manufactured year",i[3])
            print("Manufactured month",i[4])
            print("Price of the mobile",i[5])

    elif a==3:
        data = sqlite3.connect("mobile.db")
        result = data.execute("select * from smartphones")
        table = PrettyTable(["Mobile name","Mobile brand","Mobile S.no","Manu.year","Manu.month","Price"])
        for i in result:
            table.add_row([i[0],i[1],i[2],i[3],i[4],i[5]])
        print(table)
    elif a==4:
        getSno = input("Enter the serial number to be updated:")
        getMname = input("Enter the new mobile name:")
        getMbrand = input("Enter the new mobile brand:")
        getMyear = input("Enter the new manufactured year:")
        getMmonth = input("Enter the new manufactured month:")
        getPrice = input("Enter the new price:")
        data.execute("update smartphones set name='"+getMname+"',brand='"+getMbrand+"',\
         myear='"+getMmonth+"',mmonth='"+getMmonth+"',price="+getPrice+"")
        data.commit()
        print("updated successfully")

    elif a==5:
        getSno = input("Enter the serial number to be updated:")
        data.execute("delete from smartphones where sno="+getSno)
        data.commit()
        print("Deleted successfully")

    elif a==6:
        print("Exited")
        break

    else:
        print("Enter a valid choice"