import streamlit as st
from PIL import Image

    #체질량 지수 구하는 앱
    #몸무게, 키 입력 받기
    
def bmi_check(bmi):
    if bmi<25 :
        st.error('비만.')

    elif bmi>=23:
        st.warning("과체중")

    elif bmi>=18.5:
        st.success("정상")
    else:
        st.info("저체중")         
           
st.write("# 체 질 량 계 산 기~~")

height = st.number_input('키를 입력하세요, (cm)',100,200,170,5)
st.write('키: ', height,'cm')                  #최소값,최대값,시작값,step값

weight = st.number_input('몸무게를 입력하세요, (kg)',50,100,50,5)
st.write('몸무게: ', weight,'kg')

bmi=weight/(height/100)**2




if st.button('계산'):
    st.balloons()
    st.write('당신의 체질량 지수는', round(bmi,2),'입니다')
    bmi_check(bmi)



image = Image.open('vegetable.jpg')

st.image(image, caption='eat a lot!') #cation