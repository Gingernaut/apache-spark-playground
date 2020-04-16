package com.example

import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark._
import org.apache.spark.SparkConf
import org.apache.spark.sql.SparkSession


import java.io.File
object HelloSpark {
    
    def getSparkConfig: SparkConf = {
        new SparkConf()
          .setAppName("HelloWorld")
    }
    
    def main(args: Array[String]): Unit = {   
        println("creating Spark Context")
        
        val sc = SparkSession.builder.config(getSparkConfig).getOrCreate()
        
        val data = sc.read.textFile("/data/reddit1.txt")
        println(data.count())
        
        sc.stop()   
    }
}

HelloSpark.main(Array(""))