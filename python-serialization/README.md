# Python Serialization Project

This project demonstrates various serialization techniques in Python, including JSON, Pickle, CSV to JSON conversion, and XML serialization.

## Files in this Project

1. `task_00_basic_serialization.py`: Basic JSON serialization module
2. `task_01_pickle.py`: Custom class serialization using Pickle
3. `task_02_csv.py`: CSV to JSON conversion
4. `task_03_xml.py`: XML serialization and deserialization

## Usage

### 1. Basic JSON Serialization

This module provides functions to serialize a Python dictionary to a JSON file and deserialize it back.

```python
from task_00_basic_serialization import serialize_and_save_to_file, load_and_deserialize

# Serialize data
data = {"name": "John", "age": 30}
serialize_and_save_to_file(data, "data.json")

# Deserialize data
loaded_data = load_and_deserialize("data.json")
```

### 2. Custom Class Serialization (Pickle)

This module demonstrates how to serialize and deserialize custom Python objects using the `pickle` module.

```python
from task_01_pickle import CustomObject

# Create and serialize an object
obj = CustomObject(name="John", age=25, is_student=True)
obj.serialize("object.pkl")

# Deserialize the object
new_obj = CustomObject.deserialize("object.pkl")
new_obj.display()
```

### 3. CSV to JSON Conversion

This script converts CSV data to JSON format.

```python
from task_02_csv import convert_csv_to_json

csv_file = "data.csv"
convert_csv_to_json(csv_file)
# Result is saved in "data.json"
```

### 4. XML Serialization

This module provides functions to serialize Python dictionaries to XML and deserialize XML back to dictionaries.

```python
from task_03_xml import serialize_to_xml, deserialize_from_xml

# Serialize dictionary to XML
data = {"name": "John", "age": "28", "city": "New York"}
serialize_to_xml(data, "data.xml")

# Deserialize XML to dictionary
deserialized_data = deserialize_from_xml("data.xml")
```

## Requirements

- Python 3.10+
- No external libraries required (all modules used are part of the Python standard library)

## Running the Scripts

Ensure that all files are in the same directory. Make the Python files executable:

```bash
chmod +x task_00_basic_serialization.py task_01_pickle.py task_02_csv.py task_03_xml.py
```

Then, you can run each script directly or import the functions into your own Python scripts as shown in the usage examples above.

## Note

This project is for educational purposes to demonstrate various serialization techniques in Python. In a production environment, consider factors such as data validation, error handling, and security when working with serialized data.