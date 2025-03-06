import streamlit as st
from PIL import Image

def main():
    st.title("Contrôle Qualité : Vis")
    st.write("Cette application diagnostique toujours que la vis est conforme.")

    uploaded_file = st.file_uploader("Chargez une image de vis (format .jpg/.png)...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Affiche l'image chargée
        image = Image.open(uploaded_file)
        st.image(image, caption="Vis chargée", use_container_width=True)

        # Diagnostic fixe : la vis est toujours de bonne qualité
        st.write("**Diagnostic :** Aucun défaut détecté.\n")
        st.success("Vis de bonne qualité !")

if __name__ == "__main__":
    main()