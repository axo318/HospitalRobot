package com.example.s1651374.papadocapp;

import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.InputType;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;

public class QuestionsActivity extends AppCompatActivity {

    public ArrayList questions = new ArrayList(5);

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_questions);

        questions.add("H");
        questions.add("e");
        questions.add("l");
        questions.add("l");

        if (!(questions.size() == 0)) {
            populateScroll();
        }
        ImageButton addButton = findViewById(R.id.addButton);
        ImageButton deleteButton = findViewById(R.id.deleteButton);

        addButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (questions.size() == 5) {
                    Toast.makeText(QuestionsActivity.this, "You have added the maximum amount of questions",
                            Toast.LENGTH_SHORT).show();
                } else {

                    AlertDialog.Builder builder = new AlertDialog.Builder(QuestionsActivity.this);
                    builder.setTitle("Title");

// Set up the input
                    final EditText input = new EditText(QuestionsActivity.this);
// Specify the type of input expected; this, for example, sets the input as a password, and will mask the text
                    input.setInputType(InputType.TYPE_CLASS_TEXT | InputType.TYPE_TEXT_VARIATION_SHORT_MESSAGE);
                    builder.setView(input);

// Set up the buttons
                    builder.setPositiveButton("OK", new DialogInterface.OnClickListener() {
                        @Override
                        public void onClick(DialogInterface dialog, int which) {
                            questions.add(input.getText().toString());
                            populateScroll();
                        }
                    });
                    builder.setNegativeButton("Cancel", new DialogInterface.OnClickListener() {
                        @Override
                        public void onClick(DialogInterface dialog, int which) {
                            dialog.cancel();
                        }
                    });

                    builder.show();

                    populateScroll();
                }
            }
        });

    }


    public void populateScroll() {

        TextView question1 = findViewById(R.id.question1);
        TextView question2 = findViewById(R.id.question2);
        TextView question3 = findViewById(R.id.question3);
        TextView question4 = findViewById(R.id.question4);
        TextView question5 = findViewById(R.id.question5);

        if (questions.size() == 5) {
            String q1 = questions.get(0).toString();
            String q2 = questions.get(1).toString();
            String q3 = questions.get(2).toString();
            String q4 = questions.get(3).toString();
            String q5 = questions.get(4).toString();

            question1.setText(q1);
            question2.setText(q2);
            question3.setText(q3);
            question4.setText(q4);
            question5.setText(q5);
        }
        else if (questions.size() == 4) {
            String q1 = questions.get(0).toString();
            String q2 = questions.get(1).toString();
            String q3 = questions.get(2).toString();
            String q4 = questions.get(3).toString();

            question1.setText(q1);
            question2.setText(q2);
            question3.setText(q3);
            question4.setText(q4);
        }
        else if (questions.size() == 3) {
            String q1 = questions.get(0).toString();
            String q2 = questions.get(1).toString();
            String q3 = questions.get(2).toString();

            question1.setText(q1);
            question2.setText(q2);
            question3.setText(q3);
        }
        else if (questions.size() == 2) {
            String q1 = questions.get(0).toString();
            String q2 = questions.get(1).toString();
            question1.setText(q1);
            question2.setText(q2);
        }
        else if (questions.size() == 1) {
            String q1 = questions.get(0).toString();
            question1.setText(q1);
        }

    }
}
