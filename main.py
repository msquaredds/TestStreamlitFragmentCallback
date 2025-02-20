import streamlit as st


def _set_state():
    st.session_state.test = True


@st.fragment
def _frag_test():
    st.button("Test", on_click=_set_state)
    if 'test' in st.session_state and st.session_state.test:
        st.write("Test is True")


def main():
    _frag_test()


if __name__ == "__main__":
    main()
