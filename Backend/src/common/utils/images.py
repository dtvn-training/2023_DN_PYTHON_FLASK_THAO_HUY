import photos
from src.common.constants.media import IMAGE_ALLOWED_EXTENSIONS


def save_preview(_image):
    try:
        filename = photos.save(_image)
        file_url = photos.url(filename)
        return file_url
    except:
        return None


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in IMAGE_ALLOWED_EXTENSIONS

