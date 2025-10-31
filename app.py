import json
import gradio as gr
import re

# --- Load JSON file dynamically every time (auto-refresh when changed) ---
def load_school_data():
    with open("Oloom.json", "r") as f:
        return json.load(f)["school_info"]

# --- Smart reasoning engine ---
def analyze_query(query, data):
    q = query.lower()
    response = ""

    # --- Basic fields ---
    if any(word in q for word in ["name", "school name"]):
        response = f"The name of the school is {data['name']}."

    elif any(word in q for word in ["headmaster", "principal", "head teacher"]):
        response = f"The headmaster of {data['name']} is {data['headmaster']}."

    elif any(word in q for word in ["location", "where", "situated", "address"]):
        loc = data["location"]
        response = f"{data['name']} is located at {loc['address']} in {loc['region']} region, {loc['country']}."

    elif any(word in q for word in ["contact", "phone", "email", "reach"]):
        c = data["contact"]
        response = (
            f"You can contact {data['name']} at {c['phone']} or email {c['email']}. "
            f"The office is open {c['office_hours']}."
        )

    elif "type" in q or "kind of school" in q:
        response = f"{data['name']} is a {data['school_type']}."

    elif "founded" in q or "established" in q or "year" in q:
        response = f"{data['name']} was founded in {data['founded_year']}."

    # --- Academic info ---
    elif "subject" in q or "teach" in q:
        subjects = data["academic_structure"]["subjects_offered"]
        if any(x in q for x in ["how many", "number", "count"]):
            response = f"The school teaches {len(subjects)} subjects in total."
        else:
            response = (
                f"The school offers the following subjects: {', '.join(subjects)}."
            )

    elif any(word in q for word in ["schedule", "time", "start", "end", "closing", "arabic"]):
        sch = data["academic_structure"]["class_schedule"]
        response = (
            f"Classes start at {sch['start_time']} and close at {sch['end_time']}. "
            f"Arabic lessons run from {sch['arabic_teaching_time']}."
        )

    # --- Fees ---
    elif "fee" in q or "payment" in q or "price" in q:
        f = data["fees_structure"]
        response = (
            f"The school fees are {f['primary_school']} for Primary "
            f"and {f['junior_high_school']} for Junior High per term. "
            f"Payment deadline is {f['payment_deadline']}."
        )

    # --- Admissions ---
    elif "admission" in q or "enroll" in q or "register" in q:
        a = data["admission_info"]
        response = (
            f"Admissions are currently {a['status'].lower()}. "
            f"{a['details']}. Requirements include {', '.join(a['requirements'])}."
        )

    # --- Teachers ---
    elif "teacher" in q:
        t = data["teacher_info"]
        if any(w in q for w in ["salary", "paid", "payment", "earn", "take"]):
            response = (
                f"Teachers are paid on the {t['payment_schedule']}. "
                f"Primary teachers earn {t['teacher_fees']['primary_school_teacher']} "
                f"while junior high teachers earn {t['teacher_fees']['junior_high_teacher']}."
            )
        else:
            response = "Teachers are dedicated and well-compensated at the school."

    # --- Motto / Vision / Mission ---
    elif "vision" in q:
        response = f"The school’s vision is: {data['vision']}."
    elif "mission" in q:
        response = f"The school’s mission is: {data['mission']}."
    elif "motto" in q and data["motto"]:
        response = f"The school’s motto is: {data['motto']}."
    elif "motto" in q:
        response = "The school has no official motto recorded yet."

    # --- Guidance ---
    elif "internet" in q or "research" in q or "guidance" in q:
        g = data["student_guidance"]
        response = f"{g['internet_use']} {g['research']}"

    # --- Fallback ---
    else:
        response = "I'm not sure about that yet, but I'll learn it as more data is added."

    return response

# --- Chatbot logic ---
def chat_with_school_bot(query):
    data = load_school_data()
    return analyze_query(query, data)

# --- Gradio interface ---
gr.Interface(
    fn=chat_with_school_bot,
    inputs=gr.Textbox(label="Ask Daruk OLOOM something"),
    outputs=gr.Textbox(label="OLOOM's Response", lines=5), # Added lines=5 here
    title="🏫 Daruk OLOOM Intelligent School Assistant",
    description="Ask anything about the school — fees, teachers, schedule, admissions, or contact details."
).launch()