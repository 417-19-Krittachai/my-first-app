import streamlit as st
st.title("🛒แอปพลิเคชั่นคำนวณราคาสินค้ารวม VAT 7%")
price=st.number_input("200 (บาท):",value=0.0)
import streamlit as st
price = st.number_input("35 (บาท):", value=0.0)
net_price = 200 - 35
st.write("นายกฤตชัย เเก้วอุ่น เลขที่ 19  ม.4/17")
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")
