import whisper
import streamlit as st
import tempfile

def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1588345921523-c2dcdb7f1dcd?w=800&dpr=2&q=80");
             background-attachment: fixed;
             background-size: cover

         }}
         </style>
         """,
        unsafe_allow_html=True
    )
add_bg_from_url()
#st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/OpenAI_Logo.svg/512px-OpenAI_Logo.svg.png", width=200)

model = whisper.load_model("small")
#result_kr = model.transcribe("kr_food.mp3", fp16=False)
#result_en = model.transcribe("en_food.mp3", fp16=False)
#result_jp = model.transcribe("jp_food.mp3", fp16=False)
#result_cn = model.transcribe("cn_food.mp3", fp16=False)

st.markdown("<h3 style='text-align: center; color: #333333;font-size: 34px;'>Whisper 데모</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #333333;font-size: 24px;'>(ChatGPT에서 사용하는 AI 음성인식 기능)</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #333333;font-size: 14px;'>68만 시간 & 100개 나라의 언어를 학습하여, 정확도가 높고 인식속도가 빠름</h3>", unsafe_allow_html=True)

with st.expander(":material/experiment: 동작 원리"):
    st.image("https://raw.githubusercontent.com/openai/whisper/main/approach.png")

st.space(size="small")

#st.audio("kr_food.mp3", format="audio/mpeg", loop=False)
#if st.button("**:material/hearing: 음성 변환하기**"):
#    container = st.container(border=True)
#    container.write(result_kr["text"])
#st.divider()
#st.space(size="small")

audio_value = st.audio_input("Whisper 테스트 해 보기")

if audio_value is not None:

    # Streamlit에서 받은 오디오 데이터를 임시 파일로 저장
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_value.getbuffer())
        audio_path = tmp.name

    # 업로드한 오디오 재생
    #st.audio(audio_path)

    # Whisper에 파일 경로 전달
    result_test = model.transcribe(audio_path, language="ko")
#    st.write(result_test["text"])
    if st.button("**:material/voice_chat: 인식 결과 보기**"):
        container = st.container(border=True)
        container.write(result_test["text"])

else:
    st.info("녹음 또는 업로드한 오디오가 없습니다.")
