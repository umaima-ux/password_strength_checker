import re
import random
import string
import streamlit as st

# ✅ Function to Check Password Strength
def check_password_strength(password):
    score = 0
    messages = []
    
    # ✅ Length Check
    if len(password) >= 8:
        score += 1
    else:
        messages.append("❌ Password should be at least 8 characters long.")

    # ✅ Uppercase & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        messages.append("❌ Include both uppercase and lowercase letters.")

    # ✅ Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        messages.append("❌ Add at least one number (0-9).")

    # ✅ Special Character Check (More Secure)
    special_chars = "!@#$%^&*()_+[]{}|;:',.<>?/~`"
    if re.search(f"[{re.escape(special_chars)}]", password):
        score += 1
    else:
        messages.append("❌ Include at least one special character (!@#$%^&*).")

    return score, messages

# ✅ Function to Generate a Strong Password
def generate_strong_password():
    length = random.randint(12, 16)  # Random length between 12-16
    characters = string.ascii_letters + string.digits + "!@#$%^&*()_+[]{}|;:',.<>?/~`"
    return ''.join(random.choice(characters) for _ in range(length))

# ✅ Streamlit UI
st.set_page_config(page_title="Password Strength Checker", page_icon="🔒", layout="centered")

# 🏷 Title
st.markdown("<h2 style='text-align: center; color: #4A90E2;'>🔒 Password Strength Checker</h2>", unsafe_allow_html=True)

# 📝 User Input
password = st.text_input("Enter your password:", type="password")

# 🎨 UI Enhancements
st.markdown("---")  # Divider Line

# 🔘 Submit Button
if st.button("Check Password"):
    if password:
        score, results = check_password_strength(password)

        # 🟢 Progress Bar with Color Code
        progress_color = ["red", "yellow", "green"]
        progress_value = score / 4
        st.markdown(
            f"""
            <style>
            .stProgress > div > div > div > div {{
                background-color: {progress_color[min(score, 2)]};
            }}
            </style>""",
            unsafe_allow_html=True,
        )
        st.progress(progress_value)

        # 🎯 Color-Coded Feedback
        if score == 4:
            st.success("✅ Strong Password!")
        elif score == 3:
            st.warning("⚠️ Moderate Password - Consider adding more security features.")
        else:
            st.error("❌ Weak Password - Improve it using the suggestions below.")

            # ✅ Generate a Strong Password if the entered one is weak
            strong_password = generate_strong_password()
            st.warning(f"🔑 Try this strong password: `{strong_password}`")
            
            # ✅ Corrected Copy Button (Replaced deprecated function)
            st.button("Copy to Clipboard", on_click=lambda: st.query_params.update({"pwd": strong_password}))

        # 🟢 Show improvement suggestions
        for msg in results:
            st.write(msg)
    else:
        st.error("⚠️ Please enter a password first!")
