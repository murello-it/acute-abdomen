import streamlit as st
from streamlit.components.v1 import html

# Function to calculate the risk score
def calculate_risk_score(data):
    score = 0
    score += data['nausea_vomiting']
    score += data['bmi_le_19']
    score += data['bmi_ge_30']
    score += data['pain_iliac_region']
    score += data['rovsings_sign']
    score += data['blumbergs_sign']
    score += data['temperature']
    score += data['leukocytes']
    score += data['age']
    return score

# Function to determine risk level
def determine_risk_level(score):
    if score <= 3:
        return "Крайне низкая вероятность"
    elif 4 <= score <= 7:
        return "Низкая вероятность"
    elif 8 <= score < 10:
        return "Средняя вероятность"
    else:
        return "Высокая вероятность"

# Streamlit app
st.title("Оценка вероятности острого живота у женщин")

# User input form
with st.form("acute_abdomen_form"):
    st.write("Пожалуйста, введите данные:")
    nausea_vomiting = st.selectbox("Тошнота, рвота", ["Нет", "Есть"], key="nausea_vomiting")
    bmi_le_19 = st.selectbox("Индекс массы тела (ИМТ) ≤ 19", ["Нет", "Есть"], key="bmi_le_19")
    bmi_ge_30 = st.selectbox("Индекс массы тела (ИМТ) ≥ 30", ["Нет", "Есть"], key="bmi_ge_30")
    pain_iliac_region = st.selectbox("Боль в правой и левой подвздошной области", ["Нет", "Есть"], key="pain_iliac_region")
    rovsings_sign = st.selectbox("Симптом Ровзинга", ["Нет", "Есть"], key="rovsings_sign")
    blumbergs_sign = st.selectbox("Симптом Щеткина-Блюмберга", ["Нет", "Есть"], key="blumbergs_sign")
    temperature = st.selectbox("Температура тела", ["≤ 37,0 С", "> 37,0 С"], key="temperature")
    leukocytes = st.selectbox("Уровень лейкоцитов", ["≤ 10,0 × 10^9/л", "≥ 10,0 × 10^9/л"], key="leukocytes")
    age = st.selectbox("Возраст", ["≤ 40 лет", "≥ 40 лет"], key="age")
    
    submitted = st.form_submit_button("Отправить")

    if submitted:
        # Convert user input to scores
        data = {
            'nausea_vomiting': 0 if nausea_vomiting == "Нет" else 1,
            'bmi_le_19': 0 if bmi_le_19 == "Нет" else 1,
            'bmi_ge_30': 0 if bmi_ge_30 == "Нет" else 2,
            'pain_iliac_region': 0 if pain_iliac_region == "Нет" else 1,
            'rovsings_sign': 0 if rovsings_sign == "Нет" else 1,
            'blumbergs_sign': 0 if blumbergs_sign == "Нет" else 1,
            'temperature': 0 if temperature == "≤ 37,0 С" else 1,
            'leukocytes': 0 if leukocytes == "≤ 10,0 × 10^9/л" else 1,
            'age': 2 if age == "≤ 40 лет" else 1
        }
        
        # Calculate total score
        total_score = calculate_risk_score(data)
        
        # Determine risk level
        risk_level = determine_risk_level(total_score)
        
        # Display results
        st.write(f"Итоговое количество баллов: {total_score}")
        st.write(f"Уровень риска: {risk_level}")
        
        # st.balloons()