import streamlit as st

def _set_state():
    st.session_state.test = True


def main():
    st.button("Test", on_click=_set_state)
    if st.session_state.test:
        st.write("Test is True")


if __name__ == "__main__":
    main()