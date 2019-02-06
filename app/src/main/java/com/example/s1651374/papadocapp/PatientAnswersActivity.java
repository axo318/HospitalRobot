package com.example.s1651374.papadocapp;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

public class PatientAnswersActivity extends AppCompatActivity {

    private String[] questions = new String[5];
    private String[] answers = new String[5];
    private String patient;
    private String app_time;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_patient_answers);

        TextView nameView = findViewById(R.id.PAns_TextView2);
        TextView timeView = findViewById(R.id.PAns_TextView4);
        TextView q1 = findViewById(R.id.PAns_Question1);
        TextView q2 = findViewById(R.id.PAns_Question2);
        TextView q3 = findViewById(R.id.PAns_Question3);
        TextView q4 = findViewById(R.id.PAns_Question4);
        TextView q5 = findViewById(R.id.PAns_Question5);
        TextView a1 = findViewById(R.id.PAns_Answer1);
        TextView a2 = findViewById(R.id.PAns_Answer2);
        TextView a3 = findViewById(R.id.PAns_Answer3);
        TextView a4 = findViewById(R.id.PAns_Answer4);
        TextView a5 = findViewById(R.id.PAns_Answer5);

        // Here we will populate the question and answer String arrays from wherever this is being
        // stored (likely database).  For now though, they will be manually populated to display
        // information.

        questions[0] = "Do you smoke?";
        questions[1] = "Do you drink more than 14 units of alcohol a week?";
        questions[2] = "Do you exercise more than 3 times a week?";
        questions[3] = "Have your symptoms worsened since your last visit?";
        questions[4] = "Is your favourite colour luminous orange?";
        answers[0] = "No";
        answers[1] = "No";
        answers[2] = "Yes";
        answers[3] = "Yes";
        answers[4] = "No";

        // Here we will initialise the patient and time info possibly from shared preferences
        // For now it will be manually populated

        patient = "John Smith";
        app_time = "14:30";

        // The TextFields can now be populated with these Strings

        nameView.setText(patient);
        timeView.setText(app_time);

        if (questions[0].equals(" ")) {
            q1.setText("No questions chosen.");
        }
        else {
            q1.setText(questions[0]);
            a1.setText(answers[0]);
            q2.setText(questions[1]);
            a2.setText(answers[1]);
            q3.setText(questions[2]);
            a3.setText(answers[2]);
            q4.setText(questions[3]);
            a4.setText(answers[3]);
            q5.setText(questions[4]);
            a5.setText(answers[4]);
        }
    }
}
