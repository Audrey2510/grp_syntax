package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;
import androidx.cardview.widget.CardView;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.os.Bundle;
import android.view.View;

import java.util.ArrayList;

public class java extends AppCompatActivity{

    ArrayList<java_category> java_category = new ArrayList<>();
    int [] java_images = {R.drawable.a_basics, R.drawable.a_config, R.drawable.a_introduction, R.drawable.a_tmn, R.drawable.a_basics};

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_java);

        RecyclerView recyclerView = findViewById(R.id.java_recycler);

        setUpjava_categories();

        JtRecycler recycler = new JtRecycler(this, java_category);

        recyclerView.setAdapter(recycler);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));



    }

    private void setUpjava_categories(){
        String [] java_topics = getResources().getStringArray(R.array.java_topics);

        for (int i = 0; i<java_topics.length; i++) {
            java_category.add(new java_category (java_topics[i], java_images[i]));
        }
    }
}