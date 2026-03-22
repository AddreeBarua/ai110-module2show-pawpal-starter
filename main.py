from datetime import datetime
from pawpal_system import Task, Pet, Owner, Scheduler
from tabulate import tabulate


def get_task_emoji(task_name: str) -> str:
    """Return emoji based on task type."""
    task_lower = task_name.lower()
    if "walk" in task_lower:
        return "🚶"
    elif "feed" in task_lower:
        return "🍽️"
    elif "medicin" in task_lower or "medication" in task_lower:
        return "💊"
    elif "groom" in task_lower:
        return "✂️"
    elif "play" in task_lower:
        return "🎾"
    else:
        return "📋"


def get_status_emoji(is_complete: bool) -> str:
    """Return emoji based on task completion status."""
    return "✅ Complete" if is_complete else "⏳ Pending"

# Create an owner
owner = Owner("Jordan", "jordan@email.com")

# Create pets
mochi = Pet("Mochi", "cat", 3)
rex = Pet("Rex", "dog", 5)

# Create tasks for Mochi
feed_mochi = Task(
    name="Feed Mochi",
    description="Give Mochi breakfast",
    scheduled_time=datetime(2026, 3, 21, 8, 0),
    duration=10,
    priority="high",
    frequency="daily",
    pet_name="Mochi"
)

groom_mochi = Task(
    name="Groom Mochi",
    description="Brush and groom Mochi",
    scheduled_time=datetime(2026, 3, 21, 10, 0),
    duration=20,
    priority="medium",
    frequency="weekly",
    pet_name="Mochi"
)

# Create tasks for Rex
walk_rex = Task(
    name="Walk Rex",
    description="Take Rex for a morning walk",
    scheduled_time=datetime(2026, 3, 21, 7, 0),
    duration=30,
    priority="high",
    frequency="daily",
    pet_name="Rex"
)

# Add tasks to pets
mochi.add_task(feed_mochi)
mochi.add_task(groom_mochi)
rex.add_task(walk_rex)

# Add pets to owner
owner.add_pet(mochi)
owner.add_pet(rex)

# Create scheduler
scheduler = Scheduler(owner)

# Print today's schedule sorted by time
print("=" * 80)
print(f"🐾 Today's Schedule for {owner.name}")
print(f"📧 Contact: {owner.contact}")
print("=" * 80)
print()

sorted_tasks = scheduler.sort_by_time()

# Build table data with emojis and formatted status
table_data = []
for task in sorted_tasks:
    time_str = task.scheduled_time.strftime("%H:%M")
    task_emoji = get_task_emoji(task.name)
    status_emoji = get_status_emoji(task.is_complete)
    
    table_data.append([
        time_str,
        f"{task_emoji} {task.name}",
        task.pet_name,
        task.priority.upper(),
        f"{task.duration} min",
        status_emoji
    ])

# Print formatted table
headers = ["Time", "Task", "Pet", "Priority", "Duration", "Status"]
print(tabulate(table_data, headers=headers, tablefmt="grid", stralign="left"))

print()
print("=" * 80)
