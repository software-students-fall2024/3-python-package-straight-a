import pytest
from src.virtualpet.pet import VirtualPet

def test_feed_pet():
    """Test feed_pet() functionality comprehensively"""
    pet = VirtualPet("TestPet")
    
    # Test initial state
    assert pet.happiness == 10, "Initial happiness should be 10"
    assert pet.cleanness == 10, "Initial cleanness should be 10"
    
    # Test feeding multiple times and check values
    pet.feed_pet()
    assert pet.happiness == 10, "Happiness should stay at 10 (max)"
    assert pet.cleanness == 8, "Cleanness should decrease by 2"
    
    # Test feeding until pet gets dirty
    for _ in range(3):  # Feed 3 more times
        pet.feed_pet()
    
    assert pet.cleanness == 2, "Cleanness should be 2 after 4 feedings"
    assert pet.dirty_command_count == 1, "Should have 1 dirty command"
    
    # Test feeding with minimum cleanness
    pet.feed_pet()
    assert pet.cleanness == 1, "Cleanness shouldn't go below 1"
    assert pet.dirty_command_count == 2, "Should have 2 dirty commands"

def test_feed_sleeping_pet():
    """Test feeding a sleeping pet"""
    pet = VirtualPet("TestPet")
    pet.is_sleeping = True
    
    initial_happiness = pet.happiness
    initial_cleanness = pet.cleanness
    
    pet.feed_pet()
    
    assert pet.happiness == initial_happiness, "Sleeping pet's happiness shouldn't change"
    assert pet.cleanness == initial_cleanness, "Sleeping pet's cleanness shouldn't change"

def test_exit():
    """Test basic exit functionality"""
    pet = VirtualPet("TestPet")
    pet.exit()
    assert pet.active == False, "Pet should not be active after exit"
