import pytest
from src.virtualpet.pet import VirtualPet
from unittest.mock import patch
import io
import sys

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

def test_take_shower():
    """Test the take_shower() functionality"""
    pet = VirtualPet("TestPet")
    pet.cleanness = 2

    # Take a shower to reset cleanness
    pet.take_shower()
    assert pet.cleanness == 10, "Cleanness should be reset to 10 after a shower"
    assert pet.dirty_command_count == 0, "Dirty command count should be reset to 0 after a shower"

def test_restart():
    """Test the restart() functionality"""
    pet = VirtualPet("TestPet")

    # Assign non-default values
    pet.happiness = 1
    pet.cleanness = 6
    pet.is_sleeping = True
    pet.dirty_command_count = 3

    # Reset everything
    pet.restart()

    assert pet.happiness == 10, "Happiness should be reset to 10 after restart"
    assert pet.cleanness == 10, "Cleanness should be reset to 10 after restart"
    assert not pet.is_sleeping, "Pet should not be sleeping after restart"
    assert pet.dirty_command_count == 0, "Dirty command count should be reset to 0 after restart"
    assert pet.active == True, "Pet should be active after restart"

def test_pet_sleep():
    """Test pet_sleep() functionality to simulate pet sleeping and waking up."""
    pet = VirtualPet("TestPet")

    # Setup to capture print statements
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput

    # Mock sleep to prevent actual sleep delay
    with patch('time.sleep', return_value=None) as mock_sleep:
        pet.pet_sleep()
        
    # Reset redirect
    sys.stdout = sys.__stdout__             

    # Check outputs
    assert "is going to sleep..." in capturedOutput.getvalue(), "Should indicate going to sleep"
    assert "woke up after" in capturedOutput.getvalue(), "Should indicate waking up"

    # Check that time.sleep was called
    mock_sleep.assert_called()