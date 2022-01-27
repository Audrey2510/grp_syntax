package com.example.myapplication.ProgrammingLanguages;

import androidx.appcompat.app.AppCompatActivity;
import androidx.cardview.widget.CardView;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

import com.example.myapplication.R;
import com.example.myapplication.html.Attributes;
import com.example.myapplication.html.Elements;
import com.example.myapplication.html.HTML_Introduction;
import com.example.myapplication.html.colors;
import com.example.myapplication.html.comment;
import com.example.myapplication.html.hbasics;
import com.example.myapplication.html.tables;

public class HTML extends AppCompatActivity implements View.OnClickListener{

    public CardView card1,card2,card3,card4,card5,card6,card7;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        getSupportActionBar().setTitle("HTML");
        getSupportActionBar().setDisplayHomeAsUpEnabled(true);

        card1 = (CardView) findViewById(R.id.Intro);
        card2 = (CardView) findViewById(R.id.basic);
        card3 = (CardView) findViewById(R.id.elements);
        card4 = (CardView) findViewById(R.id.attributes);
        card5 = (CardView) findViewById(R.id.comments);
        card6 = (CardView) findViewById(R.id.colors);
        card7 = (CardView) findViewById(R.id.tables);


        card1.setOnClickListener(this);
        card2.setOnClickListener(this);
        card3.setOnClickListener(this);
        card4.setOnClickListener(this);
        card5.setOnClickListener(this);
        card6.setOnClickListener(this);


    }

    @Override
    public void onClick(View v) {

        Intent i;

        switch (v.getId()) {

            case R.id.Intro:
                i = new Intent(this, HTML_Introduction.class);
                startActivity(i);
                break;

            case R.id.basic:
                i = new Intent(this, hbasics.class);
                startActivity(i);
                break;

            case R.id.elements:
                i = new Intent(this, Elements.class);
                startActivity(i);
                break;

            case R.id.attributes:
                i = new Intent(this, Attributes.class);
                startActivity(i);
                break;

            case R.id.comments:
                i = new Intent(this, comment.class);
                startActivity(i);
                break;

            case R.id.colors:
                i = new Intent(this, colors.class);
                startActivity(i);
                break;

            case R.id.tables:
                i = new Intent(this, tables.class);
                startActivity(i);
                break;
        }

    }
}