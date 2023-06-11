
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('C:/Users/ADITYA AWASTHI/Multiple Disease Prediction/saved models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/ADITYA AWASTHI/Multiple Disease Prediction/saved models/hearttt_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('C:/Users/ADITYA AWASTHI/Multiple Disease Prediction/saved models/parkinsons_model.sav', 'rb'))

breast_cancer_model = pickle.load(open('C:/Users/ADITYA AWASTHI/Multiple Disease Prediction/saved models/breast_cancer_detection.sav', 'rb'))

liver_disease_model = pickle.load(open('C:/Users/ADITYA AWASTHI/Multiple Disease Prediction/saved models/liver_disease_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction',
                           'Breast Cancer Prediction',
                           'Liver Disease Prediction'],
                          icons=['activity','heart','person','pause',''],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input(
            'Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page

if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age')
        
    with col2:
        sex = st.number_input('Sex')
        
    with col3:
        cp = st.number_input('Chest Pain types')
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure')
        
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.number_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise')
        
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
        
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')
    
    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)


#Breast Cancer Prediction Page-

if (selected == "Breast Cancer Prediction"):
    
    # page title
    st.title("Breast Cancer Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        Mean_Radius = st.number_input('Mean_Radius')
        
    with col2:
        Mean_Texture = st.number_input('Mean_Texture')
        
    with col3:
        Mean_Perimeter = st.number_input('Mean_Perimeter')
        
    with col4:
        Mean_Area = st.number_input('Mean_Area')
        
    with col5:
        Mean_Smoothness = st.number_input('Mean_Smoothness')
        
    with col1:
        Mean_Compactness = st.number_input('Mean_Compactness')
        
    with col2:
        Mean_Concavity = st.number_input('Mean_Concavity')
        
    with col3:
        Mean_Concave_Points = st.number_input('Mean_Concave_Points')
        
    with col4:
        Mean_Symmetry = st.number_input('Mean_Symmetry')
        
    with col5:
        Mean_Fractal_Dimension = st.number_input('Mean_Fractal_Dimension')
        
    with col1:
        Radius_Error = st.number_input('Radius_Error')
        
    with col2:
        Texture_Error = st.number_input('Texture_Error')
        
    with col3:
        Perimeter_Error = st.number_input('Perimeter_Error ')
        
    with col4:
        Area_Error = st.number_input('Area_Error')
        
    with col5:
        Smoothness_Error = st.number_input('Smoothness_Error')
        
    with col1:
        Compactness_Error = st.number_input('Compactness_Error')
        
    with col2:
        Concavity_Error = st.number_input('Concavity_Error')
        
    with col3:
        Concave_Points_Error = st.number_input('Concave_Points_Error')
        
    with col4:
        Symmetry_Error = st.number_input('Symmetry_Error')
        
    with col5:
        Fractal_Dimension_Error = st.number_input('Fractal_Dimension_Error')
        
    with col1:
        Worst_Radius = st.number_input('Worst_Radius')
        
    with col2:
        Worst_Texture = st.number_input('Worst_Texture')
        
    with col3:
        Worst_Perimeter = st.number_input('Worst_Perimeter')
        
    with col4:
        Worst_Area = st.number_input('Worst_Area')
        
    with col5:
        Worst_Smoothness = st.number_input('Worst_Smoothness')
        
    with col1:
        Worst_Compactness = st.number_input('Worst_Compactness')
        
    with col2:
        Worst_Concavity = st.number_input('Worst_Concavity')

    with col3:
        Worst_Concave_Points = st.number_input('Worst_Concave_Points')
        
    with col4:
        Worst_Symmetry = st.number_input('Worst_Symmetry')
        
    with col5:
        Worst_Fractal_Dimension = st.number_input('Worst_Fractal_Dimension')
    
    # code for Prediction
    breast_cancer_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Breast Cancer Test Result"):
        breast_cancer_prediction = breast_cancer_model.predict([[Mean_Radius, Mean_Texture, Mean_Perimeter, Mean_Area, Mean_Smoothness, Mean_Compactness, Mean_Concavity, Mean_Concave_Points, Mean_Symmetry, Mean_Fractal_Dimension, Radius_Error, Texture_Error, Perimeter_Error, Area_Error, Smoothness_Error, Compactness_Error, Concavity_Error, Concave_Points_Error, Symmetry_Error, Fractal_Dimension_Error, Worst_Radius, Worst_Texture, Worst_Perimeter, Worst_Area, Worst_Smoothness, Worst_Compactness, Worst_Concavity, Worst_Concave_Points, Worst_Symmetry, Worst_Fractal_Dimension]])
        
        if (breast_cancer_prediction[0] == 1):
          breast_cancer_diagnosis = "The person has Breast Cancer disease"
        else:
          breast_cancer_diagnosis = "The person does not have Breast Cancer disease"
        
    st.success(breast_cancer_diagnosis)


# Liver Disease Prediction Page
if (selected == 'Liver Disease Prediction'):
    
    # page title
    st.title('Liver Disease Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Age = st.number_input('Age')

    with col2:
        Sex = st.number_input('Sex')

    with col3:
        Total_Bilirubin = st.number_input('Total Bilirubin')

    with col1:
        Direct_Bilirubin = st.number_input('Direct Bilirubin')

    with col2:
        Alkaline_Phosphotase = st.number_input('Alkaline Phosphotase')

    with col3:
        Alamine_Aminotransferase = st.number_input('Alamine Aminotransferase')

    with col1:
        Aspartate_Aminotransferase	 = st.number_input(
            'Aspartate Aminotransferase	')

    with col2:
        Total_Protiens = st.number_input('Total Protiens')

    with col3:
        Albumin = st.number_input('Albumin')

    with col1:
        Albumin_and_Globulin_Ratio	 = st.number_input(
            'Albumin and Globulin Ratio')
    
    
    # code for Prediction
    liver_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Liver Disease Test Result'):
        liver_prediction = liver_disease_model.predict([[Age, Sex, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Aspartate_Aminotransferase	, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio]])
        
        if (liver_prediction[0] == 1):
          liver_diagnosis = 'The person has liver disease'
        else:
          liver_diagnosis = 'The person has no liver disease'
        
    st.success(liver_diagnosis)