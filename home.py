import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt



menu=['ice americano','cold brew','cappuccino','cafelatte','cafemoca','espresso',] #인기음료 6가지
# 스타벅스  음료 영양 정보

st_kcal=[10,5,110,180,290,5,] # 각음료의 칼로리, 당류,단백질,나트륨,포화지방,카페인
st_당류=[0,0,8,13,25,0,]# 카페인 정보를 배열로 나타낸것
st_단백질=[1,0,6,10,10,0]
st_나트륨=[5,11,70,115,105,0]
st_포화지방=[0,0,3,5,9,0]
st_카페인=[150,155,75,75,95,75]
p_menu=pd.Series(menu)# menu 들을 pandas에 나타내기 위해서 Series 속성 사용.
# 영양정보 배열들도 series로 나타내야하니 변수에 적용.
p_st_kcal=pd.Series(st_kcal)
p_st_당류=pd.Series(st_당류)
p_st_나트륨=pd.Series(st_나트륨)
p_st_단백질=pd.Series(st_단백질)
p_st_포화지방=pd.Series(st_포화지방)
p_st_카페인=pd.Series(st_카페인)
#행 값에 key값, 열에 value 생성 그런데 pandas 데이터프레임 구조에 맞게 설정.
data1=pd.DataFrame({'메뉴':p_menu,'칼로리':p_st_kcal,'당류':p_st_당류,'단백질':p_st_단백질,"나트륨":p_st_나트륨,"포화지방":p_st_포화지방,"카페인":p_st_카페인})

#이디야 음료 영양정보.
edya_kcal=[9,7,131,186,289,9] # 각음료의 칼로리, 당류,단백질,나트륨,포화지방,카페인
edya_당류=[0,0,9,22,25,0]# 카페인 정보를 배열로 나타낸것
edya_단백질=[1,0,6,9,7,0]
edya_나트륨=[0,0,96,135,124,0]
edya_포화지방=[0,0,4.3,5.6,11.6,0]
edya_카페인=[60,150,60,121,68,60]

# 영양정보 배열들도 series로 나타내야하니 변수에 적용.
p_edya_kcal=pd.Series(edya_kcal)
p_edya_당류=pd.Series(edya_당류)
p_edya_단백질=pd.Series(edya_나트륨)
p_edya_나트륨=pd.Series(edya_단백질)
p_edya_포화지방=pd.Series(edya_포화지방)
p_edya_카페인=pd.Series(edya_카페인)
#행 값에 key값, 열에 value 생성 그런데 pandas 데이터프레임 구조에 맞게 설정.
data2=pd.DataFrame({'메뉴':p_menu,'칼로리':p_edya_kcal,'당류':p_edya_당류,'단백질':p_edya_단백질,"나트륨":p_edya_나트륨,"포화지방":p_edya_포화지방,"카페인":p_edya_카페인})

#할리스
holy_kcal=[12,12,149,167,240,5]# 각음료의 칼로리, 당류,단백질,나트륨,포화지방,카페인
holy_당류=[0,0,10,12,27,0]# 카페인 정보를 배열로 나타낸것
holy_단백질=[1,1,8,8,8,0]
holy_나트륨=[5,3,115,130,146,0]
holy_포화지방=[0.1,0,5.3,6,5.9,0]
holy_카페인=[114,195,127,127,132,61]
# 영양정보 배열들도 series로 나타내야하니 변수에 적용.
p_holy_kcal=pd.Series(holy_kcal)
p_holy_당류=pd.Series(holy_당류)
p_holy_나트륨=pd.Series(holy_나트륨)
p_holy_단백질=pd.Series(holy_단백질)
p_holy_포화지방=pd.Series(holy_포화지방)
p_holy_카페인=pd.Series(holy_카페인)
#행 값에 key값, 열에 value 생성 그런데 pandas 데이터프레임 구조에 맞게 설정.
data3=pd.DataFrame({'메뉴':p_menu,'칼로리':p_holy_kcal,'당류':p_holy_당류,'단백질':p_holy_단백질,"나트륨":p_holy_나트륨,"포화지방":p_holy_포화지방,"카페인":p_holy_카페인})

