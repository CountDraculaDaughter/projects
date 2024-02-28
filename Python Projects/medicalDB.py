import sqlite3
sqlConnect = sqlite3.connect("medical.db")
dbCursor = sqlConnect.cursor()
#Select 1 statement
dbCursor.execute("Select * from surgery")
rows = dbCursor.fetchall()
for row in rows:
    print(row)
#Select 2 statement
dbCursor.execute("Select * from doctor")
rows2 = dbCursor.fetchall()
for row2 in rows2:
    print(row2)
#Select 3 statement
dbCursor.execute("Select * from patient")
rows3 = dbCursor.fetchall()
for row3 in rows3:
    print(row3)
#Select 4 statement
dbCursor.execute("Select patientFN, patientLN, doctorFN, doctorLN from patient, doctor where patient.doctorID = doctor.doctorID")
rows4 = dbCursor.fetchall()
for pfn, pln, dfn, dln in rows4:
    print(f"Patient: {pfn} {pln} \t Doctor: {dfn} {dln}")
#Select 5 statement
dbCursor.execute("Select patientFN, patientLN, surgeryDesc, doctorFN, doctorLN from patient, surgery, doctor where surgery.doctorID = doctor.doctorID and surgery.patientID = patient.patientID order by surgeryDesc")
rows5 = dbCursor.fetchall()
for pfn, pln, sd, dfn, dln in rows5:
    print(f"Patient: {pfn} {pln} \t Surgery: {sd} \t Doctor: {dfn} {dln}")
#Select 6 statement
dbCursor.execute("Select surgeryDesc, sum(surgerycost) Cost from surgery group by surgeryDesc")
rows6 = dbCursor.fetchall()
total = 0
for sd, sc in rows6:
    print(f"Surgery: {sd} \t Surgery Cost: {sc}")
    total += sc
print(f"Total Cost is: ${total}")
