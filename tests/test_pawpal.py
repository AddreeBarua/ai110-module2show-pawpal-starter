import pytest
from datetime import datetime
from pawpal_system import Task, Pet


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
