import os
import plyvel
import json

# Path to Chrome's LevelDB directory on Linux Ubuntu
leveldb_path = os.path.expanduser("~/.config/google-chrome/Default/Local Storage")

def fetch_chrome_storage():
    db = plyvel.DB(os.path.join(leveldb_path, "leveldb"), create_if_missing=False)
    results = []

    for key, value in db:
        if key.startswith(b'chrome-extension://'):
            try:
                data = json.loads(value.decode('utf-8'))
                results.append((key.decode('utf-8'), data))
            except ValueError:
                pass
    
    db.close()
    return results

if __name__ == "__main__":
    stored_data = fetch_chrome_storage()
    if stored_data:
        print("Stored Chrome Extension Data:")
        for url, data in stored_data:
            print(f"Extension URL: {url}")
            print(f"Data: {data}\n")
    else:
        print("No Chrome extension data found.")