#빽다방
back_kcal=[0,19,319,198,365,22]# 각음료의 칼로리, 당류,단백질,나트륨,포화지방,카페인
back_당류=[0,0,32,10,36,0]# 카페인 정보를 배열로 나타낸것
back_단백질=[0,2,13,10,13,1]
back_나트륨=[20,5,144,81,146,0]
back_포화지방=[0,0,8,8,8,0]
back_카페인=[237,195,237,237,237,237]
# 영양정보 배열들도 series로 나타내야하니 변수에 적용
p_back_kcal=pd.Series(back_kcal)
p_back_당류=pd.Series(back_당류)
p_back_단백질=pd.Series(back_단백질)
p_back_나트륨=pd.Series(back_나트륨)
p_back_포화지방=pd.Series(back_포화지방)
p_back_카페인=pd.Series(back_카페인)
#행 값에 key값, 열에 value 생성 그런데 pandas 데이터프레임 구조에 맞게 설정.
data4=pd.DataFrame({'메뉴':p_menu,'칼로리':p_back_kcal,'당류':p_back_당류,'단백질':p_back_단백질,"나트륨":p_back_나트륨,"포화지방":p_back_포화지방,"카페인":p_back_카페인})


#메가커피
mega_kcal=[12.2,10.6,145.5,175.4,380.9,7.6]# 각음료의 칼로리, 당류,단백질,나트륨,포화지방,카페인
mega_당류=[0,0,3.4,10.8,38.5,0]# 카페인 정보를 배열로 나타낸것
mega_단백질=[0.9, 0.8 ,8.2 ,10,10.9,0.5]
mega_나트륨=[2.4,1.5,60.7,101.5,185.2,0.2]
mega_포화지방=[0,0,4.1,5.2,10.5,0]
mega_카페인=[204.2,217,201.4,189.9,211.2,104.8]
# 영양정보 배열들도 series로 나타내야하니 변수에 적용
p_mega_kcal=pd.Series(mega_kcal)
p_mega_당류=pd.Series(mega_당류)
p_mega_단백질=pd.Series(mega_단백질)
p_mega_나트륨=pd.Series(mega_나트륨)
p_mega_포화지방=pd.Series(mega_포화지방)
p_mega_카페인=pd.Series(mega_카페인)
#행 값에 key값, 열에 value 생성 그런데 pandas 데이터프레임 구조에 맞게 설정.
data5=pd.DataFrame({'메뉴':p_menu,'칼로리':p_mega_kcal,'당류':p_mega_당류,'단백질':p_mega_단백질,"나트륨":p_mega_나트륨,"포화지방":p_mega_포화지방,"카페인":p_mega_카페인})
#파스쿠찌

pass_kcal=[15,10,131,110,280,7]# 각음료의 칼로리, 당류,단백질,나트륨,포화지방,카페인
pass_당류=[0,0,12,7,28,0]# 카페인 정보를 배열로 나타낸것
pass_단백질=[1,1,6,6,6,0]
pass_나트륨=[15,10,89,85,95,0]
pass_포화지방=[0,0,4.4,4,10,0]
pass_카페인=[227,201,190,219,202,138]
# 영양정보 배열들도 series로 나타내야하니 변수에 적용
p_pass_kcal=pd.Series(pass_kcal)
p_pass_당류=pd.Series(pass_당류)
p_pass_단백질=pd.Series(pass_단백질)
p_pass_나트륨=pd.Series(pass_나트륨)
p_pass_포화지방=pd.Series(pass_포화지방)
p_pass_카페인=pd.Series(pass_카페인)
#행 값에 key값, 열에 value 생성 그런데 pandas 데이터프레임 구조에 맞게 설정.
data6=pd.DataFrame({'메뉴':p_menu,'칼로리':p_pass_kcal,'당류':p_pass_당류,'단백질':p_pass_단백질,"나트륨":p_pass_나트륨,"포화지방":p_pass_포화지방,"카페인":p_pass_카페인})




add_selectbox = st.sidebar.selectbox( # 한페이지에 나타내기 복잡하니 목차 설정.
    "목차",
    ("1.프랜차이즈별 인기음료 영양정보", "2.카페인 순위","3.매장별 1등카페인")
)
st.title("카페 프렌차이즈 음료의 영양소")

