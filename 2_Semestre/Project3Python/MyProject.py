# ====================================================================

import math
import pandas as pd
import os

# ====================================================================

def fetchDocuments(filesPath):

    dataframes = []

    for filee in os.listdir(filesPath):
        if filee.endswith(".csv"):
            completePath = os.path.join(filesPath, filee)
            df = pd.read_csv(completePath)
            dataframes.append(df)
    
    return dataframes

# ====================================================================

def mergeTables(tables):

    finalTable = tables[0]

    for df in tables[1:]:
        finalTable = pd.merge(finalTable, df, on="Student", how="left")

    return finalTable

# ====================================================================

def includeScoreAndGrade(table):

    cols = ["Proj1", "Proj2", "Test1", "Test2"]

    for index, row in table.iterrows():
        absent = False
        failed = False

        for col in cols:
            value = row[col]

            if pd.isna(value):
                absent = True

            if value < 8:
                failed = True

        score = calculateScore(table.loc[index])
        table.loc[index, "Score"] = score

        if failed:
            table.loc[index, "Grade"] = "F"
        elif absent:
            table.loc[index, "Grade"] = "ABS"
        else:
            table.loc[index, "Grade"] = defineGrade(score)

    return table

# ====================================================================

def calculateScore(row):

    totalSum = (
        (0 if pd.isna(row["Test1"]) else row["Test1"]) * 0.3 +
        (0 if pd.isna(row["Test2"]) else row["Test2"]) * 0.3 +
        (0 if pd.isna(row["Proj1"]) else row["Proj1"]) * 0.2 +
        (0 if pd.isna(row["Proj2"]) else row["Proj2"]) * 0.2
    )

    return math.ceil(totalSum)

# ====================================================================

def defineGrade(avg):
    
    if avg >= 19 and avg <= 20:
        grade = "A+"
    elif avg >= 17 and avg <= 18:
        grade = "A"
    elif avg == 16:
        grade = "A-"
    elif avg >= 14 and avg <= 15:
        grade = "B"
    elif avg >= 11 and avg <= 13:
        grade = "C"
    elif avg == 10:
        grade = "D"
    else:
        grade = "F"
    
    return grade

# ====================================================================

def generateReportForAbsentStudents(table):
    
    report = pd.DataFrame(columns=["Student", "Name", "MissingCount", "MissingCols"])
    cols = ["Proj1", "Proj2", "Test1", "Test2"]

    for index, row in table.iterrows():
        
        if row["Grade"] != "ABS":
            continue

        missing_count = 0
        missing_cols = []
        
        for col in cols:
            value = row[col]

            if pd.isna(value):
                missing_count += 1
                missing_cols.append(col)

        report.loc[len(report)] = [row["Student"], row["Name"], missing_count, ",".join(missing_cols)]
        
    report.to_csv("GeneratedDocs/report.csv", index=False)

    return report

# ====================================================================

def generateStatistics(table):

    total_students = len(table)

    passing_grades = ["A+", "A", "A-", "B", "C", "D"]
    passed_all = table["Grade"].isin(passing_grades).sum()

    percent_passed_all = (passed_all / total_students) * 100

    completed = table[table["Grade"] != "ABS"]
    completed_total = len(completed)

    passed_completed = completed["Grade"].isin(passing_grades).sum()

    percent_passed_completed = (
        (passed_completed / completed_total) * 100
        if completed_total > 0 else 0
    )

    absent_students = table["Grade"].eq("ABS").sum()
    percent_absent = (absent_students / total_students) * 100

    stats = {
        "Total Students": total_students,
        "Passed (All)": round(percent_passed_all, 2),
        "Passed (Completed Only)": round(percent_passed_completed, 2),
        "Absent (%)": round(percent_absent, 2)
    }

    statsDF = pd.DataFrame([stats])

    statsDF.to_csv("GeneratedDocs/stats.csv", index=False)

    return statsDF

# ====================================================================

def main():
   
    currentDirectory = os.path.dirname(os.path.abspath(__file__))
    dtfrm = fetchDocuments(os.path.join(currentDirectory, "SupportFiles"))

    mainTable = mergeTables(dtfrm)
    mainTable = includeScoreAndGrade(mainTable)

    absentsReport = generateReportForAbsentStudents(mainTable)
    statsReport = generateStatistics(mainTable)

    print("\n")
    print("############ MAIN TABLE ############")
    print("\n")
    print(mainTable)
    print("\n")
    print("############ ABSENTS REPORT ############")
    print("\n")
    print(absentsReport)
    print("\n")
    print("############ STATISTICS ############")
    print("\n")
    print(statsReport)
    print("\n")

    return 0

main()

# ====================================================================
