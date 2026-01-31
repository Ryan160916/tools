import streamlit as st
from datetime import time, datetime

st.header('任务')
task_name = st.text_input('任务名称')
task_project = st.text_input('所属项目')
task_tgpe = st.selectbox('任务类型',('学习','编程','运动'))
task_state = st.multiselect('任务状态',('计划中','执行中','已完成'))
task_date = st.text_input('任务日期')
task_time = st.slider('任务时间',value=(time(0,00),time(23,59)))
task_keywod = st.multiselect('关键词',('计算机','AI','学习','运动'))
if st.button('提交'):
    st.write('提交成功')