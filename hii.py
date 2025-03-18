import streamlit as st
import requests
import json
import random
from streamlit_lottie import st_lottie

# ✅ Secure API Key
API_KEY = "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"

# ✅ Load Lottie Animation
st.set_page_config(page_title="Manasāroha: Your Mental Wellness Companion", page_icon="🧘", layout="centered")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ✅ OpenRouter Mood Analysis Function
@st.cache_data
def get_mood_analysis(user_input):
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "model": "deepseek/deepseek-r1:free",
                "messages": [
                    {"role": "system", "content": "You are an AI assistant that detects user mood based on text input and provides recommendations."},
                    {"role": "user", "content": user_input}
                ]
            })
        )
        response_json = response.json()
        return response_json["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"API Error: {str(e)}"
    # ✅ Lists for Recommendations
movies = ["Inception", "3 Idiots", "The Shawshank Redemption", "Lagaan", "Interstellar", "Zindagi Na Milegi Dobara", "The Dark Knight", "Dil Chahta Hai", "Forrest Gump", "Gully Boy", "Pulp Fiction", "Queen", "Titanic", "Taare Zameen Par", "The Matrix", "Swades", "Gladiator", "Kahaani", "Avengers: Endgame", "Barfi!", "The Godfather", "Andhadhun", "Schindler's List", "Drishyam", "Fight Club", "PK", "Joker", "Black", "The Pursuit of Happyness", "Rockstar", "La La Land", "Shershaah", "The Lion King", "Article 15", "Eternal Sunshine of the Spotless Mind", "Bajrangi Bhaijaan", "Dead Poets Society", "Tamasha", "The Green Mile", "Super 30", "Good Will Hunting", "Haider", "The Social Network", "Parineeta", "Catch Me If You Can", "Highway", "12 Angry Men", "Bhaag Milkha Bhaag", "The Grand Budapest Hotel", "Rang De Basanti", "Cast Away", "Paan Singh Tomar", "The Truman Show", "Masaan", "A Beautiful Mind", "Dear Zindagi", "The Departed", "M.S. Dhoni: The Untold Story", "The Prestige", "Kantara", "Oppenheimer", "Everything Everywhere All at Once", "Drishyam 2", "The Whale", "Top Gun: Maverick"]

songs = ["Shape of You - Ed Sheeran", "Tum Hi Ho - Arijit Singh", "Someone Like You - Adele", "Channa Mereya - Arijit Singh", "Blinding Lights - The Weeknd", "Kun Faya Kun - A.R. Rahman", "Hello - Adele", "Agar Tum Saath Ho - Alka Yagnik, Arijit Singh", "Bohemian Rhapsody - Queen", "Kesariya - Arijit Singh", "Rolling in the Deep - Adele", "Bekhayali - Sachet Tandon", "Let It Be - The Beatles", "Phir Le Aya Dil - Arijit Singh", "Thinking Out Loud - Ed Sheeran", "Kabira - Tochi Raina", "Smells Like Teen Spirit - Nirvana", "Tera Ban Jaunga - Akhil Sachdeva", "Take Me to Church - Hozier", "Dil Dhadakne Do - Priyanka Chopra", "Counting Stars - OneRepublic", "Raabta - Arijit Singh", "Believer - Imagine Dragons", "Ilahi - Mohit Chauhan", "Stay - Justin Bieber", "Suno Na Sangemarmar - Arijit Singh", "Viva La Vida - Coldplay", "Galliyan - Ankit Tiwari", "Senorita - Shawn Mendes, Camila Cabello", "Jeene Laga Hoon - Atif Aslam"]

books = ["The Alchemist - Paulo Coelho", "Bhagavad Gita - Vyasa", "To Kill a Mockingbird - Harper Lee", "The Palace of Illusions - Chitra Banerjee", "1984 - George Orwell", "Train to Pakistan - Khushwant Singh", "Pride and Prejudice - Jane Austen", "The White Tiger - Aravind Adiga", "Atomic Habits - James Clear", "The Monk Who Sold His Ferrari - Robin Sharma", "Harry Potter Series - J.K. Rowling", "Shiva Trilogy - Amish Tripathi", "Sapiens - Yuval Noah Harari", "Ikigai - Hector Garcia", "Wings of Fire - A.P.J. Abdul Kalam", "Rich Dad Poor Dad - Robert Kiyosaki", "The Subtle Art of Not Giving a F*ck - Mark Manson", "The Kite Runner - Khaled Hosseini", "Zero to One - Peter Thiel", "Mahabharata - Vyasa", "Steve Jobs - Walter Isaacson", "The Psychology of Money - Morgan Housel", "Ramayana - Valmiki", "Deep Work - Cal Newport", "Can't Hurt Me - David Goggins", "The Power of Now - Eckhart Tolle"]

quotes = ["Believe you can and you're halfway there.", "Your time is limited, so don’t waste it living someone else’s life.", "Success is not final, failure is not fatal: it is the courage to continue that counts.", "Happiness depends upon ourselves.", "The only way to do great work is to love what you do."]

# 🌿 Light Mode Theme Styling
st.markdown("""
    <style>
        body { background-color: #f7f9fc; }
        h1 { color: #2c3e50; font-size: 36px; font-weight: bold; text-align: center; }
        .subtitle { color: #34495e; font-size: 18px; text-align: center; margin-bottom: 30px; }
        .button-container { text-align: center; }
        .stButton>button { background-color: #4CAF50; color: white; border-radius: 8px; padding: 10px 20px; font-size: 18px; }
    </style>
""", unsafe_allow_html=True)

# 🌿 Header Section
st.markdown("""
    <style>
        .subtitle { color: white; font-size: 18px; text-align: center; margin-bottom: 30px; }
    </style>
    <h1>🌿 Manasāroha: Your Mental Wellness Companion 🧘</h1>
    <p class='subtitle'>Guiding you towards inner peace, clarity, and emotional balance through ancient wisdom and modern mindfulness techniques.</p>
""", unsafe_allow_html=True)


# 🌟 Mood Analysis Section
st.markdown("""
    <style>
        * {
            font-family: 'Times New Roman', Times, serif;
        }
    </style>
""", unsafe_allow_html=True)
st.subheader("💭 How are you feeling today?")
st.write("Share your thoughts, and let Manasāroha guide you towards peace and positivity.")
user_input = st.text_area("Type your emotions here...", placeholder="I feel...", height=120)

if st.button("✨ Analyze Mood", use_container_width=True):
    if user_input:
        with st.spinner("Analyzing your mood..."):
            result = get_mood_analysis(user_input)
        if "API Error" in result:
            st.error(result)
        else:
            mood = result.capitalize()
            st.success(f"🌼 Detected Mood: {mood}")
    else:
        st.warning("Please enter some text to analyze your mood.")

# 🎲 Feeling Spontaneous?
st.subheader("🎲 Feeling Spontaneous?")
if st.button("I am Feeling Lucky 🎉", use_container_width=True):
    st.write(f"🎬 **Movie Recommendation:** {random.choice(movies)}")
    st.write(f"🎵 **Song Recommendation:** {random.choice(songs)}")
    st.write(f"📖 **Book Recommendation:** {random.choice(books)}")
    st.write(f"💡 **Inspirational Quote:** \"{random.choice(quotes)}\"")

# 🌸 Final Message
st.markdown("""
<p style='text-align: center; font-size: 22px;'>
    🌱 <strong>Embracing Mental Well-being</strong><br>
    Your mind is a garden—nurture it with positivity, gratitude, and self-care. Just as the body needs rest, the soul thrives in stillness. Take a deep breath, embrace the present, and let go of worries. 🌿
</p>

<p style='text-align: center; font-size: 22px;'>
    🧘 <strong>The Power of Spiritual Balance</strong><br>
    True peace is not found in external achievements but in the harmony of the heart and mind. Whether through mindfulness, meditation, or soulful reflection, every step towards inner awareness brings you closer to lasting serenity. 🌸
</p>

<p style='text-align: center; font-size: 22px;'>
    🌼 <strong>Words to Remember</strong><br>
    You are not your thoughts; you are the observer of your thoughts.<br>
    Healing begins the moment you allow yourself to feel without judgment.<br>
    A calm mind leads to a stronger spirit—embrace the journey within.
</p>

<p style='text-align: center; font-size: 22px;'>
    🌸 Let Manasāroha be your sanctuary for mental well-being. Every thought finds clarity, every heart finds peace. 🌸
</p>
<p style='text-align: center; font-size: 22px; font-weight: bold;'>
    💙 Made with love and mindfulness by [Your Name/Brand] 🙏
</p>
""", unsafe_allow_html=True)
