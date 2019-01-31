package com.example.s1651374.papadocapp;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.Locale;

public class ScheduleActivity extends AppCompatActivity {

    private String currentDate = new SimpleDateFormat("yyyy/MM/dd", Locale.getDefault()).format(new Date());
    public ArrayList departments = new ArrayList(3);
    public ArrayList doctorsCardio = new ArrayList(3);
    public ArrayList dates = new ArrayList(3);
    public ArrayList times = new ArrayList(3);
    public Boolean chosen;

    public String[] appointment = new String[4];

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_schedule);

        chosen = false;

        TextView dateView = findViewById(R.id.currentDate);
        dateView.setText("Today's date: " + currentDate);

        departments.add("-");
        departments.add("Cardiology");
        departments.add("Neurology");
        departments.add("Minor Injuries");

        doctorsCardio.add("-");
        doctorsCardio.add("Dr. A");
        doctorsCardio.add("Dr. B");
        doctorsCardio.add("Dr. C");

        dates.add("-");
        dates.add("1/2/13");
        dates.add("2/2/13");
        dates.add("3/2/13");

        times.add("-");
        times.add("11:20");
        times.add("12:00");
        times.add("14:40");

        populatespinnerDep();

        Spinner deps = findViewById(R.id.spinnerDepartment);
        final Spinner docs = findViewById(R.id.spinnerDoctor);
        final Spinner datesS = findViewById(R.id.spinnerDate);
        final Spinner timesS = findViewById(R.id.spinnerTime);

        docs.setVisibility(View.GONE);
        datesS.setVisibility(View.GONE);
        timesS.setVisibility(View.GONE);



        deps.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
                String chosenDep = parent.getItemAtPosition(position).toString();
                appointment[0] = chosenDep;
                if (!chosenDep.equals("-")) {
                    docs.setVisibility(View.VISIBLE);
                }
                if (chosenDep == "Cardiology") {
                    populatespinnerDoc(doctorsCardio);
                }
            }

            @Override
            public void onNothingSelected(AdapterView<?> parent) {

            }
        });

        docs.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
                String chosenDoc = parent.getItemAtPosition(position).toString();
                appointment[1] = chosenDoc;
                if (!chosenDoc.equals("-")) {
                    datesS.setVisibility(View.VISIBLE);
                    populatespinnerDate(dates);
                }
            }

            @Override
            public void onNothingSelected(AdapterView<?> parent) {

            }
        });

        datesS.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
                String chosenDate = parent.getItemAtPosition(position).toString();
                appointment[2] = chosenDate;
                if (!chosenDate.equals("-")) {
                    timesS.setVisibility(View.VISIBLE);
                    populatespinnerTime(times);
                }
            }

            @Override
            public void onNothingSelected(AdapterView<?> parent) {

            }
        });

        timesS.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
                String chosenTime = parent.getItemAtPosition(position).toString();
                appointment[3] = chosenTime;
            }

            @Override
            public void onNothingSelected(AdapterView<?> parent) {

            }
        });

        Button appButton = findViewById(R.id.scheduleButton);
        appButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (!(appointment[0] == "-") && !(appointment[1] == "-") && !(appointment[2] == "-") && !(appointment[3] == "-") ) {
                    //send appointment away to be logged

                    //Check if patient in database
                    EditText name = findViewById(R.id.nameEdit);
                    name.setText("");
                    EditText dob = findViewById(R.id.dobEdit);
                    dob.setText("");
                    times.remove(appointment[3]);
                    populatespinnerTime(times);

                    docs.setVisibility(View.GONE);
                    datesS.setVisibility(View.GONE);
                    timesS.setVisibility(View.GONE);


                    if (times.size() == 1) {
                        dates.remove(appointment[2]);
                        populatespinnerDate(dates);
                        if (dates.size()== 1) {
                            dates.add("Fully booked");
                            }
                        }
                    }
                    else {
                    Toast.makeText(ScheduleActivity.this, "Please fill all fields",
                            Toast.LENGTH_SHORT).show();
                }


                }
        });

    }

    public void populatespinnerDep() {

        ArrayAdapter<String> adapter = new ArrayAdapter<String>(this, android.R.layout.simple_spinner_item, departments);

        Spinner deps = findViewById(R.id.spinnerDepartment);
        deps.setAdapter(adapter);

    }

    public void populatespinnerDoc(ArrayList input ) {
        ArrayAdapter<String> adapter2 = new ArrayAdapter<String>(this, android.R.layout.simple_spinner_item, input);

        Spinner docs = findViewById(R.id.spinnerDoctor);
        docs.setAdapter(adapter2);
    }
    public void populatespinnerDate(ArrayList input) {
        ArrayAdapter<String> adapter3 = new ArrayAdapter<String>(this, android.R.layout.simple_spinner_item, input);

        Spinner dates = findViewById(R.id.spinnerDate);
        dates.setAdapter(adapter3);

    }
    public void populatespinnerTime(ArrayList input) {
        ArrayAdapter<String> adapter4 = new ArrayAdapter<String>(this, android.R.layout.simple_spinner_item, input);

        Spinner times = findViewById(R.id.spinnerTime);
        times.setAdapter(adapter4);
    }
}
