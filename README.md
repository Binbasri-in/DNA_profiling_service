[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/H2H5VAL6E)

# DNA Profiling Service

The DNA Profiling Service is a web application designed to streamline the process of storing and accessing DNA data for laboratories. Utilizing Short Tandem Repeats (STRs) for DNA profiling, this service optimizes data search and matching operations, significantly improving efficiency over traditional methods.

## How It Works
This service uses Flask, a lightweight WSGI web application framework, to manage the web interface and backend processes. By implementing STR-based data indexing, it ensures rapid query responses, facilitating quicker comparisons and matches of DNA profiles.

## Features
- User-friendly web interface for data entry and retrieval
- Efficient storage mechanism for DNA data using STRs
- Advanced search capabilities to quickly find and match DNA profiles
- Secure access control to ensure data privacy and integrity

## Setup Instructions
To set up the DNA Profiling Service on your system, follow these steps:

### Prerequisites
- Python 3.6 or later
- Flask
- An SQL database (e.g., SQLite, MySQL)

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/Binbasri-in/DNA_profiling_service.git
   ```
2. Navigate to the project directory:
   ```
   cd DNA_profiling_service
   ```
3. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```
4. Initialize the database:
   ```
   python init_db.py
   ```
5. Start the Flask application:
   ```
   flask run
   ```

## Usage
After starting the application, navigate to `http://localhost:5000` in your web browser to access the DNA Profiling Service. From there, you can:

- Add new DNA profiles
- Search for existing profiles using STR data
- Compare profiles for matches

## Contributing
Contributions to the DNA Profiling Service are welcome. If you would like to contribute, please fork the repository and submit a pull request with your proposed changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