st.header("궁금한 카페")
if add_selectbox=="1.프랜차이즈별 인기음료 영양정보": #목차에서 1.프랜차이즈별 인기음료 영양정보를 클릭했을 때.
    if st.button('Starbucks'): #스타벅스 버튼을 클릭하면
        starbucks_image = Image.open('스타벅스.jpg') # 이미지를 starbucks_image 변수에 저장
        st.image(starbucks_image, caption='스타벅스') #이미지 등장.
        st.write(data1)# data1에 스타벅스의 영양정보를 pandas 데이터 프레임 형태로 저장했음.
     
    
    
    if st.button('Ediya'): #이디야 버튼을 클릭하면.
        ediya_image = Image.open('이디야.png')
        st.image(ediya_image, caption='이디야')#이디야 사진등장.
        st.write(data2)#이디야의 영양정보가 담긴 변수를 write
        
    if st.button('HOLLYS'):# 할리스 버튼을 클릭하면.
        hollys_image = Image.open('할리스.png')
        st.image(hollys_image, caption='할리스')#할리스 사진등장.
        st.write(data3)#할리스 음료의 영양정보가 담긴 변수를 write

        
    if st.button('BBACKS'): # 빽다방 버튼을 클릭하면.
        paiks_image = Image.open('빽다방.png')
        st.image(paiks_image, caption='빽다방')# 빽다방 사진등장.
        st.write(data4)# 뺵다방 음료의 영양정보가 담긴 변수를 write
        

    
    if st.button('MEGA'):# 메가커피 버튼을 클릭하면
        mega_image = Image.open('메가커피.jpg')
        st.image(mega_image, caption='메가커피')#메가 커피 사진등장.
        st.write(data5)# 메가커피 음료의 영양정보가 담긴 변수를 write
        

    if st.button('PASSCUSSI'):# 파스쿠찌 버튼을 클릭하면
        pasucci_image = Image.open('파스쿠찌.png')
        st.image(pasucci_image, caption='파스쿠찌')#파스 쿠찌 사진 등장.
        st.write(data6)# 파스쿠찌 음료의 영양정보가 담긴 변수를 write 한다.
    
elif add_selectbox=="2.카페인 순위":    #목차에 2.카페인 순위를 클릭하면 
     
    #각 매장에서 유명한 인기음료 6개의 카페인 수치를 bar차트로 나타내서 비교 하고 싶음.
    # 코드 point.
    
    
    #1.----스타벅스 카페인 순위
    data = pd.DataFrame({'Menu': menu, 'Caffeine': st_카페인}) #data라는 변수에 1행에 key값 배열 
                                                              # 각 열에 value값 생성   pandas DataFrame 구조 생성.

    fig, ax = plt.subplots(figsize=(2, 2)) # fig라는 변수에 차트의 모양을 대입, ax에 x축 y축 정보를 대입.
    ax.bar(data['Menu'], data['Caffeine']) #bar차트를 이용할건데 x축엔 data 프레임구조에서 Menu에 있는 배열들을 설정.
                                           #y축엔 Caffeine 수치를 대입할것임.
    ax.set_xlabel('Menu',fontsize=6)  #x축의 label은 Menu
    ax.set_ylabel('Caffeine',fontsize=6)#y축의 label 은 Caffeine
    ax.set_title('Starbucks',fontsize=6)#title 은 Starbuck로 설정.

    plt.xticks(rotation=75)# 글자가 너무 길어 글자를 75도로 꺾었음.

    st.pyplot(fig)# 이러한 figure 정보가 담긴 fig 변수를 코드를 이용하여 등장. 시킹
    
    #2.----이디야 카페인 순위
    
    data = pd.DataFrame({'Menu': menu, 'Caffeine': edya_카페인}) #data 변수에 1행에 key 값배열 ,각 열에 value값 pandas data구조. 

    
    fig, ax = plt.subplots(figsize=(2, 2)) #starbucks 에서 사용한것과 설명 같음. 
    ax.bar(data['Menu'], data['Caffeine'])
    ax.set_xlabel('Menu',fontsize=6)
    ax.set_ylabel('Caffeine',fontsize=6)
    ax.set_title('Ediya',fontsize=6)

    plt.xticks(rotation=75)
    st.pyplot(fig)
    
    #3.----HOLLYS 카페인 순위
    data = pd.DataFrame({'Menu': menu, 'Caffeine': holy_카페인}) #holy_카페인 변수엔 HOLLYS 매장 음료6개의 카페인 정보가 배열로 저장되어있음.

    
    fig, ax = plt.subplots(figsize=(2, 2)) #starbucks 와 설명 같음.
    ax.bar(data['Menu'], data['Caffeine'])
    ax.set_xlabel('Menu',fontsize=6)
    ax.set_ylabel('Caffeine',fontsize=6)
    ax.set_title('HOLLYS',fontsize=6)

    plt.xticks(rotation=75)

    st.pyplot(fig)
    #4..----빽다방 카페인 순위
    data = pd.DataFrame({'Menu': menu, 'Caffeine': back_카페인}) # 뺵다방매장의 6개 카페인 수치가 back_카페인에 저장되어있음.

    
    fig, ax = plt.subplots(figsize=(2, 2)) # 위와 설명 같음.
    ax.bar(data['Menu'], data['Caffeine'])
    ax.set_xlabel('Menu',fontsize=6)
    ax.set_ylabel('Caffeine',fontsize=6)
    ax.set_title('BbackDabang',fontsize=6)

      
    plt.xticks(rotation=75)

    st.pyplot(fig)
    #5.----메가 카페 카페인 순위
    data = pd.DataFrame({'Menu': menu, 'Caffeine': mega_카페인}) # 위 설명과 같음.

   
    fig, ax = plt.subplots(figsize=(2, 2))
    ax.bar(data['Menu'], data['Caffeine'])
    ax.set_xlabel('Menu',fontsize=6)
    ax.set_ylabel('Caffeine',fontsize=6)
    ax.set_title('Mega',fontsize=6)

        
    plt.xticks(rotation=75)


    st.pyplot(fig)
    #5.----파스쿠찌 카페인 순위
    data = pd.DataFrame({'Menu': menu, 'Caffeine': pass_카페인})

    fig, ax = plt.subplots(figsize=(2, 2))
    ax.bar(data['Menu'], data['Caffeine'])
    ax.set_xlabel('Menu',fontsize=6)
    ax.set_ylabel('Caffeine',fontsize=6)
    ax.set_title('Pascucci',fontsize=6)

        
    plt.xticks(rotation=75)

    st.pyplot(fig)
    
 
    
