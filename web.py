import streamlit as st
from funktions import *

todo_list = import_todo_list()

def add_todo():
    new_todo = st.session_state['new_todo']
    if new_todo == '':
        pass
    else:
        todo_list.append(new_todo + '\n')
        save_todo_list(todo_list)

def clear_list():
    todo_list.clear()
    save_todo_list(todo_list)

st.title('My Todo-App')
st.write('\n')
st.write('''
<p>This App only exists to increase my productivity o_O \n
What a poor and sad existence this must be!</p>
''', unsafe_allow_html=True)
st.write('\n')

st.text_input(label="Enter a todo:",
              placeholder='Add a new todo here...',
              on_change=add_todo,
              key='new_todo')

for index, todo in enumerate(todo_list):
    checkbox = st.checkbox(todo,
                           key=index)
    if checkbox:
        todo_list.pop(index)
        save_todo_list(todo_list)
        del st.session_state[index]
        st._rerun()

st.button(label='Clear List',
          on_click=clear_list)

