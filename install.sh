
#!/bin/bash
echo "🔧 Installing AllSiteX Monitor Pro..."
pkg update -y
pkg install python -y
mkdir -p logs
touch logs/db.json
echo "✅ Installation complete. Run: python main.py"
