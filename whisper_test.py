import streamlit as st
from elevenlabs.client import ElevenLabs

api_key = st.secrets["ELEVENLABS_API_KEY"]
st.session_state.voice_id = st.secrets["VOICE_ID"]
client = ElevenLabs(api_key=api_key)

# 세션 상태에 voice_id 없으면 초기화
if "voice_id" not in st.session_state:
    st.session_state.voice_id = None

st.markdown("<h1 style='text-align: center; color: #555555;font-size: 22px;'>1. 화자를 선택하세요</h1>", unsafe_allow_html=True)

cols = st.columns(3, border=True)
with cols[0]:
    if st.button("**JiYoung**"):
        st.session_state.voice_id = st.secrets["VOICE_ID"]
with cols[1]:
    if st.button("**Anna KIM**"):
        st.session_state.voice_id = st.secrets["VOICE_ID"]
with cols[2]:
    if st.button("**Bin**"):
        st.session_state.voice_id = st.secrets["VOICE_ID"]
st.space(size="small")

st.divider()
st.markdown("<h1 style='text-align: center; color: #555555;font-size: 22px;'>2. 텍스트를 입력해 보세요</h1>", unsafe_allow_html=True)
text = st.text_input("입력창", value="이 목소리는 일레븐랩스의 샘플 목소리입니다.")

st.divider()
st.markdown("<h1 style='text-align: center; color: #555555;font-size: 22px;'>3. 생성된 목소리를 들어보세요</h1>", unsafe_allow_html=True)

if st.button("들어보기"):
    if not st.session_state.voice_id:
        st.error("먼저 화자를 선택해 주세요.")
    else:
        audio = client.text_to_speech.convert(
            text=text,
            voice_id=st.session_state.voice_id,
            model_id="eleven_multilingual_v2"
        )

        save_file_path = "temp.mp3"
        with open(save_file_path, "wb") as f:
            for chunk in audio:
                if chunk:
                    f.write(chunk)

        st.success("생성이 완료되었습니다. 아래에서 들어보세요.")
        st.audio(save_file_path, format="audio/mp3")
