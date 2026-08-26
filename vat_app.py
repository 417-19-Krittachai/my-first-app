import steamlit as st
st.title("🛒แอปพลิเคชั่นคำนวณราคาสินค้ารวม VAT 7%")
vat = price * 0.07
st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")
import streamlit as st
price = st.number_input("กรอกราคาสินค้า (บาท):", value=0.0)
net_price = price - vat
st.write("นายกฤตชัย เเก้วอุ่น เลขที่ 19  ม.4/17")
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")
