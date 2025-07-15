def fetch_email():
    return {
        "subject": "March Edition of GLA Newsletter",
        "body": "Dear GLA Family,\nWe are pleased to share the March highlights: tech fests, placement drives, and more..."
    }

def summarize_email(email):
    return f"Summary: {email['subject']} - A recap of March events like tech fests and placements."

def main():
    print("📥 Fetching Email...")
    email = fetch_email()
    print("✅ Email Retrieved:\n", email)

    print("\n🤖 Simulating OpenAI Summarization...")
    summary = summarize_email(email)
    print("\n📄 Summary:\n", summary)

    with open("simulated_summary_output.txt", "w", encoding="utf-8") as file:
        file.write(summary)
    print("\n📁 Summary saved to 'simulated_summary_output.txt'.")

if __name__ == "__main__":
    main()
