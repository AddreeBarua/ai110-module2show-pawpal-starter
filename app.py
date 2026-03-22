import streamlit as st
from datetime import datetime, timedelta
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")

# Initialize Owner in session_state
if "owner" not in st.session_state:
    owner_name = st.text_input("Owner name", value="Jordan")
    contact = st.text_input("Owner contact", value="jordan@email.com")
    if owner_name and contact:
        st.session_state.owner = Owner(owner_name, contact)

# Get or create owner from session_state
if "owner" in st.session_state:
    owner = st.session_state.owner
    st.write(f"**Owner:** {owner.name} ({owner.contact})")
    
    pet_name = st.text_input("Pet name", value="Mochi")
    species = st.selectbox("Species", ["dog", "cat", "other"])
    
    st.markdown("### Tasks")
    st.caption("Add tasks. They will be added to the selected pet and stored in the schedule.")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        task_title = st.text_input("Task title", value="Morning walk")
    with col2:
        duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
    with col3:
        priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)
    with col4:
        frequency = st.selectbox("Frequency", ["daily", "weekly", "once"], index=0)
    
    # Get or create pet
    pet_exists = any(p.name == pet_name for p in owner.pets)
    if not pet_exists:
        new_pet = Pet(pet_name, species, 1)
        owner.add_pet(new_pet)
    
    current_pet = next((p for p in owner.pets if p.name == pet_name), None)
    
    if st.button("Add task"):
        if current_pet and task_title:
            # Create task with current time + offset for demo
            task_time = datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)
            task_time = task_time + timedelta(minutes=len(current_pet.get_tasks()) * 30)
            
            task = Task(
                name=task_title,
                description=f"{task_title} for {pet_name}",
                scheduled_time=task_time,
                duration=int(duration),
                priority=priority,
                frequency=frequency,
                pet_name=pet_name
            )
            current_pet.add_task(task)
            st.success(f"Task '{task_title}' added to {pet_name}!")
    
    if current_pet and current_pet.get_tasks():
        st.write(f"**Tasks for {pet_name}:**")
        task_data = [
            {
                "Time": t.scheduled_time.strftime("%H:%M"),
                "Task": t.name,
                "Duration": f"{t.duration} min",
                "Priority": t.priority,
                "Frequency": t.frequency,
                "Status": "✓ Done" if t.is_complete else "○ Pending"
            }
            for t in current_pet.get_tasks()
        ]
        st.table(task_data)
    else:
        st.info("No tasks yet. Add one above.")
    
    st.divider()
    
    st.subheader("Build Schedule")
    st.caption("Generate a sorted schedule and check for conflicts.")
    
    if st.button("Generate schedule"):
        scheduler = Scheduler(owner)
        
        # Check for conflicts
        conflicts = scheduler.detect_conflicts()
        if conflicts:
            st.warning(
                f"⚠️ **{len(conflicts)} schedule conflict(s) detected!**\n\n"
                + "\n".join([f"- {c[0].name} and {c[1].name} at {c[0].scheduled_time.strftime('%H:%M')}" for c in conflicts])
            )
        
        # Display sorted schedule
        sorted_tasks = scheduler.sort_by_time()
        if sorted_tasks:
            st.success("✓ Schedule generated successfully!")
            schedule_data = [
                {
                    "Time": t.scheduled_time.strftime("%H:%M"),
                    "Task": t.name,
                    "Pet": t.pet_name,
                    "Duration": f"{t.duration} min",
                    "Priority": t.priority,
                    "Status": "✓ Done" if t.is_complete else "○ Pending"
                }
                for t in sorted_tasks
            ]
            st.table(schedule_data)
        else:
            st.info("No tasks to schedule. Add tasks above first.")
else:
    st.info("Enter owner information to get started.")
