import streamlit as st

st.write("# Hi Welcome to my App") # #하면 글씨 크게 

st.write('반갑습니다. 저의 웹에 오신 것을 환영합니다')


if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')


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