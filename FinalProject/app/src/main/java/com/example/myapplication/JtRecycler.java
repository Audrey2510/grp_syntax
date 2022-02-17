package com.example.myapplication;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;

public class JtRecycler extends RecyclerView.Adapter<JtRecycler.MyViewHolder>{

    Context context;
    ArrayList<java_category>java_categories;



    public JtRecycler(Context context, ArrayList<java_category>java_categories){

        this.context = context;
        this.java_categories = java_categories;

    }

    @NonNull
    @Override
    public JtRecycler.MyViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {

        LayoutInflater inflater = LayoutInflater.from(context);
        View view = inflater.inflate(R.layout.java_recycler_row, parent);

        return new JtRecycler.MyViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull JtRecycler.MyViewHolder holder, int position) {

        holder.txtjava.setText(java_categories.get(position).getJava_topic());
        holder.imgview.setImageResource(java_categories.get(position).getImg());

    }

    @Override
    public int getItemCount() {
        return java_categories.size();
    }

    public static class MyViewHolder extends RecyclerView.ViewHolder{

        ImageView imgview;
        TextView txtjava;

        public MyViewHolder(@NonNull View itemView){
            super(itemView);

            imgview = itemView.findViewById(R.id.imageView6);
            txtjava = itemView.findViewById(R.id.textView12);

        }

    }

}
