import sqlite3

def create_db():
    conn = sqlite3.connect('candela.db')
    cur = conn.cursor()

    # Drop existing tables if re-running
    cur.execute('DROP TABLE IF EXISTS catalog')
    cur.execute('DROP TABLE IF EXISTS departments')
    cur.execute('DROP TABLE IF EXISTS employee')

    # Create Catalog
    cur.execute('CREATE TABLE catalog(sno varchar(5), type varchar(60), model varchar(60), max_seats int, colours varchar(60), emi_interest varchar(60), base_price int)')
    catalogs = [
        ('1','HATCHBACK','S',2,'CUSTOM','12',45000),
        ('2','HATCHBACK','X',4,'CUSTOM','12',48000),
        ('3','HATCHBACK','Y',8,'CUSTOM','12',55000),
        ('4','SUV','M',4,'CUSTOM','10',65000),
        ('5','SUV','C',7,'CUSTOM','10',70000),
        ('6','SUV','D',8,'CUSTOM','10',80000),
        ('8','SEDAN','T',2,'CUSTOM','8',120000),
        ('9','SEDAN','Z',4,'CUSTOM','8',150000),
        ('10','SEDAN','F',4,'CUSTOM','6',200000)
    ]
    cur.executemany("INSERT INTO catalog VALUES (?,?,?,?,?,?,?)", catalogs)

    # Create Departments
    cur.execute('CREATE TABLE departments(DEPT_NAME VARCHAR(80), NUM_EMPLOYEE VARCHAR(80), DEPT_HEAD VARCHAR(80), INVEST_PER_EMP INT, EARN_PER_EMP INT, BUDGET INT)')
    depts = [
        ('MARKETING','5','TINLEY',40000,50000,0),
        ('MANUFACTURING','6','ELLA',40000,62000,0),
        ('HR','5','TATUM',40000,80000,0),
        ('PURCHASE','5','SHILOH',40000,71000,0)
    ]
    cur.executemany("INSERT INTO departments VALUES (?,?,?,?,?,?)", depts)

    # Create Employee
    cur.execute('CREATE TABLE employee(EMP_ID VARCHAR(20), EMP_NAME VARCHAR(80), DEPARTMENT VARCHAR(80), DESIGNATION VARCHAR(80), SALARY INT, DOJ DATE, POINTS INT, NO_WARNINGS INT, BONUS INT)')
    emps = [
        ('CAN001','TINLEY','MARKETING','DGM',50000,'2005-01-01',20,0,0),
        ('CAN002','HOLDEN','MARKETING','CHIEF MANAGER',40000,'2006-01-01',18,0,0),
        ('CAN003','BLAINE','MARKETING','SR. MANAGER',35000,'2007-01-01',16,0,0),
        ('CAN004','DOLOVAN','MARKETING','MANAGER',30000,'2008-01-01',14,0,0),
        ('CAN005','PRESTON','MARKETING','ENGINEER',20000,'2009-01-01',12,0,0),
        ('CAN006','ELLA','MANUFACTURING','DGM',50000,'2005-01-01',20,0,0),
        ('CAN007','TOM','MANUFACTURING','CHIEF MANAGER',40000,'2006-01-01',18,0,0),
        ('CAN008','DECK','MANUFACTURING','SR. MANAGER',35000,'2007-01-01',16,0,0),
        ('CAN009','HARRY','MANUFACTURING','MANAGER',30000,'2008-01-01',14,0,0),
        ('CAN010','JAMES','MANUFACTURING','ENGINEER',20000,'2009-01-01',12,0,0),
        ('CAN011','TATUM','HR','DGM',50000,'2005-01-01',20,0,0),
        ('CAN012','WILLIAM','HR','CHIEF MANAGER',40000,'2006-01-01',18,0,0),
        ('CAN013','SHAWN','HR','SR. MANAGER',35000,'2007-01-01',16,0,0),
        ('CAN014','HENRY','HR','MANAGER',30000,'2008-01-01',14,0,0),
        ('CAN015','MARGRET','HR','ENGINEER',20000,'2009-01-01',12,0,0),
        ('CAN016','SHILOH','PURCHASE','DGM',50000,'2005-01-01',20,0,0),
        ('CAN017','SAMUEL','PURCHASE','CHIEF MANAGER',40000,'2006-01-01',18,0,0),
        ('CAN018','GAMBART','PURCHASE','SR. MANAGER',35000,'2007-01-01',16,0,0),
        ('CAN019','BROCK','PURCHASE','MANAGER',30000,'2008-01-01',14,0,0),
        ('CAN020','ASHLEY','PURCHASE','ENGINEER',20000,'2009-01-01',12,0,0)
    ]
    cur.executemany("INSERT INTO employee VALUES (?,?,?,?,?,?,?,?,?)", emps)

    conn.commit()
    conn.close()
    print("candela.db generated successfully.")

if __name__ == '__main__':
    create_db()
