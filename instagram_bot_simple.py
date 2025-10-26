"""
Instagram Close Friends Automation Script - Safer Version
Reads usernames from a CSV file and adds them to close friends list
"""

import csv
import time
import os
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

# ==== CONFIGURATION ====
CSV_FILE = "output.csv"          # CSV file with usernames
USERNAME_COLUMN = "username"     # Column name in CSV containing usernames
WAIT_TIME = 10                   # Seconds to wait for page elements
# =======================

def human_sleep(base=2.5, spread=4.0):
    """Randomized sleep to act more human-like"""
    delay = base + random.random() * spread
    print(f"⏳ Sleeping {delay:.2f}s...")
    time.sleep(delay)

def maybe_cooldown(i, low=8, high=12):
    """Cooldown every few actions"""
    if i % random.randint(low, high) == 0:
        pause = random.uniform(30, 90)
        print(f"⏸️ Cooldown for {pause:.1f}s to look human…")
        time.sleep(pause)

class InstagramCloseFriendsBot:
    def __init__(self):
        self.driver = None
        self.wait = None
        
    def setup_browser(self):
        """Setup Brave browser - simplified version"""
        print("🚀 Starting Brave browser...")
        
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--no-first-run")
        chrome_options.add_argument("--no-default-browser-check")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        # Find Brave executable
        brave_paths = [
            r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
            r"C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe",
            r"C:\Users\{}\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe".format(os.getenv('USERNAME')),
        ]
        
        brave_path = None
        for path in brave_paths:
            if os.path.exists(path):
                brave_path = path
                break
                
        if brave_path:
            chrome_options.binary_location = brave_path
            print(f"✅ Found Brave at: {brave_path}")
        else:
            print("⚠️ Brave not found, using Chrome...")
        
        try:
            # Get correct ChromeDriver
            print("📥 Getting ChromeDriver...")
            driver_path = ChromeDriverManager().install()
            if driver_path.endswith('THIRD_PARTY_NOTICES.chromedriver'):
                driver_path = driver_path.replace('THIRD_PARTY_NOTICES.chromedriver', 'chromedriver.exe')
            
            service = Service(driver_path)
            print("🌐 Starting browser...")
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            self.wait = WebDriverWait(self.driver, WAIT_TIME)
            
            # Remove automation indicators
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            
            print("✅ Browser started successfully!")
            return True
            
        except Exception as e:
            print(f"❌ Failed to start browser: {str(e)}")
            return False
        
    def login_instagram(self):
        """Navigate to Instagram and wait for manual login"""
        print("🌐 Opening Instagram...")
        self.driver.get("https://www.instagram.com")
        
        print("\n" + "="*50)
        print("📱 PLEASE LOG IN TO INSTAGRAM MANUALLY")
        print("After logging in, press ENTER to continue...")
        print("="*50)
        input()
        
    def navigate_to_close_friends(self):
        """Navigate to close friends page"""
        print("📍 Navigating to close friends page...")
        self.driver.get("https://www.instagram.com/accounts/close_friends/")
        
        try:
            self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            human_sleep(3, 1)
            print("✅ Close friends page loaded")
        except TimeoutException:
            print("❌ Failed to load close friends page")
            return False
        return True
        
    def search_and_add_user(self, username):
        """Search for a user and add them to close friends"""
        print(f"🔍 Processing {username}...")
        
        try:
            # Look for search input field
            candidates = [
                (By.CSS_SELECTOR, "input[placeholder*='Search']"),
                (By.CSS_SELECTOR, "input[aria-label*='Search']"),
                (By.TAG_NAME, "input")
            ]
            search_input = None
            for how, sel in candidates:
                try:
                    search_input = self.wait.until(EC.presence_of_element_located((how, sel)))
                    if search_input.is_displayed():
                        break
                except TimeoutException:
                    continue
                    
            if not search_input:
                print("❌ Could not find search input")
                return False
                
            search_input.clear()
            search_input.send_keys(username)
            human_sleep(2.5, 3.5)
            
            # Look for user rows
            user_rows = self.driver.find_elements(By.CSS_SELECTOR, "div[role='button'], div[style*='cursor: pointer']")
            target = None
            for row in user_rows:
                try:
                    text_bits = [el.text.strip().lower() for el in row.find_elements(By.TAG_NAME, "span")]
                    if username.lower() in text_bits:
                        target = row
                        break
                except Exception:
                    continue
            
            if not target:
                print(f"❌ User {username} not found")
                return False
            
            target.click()
            human_sleep(0.8, 1.4)
            print(f"✅ Added {username}")
            return True
            
        except Exception as e:
            print(f"❌ Error with {username}: {str(e)}")
            human_sleep(8, 12)
            return False
            
    def read_csv_file(self):
        """Read usernames from CSV file, deduplicated"""
        if not os.path.exists(CSV_FILE):
            print(f"❌ CSV file '{CSV_FILE}' not found!")
            return []
            
        usernames = []
        seen = set()
        try:
            with open(CSV_FILE, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if USERNAME_COLUMN in row:
                        u = row[USERNAME_COLUMN].strip()
                        if u and u.lower() not in seen:
                            seen.add(u.lower())
                            usernames.append(u)
            print(f"📁 Found {len(usernames)} unique usernames in CSV")
            return usernames
        except Exception as e:
            print(f"❌ Error reading CSV: {str(e)}")
            return []
            
    def run(self):
        """Main execution function"""
        try:
            usernames = self.read_csv_file()
            if not usernames:
                return
                
            if not self.setup_browser():
                return
            
            self.login_instagram()
            
            if not self.navigate_to_close_friends():
                return
                
            successful = 0
            failed = 0
            print(f"\n🚀 Starting to process {len(usernames)} users...")
            
            for i, username in enumerate(usernames, 1):
                print(f"\n[{i}/{len(usernames)}] {username}")
                if self.search_and_add_user(username):
                    successful += 1
                else:
                    failed += 1
                human_sleep()
                maybe_cooldown(i)
                
            print(f"\n{'='*50}")
            print(f"🎉 SUMMARY:")
            print(f"✅ Successfully added: {successful}")
            print(f"❌ Failed to add: {failed}")
            print(f"📊 Total processed: {len(usernames)}")
            print(f"{'='*50}")
            
        except KeyboardInterrupt:
            print("\n⚠️ Stopped by user")
        except Exception as e:
            print(f"❌ Error: {str(e)}")
        finally:
            print("\n🌐 Browser will stay open for review")

if __name__ == "__main__":
    print("Instagram Close Friends Bot - Safer")
    print("="*40)
    bot = InstagramCloseFriendsBot()
    bot.run()
