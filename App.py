from dis import findlabels

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from Bio.Seq import Seq
import os

from streamlit.elements import write

print("Alles werkt!")

import streamlit as st

os.chdir("C:/Users/ayaza/OneDrive - Hogeschool Inholland/P12 Informatics/Bestanden- Project")  # Zet de werkmap
print(os.getcwd())  # Laat zien waar Python zoekt

# ==========================
# Pagina instellingen
# ==========================

st.set_page_config(
    page_title="DNA Analyzer",
    page_icon="🧬"
)



# ==========================
# Kleuren aanpassen
# ==========================

st.markdown(
    """
    <style>

    /* Achtergrond pagina */
    .stApp {
        background-color: #FCE4EC;
    }


    /* Keuzemenu achtergrond */
    section[data-testid="stSidebar"] {
        background-color: #F8C8DC;
    }


    /* Titel kleur */
    h1 {
        color: #D81B60;
    }


    </style>
    """,
    unsafe_allow_html=True
)



# ==========================
# Afbeelding toevoegen
# ==========================

with st.sidebar:

    st.image(
        "DNA22.png",
        width=300
    )



# ==========================
# Originele startpagina
# ==========================

st.title("DNA Analyzer")


st.write(
    "Welkom bij DNA analyzer! Analyseer DNA-sequenties, "
    "bereken GC-content, zoek restrictiesites, voer transcriptie uit "
    "en vergelijk twee sequenties. Kies hieronder een functie om te beginnen."
)



option = st.selectbox(
    "Kies een functie om je DNA-sequentie te analyseren",
    (
        "Aantal DNA-basen berekenen",
        "GC-content berekenen",
        "Restrictiesites herkennen",
        "DNA → mRNA transcriptie-> Translatie",
        "Twee DNA-sequenties vergelijken"
    ),
    index=None,
    placeholder="Selecteer een functie om te beginnen...",
)



st.write(
    "Uw keuze:",
    option
)
if option == "Aantal DNA-basen berekenen":

    txt = st.text_area(
        "DNA sequentie analyseren",
        "ATGCGTACCTGATCGTAACTGGCATCGTACGATCGGATCCTAGCTAGTACGATCGA",
    )

    st.write(f"Je DNA sequentie bevat {len(txt)} basen.")

    uploaded_files = st.file_uploader(
        "Upload DNA-bestanden",
        accept_multiple_files=True,
        type=["txt", "fasta"]
    )

    for uploaded_file in uploaded_files:

        st.write(uploaded_file.name)

        content = uploaded_file.read().decode("utf-8")

        sequence = ""

        for line in content.splitlines():
            if not line.startswith(">"):
                sequence += line.strip().upper()

        st.write(f"Aantal basen: {len(sequence)}")
        st.write(f"A: {sequence.count('A')}")
        st.write(f"T: {sequence.count('T')}")
        st.write(f"G: {sequence.count('G')}")
        st.write(f"C: {sequence.count('C')}")

