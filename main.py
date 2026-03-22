from datetime import datetime
from pawpal_system import Task, Pet, Owner, Scheduler

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
print("=" * 60)
print(f"Today's Schedule for {owner.name}")
print(f"Contact: {owner.contact}")
print("=" * 60)
print()

sorted_tasks = scheduler.sort_by_time()

for task in sorted_tasks:
    time_str = task.scheduled_time.strftime("%H:%M")
    status = "✓ Done" if task.is_complete else "○ Pending"
    print(f"{time_str} | {task.name:20} | {task.pet_name:10} | {task.priority:8} | {task.duration} min | {status}")

print()
print("=" * 60)
