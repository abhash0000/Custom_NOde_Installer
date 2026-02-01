# 🚀 ComfyUI Node Manager (Pro Suite)

A high-performance, terminal-based management tool for ComfyUI. This utility automates the process of cloning, updating, and managing dependencies for over 40+ of the most powerful custom nodes in the ecosystem.

<img width="822" height="683" alt="Screenshot 2026-02-01 220044" src="https://github.com/user-attachments/assets/5438d8a4-dc48-432a-ba80-80348572d3a5" />

## ✨ Features

* **One-Click Batch Updates:** Update all 40+ nodes and their Python dependencies simultaneously with a single command.
* **Venv Integration:** Automatically detects and activates your ComfyUI virtual environment (`venv` or `.venv`) to ensure no system-wide library conflicts.
* **Dual-Column Interface:** A sleek, Linux-style terminal UI with optimized space for 2026's most essential nodes.
* **Automated Dependency Resolution:** Physically enters (`cd`) each node directory to run `pip install -r requirements.txt`, ensuring complex nodes install correctly.
* **Custom Repo Support:** Easily install any GitHub repository by pasting the URL directly into the manager.

## 🛠️ Installation

1.  **Placement:** Move `Node_manager.bat` and `manager.py` into your **root ComfyUI directory** (the folder containing your `venv` and the `ComfyUI` source folder).
2.  **Git:** Ensure you have [Git](https://git-scm.com/) installed on your Windows machine.
3.  **Run:** Double-click `Node_manager.bat`.

## 📂 Project Structure

Your directory should look like this for the manager to function correctly:

```text
ComfyUI_Project/
├── venv/                 # Your Virtual Environment
├── ComfyUI/              # Core ComfyUI Folder
│   └── custom_nodes/     # Target folder for installs
├── Node_manager.bat      # The Launcher
└── manager.py            # The Logic Engine
