# Ai_automation


This repository contains two hands-on projects showcasing how to build smart automations using **OpenAI (ChatGPT)** and **Zapier**, along with local simulations. These are designed to demonstrate AI prompting, automation, and real-world workflows for resumes, job portfolios, and interviews.

---

Project 1: Prompt Comparison Tool

A Python tool to compare the responses from **GPT-3.5** and **GPT-4** side-by-side for the same user prompt.

- User inputs a prompt via terminal
- Sends request to GPT-3.5 (simulated, due to quota)
- (Optional) GPT-4 support
- Saves outputs in a text file for later analysis

- `prompt_comparison.py` – main code
- `prompt_results.txt` – output history (appended)


Project 2: Email Summarizer (Simulated with Zapier + OpenAI)

Simulates a Zapier workflow:
1. Trigger: Gmail fetches new emails.
2. Action: ChatGPT summarizes the email content in plain English.

Due to quota issues, this version simulates the summarization locally with a dummy email.

- `email_summarizer_simulation.py` – main script
- `simulated_summary_output.txt` – summary output

---
Tech Stack

- Python 3.10+
- OpenAI API (Simulated)
- Zapier (UI automation, simulated logic)
- Gmail (trigger source)

---

##  Project Purpose

These projects were created to:
- Practice AI integration using Zapier and OpenAI
- Build real-world automation workflows
- Demonstrate technical skills in AI and automation

⭐ Star this repo if you found it helpful!
