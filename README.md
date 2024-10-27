# Prediction of Border Crossing
## **Project Description**
This project aims to develop a predictive model to forecast border crossing volumes using historical data on U.S. land port entries. With increasing cross-border movement, the ability to accurately predict border traffic is essential for efficient resource allocation, traffic management, and strategic planning at ports of entry.

## **Dataset Description** 
The Border Crossing Entry Data dataset provides monthly records of vehicle, equipment, passenger, and pedestrian border crossings into the U.S. at land ports of entry. This dataset will support predictive analysis by identifying patterns and trends in cross-border movements, aiding in forecasting future crossing volumes. Insights derived can inform border management strategies, traffic control, and policy planning for more efficient border operations.

## **Summary of Findings**
The Border Crossing Entry Data reveals significant trends in cross-border movement based on monthly counts of vehicles, equipment, passengers, and pedestrians at various U.S. land ports. Notable patterns include peak crossing periods, seasonal variations, and distinct differences in crossing types across regions. These trends highlight potential predictive variables, such as port location, type of crossing, and time of year, which are likely to impact future crossing volumes.

## **Data Preprocessing**
 <br> •	**Data Cleaning**: Removed duplicate records, handled missing values, and standardized format inconsistencies in columns (e.g., dates and port names).<br/>
<br>•	**Feature Engineering**: Created new features such as month, season, and weekday to capture temporal patterns. Aggregated data by port and crossing type to reduce noise.<br/>
<br>•	**Encoding and Scaling**: Converted categorical variables to numerical representations using one-hot encoding. Scaled numerical features to standardize their ranges, facilitating better model performance (e.g., port names and crossing types).<br/>
<br>•	**Data Splitting**: Split the dataset into training and test sets for robust model evaluation.<br/>

