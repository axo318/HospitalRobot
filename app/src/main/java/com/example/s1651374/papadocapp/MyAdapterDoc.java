package com.example.s1651374.papadocapp;

import android.content.Intent;
import android.graphics.Color;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.TextView;


public class MyAdapterDoc extends RecyclerView.Adapter<MyAdapterDoc.MyViewHolder> {

    private String[] mDataset;
    private String[] mDataset2;

    // Provide a reference to the views for each data item
    // Complex data items may need more than one view per item, and
    // you provide access to all the views for a data item in a view holder
    public static class MyViewHolder extends RecyclerView.ViewHolder {
        // each data item is just a string in this case
        private TextView currency;
        private TextView value;
        private TextView colorCode;
        private Button viewResponse;

        public MyViewHolder(final View itemView) {
            super(itemView);
            colorCode = (TextView) itemView.findViewById(R.id.colorCode);
            currency = (TextView) itemView.findViewById(R.id.currency);
            value = (TextView) itemView.findViewById(R.id.value);
            viewResponse = (Button) itemView.findViewById(R.id.viewResponse);

            itemView.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    itemView.getContext().startActivity(new Intent(itemView.getContext(), PatientAnswersActivity.class));
                }
            });


        }
    }

    // Provide a suitable constructor (depends on the kind of dataset)
    public MyAdapterDoc(String[] myDataset, String[] myDataset2) {
        mDataset = myDataset;
        mDataset2 = myDataset2;
    }

    // Create new views (invoked by the layout manager)
    @Override
    public MyAdapterDoc.MyViewHolder onCreateViewHolder(ViewGroup parent,
                                                     int viewType) {
        // create a new view
        LinearLayout v = (LinearLayout) LayoutInflater.from(parent.getContext())
                .inflate(R.layout.rv_item_doc, parent, false);
        MyViewHolder vh = new MyViewHolder(v);
        return vh;
    }

    @Override
    public void onBindViewHolder(MyAdapterDoc.MyViewHolder holder, int position) {
        // - get element from your dataset at this position
        // - replace the contents of the view with that element
        holder.currency.setText(mDataset[position]);
        holder.value.setText(mDataset2[position]);
        if (mDataset2[position].equals("20/07/1968")){
            holder.colorCode.setBackgroundColor(Color.parseColor("#ff6961"));
        }
        else if (mDataset2[position].equals("08/09/1982")) {
            holder.colorCode.setBackgroundColor(Color.parseColor("#88dd77"));
        } else {
            holder.colorCode.setBackgroundColor(Color.parseColor("#fdf496"));
        }

//        holder.viewResponse.setOnClickListener(new View.OnClickListener(){
//            @Override
//            public void onClick(View v) {
//                itemView.getContext().startActivity(new Intent(itemView.getContext(), PatientInfoActivity.class));
//            }
//        });



    }


    // Return the size of your dataset (invoked by the layout manager)
    @Override
    public int getItemCount() {
        return mDataset.length;
    }
}