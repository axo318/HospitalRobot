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
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;

public class QuestionsActivity extends AppCompatActivity {

    public ArrayList<String> questions = new ArrayList();
    private ListView listView;
    private ArrayAdapter arrayAdapter;
    private String chosen;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_questions);

        questions.add("Do you smoke?");
        questions.add("Do you drink more than 14 units a week?");
        questions.add("Do you exercise more than three times a week?");
        questions.add("Have your symptoms worsened since your last visit?");

        ImageButton addButton = findViewById(R.id.addButton);
        final ImageButton deleteButton = findViewById(R.id.deleteButton);


        populateList();

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
                            populateList();
                        }
                    });
                    builder.setNegativeButton("Cancel", new DialogInterface.OnClickListener() {
                        @Override
                        public void onClick(DialogInterface dialog, int which) {
                            dialog.cancel();
                        }
                    });

                    builder.show();

                }
            }
        });

        deleteButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
               if (chosen == "") {
                   Toast.makeText(QuestionsActivity.this, "Please select a question to remove",
                           Toast.LENGTH_SHORT).show();
               }
               else {
                   for (int i = 0; i<questions.size(); i++) {
                       if (questions.get(i).equals(chosen)) {
                           questions.remove(i);
                           populateList();
                       }
                   }
               }
            }
            });

    }


    public void populateList() {

        chosen = "";

        listView = (ListView) findViewById(R.id.Questions_ListView1);
        arrayAdapter = new ArrayAdapter(QuestionsActivity.this,
                R.layout.questions_layout, R.id.row_layout, questions);
        listView.setAdapter(arrayAdapter);
        listView.setChoiceMode(ListView.CHOICE_MODE_SINGLE);

        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                final ImageButton deleteButton = findViewById(R.id.deleteButton);
                deleteButton.setVisibility(View.VISIBLE);
                TextView delLabel = findViewById(R.id.delLabel);
                delLabel.setVisibility(View.VISIBLE);
                chosen = ((TextView) view).getText().toString();
            }
        });
    }
}
