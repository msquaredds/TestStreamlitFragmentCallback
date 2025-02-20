import streamlit as st


def _set_state():
    st.session_state.test = True


@st.fragment
def _fragment_test():
    button_cols = st.sidebar.columns(2)
    with button_cols[0]:
        st.button("Test", on_click=_set_state)
    if 'test' in st.session_state and st.session_state.test:
        st.write("Test is True")


def main():
    _fragment_test()


if __name__ == "__main__":
    main()
