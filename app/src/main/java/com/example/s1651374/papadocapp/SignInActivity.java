package com.example.s1651374.papadocapp;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.view.WindowManager;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;

public class SignInActivity extends AppCompatActivity {

    private ListView listView;
    private ArrayAdapter arrayAdapter;
    private ArrayList<String> choices = new ArrayList<>();
    private String chosen = " ";

    private EditText emailField;
    private EditText passwordField;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sign_in);

        emailField = findViewById(R.id.SignIn_EditText1);
        passwordField = findViewById(R.id.SignIn_EditText2);
        emailField.setText("");
        passwordField.setText("");

        Button docButton = findViewById(R.id.docButton);
        docButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(SignInActivity.this, DoctorMenuActivity.class);
                startActivity(intent);
            }
        });

        getWindow().setSoftInputMode(WindowManager.LayoutParams.SOFT_INPUT_ADJUST_NOTHING);

        choices.add("Receptionist");
        choices.add("Doctor");

        listView = (ListView) findViewById(R.id.SignIn_ListView1);
        arrayAdapter = new ArrayAdapter(SignInActivity.this,
                R.layout.my_layout, R.id.row_layout, choices);
        listView.setAdapter(arrayAdapter);
        listView.setChoiceMode(ListView.CHOICE_MODE_SINGLE);

        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                chosen = ((TextView) view).getText().toString();
            }
        });

    }

    public void userLogin(View view) {
        if (TextUtils.isEmpty(emailField.getText().toString()) &&
                TextUtils.isEmpty(passwordField.getText().toString())) {
            emailField.setError("Required");
            passwordField.setError("Required");
            Toast.makeText(this, "Authentication failed.",
                    Toast.LENGTH_SHORT).show();
        } else if (TextUtils.isEmpty(emailField.getText().toString())) {
            emailField.setError("Required");
            Toast.makeText(this, "Authentication failed.",
                    Toast.LENGTH_SHORT).show();
        } else if (TextUtils.isEmpty(passwordField.getText().toString())){
            passwordField.setError("Required");
            Toast.makeText(this, "Authentication failed.",
                    Toast.LENGTH_SHORT).show();
        }
        else {
            // This is where the user will be able to sign into an existing account via whichever
            // method ends up being chosen.  For now it takes them to the Main Menu.
            Intent intent = new Intent(SignInActivity.this, ReceptionistMenuActivity.class);
            SignInActivity.this.startActivity(intent);
        }
    }

    public void userSignup(View view) {
        if (TextUtils.isEmpty(emailField.getText().toString()) &&
                TextUtils.isEmpty(passwordField.getText().toString())) {
            emailField.setError("Required");
            passwordField.setError("Required");
            Toast.makeText(this, "Please enter a valid email address and password",
                    Toast.LENGTH_LONG).show();
        } else if (TextUtils.isEmpty(emailField.getText().toString())) {
            emailField.setError("Required");
            Toast.makeText(this, "Please enter a valid email address",
                    Toast.LENGTH_LONG).show();
        } else if (TextUtils.isEmpty(passwordField.getText().toString())){
            passwordField.setError("Required");
            Toast.makeText(this, "Please enter a valid password",
                    Toast.LENGTH_LONG).show();
        } else if (chosen.equals(" ")) {
            Toast.makeText(this, "You must select to create either a Receptionist or" +
                    " Doctor account", Toast.LENGTH_LONG).show();
        }
        else {
            // This is where the user will be able to create an account via whichever method ends
            // up being chosen.  For now it takes them to the Main Menu.
            Intent intent = new Intent(SignInActivity.this, ReceptionistMenuActivity.class);
            SignInActivity.this.startActivity(intent);
        }
    }

}