if option == "GC-content berekenen":

    gc_txt = st.text_area(
        "DNA sequentie analyseren voor GC-content",
        "ATGCGTACCTGATCGTAACTGGCATCGTACGATCGGATCCTAGCTAGTACGATCGA",
    )

    gc_percentage = ((gc_txt.count("G") + gc_txt.count("C")) / len(gc_txt)) * 100
    at_percentage = 100 - gc_percentage

    st.write(f"Aantal basen: {len(gc_txt)}")
    st.write(f"GC content in %: {gc_percentage:.2f}")
    st.write(f"AT content in %: {at_percentage:.2f}")

    if gc_percentage < 40:
        st.write("Deze sequentie heeft een laag GC-gehalte.")

    elif gc_percentage > 60:
        st.write("Deze sequentie heeft een hoog GC-gehalte.")

    else:
        st.write("Deze sequentie heeft een gemiddeld GC-gehalte.")

    # Staafdiagram voor tekstvak
    data_txt = {
        "Base": ["A", "T", "G", "C"],
        "Aantal": [
            gc_txt.count("A"),
            gc_txt.count("T"),
            gc_txt.count("G"),
            gc_txt.count("C")
        ]
    }

    df_txt = pd.DataFrame(data_txt)

    fig, ax = plt.subplots()
    ax.bar(df_txt["Base"], df_txt["Aantal"], color="hotpink")
    ax.set_xlabel("DNA-base")
    ax.set_ylabel("Aantal")

    st.pyplot(fig)

    uploaded_files = st.file_uploader(
        "Upload DNA-bestanden",
        accept_multiple_files=True,
        type=["txt", "fasta"]
    )

    for uploaded_file in uploaded_files:

        st.write(uploaded_file.name)

        content = uploaded_file.read().decode("utf-8")

        sequence = ""

        for line in content.splitlines():
            if not line.startswith(">"):
                sequence += line.strip().upper()


        gc_content = ((sequence.count("G") + sequence.count("C")) / len(sequence)) * 100
        at_content = 100 - gc_content

        st.write(f"Aantal basen: {len(sequence)}")
        st.write(f"GC content in %: {gc_content:.2f}")
        st.write(f"AT content in %: {at_content:.2f}")

        if gc_content < 40:
            st.write("Deze sequentie heeft een laag GC-gehalte.")

        elif gc_content > 60:
            st.write("Deze sequentie heeft een hoog GC-gehalte.")

        else:
            st.write("Deze sequentie heeft een gemiddeld GC-gehalte.")


        # Staafdiagram voor geüploade file
        data = {
            "Base": ["A", "T", "G", "C"],
            "Aantal": [
                sequence.count("A"),
                sequence.count("T"),
                sequence.count("G"),
                sequence.count("C")
            ]
        }

        df = pd.DataFrame(data)

        fig, ax = plt.subplots()
        ax.bar(df["Base"], df["Aantal"], color="hotpink")

        st.pyplot(fig)

def DNA_uploaden():
    uploaded_files = st.file_uploader(
        "Upload DNA-bestanden",
        accept_multiple_files=True,
        type=["txt", "fasta"]
    )

    if uploaded_files:
        for uploaded_file in uploaded_files:
            content = uploaded_file.read().decode("utf-8")

            sequence = ""

            for line in content.splitlines():
                if not line.startswith(">"):
                    sequence += line.strip().upper()

            return sequence

    return None

os.chdir("C:/Users/ayaza/OneDrive - Hogeschool Inholland/P12 Informatics/Bestanden- Project")  # Zet de werkmap
print(os.getcwd())  # Laat zien waar Python zoekt

if option == "DNA → mRNA transcriptie-> Translatie":

    sequence = DNA_uploaden()

    if sequence:

        dna = Seq(sequence)
        mrna = dna.transcribe()

        mrna_str = str(mrna)

        # Translatie starten bij eerste AUG
        start = mrna_str.find("AUG")

        highlighted_mrna = mrna_str
        protein = "Geen startcodon (AUG) gevonden."

        if start != -1:

            stop_pos = None

            # Zoek eerste stopcodon na eerste AUG in hetzelfde leesraam
            for i in range(start + 3, len(mrna_str), 3):

                codon = mrna_str[i:i+3]

                if codon in ["UAA", "UAG", "UGA"]:
                    stop_pos = i
                    break


            # Translatiegebied bepalen
            if stop_pos is not None:

                coding_region = mrna_str[start:stop_pos+3]

            else:

                coding_region = mrna_str[start:]


            protein = Seq(coding_region).translate()


        # Markeer alle start- en stopcodons in mRNA

        highlighted_mrna = mrna_str

        # Alle AUG startcodons roze maken
        highlighted_mrna = highlighted_mrna.replace(
            "AUG",
            "<span style='color:#ff1493; font-weight:bold;'>AUG</span>"
        )

        # Alle stopcodons donkerblauw maken
        for stop in ["UAA", "UAG", "UGA"]:

            highlighted_mrna = highlighted_mrna.replace(
                stop,
                f"<span style='color:#00008B; font-weight:bold;'>{stop}</span>"
            )


        st.write("Originele DNA-sequentie:")
        st.write(dna)

        st.write("mRNA-sequentie (startcodons roze, stopcodons donkerblauw):")
        st.markdown(highlighted_mrna, unsafe_allow_html=True)

        st.write("Aminozuursequentie:")
        st.write(protein)

        st.info(
            "Hoewel meerdere start- en stopcodons aanwezig kunnen zijn in een mRNA-sequentie, "
            "wordt voor translatie de eerste mogelijke open reading frame (ORF) gebruikt."
        )

        st.image(
            "Aminozuur_def.png",
            caption="Aminozuren met juiste lettercode"
        )


        st.download_button(
            label="Download mRNA",
            data=str(mrna),
            file_name="mRNA_transcript_data.txt",
            mime="text/plain",
            icon=":material/download:"
        )


        st.download_button(
            label="Download aminozuursequentie",
            data=str(protein),
            file_name="aminozuur_sequentie.txt",
            mime="text/plain",
            icon=":material/download:"
        )


    else:
        st.write("Upload eerst een DNA-bestand.")


