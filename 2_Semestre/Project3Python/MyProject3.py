# ====================================================================

import math
import pandas as pd
import os
import matplotlib as mpl
import matplotlib.pyplot as plt

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

    finalTable = None

    for df in tables:
        if finalTable is None:
            finalTable = df
        else:
            finalTable = pd.merge(finalTable, df, on="Student", how="left")

    return finalTable

# ====================================================================

def includeScoreAndGrade(table):

    cols = ["Proj1", "Proj2", "Test1", "Test2"]

    for index, row in table.iterrows():

        absent = False
        failed = False
        invalid = False

        for col in cols:

            value = row[col]

            if pd.isna(value):
                absent = True

            if not pd.isna(value) and value < 8:
                failed = True

            if not pd.isna(value) and (value < 0 or value > 20):
                invalid = True
                print("The student", row["Student"], "has an invalid score for", col)

        if invalid:

            score = None
            grade = None

            print(
                "The student",
                row["Student"],
                "has invalid values. Score and Grade definition have failed."
            )

        else:

            score = calculateScore(table.loc[index])

            if failed:
                grade = "F"

            elif absent:
                grade = "ABS"

            else:
                grade = defineGrade(score)

        table.loc[index, "Score"] = score
        table.loc[index, "Grade"] = grade

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

def defineGrade(scr):

    if scr >= 19 and scr <= 20:
        grade = "A+"

    elif scr >= 17 and scr <= 18:
        grade = "A"

    elif scr == 16:
        grade = "A-"

    elif scr >= 14 and scr <= 15:
        grade = "B"

    elif scr >= 11 and scr <= 13:
        grade = "C"

    elif scr == 10:
        grade = "D"

    else:
        grade = "F"

    return grade

# ====================================================================

def generateReportForAbsentStudents(table):

    report = pd.DataFrame(
        columns=["Student", "Name", "MissingCount", "MissingCols"]
    )

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

        report.loc[len(report)] = [
            row["Student"],
            row["Name"],
            missing_count,
            ",".join(missing_cols)
        ]

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

def generatePlots(table):

    # ============================================================
    # HISTOGRAM OF NUMERIC SCORES
    # ============================================================

    plt.figure(figsize=(10, 5))

    scores = table["Score"].dropna()

    values, bins, bars = plt.hist(
        scores,
        bins=range(0, 22),
        rwidth=0.7,
        align="left",
        color="skyblue",
        edgecolor="black"
    )

    plt.title("Class Grades Histogram")
    plt.xlabel("Numeric Grades [0-20]")
    plt.ylabel("Frequency")
    plt.xticks(range(0, 21))

    for i, bar in enumerate(bars.patches):

        if values[i] > 0:

            plt.annotate(
                str(int(values[i])),
                (
                    bar.get_x() + bar.get_width() / 2,
                    bar.get_height()
                ),
                ha="center",
                va="bottom"
            )

    plt.tight_layout()

    plt.savefig("GeneratedDocs/HistogramScore.pdf")

    plt.close()

    # ============================================================
    # BAR PLOT OF LETTER GRADES
    # ============================================================

    plt.figure(figsize=(8, 5))

    grade_categories = ["ABS", "F", "D", "C", "B", "A-", "A", "A+"]

    grades = table["Grade"].tolist()

    counts = [grades.count(g) for g in grade_categories]

    bars = plt.bar(
        grade_categories,
        counts,
        color="orange",
        edgecolor="black"
    )

    plt.title("Class Letter Grade Distribution")
    plt.xlabel("Letter Grade")
    plt.ylabel("Frequency")

    for i, bar in enumerate(bars):

        if counts[i] > 0:

            plt.annotate(
                str(counts[i]),
                (
                    bar.get_x() + bar.get_width() / 2,
                    bar.get_height()
                ),
                ha="center",
                va="bottom"
            )

    plt.tight_layout()

    plt.savefig("GeneratedDocs/LetterGradeBar.pdf")

    plt.close()

# ====================================================================

def main():

    currentDirectory = os.path.dirname(os.path.abspath(__file__))

    generatedDocsPath = os.path.join(currentDirectory, "GeneratedDocs")

    os.makedirs(generatedDocsPath, exist_ok=True)

    dtfrm = fetchDocuments(
        os.path.join(currentDirectory, "SupportFiles")
    )

    mainTable = mergeTables(dtfrm)

    mainTable = includeScoreAndGrade(mainTable)

    absentsReport = generateReportForAbsentStudents(mainTable)

    statsReport = generateStatistics(mainTable)

    generatePlots(mainTable)

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
    print("Graphs successfully generated in GeneratedDocs/")
    print("\n")

    return 0

# ====================================================================

main()

# ====================================================================