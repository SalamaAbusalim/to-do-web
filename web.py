import streamlit
import functions

todos = functions.get_todo()


def add_todo():
    todo = streamlit.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todo(todos)


streamlit.title("My Todo App ")
streamlit.subheader("This is my todo app")
streamlit.write("This app aims to increase productivity")

for index, todo in enumerate(todos):
    checkbox = streamlit.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todo(todos)
        del streamlit.session_state[todo]
        streamlit.experimental_rerun()

streamlit.text_input(label="", placeholder="Add todo...",
                     on_change=add_todo, key="new_todo")
