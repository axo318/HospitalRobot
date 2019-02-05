package com.example.s1651374.papadocapp;

import android.content.DialogInterface;
import android.content.Intent;
import android.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.ImageButton;
import android.util.Log;
import android.widget.Button;

import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.Socket;

public class PatientInfoActivity extends AppCompatActivity {

    String ipAddress;

    private static final String tag = "MainActivity";

    // Raspberry pi internal address and port
    public static final int SERVERPORT = 9999;
    public static String SERVER_IP = "192.168.105.102";

    private ClientThread clientThread;
    private Thread thread;
    private EditText msgToSend;
    private Button sendBtn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_patient_info);

        Log.d(tag,"[onCreate]: Has started");

        ImageButton ipFix = findViewById(R.id.ipButton);
        ipFix.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                final EditText txtUrl = new EditText(PatientInfoActivity.this);

// Set the default text to a link of the Queen

                new AlertDialog.Builder(PatientInfoActivity.this)
                        .setTitle("Enter new IP Address")
                        .setView(txtUrl)
                        .setPositiveButton("Okay", new DialogInterface.OnClickListener() {
                            public void onClick(DialogInterface dialog, int whichButton) {
                                SERVER_IP = txtUrl.getText().toString();
                            }
                        })
                        .setNegativeButton("Cancel", new DialogInterface.OnClickListener() {
                            public void onClick(DialogInterface dialog, int whichButton) {
                            }
                        })
                        .show();
            }
        });

        Button sendButton = findViewById(R.id.PInfo_Button1);
        sendButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (v.getId() == R.id.PInfo_Button1) {
                    connectAndSend("start");
                }
            }
        });
    }

    private void connectAndSend(String message) {
        Log.d(tag, "[connectToServer]: Connecting to server...");
        clientThread = new ClientThread();
        thread = new Thread(clientThread);
        thread.start();
        Log.d(tag, "[connectToServer]: Connected to server");
        if (null != clientThread) {
            Log.d(tag, "[onClick]: clientThread is not null, sending msg");
            clientThread.sendMessage(message);
        }else{
            Log.d(tag, "[onClick]: clientThread is null");
        }
    }


    class ClientThread implements Runnable {

        // Variable held in the class for each connection
        private Socket socket;

        @Override
        public void run() {
        }

        // Runs when the string gets sent
        void sendMessage(final String message) {
            new Thread(new Runnable() {
                @Override
                public void run() {
                    try {
                        socket = new Socket(SERVER_IP, SERVERPORT);
                        if (null != socket) {
                            PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(socket.getOutputStream())),true);
                            out.println(message);
                            socket.close();
                            return;
                        }
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                }
            }).start();
        }
    }



    // This function must be updated to connect and send the information to the PapaDoc robot.
    // The moving to MainMenu could be changed to move to a confirmation/error screen to inform the
    // receptionist as to whether or not the PapaDoc received the information correctly.
    public void sendToPapaDoc(View view) {
        Intent intent = new Intent(PatientInfoActivity.this, ReceptionistMenuActivity.class);
        PatientInfoActivity.this.startActivity(intent);
    }



}