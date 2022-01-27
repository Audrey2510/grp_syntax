package com.example.myapplication.ProgrammingLanguages;

import androidx.appcompat.app.AppCompatActivity;
import androidx.cardview.widget.CardView;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import com.example.myapplication.Android.AVD;
import com.example.myapplication.Android.Basics;
import com.example.myapplication.Android.Configure;
import com.example.myapplication.Android.Introduction;
import com.example.myapplication.Android.menu_toast_notif;
import com.example.myapplication.Android.run;
import com.example.myapplication.R;


public class Android extends AppCompatActivity implements View.OnClickListener {


    public CardView card1, card2, card3, card4, card5, card6, card7, card8;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        


        card1 = (CardView) findViewById(R.id.Introduction);
        card2 = (CardView) findViewById(R.id.Basics);
        card3 = (CardView) findViewById(R.id.create);
        card4 = (CardView) findViewById(R.id.avd);
        card5 = (CardView) findViewById(R.id.Configure);
        card6 = (CardView) findViewById(R.id.run);
        card7 = (CardView) findViewById(R.id.tmn);




        card1.setOnClickListener(this);
        card2.setOnClickListener(this);
        card3.setOnClickListener(this);
        card4.setOnClickListener(this);
        card5.setOnClickListener(this);
        card6.setOnClickListener(this);
        card7.setOnClickListener(this);
        card8.setOnClickListener(this);





    }

    @Override
    public void onClick(View v) {

        Intent i;

        switch (v.getId()) {

            case R.id.Introduction:
                i = new Intent(this, Introduction.class);
                startActivity(i);
                break;

            case R.id.Basics:
                i = new Intent(this, Basics.class);
                startActivity(i);
                break;

            case R.id.avd:
                i = new Intent(this, AVD.class);
                startActivity(i);
                break;

            case R.id.Configure:
                i = new Intent(this, Configure.class);
                startActivity(i);
                break;

            case R.id.run:
                i = new Intent(this, run.class);
                startActivity(i);
                break;

            case R.id.tmn:
                i = new Intent(this, menu_toast_notif.class);
                startActivity(i);
                break;



        }

    }
}
