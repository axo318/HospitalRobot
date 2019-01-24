package com.example.s1651374.papadocapp;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class PatientInfoActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_patient_info);
    }

    // This function must be updated to connect and send the information to the PapaDoc robot.
    // The moving to MainMenu could be changed to move to a confirmation/error screen to inform the
    // receptionist as to whether or not the PapaDoc received the information correctly.
    public void sendToPapaDoc(View view) {
        Intent intent = new Intent(PatientInfoActivity.this, ReceptionistMenuActivity.class);
        PatientInfoActivity.this.startActivity(intent);
    }

}