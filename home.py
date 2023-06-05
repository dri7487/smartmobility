import streamlit as st
from PIL import Image

st.write("# Hi Welcome to my App") # #하면 글씨 크게 

st.write('반갑습니다. 저의 웹에 오신 것을 환영합니다')


if st.button('Say hello'):
    st.write('Why hello there') #say hello text가 있는 버튼을 누르면  Why hello there 이 write 됌.
else:
    st.write('Goodbye') # else는뭐지?  


option = st.selectbox(
    '좋아하는 동물은?',
    ('강아지', '고양이', '말','코끼리'))

st.write('내가 좋아하는 동물은?',option,'입니다')
st.write(f'내가 좋아하는 동물은{option}입니다.')

txt = st.text_area('자신을 소개해 보세요.', '''
    동아대학교 전자공학과 3학년 재학중인 김승환.
    
    

    
    ''')
st.write('입력한 내용:',txt)

age = st.slider('나이를 선택하세요.', 0, 130, 25)
st.write("나는", age, '살 입니다.')



number = st.number_input('Insert a number')
st.write('The current number is ', number)





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