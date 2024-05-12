import streamlit as st  
  
# 设置页面标题  
st.title('字符计数器')  
  
# 获取用户输入  
user_input = st.text_input('请输入一些文本:', '')  
  
# 检查是否有输入  
if user_input:  
    # 计算字符数  
    char_count = len(user_input)  
      
    # 显示结果  
    st.write(f'您输入的文本有 {char_count} 个字符。')  
else:  
    st.write('请输入一些文本以查看字符数。')  
  
# 你可以在这里添加更多的Streamlit组件和功能  
  
# 如果你想在Streamlit应用中使用外部库或数据，你可以在这里导入它们  
# 例如：  
# import pandas as pd  
# data = pd.read_csv('your_data.csv')  
# st.table(data)
