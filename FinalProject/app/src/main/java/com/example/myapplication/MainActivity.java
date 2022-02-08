package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;
import androidx.cardview.widget.CardView;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;



public class MainActivity extends AppCompatActivity implements View.OnClickListener{

    public CardView card1,card2,card3,card4,card5,card6, card7;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        card1 = (CardView) findViewById(R.id.html);
        card2 = (CardView) findViewById(R.id.java);
        card3 = (CardView) findViewById(R.id.python);
        card4 = (CardView) findViewById(R.id.sql);
        card5 = (CardView) findViewById(R.id.vb);
        card6 = (CardView) findViewById(R.id.as);



        card1.setOnClickListener(this);
        card2.setOnClickListener(this);
        card3.setOnClickListener(this);
        card4.setOnClickListener(this);
        card5.setOnClickListener(this);
        card6.setOnClickListener(this);
        card7.setOnClickListener(this);


    }

    @Override
    public void onClick(View v) {

        Intent i;

        switch (v.getId()) {

            case R.id.html:
                i = new Intent(this, html.class);
                startActivity(i);
                break;

            case R.id.java:
                i = new Intent(this, java.class);
                startActivity(i);
                break;

            case R.id.python:
                i = new Intent(this, python.class);
                startActivity(i);
                break;

            case R.id.sql:
                i = new Intent(this, sql.class);
                startActivity(i);
                break;

            case R.id.vb:
                i = new Intent(this, vb_net.class);
                startActivity(i);
                break;

            case R.id.as:
                i = new Intent(this, android.class);
                startActivity(i);
                break;


        }

    }
}