import hashlib
import json
import os
import platform
from typing import Any, List, Optional
from datetime import datetime

def read_json(filepath: str) -> List:
    with open(filepath) as data_file:
        data = json.load(data_file)
    return data


def write_json(filepath: str, data: Any) -> Any:
    kwargs = {'indent':4, 'sort_keys':True, 'separators': (",",": "), 'ensure_ascii': False}
    with open(filepath, "w", encoding="utf8") as outfile:
        str_ = json.dumps(data, **kwargs)
        outfile.write(str_)
    return data


def get_creation_datetime(filepath: str) -> Optional[datetime]:
    """
    Get the date that a file was created.
    Parameters
    ----------
    filepath : str
    Returns
    -------
    creation_datetime : Optional[datetime]
    """
    if platform.system() == "Windows":
        return datetime.fromtimestamp(os.path.getctime(filepath))
    else:
        stat = os.stat(filepath)
        try:
            return datetime.fromtimestamp(stat.st_birthtime)
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return None


def get_modification_datetime(filepath: str) -> datetime:
    """
    Get the datetime that a file was last modified.
    Parameters
    ----------
    filepath : str
    Returns
    -------
    modification_datetime : datetime
    """
    import tzlocal

    timezone = tzlocal.get_localzone()
    mtime = datetime.fromtimestamp(os.path.getmtime(filepath))
    return mtime.replace(tzinfo=timezone)


    def md5(fname):
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()