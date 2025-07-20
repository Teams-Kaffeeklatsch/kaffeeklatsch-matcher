import streamlit as st
import random
import pandas as pd

st.title("Kaffeeklatsch Gruppen-Matcher ☕")

# Namen eingeben
names_input = st.text_area("Gib die Namen der Mitarbeiter*innen ein (ein Name pro Zeile):")
names = [name.strip() for name in names_input.split("\n") if name.strip()]

# Gruppengröße wählen
group_size = st.radio("Gruppengröße:", options=[2, 3])

if st.button("Gruppen bilden"):
    if len(names) < 2:
        st.warning("Bitte mindestens 2 Namen eingeben.")
    else:
        # Shuffle und Gruppen bilden
        random.shuffle(names)
        groups = []
        i = 0
        n = len(names)

        while i < n:
            # Wenn am Ende 1 übrig ist, mache eine Gruppe mit 3
            if n - i == 3 or (group_size == 2 and n - i == 1):
                group = names[i:i+3]
                i += 3
            else:
                group = names[i:i+group_size]
                i += group_size
            groups.append(group)

        st.write("### Hier sind deine Gruppen:")
        for idx, group in enumerate(groups, 1):
            st.write(f"**Gruppe {idx}:** " + ", ".join(group))

        # Download als CSV
        df = pd.DataFrame({"Gruppe": [f"Gruppe {i+1}" for i in range(len(groups))],
                           "Mitglieder": [", ".join(g) for g in groups]})
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Gruppen als CSV herunterladen", csv, "kaffeeklatsch_gruppen.csv", "text/csv")
