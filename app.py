import streamlit as st
from datetime import datetime
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

# --- Persistent state ---
if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Jordan", phone_number="555-1234", email="jordan@example.com")

owner: Owner = st.session_state.owner

# ---------------------------------------------------------------------------
# Section 1 — Add a Pet
# ---------------------------------------------------------------------------
st.divider()
st.subheader("Add a Pet")

pet_name = st.text_input("Pet name", value="Mochi")
species   = st.selectbox("Species", ["dog", "cat", "other"])
breed     = st.text_input("Breed", value="Mixed")
age       = st.number_input("Age (years)", min_value=0, max_value=30, value=2)
gender    = st.selectbox("Gender", ["female", "male"])
weight    = st.number_input("Weight (lbs)", min_value=0.1, max_value=300.0, value=10.0)

if st.button("Add pet"):
    new_pet = Pet(
        name=pet_name,
        species=species,
        breed=breed,
        age=int(age),
        gender=gender,
        weight=float(weight),
    )
    owner.add_pet(new_pet)
    st.success(f"{new_pet.name} added!")

current_pets = owner.list_pets()
if current_pets:
    st.write(f"**{owner.name}'s pets:** " + ", ".join(p.name for p in current_pets))
else:
    st.info("No pets yet. Add one above.")

# ---------------------------------------------------------------------------
# Section 2 — Add a Task to a Pet
# ---------------------------------------------------------------------------
st.divider()
st.subheader("Add a Task")

if not current_pets:
    st.info("Add a pet first before scheduling tasks.")
else:
    pet_names   = [p.name for p in current_pets]
    target_name = st.selectbox("Assign to pet", pet_names)
    target_pet  = next(p for p in current_pets if p.name == target_name)

    col1, col2, col3 = st.columns(3)
    with col1:
        task_title = st.text_input("Task title", value="Morning walk")
    with col2:
        duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
    with col3:
        priority_label = st.selectbox("Priority", ["High", "Medium", "Low"])

    task_time = st.time_input("Due time (today)", value=datetime.now().replace(hour=8, minute=0).time())

    priority_map = {"High": 1, "Medium": 2, "Low": 3}

    if st.button("Add task"):
        due_dt = datetime.now().replace(
            hour=task_time.hour,
            minute=task_time.minute,
            second=0,
            microsecond=0,
        )
        new_task = Task(
            description=task_title,
            due_date_time=due_dt,
            pet_id=target_pet.id,
            duration_minutes=int(duration),
            priority=priority_map[priority_label],
        )
        target_pet.add_task(new_task)
        st.success(f"Task '{task_title}' added to {target_pet.name}.")

    if target_pet.list_tasks():
        st.write(f"**{target_pet.name}'s tasks:**")
        st.table([
            {
                "Task": t.description,
                "Time": t.due_date_time.strftime("%I:%M %p"),
                "Duration": f"{t.duration_minutes} min",
                "Priority": {1: "High", 2: "Medium", 3: "Low"}[t.priority],
                "Status": t.status.value,
            }
            for t in target_pet.list_tasks()
        ])

# ---------------------------------------------------------------------------
# Section 3 — Generate Schedule
# ---------------------------------------------------------------------------
st.divider()
st.subheader("Generate Today's Schedule")

if st.button("Generate schedule"):
    plan = Scheduler().generate_daily_plan(owner)
    if not plan:
        st.warning("No pending tasks scheduled for today. Add tasks above.")
    else:
        from datetime import timedelta
        priority_label_map = {1: "High", 2: "Medium", 3: "Low"}
        pet_lookup = {p.id: p.name for p in owner.list_pets()}
        rows = [
            {
                "Time": t.due_date_time.strftime("%I:%M %p"),
                "Ends": (t.due_date_time + timedelta(minutes=t.duration_minutes)).strftime("%I:%M %p"),
                "Pet": pet_lookup[t.pet_id],
                "Task": t.description,
                "Priority": priority_label_map[t.priority],
            }
            for t in plan
        ]
        st.success(f"{len(plan)} task(s) scheduled for today.")
        st.table(rows)
