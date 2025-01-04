import streamlit as st
import pandas as pd

# Title of the application
st.title("2024 Fall DeFi Semester Final Grades")

# Provide the path to the CSV file
csv_file_path = "data.csv"  # Replace with the actual path to your CSV file
df = pd.read_csv(csv_file_path)

# Handle missing values by filling them with 0
df.fillna(0, inplace=True)

# Input for the student's name
name = st.text_input("Please enter the student's name:")

if name:
    # Search for the student's name in the 'Student' column
    for student in df['Student']:
        if name in student:
            student_data = df[df['Student'] == student]

            st.write(f"Searching for student: {student}")

            # Get Homework 0-4 scores for the student
            homework_scores = student_data[['Homework 0', 'Homework 1', 'Homework 2', 'Homework 3', 'Homework 4']]
            homework_total = 100 + int(homework_scores['Homework 1']) + int(homework_scores['Homework 2']) + int(homework_scores['Homework 3']) + int(homework_scores['Homework 4'])
            
            st.text(f"Homework Scores: {homework_total:.2f}")
            st.write(homework_scores)

            # Get Exercise 1-10 scores for the student
            exercise_scores = student_data[
                ['Exercise 1', 'Exercise 2', 'Exercise 3', 'Exercise 4', 
                 'Exercise 5', 'Exercise 6', 'Exercise 7', 'Exercise 8', 
                 'Exercise 9', 'Exercise 10']
            ]
            exercise_total = exercise_scores.sum(axis=1).iloc[0]
            st.text(f"Exercise Scores: {exercise_total:.2f}")
            st.write(exercise_scores)

            # Get Midterm and Final scores for the student
            exam_scores = student_data[['Midterm Exam', 'Final Exam']]
            exam_total = exam_scores.sum(axis=1).iloc[0]
            st.text(f"Exam Scores: {exam_total:.2f}")
            st.write(exam_scores)

            # Get Class Participation score for the student
            participation_total = student_data[['Class Participation']].iloc[0, 0]
            st.text(f"Class Participation Score: {participation_total:.2f}")

            # Get Bonus score for the student
            bonus_total = student_data[['Bonus']].iloc[0, 0]
            st.text(f"Bonus Score: {bonus_total:.2f}")

            table_data = {
                "Category": [
                    "Homework 0",
                    "Homework 1",
                    "Homework 2",
                    "Homework 3",
                    "Homework 4",
                    "Exercise 1-10",
                    "Midterm Exam",
                    "Final Exam",
                    "Class Participation",
                    "Bonus"
                ],
                "Weight": [
                    "5%",
                    "10%",
                    "10%",
                    "10%",
                    "10%",
                    "10% (each 1%)",
                    "20%",
                    "20%",
                    "5%",
                    ""
                ],
                "Value": [
                    100,
                    float(homework_scores['Homework 1']),
                    float(homework_scores['Homework 2']),
                    float(homework_scores['Homework 3']),
                    float(homework_scores['Homework 4']),
                    round(float(exercise_total), 2),
                    round(float(exam_scores['Midterm Exam']), 2),
                    round(float(exam_scores['Final Exam']), 2),
                    round(int(participation_total), 2),
                    round(float(bonus_total), 2)
                ],
                "Score": [
                    5,
                    round(float(homework_scores['Homework 1']) * 0.1, 2),
                    round(float(homework_scores['Homework 2']) * 0.1, 2),
                    round(float(homework_scores['Homework 3']) * 0.1, 2),
                    round(float(homework_scores['Homework 4']) * 0.1, 2),
                    round(float(exercise_total) * 1, 2),
                    round(float(exam_scores['Midterm Exam']) * 0.2, 2),
                    round(float(exam_scores['Final Exam']) * 0.2, 2),
                    round(int(participation_total) * 0.05, 2),
                    round(float(bonus_total) * 0.05, 2)
                ]
            }
            # Create a DataFrame
            score_df = pd.DataFrame(table_data)

            # Display the table
            st.subheader("Final Grading Breakdown")
            st.table(score_df)

            st.write(f"Total Score: {round(float(student_data['Final']), 2)} GPA: {student_data['GPA'].iloc[0]}")
            st.balloons()
            break
