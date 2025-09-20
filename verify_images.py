import os
from PIL import Image

# Set the root directory of your dataset
dataset_root = 'dataset/train'
num_bad_files = 0

print(f"🚀 Starting verification of images in: {dataset_root}")

# Recursively walk through all subdirectories and files
for subdir, _, files in os.walk(dataset_root):
    for file in files:
        file_path = os.path.join(subdir, file)
        try:
            # Attempt to open the image file
            with Image.open(file_path) as img:
                # The verify() method checks for file integrity
                img.verify()
        except (IOError, SyntaxError) as e:
            # This block will execute if the file is corrupted or not a valid image
            print(f"❌ Bad file detected: {file_path}")
            print(f"   Reason: {e}")
            num_bad_files += 1

            # --- DANGER ZONE: UNCOMMENT TO AUTOMATICALLY DELETE BAD FILES ---
            # Be careful with this. It's safer to review the list first.
            # os.remove(file_path)
            # print(f"   🗑️ File deleted.")
            # ----------------------------------------------------------------

if num_bad_files == 0:
    print("\n✅ Verification complete. No bad files found!")
else:
    print(f"\n⚠️ Verification complete. Found {num_bad_files} bad files.")
    print("   Please review the list above and delete them manually, or")
    print("   uncomment the 'os.remove()' line in the script to delete them automatically.")