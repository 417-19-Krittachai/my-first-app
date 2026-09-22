import time
import streamlit as st

st.title("@ เกมเติมศัพท์จับเวลา")

# 1. กำหนดค่าเริ่มต้นใน session_state ถ้ายังไม่มี
if "ans1_val" not in st.session_state:
st. session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
st.session_state.ans2_val = ""

# * ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
def reset_game():
st.session_state.ans2_val
# เคลียร์ค่าช่องข้อ 1
st.session_state.ans2_val = "" # เคลียร์ค่าช่องข้อ 2
st.session_state.start = time.time() # เริ่มเวลาใหม่
st.session_state.is_ended = False # ilø Dialog

#

#

*ฟังก์ชัน MessageBox (Dialog)

@st.dialog("สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2):
st.balloons()
score = 0

@st.dialog("ll
u_ans1= ans1.strip().lower()
u_ans2 = ans2.strip().lower()

# ตรวจข้อ 1
if u_ans1 == "apple":
ข้อ 1: ถูกต้อง")

st. success("
score += 1

else:
st.error(f"X ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1} )")
# ตรวจข้อ 2
if u_ans2 == "fish":
ข้อ 2: ถูกต้อง")

st. success("

score += 1

else:
st.error(f"X ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}*)")

# * [พื้นที่สำหรับนักเรียน]: เพิ่มตรวจข้อ 3, 4 ตรงนี้

st.info(f"2 ได้คะแนนรวม: {score} คะแนน")

if score == 2:
st.success(" You win!")
else:
st.error("* You lose!")
#
# 1. ปุ่มเริ่มเล่นเกม
#

st.button(" เริ่มเล่นเกม", on_click=reset_game)

# 2. แถบแสดงเวลานับถอยหลัง
if "start" in st.session_state and not st.session_state.get("is_ended", False):
time_left = int(30 - (time.time() - st.session_state.start))

if time_left > 0:
st.error(f" Z เหลือเวลา: {time_left} วินาที")
else:
st.session_state.is_ended = True
st.rerun()

st.divider()
# 3. ช่องรับคำตอบ (ใช้ value ผูกกับตัวแปรตรงๆ เพื่อสั่งเคลียร์ได้)
ans1 = st.text_input(
"2ia 1: An "a _ _ 1 e' a day keeps the doctor away.
value=st.session_state.ans1_val,

ans2 = st.text_input(
"2ia 2: Cats love to eat 'f _ sh. @",
value=st.session_state.ans2_val,

# อัปเดตค่าล่าสุดเข้าตัวแปร
st. session_state.ans1_val = ans1
st.session_state.ans2_val = ans2

# * [พื้นที่สำหรับนักเรียน]: เพิ่มข้อ 3, 4 ตรงนี้

# 4. ปุ่มส่งคำตอบ
if "start" in st.session_state and not st.session_state.get("is_ended", False):
ส่งคำตอบ*) :
st. session_state. is_ended = True
st.rerun()

if st.button("

time.sleep(1)
st.rerun()
# 5. แสดง Dialog ผลลัพธ์
if st.session_state.get("is_ended", False):
show_result_dialog(ans1, ans2)
