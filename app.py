import streamlit as st
import time

# 웹페이지 탭 설정
st.set_page_config(page_title="2026년 하반기 최종 합격 조회", page_icon="💌")

st.title("2026년 하반기 채용 최종 합격 조회")
st.write("지원자님의 이름과 생년월일을 입력해주세요.")

# 입력 폼
name = st.text_input("이름 (예: 홍길동)")
birth_date = st.text_input("생년월일 8자리 (예: 19930101)")

if st.button("조회하기"):
    if name == "장진아":
        with st.spinner("지원자 정보를 조회 중입니다..."):
            time.sleep(2)
        
        st.balloons()
        
        # 고급스러운 HTML/CSS 통지서 디자인
        fancy_html = """
        <style>
        .certificate {
            border: 8px double #d4af37; /* 고급스러운 금색 이중 테두리 */
            padding: 40px;
            background-color: #fffdf9; /* 따뜻한 아이보리 배경 */
            font-family: 'KoPub Batang', 'Malgun Gothic', serif;
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            border-radius: 5px;
            margin-top: 20px;
        }
        .cert-header {
            text-align: center;
            color: #4a3b32;
            font-size: 32px;
            font-weight: 900;
            border-bottom: 2px solid #d4af37;
            padding-bottom: 20px;
            margin-bottom: 30px;
            letter-spacing: 5px;
        }
        .cert-body {
            line-height: 1.9;
            color: #333;
            font-size: 17px;
        }
        .highlight {
            color: #b8860b;
            font-weight: bold;
            font-size: 19px;
        }
        .cert-footer {
            margin-top: 60px;
            text-align: center;
            font-weight: bold;
            color: #4a3b32;
        }
        .signature {
            font-size: 24px;
            margin-top: 15px;
            font-family: 'Brush Script MT', '궁서', cursive; 
        }
        </style>

        <div class="certificate">
            <div class="cert-header">
                최 종 합 격 통 지 서
            </div>
            <div class="cert-body">
                <p><b>수신:</b> 장진아 지원자님</p>
                <p><b>발신:</b> 나대식 평생동반자 채용위원회</p>
                <br>
                <p>안녕하십니까, 장진아 님.</p>
                <p>우선 당사의 <span class="highlight">‘평생 반려자 및 유일한 아내’</span> 부문에 지원해 주셔서 진심으로 감사드립니다.</p>
                <p>최근 여러 가지 고된 일정과 일상의 무게 속에서도 장진아 님이 보여주신 눈부신 미소와 따뜻한 마음, 그리고 곁에 있는 사람을 행복하게 만드는 압도적인 역량에 당사의 모든 심사위원은 깊은 감동을 받았습니다.</p>
                <p>이에 치열한 경쟁을 뚫고, 본 전형에 <span class="highlight">최종 합격</span>하셨음을 기쁜 마음으로 통지해 드립니다.</p>
                <br>
                <p><b>[특별 복리후생]</b></p>
                <ul>
                    <li>24시간 무제한 감정 지원 서비스 (항시 대기)</li>
                    <li>원할 때마다 맛집으로 안내하는 전속 매니저 무상 제공</li>
                    <li>세상이 버거울 때 언제든 쉴 수 있는 완벽한 안식처 제공</li>
                </ul>
                <br>
                <p>앞으로의 모든 날들은 당신이 더 많이 웃고 조금 덜 힘들 수 있도록, 제가 당신의 가장 든든하고 따뜻한 안식처가 되어드리겠습니다.</p>
            </div>
            <div class="cert-footer">
                <p>2026년 10월 1일</p>
                <p class="signature">대표 &nbsp; 나 대 식 &nbsp; (인)</p>
            </div>
        </div>
        """
        
        # HTML 렌더링 허용 옵션을 켜서 출력
        st.markdown(fancy_html, unsafe_allow_html=True)
        
    elif name:
        st.error("일치하는 지원자 정보가 없습니다. 이름과 생년월일을 다시 확인해주세요.")