if option == "Twee DNA-sequenties vergelijken":

    import pandas as pd

    st.header("🧬 DNA-sequenties vergelijken")


    # Bestanden uploaden

    uploaded_file1 = st.file_uploader(
        "Upload wildtype sequentie",
        type=["txt", "fasta"]
    )

    uploaded_file2 = st.file_uploader(
        "Upload mutant sequentie",
        type=["txt", "fasta"]
    )



    # Functie om alleen DNA-sequentie te lezen

    def lees_sequentie(file):

        content = file.read().decode("utf-8")

        sequence = ""

        for line in content.splitlines():

            # FASTA header overslaan
            if line.startswith(">"):
                continue

            # Alleen DNA basen behouden
            for base in line.upper():

                if base in ["A", "T", "G", "C"]:
                    sequence += base

        return sequence



    if uploaded_file1 and uploaded_file2:


        # Sequenties inlezen

        wildtype = lees_sequentie(uploaded_file1)

        mutant = lees_sequentie(uploaded_file2)



        # Controleren of er DNA gevonden is

        if len(wildtype) == 0 or len(mutant) == 0:

            st.error(
                "Er is geen geldige DNA-sequentie gevonden in één van de bestanden."
            )

            st.stop()



        # Resultaten

        st.subheader("Resultaat")


        col1, col2 = st.columns(2)


        with col1:

            st.metric(
                "Lengte wildtype",
                f"{len(wildtype)} bp"
            )


        with col2:

            st.metric(
                "Lengte mutant",
                f"{len(mutant)} bp"
            )



        # Lengte vergelijken

        if len(wildtype) == len(mutant):

            st.success(
                "✅ De sequenties hebben dezelfde lengte."
            )

        else:

            st.warning(
                "⚠️ De sequenties hebben verschillende lengtes."
            )



        # Mutaties zoeken

        verschillen = []


        lengte = min(len(wildtype), len(mutant))


        for i in range(lengte):

            if wildtype[i] != mutant[i]:

                verschillen.append(
                    {
                        "Positie": i + 1,
                        "WT": wildtype[i],
                        "Mutant": mutant[i]
                    }
                )



        # Extra verschillen bij ongelijke lengte

        if len(wildtype) != len(mutant):

            if len(wildtype) > len(mutant):

                for i in range(lengte, len(wildtype)):

                    verschillen.append(
                        {
                            "Positie": i + 1,
                            "WT": wildtype[i],
                            "Mutant": "-"
                        }
                    )


            else:

                for i in range(lengte, len(mutant)):

                    verschillen.append(
                        {
                            "Positie": i + 1,
                            "WT": "-",
                            "Mutant": mutant[i]
                        }
                    )



        # Aantal mutaties

        st.subheader("Mutaties")


        st.metric(
            "Aantal verschillen",
            len(verschillen)
        )



        # Dataframe maken

        if verschillen:

            df = pd.DataFrame(verschillen)


            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )


        else:

            st.success(
                "Geen verschillen gevonden tussen de sequenties."
            )


            df = pd.DataFrame(
                columns=[
                    "Positie",
                    "WT",
                    "Mutant"
                ]
            )



        # Download resultaten

        st.subheader("⬇️ Resultaten downloaden")


        # CSV bestand maken

        csv = df.to_csv(
            index=False
        ).encode("utf-8")


        # TXT bestand maken

        txt = df.to_string(
            index=False
        ).encode("utf-8")



        col1, col2 = st.columns(2)



        with col1:

            st.download_button(
                label="📄 Download CSV",
                data=csv,
                file_name="DNA_mutaties_resultaat.csv",
                mime="text/csv"
            )



        with col2:

            st.download_button(
                label="📝 Download TXT",
                data=txt,
                file_name="DNA_mutaties_resultaat.txt",
                mime="text/plain"
            )

