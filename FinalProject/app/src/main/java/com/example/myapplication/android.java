package com.example.myapplication;

import android.content.Intent;
import android.os.Bundle;

import android.view.View;


import androidx.appcompat.app.AppCompatActivity;
import androidx.cardview.widget.CardView;


public class android extends AppCompatActivity implements View.OnClickListener {

    private CardView card1, card2, card3, card4, card5, card6;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        card1 = (CardView) findViewById(R.id.a_intro);
        card2 = (CardView) findViewById(R.id.a_basics);
        card3 = (CardView) findViewById(R.id.a_ui);
        card4 = (CardView) findViewById(R.id.create);
        card5 = (CardView) findViewById(R.id.avd);
        card6 = (CardView) findViewById(R.id.run);



        card1.setOnClickListener((View.OnClickListener) this);
        card2.setOnClickListener((View.OnClickListener) this);
        card3.setOnClickListener((View.OnClickListener) this);
        card4.setOnClickListener((View.OnClickListener) this);
        card5.setOnClickListener((View.OnClickListener) this);
        card6.setOnClickListener((View.OnClickListener) this);


    }

    @Override
    public void onClick(View v) {

        Intent i;

        switch (v.getId()) {

            case R.id.a_intro:
                i = new Intent(this,as_intro.class);
                startActivity(i);
                break;

            case R.id.a_basics:
                i = new Intent(this, as_basic.class);
                startActivity(i);
                break;

            case R.id.a_ui:
                i = new Intent(this, as_ui.class);
                startActivity(i);
                break;

            case R.id.create:
                i = new Intent(this, as_create.class);
                startActivity(i);
                break;

            case R.id.avd:
                i = new Intent(this, as_avd.class);
                startActivity(i);
                break;

            case R.id.run:
                i = new Intent(this, as_run.class);
                startActivity(i);
                break;



        }
    }
}


