import cloudinary
import cloudinary.uploader
import os
from dotenv import load_dotenv

load_dotenv()

# Configure Cloudinary
cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME'),
    api_key=os.environ.get('CLOUDINARY_API_KEY'),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET')
)

# Test upload
try:
    result = cloudinary.uploader.upload("media/RecipeImages/img2.jpg")
    print("Connection successful!")
    print(f"Image uploaded: {result['url']}")
except Exception as e:
    print(f"Connection failed: {e}")