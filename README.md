# Instagram Close Friends Automation Script

A Python automation script that helps you add multiple users to your Instagram Close Friends list from a CSV file. This script uses Selenium WebDriver with Brave browser to automate the process while implementing human-like behavior patterns.

## ⚠️ Disclaimer

This script is for educational purposes only. Use it responsibly and in accordance with Instagram's Terms of Service. Automated actions may violate Instagram's policies and could result in account restrictions. Use at your own risk.

## Features

- 🤖 Automated Close Friends list management
- 📊 Bulk add users from CSV file
- 🎭 Human-like behavior simulation (randomized delays, cooldowns)
- 🦁 Brave browser support (falls back to Chrome)
- 🔒 Manual login for security
- 📈 Progress tracking and summary statistics
- ✅ Duplicate username prevention
- 🔄 JSON to CSV converter utility (for Instagram data exports)

## Prerequisites

- Python 3.7 or higher
- Brave Browser or Google Chrome installed
- An Instagram account
- CSV file with usernames to add

## Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/instagram-close-friends-automation.git
cd instagram-close-friends-automation
```

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

## Setup

### Option 1: Using Instagram Data Export

If you have an Instagram data export with a `followers_1.json` file:

1. Place your `followers_1.json` file in the same directory as the scripts

2. Run the JSON to CSV converter:

```bash
python jsoncsv.py
```

3. This will create `output.csv` with all usernames from your JSON file

### Option 2: Manual CSV Creation

1. Prepare your CSV file (`output.csv`) with the following format:

```csv
username
user1
user2
user3
```

2. Make sure the CSV file is in the same directory as the script.

## Usage

1. Run the script:

```bash
python instagram_bot_simple.py
```

2. The browser will open automatically

3. **Manually log in to Instagram** when prompted

4. Press ENTER in the terminal after logging in

5. The script will automatically:
   - Navigate to the Close Friends page
   - Search for each username from the CSV
   - Add them to your Close Friends list
   - Display progress and summary

## Configuration

You can customize the following settings in `instagram_bot_simple.py`:

```python
CSV_FILE = "output.csv"          # Path to your CSV file
USERNAME_COLUMN = "username"     # Column name containing usernames
WAIT_TIME = 10                   # Seconds to wait for page elements
```

### Human-like Behavior

The script includes several features to mimic human behavior:

- **Randomized delays**: 2.5-6.5 seconds between actions
- **Cooldown periods**: 30-90 second breaks every 8-12 actions
- **Anti-detection measures**: Removes automation indicators

## File Structure

```
.
├── instagram_bot_simple.py    # Main automation script
├── jsoncsv.py                 # Utility to convert Instagram JSON export to CSV
├── output.csv                 # Input file with usernames (generated or manual)
├── example.csv                # Example CSV format
├── requirements.txt           # Python dependencies
├── LICENSE                    # MIT License
└── README.md                  # This file
```

## Troubleshooting

### Browser not found

- Make sure Brave Browser is installed in the default location
- The script will automatically fall back to Chrome if Brave is not found

### Search input not found

- Instagram's UI may have changed
- Try waiting a few seconds and running again
- Check if you're still logged in

### Users not being added

- Verify the usernames are correct in your CSV
- Check if the users exist on Instagram
- Ensure you have permission to add them to Close Friends

### JSON file format issues

- Make sure your `followers_1.json` is from an official Instagram data export
- The file should contain a list of objects with `string_list_data` fields
- If the conversion fails, check the JSON structure matches Instagram's export format

## Safety Features

- ✅ Manual login (no password storage)
- ✅ Browser stays open for review
- ✅ Randomized timing to avoid detection
- ✅ Error handling and recovery
- ✅ Progress tracking

## Dependencies

- `selenium` - Web browser automation
- `webdriver-manager` - Automatic ChromeDriver management

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Remember**: Always use automation tools responsibly and in compliance with platform policies.
