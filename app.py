import streamlit as st
import random

# 페이지 기본 설정
st.set_page_config(page_title="오늘 뭐 먹지?", page_icon="🍱")

# 앱 제목 및 설명
st.title("🍱 오늘의 점심 메뉴 추천기")
st.write("결정 장애 해결! 아래 버튼을 눌러 오늘의 점심 메뉴를 골라보세요.")

# 점심 메뉴 리스트 (원하는 메뉴를 자유롭게 추가/수정하세요)
lunch_menus = [
    "김치찌개", "된장찌개", "제육볶음", "돈까스", "비빔밥",
    "짜장면", "짬뽕", "탕수육", "마라탕", "쌀국수",
    "초밥", "라멘", "우동", "햄버거", "피자",
    "파스타", "샌드위치", "국밥", "냉면", "떡볶이"
]

st.divider()

# 버튼 생성 및 클릭 이벤트 처리
if st.button("🎲 오늘의 메뉴 뽑기!", use_container_width=True):
    # random.choice를 이용해 리스트에서 무작위로 하나 선택
    selected_menu = random.choice(lunch_menus)
    
    # 결과 출력
    st.balloons() # 축하 풍선 효과
    st.success(f"오늘의 추천 메뉴는 **'{selected_menu}'** 입니다! 맛있게 드세요 😋")
