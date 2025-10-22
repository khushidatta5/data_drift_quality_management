from pyspark.sql import DataFrame
from pyspark.sql.functions import col, count, when, isnan, isnull
from typing import Dict, Any
import logging
import pandas as pd
import numpy as np

logger = logging.getLogger(__name__)

class DataQualityChecker:
    def __init__(self):
        pass
    
    def check_missing_values(self, df: DataFrame) -> Dict[str, Any]:
        """Check for missing values in each column"""
        try:
            total_rows = df.count()
            missing_info = {}
            
            for column in df.columns:
                missing_count = df.filter(
                    col(column).isNull() | isnan(col(column))
                ).count() if str(df.schema[column].dataType) in ['DoubleType', 'FloatType'] else df.filter(col(column).isNull()).count()
                
                missing_percentage = (missing_count / total_rows) * 100 if total_rows > 0 else 0
                
                missing_info[column] = {
                    'count': int(missing_count),
                    'percentage': round(missing_percentage, 2)
                }
            
            return {
                'total_rows': int(total_rows),
                'columns': missing_info
            }
        except Exception as e:
            logger.error(f"Error checking missing values: {str(e)}")
            return {}
    
    def check_duplicates(self, df: DataFrame) -> Dict[str, Any]:
        """Check for duplicate rows"""
        try:
            total_rows = df.count()
            unique_rows = df.dropDuplicates().count()
            duplicate_count = total_rows - unique_rows
            
            return {
                'total_rows': int(total_rows),
                'unique_rows': int(unique_rows),
                'duplicate_count': int(duplicate_count),
                'duplicate_percentage': round((duplicate_count / total_rows) * 100, 2) if total_rows > 0 else 0
            }
        except Exception as e:
            logger.error(f"Error checking duplicates: {str(e)}")
            return {}
    
    def detect_outliers(self, df: DataFrame) -> Dict[str, Any]:
        """Detect outliers using IQR method for numeric columns"""
        try:
            outliers_info = {}
            
            # Get numeric columns
            numeric_cols = [field.name for field in df.schema.fields 
                          if str(field.dataType) in ['IntegerType', 'LongType', 'FloatType', 'DoubleType', 'DecimalType']]
            
            for column in numeric_cols:
                # Convert to pandas for easier calculation
                col_data = df.select(column).toPandas()[column].dropna()
                
                if len(col_data) > 0:
                    Q1 = col_data.quantile(0.25)
                    Q3 = col_data.quantile(0.75)
                    IQR = Q3 - Q1
                    
                    lower_bound = Q1 - 1.5 * IQR
                    upper_bound = Q3 + 1.5 * IQR
                    
                    outliers = col_data[(col_data < lower_bound) | (col_data > upper_bound)]
                    outlier_count = len(outliers)
                    
                    outliers_info[column] = {
                        'count': int(outlier_count),
                        'percentage': round((outlier_count / len(col_data)) * 100, 2),
                        'lower_bound': float(lower_bound),
                        'upper_bound': float(upper_bound)
                    }
            
            return outliers_info
        except Exception as e:
            logger.error(f"Error detecting outliers: {str(e)}")
            return {}
    
    def check_data_types(self, df: DataFrame) -> Dict[str, str]:
        """Get data types for all columns"""
        try:
            return {field.name: str(field.dataType) for field in df.schema.fields}
        except Exception as e:
            logger.error(f"Error checking data types: {str(e)}")
            return {}
    
    def get_statistics(self, df: DataFrame) -> Dict[str, Any]:
        """Get comprehensive statistics for the dataset"""
        try:
            stats = {}
            
            # Get numeric columns
            numeric_cols = [field.name for field in df.schema.fields 
                          if str(field.dataType) in ['IntegerType', 'LongType', 'FloatType', 'DoubleType', 'DecimalType']]
            
            if numeric_cols:
                # Get summary statistics
                summary_df = df.select(numeric_cols).summary()
                summary_pandas = summary_df.toPandas()
                
                stats['numeric_summary'] = summary_pandas.to_dict('records')
            
            # Get categorical columns
            categorical_cols = [field.name for field in df.schema.fields 
                              if str(field.dataType) == 'StringType']
            
            stats['categorical_columns'] = categorical_cols
            stats['numeric_columns'] = numeric_cols
            
            # Get value counts for categorical columns (limited to first 5 columns)
            stats['categorical_summary'] = {}
            for col_name in categorical_cols[:5]:
                value_counts = df.groupBy(col_name).count().orderBy('count', ascending=False).limit(10).toPandas()
                stats['categorical_summary'][col_name] = value_counts.to_dict('records')
            
            return stats
        except Exception as e:
            logger.error(f"Error getting statistics: {str(e)}")
            return {}