
import streamlit as st

from main import generate_answer
from retrieve import retrieve_documents

st.set_page_config(
    page_title="B2G Policy Assistant",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -------------------- Styling --------------------

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    .stApp {
        font-family: 'Inter', sans-serif;
    }

    [data-testid="stSidebar"] {
        border-right: 1px solid rgba(128, 128, 128, 0.2);
    }

    .app-title {
        font-size: 30px;
        font-weight: 700;
        letter-spacing: -1px;
        margin-bottom: 6px;
    }

    .app-subtitle {
        font-size: 14px;
        opacity: 0.7;
        margin-bottom: 24px;
    }

    div[data-testid="stChatMessage"] {
        border-radius: 14px;
        padding: 12px;
    }

    .stButton > button {
        border-radius: 10px;
        text-align: left;
        min-height: 40px;
    }

    div[data-testid="stChatInput"] {
        border-radius: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------- Sidebar --------------------

with st.sidebar:
    st.markdown("### Policy Assistant")

    if st.button("＋  New conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.markdown("#### Suggested questions")

    suggestions = [
        "How should a tender be assessed for relevance?",
        "What happens if a mandatory certification is unverified?",
        "What information is recorded during tender intake?",
        "What is the financial approval limit?",
    ]

    for index, suggestion in enumerate(suggestions):
        if st.button(
            suggestion,
            key=f"suggestion_{index}",
            use_container_width=True,
        ):
            st.session_state.pending_question = suggestion

# -------------------- Chat area --------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown(
    """
    <div class="app-title">Policy Assistant</div>
    <div class="app-subtitle">
        Ask questions about your B2G policy documents.
    </div>
    """,
    unsafe_allow_html=True,
)

# Display previous messages.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message.get("sources"):
            with st.expander("Sources"):
                for source in message["sources"]:
                    st.markdown(f"**{source['name']}**")
                    st.caption(source["content"])

# Process a suggested question or typed question.
pending_question = st.session_state.pop("pending_question", None)
typed_question = st.chat_input("Ask a policy question...")

question = pending_question or typed_question

if question:
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Finding an answer..."):
            try:
                answer = generate_answer(question)
                documents = retrieve_documents(question)

                sources = []
                seen_sources = set()

                for document in documents:
                    source_name = document.metadata.get(
                        "source", "Unknown source"
                    )

                    if source_name not in seen_sources:
                        seen_sources.add(source_name)
                        sources.append(
                            {
                                "name": source_name,
                                "content": document.page_content,
                            }
                        )

                st.markdown(answer)

                if sources:
                    with st.expander("Sources"):
                        for source in sources:
                            st.markdown(f"**{source['name']}**")
                            st.caption(source["content"])

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer,
                        "sources": sources,
                    }
                )

            except Exception as error:
                st.error("Unable to generate an answer. Please try again.")
                st.caption(f"Technical details: {error}")
