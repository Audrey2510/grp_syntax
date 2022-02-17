package com.example.myapplication;

public class java_category {
    public String getJava_topic() {
        return java_topic;
    }

    public java_category(String java_topic, int java_image) {
        this.java_topic = java_topic;
    }

    String java_topic;

    public java_category(int img) {
        this.img = img;
    }

    public int getImg() {
        return img;
    }

    int img;
}
