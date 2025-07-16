import asyncio
import pandas as pd
from googletrans import Translator


class MultiTranslator:
    def __init__(self, texts):
        self.texts = texts
        self.translator = Translator()

    async def translate_for_languages(self, languages):
        for lang in languages:
            try:
                translations = await self.translator.translate(self.texts, dest=lang)
                print(f"\n=== Translations for '{lang}' ===")
                for translation in translations:
                    if translation:
                        print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
                    else:
                        print("Translation failed for some texts.")
            except Exception as e:
                print(f"Translation failed for language {lang}: {str(e)}")


def read_texts_from_csv(file_path, column_name):
    try:
        df = pd.read_csv(file_path, encoding='mac_roman')
    except Exception as e:
        raise RuntimeError(f"Failed to read CSV file: {e}")

    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in the CSV.")

    texts = df[column_name].dropna().unique().tolist()
    return texts


if __name__ == "__main__":
    # CSV file path and column to extract
    csv_file = "/home/bglbgsz0j3/Downloads/Compliance_SET2/SET2/Compliance_feedback_set_2_de-DE.csv"
    column_to_translate = "QuestionDescription"  # e.g., "Norwegian_Text"

    # Languages to translate into
    languages = ['en']

    # Extract texts from CSV
    texts = read_texts_from_csv(csv_file, column_to_translate)
    print(f"Total texts to translate: {len(texts)}")

    # Translate
    translator = MultiTranslator(texts)
    asyncio.run(translator.translate_for_languages(languages))
