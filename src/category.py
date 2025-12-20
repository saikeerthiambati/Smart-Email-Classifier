import pandas as pd
import re

print("📁 Adding category and urgency...")

# =========================
# Load datasets
# =========================
df = pd.read_csv(r"../data/Clean Datasets/spam_dataset_cleaned_encoded.csv")
email = pd.read_csv(r"../data/Raw Datasets/emailclass.csv")

# =========================
# Text cleaning function
# =========================
def clean(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www.\S+", "", text)
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Clean email text
email['clean_text'] = email['text'].apply(clean)

# Rename type → category
email = email.rename(columns={'type': 'category'})

# =========================
# Merge category
# =========================
df = df.merge(
    email[['clean_text', 'category']],
    on='clean_text',
    how='left'
)

# For spam emails, force category = spam
df.loc[df['label'] == 1, 'category'] = 'spam'

# Fill missing categories
df['category'] = df['category'].fillna('general')

# =========================
# Urgency Detection Logic
# =========================
def assign_urgency(text, category):
    text = str(text).lower()

    # Base urgency from category
    if category.lower() == "complaint":
        urgency = "High"
    elif category.lower() == "request":
        urgency = "Medium"
    else:
        urgency = "Low"

    # Keyword-based escalation
    high_keywords = [
        "urgent", "asap", "immediately",
        "not working", "down", "failed",
        "error", "critical"
    ]

    medium_keywords = [
        "please check", "follow up",
        "by today", "by tomorrow"
    ]

    for word in high_keywords:
        if word in text:
            return "High"

    for word in medium_keywords:
        if word in text and urgency != "High":
            return "Medium"

    return urgency

# Apply urgency
df['urgency'] = df.apply(
    lambda row: assign_urgency(row['clean_text'], row['category']),
    axis=1
)

# =========================
# Save final dataset
# =========================
output_path = "../data/Clean Datasets/spam_with_category_and_urgency.csv"
df.to_csv(output_path, index=False)

# =========================
# Verification
# =========================
print("✔ Category & urgency added successfully!")

print("\n📊 Category Distribution:")
print(df['category'].value_counts())

print("\n📊 Urgency Distribution:")
print(df['urgency'].value_counts())

print(f"\n🎉 Saved as {output_path}")
print("✅ Process complete!")
