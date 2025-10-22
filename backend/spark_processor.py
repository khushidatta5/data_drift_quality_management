from pyspark.sql import SparkSession
from pyspark.sql import DataFrame
import pandas as pd
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)

class SparkDataProcessor:
    def __init__(self):
        """Initialize Spark session"""
        self.spark = SparkSession.builder \
            .appName("DataDriftQualitySystem") \
            .config("spark.driver.memory", "2g") \
            .config("spark.executor.memory", "2g") \
            .getOrCreate()
        
        # Set log level to reduce noise
        self.spark.sparkContext.setLogLevel("WARN")
        logger.info("Spark session initialized successfully")
    
    def pandas_to_spark(self, df_pandas: pd.DataFrame) -> DataFrame:
        """Convert pandas DataFrame to Spark DataFrame"""
        try:
            spark_df = self.spark.createDataFrame(df_pandas)
            return spark_df
        except Exception as e:
            logger.error(f"Error converting pandas to spark: {str(e)}")
            raise
    
    def spark_to_pandas(self, spark_df: DataFrame) -> pd.DataFrame:
        """Convert Spark DataFrame to pandas DataFrame"""
        try:
            return spark_df.toPandas()
        except Exception as e:
            logger.error(f"Error converting spark to pandas: {str(e)}")
            raise
    
    def get_basic_stats(self, df: DataFrame) -> Dict[str, Any]:
        """Get basic statistics for a Spark DataFrame"""
        try:
            stats = {}
            
            # Get column types
            stats['column_types'] = {field.name: str(field.dataType) for field in df.schema.fields}
            
            # Get numeric columns
            numeric_cols = [field.name for field in df.schema.fields 
                          if str(field.dataType) in ['IntegerType', 'LongType', 'FloatType', 'DoubleType']]
            
            if numeric_cols:
                # Get summary statistics for numeric columns
                summary = df.select(numeric_cols).summary().toPandas()
                stats['numeric_summary'] = summary.to_dict()
            
            return stats
        except Exception as e:
            logger.error(f"Error getting basic stats: {str(e)}")
            return {}
    
    def clean_data(self, df: DataFrame) -> DataFrame:
        """Basic data cleaning operations"""
        try:
            # Remove duplicate rows
            df_clean = df.dropDuplicates()
            
            return df_clean
        except Exception as e:
            logger.error(f"Error cleaning data: {str(e)}")
            return df
    
    def stop(self):
        """Stop Spark session"""
        if self.spark:
            self.spark.stop()
            logger.info("Spark session stopped")