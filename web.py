import streamlit as st
import func

todos = func.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    func.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my first app.")
st.write("This app will increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        func.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo:",placeholder="Enter...",on_change=add_todo,key='new_todo')
