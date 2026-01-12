import streamlit as st
from retriever import retrieve_kurals

# Page configuration
st.set_page_config(
    page_title="Thirukkural Chatbot",
    page_icon="📜",
    layout="centered"
)

# App title
st.title("📖 Thirukkural Chatbot")
st.caption("An AI-powered, article-wise assistant for Thirukkural")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_query = st.chat_input("Ask about Thirukkural (e.g., friendship, virtue, leadership)")

if user_query:
    # Display user message
    st.session_state.messages.append(
        {"role": "user", "content": user_query}
    )
    with st.chat_message("user"):
        st.markdown(user_query)

    # Retrieve answers
    with st.chat_message("assistant"):
        with st.spinner("Searching Thirukkural..."):
            results = retrieve_kurals(user_query, top_k=2)

            if not results:
                response = "❌ No relevant Thirukkural found."
            else:
                response = ""
                for r in results:
                    response += f"""
### 📜 Kural {r['kural_id']}
**Adhigaram:** {r['adhigaram']}  
**Paal:** {r['paal']}

**Tamil Verse:**  
{r['kural_tamil']}

**English Meaning:**  
{r['meaning_english']}

**Explanation:**  
{r['explanation']}

---
"""
            st.markdown(response)

    # Save assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
