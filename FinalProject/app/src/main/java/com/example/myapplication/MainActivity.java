package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;
import androidx.cardview.widget.CardView;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;



public class MainActivity extends AppCompatActivity implements View.OnClickListener{

    private CardView card1,card2,card3,card4,card5,card6;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        card1 = (CardView) findViewById(R.id.cardView);
        card2 = (CardView) findViewById(R.id.cardView3);
        card3 = (CardView) findViewById(R.id.cardView4);
        card4 = (CardView) findViewById(R.id.cardView2);
        card5 = (CardView) findViewById(R.id.cardView5);
        card6 = (CardView) findViewById(R.id.cardview8);



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

            case R.id.cardView:
                i = new Intent(this, html.class);
                startActivity(i);
                break;

            case R.id.cardView3:
                i = new Intent(this, java.class);
                startActivity(i);
                break;

            case R.id.cardView4:
                i = new Intent(this, python.class);
                startActivity(i);
                break;

            case R.id.cardView2:
                i = new Intent(this, sql.class);
                startActivity(i);
                break;

            case R.id.cardView5:
                i = new Intent(this, vb_net.class);
                startActivity(i);
                break;

            case R.id.cardview8:
                i = new Intent(this, android.class);
                startActivity(i);
                break;


        }

    }
}