#!/usr/bin/env python3
"""
Race Classification Web Application Startup Script
This script checks dependencies and starts the Flask application.
"""

import os
import sys
import subprocess
import platform

def check_python_version():
    """Check if Python version is 3.8 or higher"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        print(f"   Current version: {sys.version}")
        sys.exit(1)
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor} detected")

def check_model_file():
    """Check if the model file exists"""
    if not os.path.exists('clip_lvm_model.pt'):
        print("❌ ERROR: clip_lvm_model.pt not found")
        print(f"   Expected location: {os.path.abspath('clip_lvm_model.pt')}")
        sys.exit(1)
    print("✓ Model file found")

def check_dependencies():
    """Check if required packages are installed"""
    required_packages = [
        'flask',
        'torch',
        'clip',
        'PIL',
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            if package == 'PIL':
                import PIL
            else:
                __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("⚠️  Missing packages detected:")
        for pkg in missing_packages:
            print(f"   - {pkg}")
        
        print("\nInstalling dependencies...")
        result = subprocess.run(
            [sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'],
            capture_output=True
        )
        
        if result.returncode != 0:
            print("❌ Failed to install dependencies")
            print(result.stderr.decode())
            sys.exit(1)
        print("✓ Dependencies installed successfully")
    else:
        print("✓ All dependencies are installed")

def main():
    """Main function"""
    print("=" * 50)
    print("🎯 Race Classification Web Application")
    print("=" * 50)
    print()
    
    # Check Python version
    print("Checking Python version...")
    check_python_version()
    print()
    
    # Check model file
    print("Checking model file...")
    check_model_file()
    print()
    
    # Check dependencies
    print("Checking dependencies...")
    check_dependencies()
    print()
    
    # Create uploads directory if it doesn't exist
    os.makedirs('uploads', exist_ok=True)
    print("✓ Upload directory ready")
    print()
    
    # Start the Flask application
    print("=" * 50)
    print("Starting Flask application...")
    print("=" * 50)
    print()
    print("🌐 Open your browser and go to:")
    print("   http://localhost:5000")
    print()
    print("Press Ctrl+C to stop the server")
    print()
    
    try:
        # Import and run Flask app
        from app import app
        
        # Determine the port
        port = os.environ.get('FLASK_PORT', 5000)
        
        # Run the Flask app
        app.run(
            debug=True,
            host='0.0.0.0',
            port=int(port),
            use_reloader=True
        )
    
    except KeyboardInterrupt:
        print("\n\n✋ Server stopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()
