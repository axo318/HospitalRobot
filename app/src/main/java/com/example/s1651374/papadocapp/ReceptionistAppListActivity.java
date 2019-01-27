package com.example.s1651374.papadocapp;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;


public class ReceptionistAppListActivity extends AppCompatActivity {

    private RecyclerView mRecyclerView;
    private RecyclerView.Adapter mAdapter;
    private RecyclerView.LayoutManager mLayoutManager;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_receptionist_app_list);

        mRecyclerView = (RecyclerView) findViewById(R.id.my_recycler_view);

        // use this setting to improve performance if you know that changes
        // in content do not change the layout size of the RecyclerView
        mRecyclerView.setHasFixedSize(true);

        // use a linear layout manager
        mLayoutManager = new LinearLayoutManager(this);
        mRecyclerView.setLayoutManager(mLayoutManager);

        // specify an adapter (see also next example)
        mAdapter = new MyAdapter(new String[]{"John Smith", "Donna Paulsen", "Keira Marsh"}, new String[]{"20/07/1968", "17/04/1990", "06/11/2001"});
        mRecyclerView.setAdapter(mAdapter);
//
//        recyclerView_main.layoutManager = LinearLayoutManager(this@WalletActivity);
//        val names = setOf("John Smith", "Donna Paulsen", "Keira Marsh");
//        val dobs = setOf("06/11/1971", "08/12/1995", "21/07/1986");
//        recyclerView_main.adapter = CustomAdaptor(names.toMutableSet(), dobs.toMutableSet());
    }
}
