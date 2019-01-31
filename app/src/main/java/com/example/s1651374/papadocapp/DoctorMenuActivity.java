package com.example.s1651374.papadocapp;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class DoctorMenuActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_doctor_menu);
    }

    public void goToQuestionsActivity(View view) {
        Intent intent = new Intent(DoctorMenuActivity.this, QuestionsActivity.class);
        DoctorMenuActivity.this.startActivity(intent);
    }

    public void goToAppointmentActivity(View view) {
        Intent intent = new Intent(DoctorMenuActivity.this, DoctorAppListActivity.class);
        DoctorMenuActivity.this.startActivity(intent);
    }

    public void goToSignInActivity(View view) {
        Intent intent = new Intent(DoctorMenuActivity.this, SignInActivity.class);
        DoctorMenuActivity.this.startActivity(intent);
    }
}
