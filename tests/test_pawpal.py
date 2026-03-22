import pytest
from datetime import datetime, timedelta
from pawpal_system import Task, Pet, Owner, Scheduler


def test_task_completion():
    """Verify that mark_complete() changes is_complete from False to True."""
    task = Task(
        name="Feed Pet",
        description="Give pet food",
        scheduled_time=datetime(2026, 3, 21, 8, 0),
        duration=10,
        priority="high",
        frequency="daily",
        pet_name="Test Pet"
    )
    assert task.is_complete == False
    task.mark_complete()
    assert task.is_complete == True


def test_task_addition():
    """Verify that add_task() increases the pet's task count by 1."""
    pet = Pet(name="Fluffy", species="cat", age=2)
    assert len(pet.get_tasks()) == 0
    
    task = Task(
        name="Play with Fluffy",
        description="Interactive play session",
        scheduled_time=datetime(2026, 3, 21, 9, 0),
        duration=15,
        priority="medium",
        frequency="daily",
        pet_name="Fluffy"
    )
    pet.add_task(task)
    assert len(pet.get_tasks()) == 1


def test_sorting_correctness():
    """Verify that sort_by_time() returns tasks in chronological order."""
    owner = Owner("Alex", "alex@email.com")
    pet = Pet(name="Buddy", species="dog", age=3)
    owner.add_pet(pet)
    
    # Create tasks out of order
    task1 = Task(
        name="Evening Walk",
        description="Late walk",
        scheduled_time=datetime(2026, 3, 21, 18, 0),
        duration=30,
        priority="medium",
        frequency="daily",
        pet_name="Buddy"
    )
    task2 = Task(
        name="Morning Feed",
        description="Breakfast",
        scheduled_time=datetime(2026, 3, 21, 8, 0),
        duration=10,
        priority="high",
        frequency="daily",
        pet_name="Buddy"
    )
    task3 = Task(
        name="Afternoon Play",
        description="Playtime",
        scheduled_time=datetime(2026, 3, 21, 14, 0),
        duration=20,
        priority="medium",
        frequency="daily",
        pet_name="Buddy"
    )
    
    pet.add_task(task1)
    pet.add_task(task2)
    pet.add_task(task3)
    
    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_by_time()
    
    assert sorted_tasks[0].name == "Morning Feed"
    assert sorted_tasks[1].name == "Afternoon Play"
    assert sorted_tasks[2].name == "Evening Walk"


def test_recurrence_logic():
    """Verify that handle_recurring_tasks() creates new tasks for next occurrence."""
    owner = Owner("Sam", "sam@email.com")
    pet = Pet(name="Max", species="cat", age=4)
    owner.add_pet(pet)
    
    task = Task(
        name="Feed Max",
        description="Daily feeding",
        scheduled_time=datetime(2026, 3, 21, 8, 0),
        duration=10,
        priority="high",
        frequency="daily",
        pet_name="Max"
    )
    pet.add_task(task)
    
    initial_count = len(pet.get_tasks())
    assert initial_count == 1
    
    task.mark_complete()
    scheduler = Scheduler(owner)
    scheduler.handle_recurring_tasks()
    
    final_count = len(pet.get_tasks())
    assert final_count == 2
    
    new_task = pet.get_tasks()[1]
    assert new_task.name == "Feed Max"
    assert new_task.is_complete == False
    assert new_task.scheduled_time == datetime(2026, 3, 22, 8, 0)


def test_conflict_detection():
    """Verify that detect_conflicts() returns conflict messages for simultaneous tasks."""
    owner = Owner("Jordan", "jordan@email.com")
    pet = Pet(name="Bella", species="cat", age=2)
    owner.add_pet(pet)
    
    # Create two tasks at the exact same time
    task1 = Task(
        name="Feed Bella",
        description="Cat food",
        scheduled_time=datetime(2026, 3, 21, 8, 0),
        duration=10,
        priority="high",
        frequency="daily",
        pet_name="Bella"
    )
    task2 = Task(
        name="Play with Bella",
        description="Interactive play",
        scheduled_time=datetime(2026, 3, 21, 8, 0),
        duration=15,
        priority="medium",
        frequency="daily",
        pet_name="Bella"
    )
    
    pet.add_task(task1)
    pet.add_task(task2)
    
    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts()
    
    # Verify at least one conflict is detected
    assert len(conflicts) >= 1
    assert isinstance(conflicts[0], str)
    assert "Feed Bella" in conflicts[0]
    assert "Play with Bella" in conflicts[0]
    assert "08:00" in conflicts[0]
