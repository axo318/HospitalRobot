package com.example.s1651374.papadocapp;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class ReceptionistMenuActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_receptionist_menu);
    }

    public void goToScheduleActivity(View view) {
        /*Intent intent = new Intent(ReceptionistMenuActivity.this, ScheduleActivity.class);
        ReceptionistMenuActivity.this.startActivity(intent);*/
    }

    public void goToAppointmentActivity(View view) {
        /*Intent intent = new Intent(ReceptionistMenuActivity.this, AppointmentActivity.class);
        ReceptionistMenuActivity.this.startActivity(intent);*/
    }

    public void goToSignInActivity(View view) {
        Intent intent = new Intent(ReceptionistMenuActivity.this, SignInActivity.class);
        ReceptionistMenuActivity.this.startActivity(intent);
    }

}