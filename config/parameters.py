import numpy as np
import random

TARGET_COL = 'Attrition'




ORDINAL_CAT_FEATURES = ['BusinessTravel']
ORDINAL_CAT_ORDER = ['Non-Travel', 'Travel_Rarely', 'Travel_Frequently']

NUMERICAL_FEATURES = ['Education', 'JobInvolvement', 'PerformanceRating',
                      'RelationshipSatisfaction', 'WorkLifeBalance',
                      'StockOptionLevel', 'JobLevel', 'JobSatisfaction',
                      'EnvironmentSatisfaction']

CATEGORICAL_FEATURES = ['Department', 'EducationField', 'Gender', 'MaritalStatus', 'OverTime', 'JobRole']

CONTINUOUS_FEATURES = ['MonthlyRate', 'MonthlyIncome', 'DailyRate', 'HourlyRate', 'Age',
                       'DistanceFromHome', 'TotalWorkingYears', 'YearsAtCompany', 'YearsInCurrentRole',
                       'YearsWithCurrManager', 'PercentSalaryHike', 'NumCompaniesWorked', 'TrainingTimesLastYear', 
                       'YearsSinceLastPromotion']

COMBINED_FEATURES = ORDINAL_CAT_FEATURES + NUMERICAL_FEATURES + CATEGORICAL_FEATURES + CONTINUOUS_FEATURES
