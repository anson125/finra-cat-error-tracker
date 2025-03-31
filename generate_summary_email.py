import pandas as pd

# Load sample mock error data
df = pd.read_csv("mock_error_data.csv")

# Summarize by severity
summary = df.groupby("Severity")["Error ID"].count().reset_index()
summary.columns = ["Severity", "Error Count"]

# Convert to email body format
email_body = "Subject: Daily CAT 2E Error Summary\n\n"
email_body += "Today's Error Breakdown by Severity:\n"
for _, row in summary.iterrows():
    email_body += f"- {row['Severity']}: {row['Error Count']} errors\n"

email_body += "\nTotal Errors: {}\n".format(len(df))
email_body += "Please review open items before EOD."

# Save summary as .txt (simulating email body)
with open("daily_summary_email.txt", "w") as f:
    f.write(email_body)

print("Email summary generated.")
