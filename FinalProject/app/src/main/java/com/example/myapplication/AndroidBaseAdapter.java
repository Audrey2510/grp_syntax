package com.example.myapplication;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

public class AndroidBaseAdapter extends BaseAdapter {

    Context context;
    String listandroid[];
    int listandroidimages[];
    LayoutInflater inflater;



    public AndroidBaseAdapter(Context ctx, String[] androidlist, int[] androidimages) {

        this.context = ctx;
        this.listandroid = androidlist;
        this.listandroidimages = androidimages;
        inflater = LayoutInflater.from(ctx);

    }
    @Override
    public int getCount() {
        return listandroid.length;
    }

    @Override
    public Object getItem(int position) {
        return null;
    }

    @Override
    public long getItemId(int position) {
        return 0;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        convertView = inflater.inflate(R.layout.activity_android_list_view, null);
        TextView textView = (TextView) convertView.findViewById(R.id.as_intro);
        ImageView androidimages = (ImageView) convertView.findViewById(R.id.intro_logo);
        textView.setText(listandroid[position]);
        androidimages.setImageResource(listandroidimages[position]);
        return convertView;


    }
}
