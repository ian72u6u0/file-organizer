from pathlib import Path
import shutil
import time

archives_dir = Path.home() / "Desktop" / "Archive"
images_dir = Path.home() / "Desktop" / "Images"
documents_dir = Path.home() / "Desktop" / "Documents"
downloads_dir = Path.home() / "Downloads"

Rules = {
    "Image": [".png",".jpg",".jpeg",".gif",".svg",".webp",".tiff",".tif",".psd"],
    "Documents": [".pdf", ".txt", ".rtf", ".odt", ".md",".doc", ".docx", ".docm", ".dotx",".xls", ".xlsx", ".xlsm", ".csv", ".ods"],
    "Archives": [".zip", ".tar", ".gz"]
}

folder_map = {
    "Image": images_dir,
    "Documents": documents_dir,
    "Archives": archives_dir
}

for folder in folder_map.values():
    folder.mkdir(exist_ok=True, parents=True)

for file_path in list(downloads_dir.rglob("*")):
    if file_path.is_file():
        file_extension = file_path.suffix.lower()
        
        for category, extensions in Rules.items():
            if file_extension in extensions:
                dest_dir = folder_map[category]
                
                if dest_dir in file_path.parents:
                    break
                    
                try:
                    # Stability Check: Wait until file stops changing size
                    initial_size = file_path.stat().st_size
                    time.sleep(2)
                    current_size = file_path.stat().st_size
                    
                    if initial_size != current_size:
                        print(f"Skipped (Still copying/downloading): {file_path.name}")
                        break
                        
                    shutil.move(str(file_path), str(dest_dir))
                    print(f"Moved to {category}: {file_path.name}")
                except Exception:
                    pass
                break
