import google.generativeai as genai

genai.configure(api_key="AIzaSyBaDl92PaCUXAX5euH6BNL4OaTSPYgLj-U")

model = genai.GenerativeModel("gemini-pro")

response = model.generate_content("Say hello in one sentence")

print(response.text)
