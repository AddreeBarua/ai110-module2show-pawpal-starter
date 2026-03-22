from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class Task:
    """A task for pet care."""
    name: str
    description: str
    scheduled_time: datetime
    duration: int
    priority: str
    frequency: str
    pet_name: str = ""
    is_complete: bool = False

    def mark_complete(self):
        """Mark the task as complete."""
        self.is_complete = True

    def reschedule(self, new_time: datetime):
        """Reschedule the task to a new time."""
        self.scheduled_time = new_time


@dataclass
class Pet:
    """A pet that requires care tasks."""
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to the pet's task list."""
        self.tasks.append(task)

    def remove_task(self, task: Task):
        """Remove a task from the pet's task list."""
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks(self):
        """Get all tasks for this pet."""
        return self.tasks


class Owner:
    """An owner who manages multiple pets."""

    def __init__(self, name: str, contact: str):
        """Initialize an owner with a name and contact information."""
        self.name = name
        self.contact = contact
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        """Add a pet to the owner's list of pets."""
        self.pets.append(pet)

    def remove_pet(self, pet: Pet):
        """Remove a pet from the owner's list of pets."""
        if pet in self.pets:
            self.pets.remove(pet)

    def get_all_tasks(self):
        """Get all tasks for all pets owned by this owner."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


class Scheduler:
    """Manages and schedules tasks for an owner's pets."""

    def __init__(self, owner: Owner):
        """Initialize the scheduler with an owner object."""
        self.owner = owner

    def get_all_tasks(self):
        """Get all tasks for the owner's pets."""
        return self.owner.get_all_tasks()

    def sort_by_time(self):
        """Sort all tasks by their scheduled time with stable secondary sorting."""
        return sorted(
            self.get_all_tasks(), 
            key=lambda t: (t.scheduled_time, t.pet_name, t.name)
        )

    def filter_tasks(self, pet_name=None, status=None, priority=None):
        """Filter tasks by pet name, completion status, and/or priority."""
        all_tasks = self.get_all_tasks()
        filtered = all_tasks
        if pet_name:
            filtered = [t for t in filtered if t.pet_name == pet_name]
        if status is not None:
            filtered = [t for t in filtered if t.is_complete == status]
        if priority:
            filtered = [t for t in filtered if t.priority == priority]
        return filtered

    def detect_conflicts(self):
        """Detect conflicting task schedules and return readable warning messages."""
        all_tasks = self.get_all_tasks()
        conflicts = []
        for i in range(len(all_tasks)):
            for j in range(i + 1, len(all_tasks)):
                if all_tasks[i].scheduled_time == all_tasks[j].scheduled_time:
                    conflict_msg = (
                        f"'{all_tasks[i].name}' ({all_tasks[i].pet_name}) "
                        f"conflicts with '{all_tasks[j].name}' ({all_tasks[j].pet_name}) "
                        f"at {all_tasks[i].scheduled_time.strftime('%H:%M')}"
                    )
                    conflicts.append(conflict_msg)
        return conflicts

    def handle_recurring_tasks(self):
        """Handle recurring tasks by creating new Task instances for next occurrence."""
        from datetime import timedelta
        all_tasks = self.get_all_tasks()
        for task in all_tasks:
            if task.is_complete and task.frequency:
                pet = next((p for p in self.owner.pets if p.name == task.pet_name), None)
                if pet:
                    if task.frequency.lower() == 'daily':
                        next_time = task.scheduled_time + timedelta(days=1)
                        new_task = Task(
                            name=task.name,
                            description=task.description,
                            scheduled_time=next_time,
                            duration=task.duration,
                            priority=task.priority,
                            frequency=task.frequency,
                            pet_name=task.pet_name,
                            is_complete=False
                        )
                        pet.add_task(new_task)
                    elif task.frequency.lower() == 'weekly':
                        next_time = task.scheduled_time + timedelta(weeks=1)
                        new_task = Task(
                            name=task.name,
                            description=task.description,
                            scheduled_time=next_time,
                            duration=task.duration,
                            priority=task.priority,
                            frequency=task.frequency,
                            pet_name=task.pet_name,
                            is_complete=False
                        )
                        pet.add_task(new_task)
