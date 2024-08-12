import streamlit as st

# 标题
st.title("简单的 Streamlit 项目")

# 获取用户输入
name = st.text_input("请输入你的名字")

# 显示一个选择框
greeting_option = st.selectbox("选择问候语", ["你好", "Hello", "Hola", "Bonjour"])

# 按钮
if st.button("显示问候"):
    st.write(f"{greeting_option}, {name}!")