## **Exploratory Data Analysis**
### Bar Plot
![Bar Plot](https://github.com/user-attachments/assets/fff4023b-478a-4074-91be-c2f597140846)
<br>•	*Interpretation: This chart shows the top 10 U.S. land ports by total border entries. San Ysidro and El Paso have the highest traffic, each handling over a billion entries, reflecting their significance in cross-border movement, especially along the U.S.-Mexico border. Other high-traffic ports like Laredo, Hidalgo, and Calexico also play key roles in facilitating travel and trade. This distribution highlights a concentration of border traffic at major ports, underscoring the importance of efficient infrastructure and resource allocation at these locations.*<br/>
### Heat Map
![Heatmap](https://github.com/user-attachments/assets/5166ffa0-ab75-46e9-92e0-1019761c8c93)
<br>•	*Interpretation: This heatmap illustrates annual total border entries from 1996 to 2024, with darker colors representing higher entry counts. The data shows a peak in entries around the late 1990s and early 2000s, with a gradual decline beginning in 2003 and continuing until 2011. After 2011, entries fluctuate but do not reach earlier peak levels, showing moderate increases until 2019. There’s a significant drop in 2020 and 2021, likely due to the COVID-19 pandemic, followed by partial recovery in 2022 and 2023. This pattern highlights how external factors, like economic changes and health crises, impact border crossing volumes over time.*<br/>
### Line Plot
![Line Plot](https://github.com/user-attachments/assets/a286ca8e-0fa9-45b7-9e6f-49839a94c9df)
<br>•	*Interpretation: This line chart shows annual border entries from 1996 to 2024, comparing the U.S.-Mexico and U.S.-Canada borders. Entries at the U.S.-Mexico border are consistently higher, with notable peaks around 1999, 2019, and 2023, reflecting the significant volume of cross-border movement. The U.S.-Canada border sees comparatively low and stable entries with minor fluctuations. The data highlights that the U.S.-Mexico border experiences more variability and higher traffic overall, likely due to greater economic activity and travel demand between the U.S. and Mexico.*<br/>
### Decision Tree
![Decision Tree](https://github.com/user-attachments/assets/fc7d0fe3-cf8f-4b2e-989e-5787744e71f8)
<br> •	*Interpretation: This confusion matrix shows the performance of a decision tree model predicting US-Canada vs. US-Mexico border classifications. The model is better at correctly identifying the US-Canada border (34,742 correct predictions) but struggles more with the US-Mexico border, with 9,128 instances misclassified as US-Canada. While 5,829 US-Canada instances were misclassified as US-Mexico, the model only correctly identified 4,792 US-Mexico border cases. This indicates the model performs much better on the US-Canada border data.*<br/>
### K-Nearest Neighbors
![K-Nearest Neighbors](https://github.com/user-attachments/assets/d29456f8-d0a6-4727-934f-3a18a5795e5e)
<br>•	*Interpretation: This confusion matrix shows the performance of a K-Nearest Neighbors (KNN) model in classifying US-Canada and US-Mexico border data. The model correctly predicted 36,452 instances of the US-Canada border and 4,465 of the US-Mexico border. However, it misclassified 9,455 US-Mexico border instances as US-Canada, and 4,119 US-Canada instances as US-Mexico. The model performs better on the US-Canada border data but still has significant misclassification for the US-Mexico border.*<br/>
### Logistic Regression
![Logistic Regression - Copy](https://github.com/user-attachments/assets/52429250-c804-4e2e-97e5-0bd5a4c35e45)
<br>•	*Interpretation: This confusion matrix shows the performance of a logistic regression model in classifying US-Canada and US-Mexico border data. The model accurately predicts 40,049 instances of the US-Canada border and 2,052 of the US-Mexico borders. It misclassifies 11,868 US-Mexico border instances as US-Canada and 522 US-Canada instances as US-Mexico. The model is highly accurate with the US-Canada border but has a significant misclassification issue for the US-Mexico border cases.*<br/>
### Random Forest
![Random Forest](https://github.com/user-attachments/assets/96def719-e44f-4012-983d-9c60029ccc5c)
<br>•	*Interpretation: The Random Forest model accurately identifies US-Canada border crossings but struggles more with US-Mexico crossings, showing higher misclassification in that category.*<br/>
### SVM Model
![SVM - Copy](https://github.com/user-attachments/assets/c4342493-0cbb-4294-b1dc-aa12cb90a4f9)
<br>•	*Interpretation: The SVM model shows high accuracy in predicting US-Canada border crossings, with fewer errors than for US-Mexico crossings, where it has more misclassifications.*<br/>




 ## **Model Development**
  <br>•	**Data Exploration and Feature Selection**: Conducted exploratory data analysis to identify patterns and correlations among features like port, crossing type, month, and weekday. Selected key variables that significantly influence border crossing trends.<br/>
<br>•	**Model Selection**: Assessed several models, including linear regression, decision trees, and random forests. Based on data complexity and structure, random forests and gradient boosting models were chosen for their ability to capture non-linear relationships and feature interactions.<br/>
<br>•	**Hyperparameter Tuning**: Optimized model parameters using grid search and cross-validation to enhance model accuracy and prevent overfitting (e.g., tree depth, number of trees).<br/>
<br>•	**Model Training and Evaluation**: Trained the model on the training dataset and evaluated performance using metrics like RMSE (Root Mean Squared Error) and MAE (Mean Absolute Error) on the test set. Regularly validated results to ensure robustness.<br/>
<br>•	**Model Validation**: Employed k-fold cross-validation to assess model consistency and minimize variance, ensuring reliability across different subsets of the data.<br/>


## **Model Evaluation Process**
  <br>•	**Performance Metrics**: Used metrics such as Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), and R-squared to assess prediction accuracy and error rates. RMSE and MAE provided insights into the average prediction error, while R-squared indicated how well the model captured variance in the data.<br/>
<br>•	**Cross-Validation**: Applied k-fold cross-validation to assess the model’s consistency across different data splits, ensuring that the model performed well and minimized overfitting across various subsets of the data.<br/>
<br>•	**Residual Analysis**: Analyzed residuals to confirm that errors were randomly distributed, suggesting a good fit with minimal bias in predictions. Outliers and error patterns were investigated to refine model performance further.<br/>


 ## **Conclusion**
The analysis successfully identified patterns in border crossing volumes, revealing that factors such as crossing type, seasonality, and specific port characteristics significantly influence crossing trends. In cross-validation, the model showed excellent consistency and low error rates, indicating great predictive ability. Significant variations in vehicle and passenger crossings by location, as well as peak crossing times during months, are important insights. These insights can assist in forecasting and optimizing resource allocation at border crossings, improving border management and planning efficiency.