elif add_selectbox=="3.매장별 1등카페인": #목차에서 3,매장별 1등 카페인 을 클릭 할 때.
        st.header("매장별 인기음료 카페인 차트")
    # 인기있는 6개의 음료중 프렌차이즈 별로 제일 높은 카페인수치.
        m_sbuck_카페인=max(st_카페인) #st_카페인 배열의 최대값 설정.
        m_ediya_카페인=max(edya_카페인)#edya_카페인 배열의 최대값 설정.
        m_holy_카페인=max(holy_카페인)#holy_카페인 배열의 최대값 설정.
        m_back_카페인=max(back_카페인)#back_카페인 배열의 최대값 설정.
        m_mega_카페인=max(mega_카페인)#mega_카페인 배열의 최대값 설정.
        m_pass_카페인=max(pass_카페인)#pass_카페인 배열의 최대값 설정.
        # 프렌차이즈별 인기 음료 중 카페인이 제일 높은 배열.
        menu1=["Starbuks","Ediya","HOLLYS","BbackDabang","MEGA","PASCUSSI"] # 메뉴룰 영어로 설정.
        max_franchise_카페인=[m_sbuck_카페인,m_ediya_카페인,m_holy_카페인,m_back_카페인,m_mega_카페인,m_pass_카페인] # 각 매장별로 카페인 수치 제일 높은 값을 가져와 max_Franchise 변수에 저장.
        data = pd.DataFrame({'Menu': menu1, 'max_Caffeine':max_franchise_카페인 })# menu1을 Menu에 value로 설정. Caffeine의 value 값엔 max_Frainchise_카페인 설정
   
        fig, ax = plt.subplots(figsize=(2, 2))# 차트 그리는건 위에 있는 차트 코드와 같음.
        ax.bar(data['Menu'], data['max_Caffeine'])# x축엔 data변수의 Menu Value값을 가져옴, y축엔 max_Caffeine의 value값을 가져옴
        ax.set_ylabel('max Caffeine',fontsize=6)#ylabel엔 maxCaffeine  글자크기는 6인치.
        ax.set_xlabel('Franchise',fontsize=6)#xlabel엔 maxCaffeine  글자크기는 6인치.

   
        plt.xticks(rotation=75)

        st.pyplot(fig)      

           