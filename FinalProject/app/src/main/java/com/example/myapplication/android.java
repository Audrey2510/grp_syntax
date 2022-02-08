package com.example.myapplication;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;

import androidx.appcompat.app.AppCompatActivity;



public class android extends AppCompatActivity {
    String androidlist[] = {"Introduction to Android Studio", "Android Studio Basics", "Creating Your First App in Android Studio", "What is AVD?", "Using and Configuring AVD", "How to make your app run", "Custom Menus, Notification, and Toast"};
    int androidImages []= {R.drawable.a_introduction, R.drawable.a_basics, R.drawable.a_create, R.drawable.a_avd, R.drawable.a_config, R.drawable.a_run,R.drawable.a_tmn };


    ListView listView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        listView = (ListView) findViewById(R.id.as_topiclist);
        AndroidBaseAdapter androidBaseAdapter = new AndroidBaseAdapter(getApplicationContext(), androidlist, androidImages);
        listView.setAdapter(androidBaseAdapter);
        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                Log.i("ANDROID_LIST_VIEW", "Item is clicked @ Position :: " +position);
            }
        });


    }
}


