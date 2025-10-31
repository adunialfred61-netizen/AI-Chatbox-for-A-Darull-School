# 🏫 Daruk OLOOM Intelligent School Assistant

A simple yet powerful **AI-powered chatbot** built using **Python** and **Gradio**, designed to provide instant answers to questions about **Daruk OLOOM Islamic School**.  
It reads from a structured **JSON data file (`Oloom.json`)** and intelligently responds to queries about school information — including admissions, fees, teachers, schedule, and more.

---

## 🚀 Features

- **Dynamic Data Loading:** Automatically reloads school information every time the JSON file is updated.  
- **Smart Reasoning Engine:** Understands natural language questions (e.g., *“Who is the headmaster?”*, *“When do classes start?”*).  
- **Multi-topic Support:** Handles queries about:
  - School name & headmaster  
  - Location and contact info  
  - Academic structure & schedule  
  - Fees & admission details  
  - Teachers’ info and salaries  
  - Motto, vision, and mission  
- **Gradio Web Interface:** Clean, interactive, and accessible chatbot UI.  
- **Expandable:** Can easily be extended to include new data fields and smarter logic.

---

## 🧠 Project Structure

```
Daruk_Oloom_Assistant/
│
├── Oloom.json               # The school information data file (editable anytime)
├── app.py                   # Main chatbot script
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation (this file)
```

---

## ⚙️ Installation

1. **Clone this repository:**
   ```bash
   git clone ....
   cd daruk-oloom-assistant
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:
   ```bash
   pip install gradio
   ```

3. **Ensure your `Uloom.json` file** is in the same directory and structured like this:
   ```json
   {
     "school_info": {
       "name": "Daruk OLOOM Islamic School",
       "headmaster": "Mallam Faruk",
       "location": {
         "address": "Paga, Nania, around the market",
         "region": "Upper East Region",
         "country": "Ghana"
       },
       "contact": {
         "phone": "054XXXXXXX",
         "email": "darukoloom@gmail.com",
         "office_hours": "8:00 AM to 4:00 PM"
       },
       "school_type": "Islamic and General Education",
       "founded_year": "2005",
       "academic_structure": {
         "subjects_offered": ["Math", "English", "Arabic", "Science", "Social Studies"...],
         "class_schedule": {
           "start_time": "8:00 AM",
           "end_time": "3:00 PM",
           "arabic_teaching_time": "3:00 PM to 5:00 PM"
         }
       },
       "fees_structure": {
         "primary_school": "₵200",
         "junior_high_school": "₵300",
         "payment_deadline": "Second week of the term"
       },
       "admission_info": {
         "status": "Open",
         "details": "Forms are available at the school office.",
         "requirements": ["Birth certificate", "Previous report card", "Passport photo"]
       },
       "teacher_info": {
         "payment_schedule": "end of every month",
         "teacher_fees": {
           "primary_school_teacher": "**0",
           "junior_high_teacher": "***"
         }
       },
       "vision": "To raise disciplined and knowledgeable students grounded in both Islamic and general education.",
       "mission": "To provide quality education with moral guidance.",
       "motto": "Knowledge and Discipline",
       "student_guidance": {
         "internet_use": "Students are encouraged to use the internet responsibly.",
         "research": "Research activities are guided by teachers."
       }
     }
   }
   ```

---

## ▶️ Running the App

Run the chatbot locally using:

```bash
python app.py
```

You’ll see an output like:
```
Running on local URL: http://127.0.0.1:7860
Running on public URL: https://your-ngrok-link.gradio.live
```

Click the **public URL** to open the chatbot in your browser.

---

## 📱 Using on Mobile

If you want to access the chatbot on your phone:
1. Run the app on your laptop.
2. Copy the **gradio public link** (e.g., `https://xxxxx.gradio.live`).
3. Open it on your phone — the chatbot will work just like a normal website.
4. You can also share the link with others for demo purposes.

---

## 💡 Example Queries

| Query | Example Response |
|-------|------------------|
| Who is the headmaster? | The headmaster of Daruk OLOOM Islamic School is Mallam Faruk. |
| Where is the school located? | Daruk OLOOM is located at Paga, Nania, around the market in Upper East Region, Ghana. |


---

## 🧩 Customization

You can modify:
- `Uloom.json` → update school info.
- `analyze_query()` → add new question logic.
- Interface title, description, and UI labels in the `gr.Interface()` section.

The chatbot automatically reflects changes without restarting — just save your JSON file.

---

## 🧱 Dependencies

- Python 3.9+
- [Gradio](https://www.gradio.app/)
- JSON (standard library)
- re (standard library)

---

## 🧑‍💻 Author

**ADUNI**  
Full Stack Developer | Data Analyst | Geospatial Expert | AI Innovator  
📧 Contact: adunialfred61@gmail.com  

---

## 🌍 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute with credit.
