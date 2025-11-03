import pandas as pd
from jiwer import wer, cer


asr1 = "s1.tsv"
asr2 = "s2.tsv"

def evaluate_asr(tsv_file):
    # Read TSV without headers
    df = pd.read_csv(tsv_file, sep="\t", header=None, names=["Start","End","ASR Output","Reference"])

    # Replace NaN with empty string and convert to string type
    df["ASR Output"] = df["ASR Output"].fillna("").astype(str)
    df["Reference"] = df["Reference"].fillna("").astype(str)

    # Normalize text
    df["ASR Output"] = df["ASR Output"].str.lower().str.strip()
    df["Reference"] = df["Reference"].str.lower().str.strip()

    # Combine all ASR outputs and references
    asr_full = " ".join(df["ASR Output"])
    ref_full = " ".join(df["Reference"])

    # Compute WER & CER
    word_error = wer(ref_full, asr_full)
    char_error = cer(ref_full, asr_full)

    return word_error, char_error


# Evaluate both systems
wer1, cer1 = evaluate_asr(asr1)
wer2, cer2 = evaluate_asr(asr2)

# Print results
print(f"ASR System 1 - WER: {wer1:.4f}, CER: {cer1:.4f}")
print(f"ASR System 2 - WER: {wer2:.4f}, CER: {cer2:.4f}")

