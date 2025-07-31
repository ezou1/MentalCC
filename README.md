# MentalCC 
**Mental Cruise Control** is a brain-computer interface (BCI) project that enables hands-free driving input using the Neurosity Crown headset. It listens for trained mental "push" kinesis signals and simulates keyboard input to control a throttle (e.g., `W` key for gas) in driving simulators or games like Roblox.

## Dependencies
- `neurosity`: Official Neurosity SDK for the Crown headset
- `python-dotenv`: Loading console login credentials from a `.env` file
- `pydirectinput`: A keystroke simulator similar to `pyautogui` or `keyboard` with DirectX support

---

## File Structure
- `main.py`: Entry point
- `eeg.py`: Neurosity Kinesis setup and authentication
- `config.py`: Loads credentials from `.env` file
- `controller.py`: Handles keystrokes and other inputs as needed
- `requirements.txt`: Lists dependencies for streamlined installation

---

## Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/mental-cc.git
cd mental-cc
```
### 2. Install dependencies
```
pip install -r requirements.txt
```
### 3. Create `.env` file and fill with credentials
```
DEVICE_ID=your_device_id
EMAIL=your@email.com
PASSWORD=your_password
```

---

## Training Kinesis
1. Complete [Neurosity Crown Quickstart](https://support.neurosity.co/en/collections/13268376-getting-started), then go to [console.neurosity.co](console.neurosity.co)
2. Select your Crown device
3. Go to Kinesis
4. Create and train a Kinesis action (e.g., "push")
5. Use that exact label in main.py

---

## To Run
```
python main.py
```
