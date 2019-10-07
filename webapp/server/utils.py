def allowed_file(filename,allowed_extensions):
    """Function to determine if file is in the extensions allowed by the pgm.

    Args:
        filename (str) -- the name of the file
        allowed_extensions (list) -- list of allowed extensions
    """
    return '.' in filename and filename.rsplit('.', 1)[1] in allowed_extensions