if option == "Restrictiesites herkennen":

    import pandas as pd
    from Bio.Restriction import RestrictionBatch, EcoRI, BamHI, HindIII, XhoI, NotI
    from Bio.Seq import Seq


    st.header("✂️ Restrictieanalyse")


    # Bestand uploaden
    uploaded_file = st.file_uploader(
        "Upload DNA-sequentie",
        type=["txt", "fasta"],
        key="restriction_file_upload"
    )


    # Functie om DNA-sequentie uit bestand te halen
    def lees_sequentie(file):

        content = file.read().decode("utf-8")

        sequence = ""

        for line in content.splitlines():

            # FASTA header overslaan
            if line.startswith(">"):
                continue

            # Alleen geldige DNA-basen behouden
            for base in line.upper():

                if base in "ATGC":
                    sequence += base

        return sequence



    if uploaded_file:


        # DNA-sequentie inlezen
        dna_sequence = lees_sequentie(
            uploaded_file
        )


        # Controleren of DNA aanwezig is
        if len(dna_sequence) == 0:

            st.error(
                "Geen geldige DNA-sequentie gevonden."
            )

            st.stop()



        # Aantal basen tonen
        st.success(
            f"DNA-sequentie geladen: {len(dna_sequence)} bp"
        )




        # Waarschuwing voor zeer korte sequenties
        if len(dna_sequence) < 20:

            st.warning(
                "De DNA-sequentie is erg kort. Restrictiesites kunnen hierdoor toevallig of onbetrouwbaar zijn."
            )



        # DNA omzetten naar Biopython Seq object
        sequence = Seq(
            dna_sequence
        )



        # Alleen veelgebruikte restrictie-enzymen gebruiken
        enzymen = RestrictionBatch(
            [
                EcoRI,
                BamHI,
                HindIII,
                XhoI,
                NotI
            ]
        )



        resultaten = []



        # Restrictiesites zoeken
        for enzym in enzymen:


            posities = enzym.search(
                sequence
            )


            if posities:


                resultaten.append(

                    {
                        "Enzym": str(enzym),

                        "Herkenningssite": str(
                            enzym.site
                        ),

                        "Aantal knippen": len(
                            posities
                        ),

                        "Posities (bp)": ", ".join(
                            map(str, posities)
                        )

                    }

                )



        st.subheader(
            "🧬 Restrictieresultaten"
        )



        if resultaten:


            df = pd.DataFrame(
                resultaten
            )


            st.dataframe(

                df,

                use_container_width=True,

                hide_index=True

            )



            # CSV bestand maken
            csv = df.to_csv(
                index=False
            ).encode(
                "utf-8"
            )



            st.download_button(

                label="Download restrictieresultaten CSV",

                data=csv,

                file_name="restrictieanalyse.csv",

                mime="text/csv",

                key="restriction_csv_download"

            )



        else:


            st.success(
                "Geen restrictiesites gevonden."
            )
