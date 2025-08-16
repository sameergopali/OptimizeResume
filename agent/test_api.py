#!/usr/bin/env python3
"""
Test script to demonstrate sending POST requests to the FastAPI server
"""

import requests
import json

# Server URL
BASE_URL = "http://localhost:8000"

def test_root_endpoint():
    """Test the root endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"Root endpoint response: {response.status_code}")
        print(f"Response: {response.json()}")
        print("-" * 50)
    except requests.exceptions.ConnectionError:
        print("❌ Server is not running. Please start the server first with: python main.py")
        return False
    return True

def test_post_message(content="Hello, FastAPI!", sender="test_user"):
    """Test sending a POST message"""
    try:
        message_data = {
            "content": content,
            "sender": sender
        }
        
        response = requests.post(
            f"{BASE_URL}/message",
            json=message_data,
            headers={"Content-Type": "application/json"}
        )
        
        print(f"POST message response: {response.status_code}")
        print(f"Response: {response.json()}")
        print("-" * 50)
        return True
    except requests.exceptions.ConnectionError:
        print("❌ Server is not running. Please start the server first with: python main.py")
        return False

def test_get_messages():
    """Test getting all messages"""
    try:
        response = requests.get(f"{BASE_URL}/messages")
        print(f"GET messages response: {response.status_code}")
        print(f"Response: {response.json()}")
        print("-" * 50)
        return True
    except requests.exceptions.ConnectionError:
        print("❌ Server is not running. Please start the server first with: python main.py")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing FastAPI Message Receiver")
    print("=" * 50)
    
    # Test root endpoint
    if not test_root_endpoint():
        return
    
    # Test posting messages
    test_post_message("First test message", "user1")
    test_post_message("Another message", "user2")
    test_post_message("Hello from Python!", "test_script")
    
    # Test getting all messages
    test_get_messages()
    
    print("✅ All tests completed!")

if __name__ == "__main__":
    main()
