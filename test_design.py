import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Preview Design", layout="wide")

# CSS personnalisé
st.markdown("""
<style>
    .title-animation {
        animation: fadeIn 1.5s ease-in;
    }
    
    .form-section {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        animation: slideIn 0.5s ease-out;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    @keyframes slideIn {
        from { transform: translateX(-20px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    .stButton > button {
        width: 100%;
        border-radius: 20px;
        background: linear-gradient(90deg, #FF4B4B 0%, #FF8080 100%);
        padding: 10px 20px;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(255, 75, 75, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# Titre
st.markdown('<h1 class="title-animation">Recommandations internes</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="title-animation">Agence Orpi Panazol, Arcades, La Souterraine et Saint-Yrieix</h3>', unsafe_allow_html=True)

# Formulaire de test
with st.form("test_form"):
    st.markdown('<div class="form-section">', unsafe_allow_html=True)
    st.subheader("📋 Informations prescripteur")
    st.text_input("Votre nom complet *")
    st.text_input("E-mail du receveur *")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="form-section">', unsafe_allow_html=True)
    st.subheader("👤 Informations client")
    col1, col2 = st.columns(2)
    with col1:
        st.text_input("Nom client *")
        st.text_input("Téléphone *")
    with col2:
        st.text_input("Email *")
        st.selectbox("Projet *", ["Vente", "Achat", "Location"])
    st.markdown('</div>', unsafe_allow_html=True)
    
    submit = st.form_submit_button("Je valide ma recommandation")

if submit:
    st.markdown('<div style="padding: 20px; border-radius: 10px; background: #4CAF50; color: white; animation: slideUp 0.5s ease-out;">✨ Test réussi !</div>', unsafe_allow_html=True)
