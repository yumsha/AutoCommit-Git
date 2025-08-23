# Git-AutoCommit

A simple Python script to automatically commit changes to your Git repository at regular intervals. Perfect for keeping your GitHub stats active or for automating backup commits!

## Features

* Automatically commits changes in your repo
* Customizable commit message
* Works with local Git repositories
* Lightweight and easy to set up

## Requirements

* Python 3.8+
* Git installed and configured
* Virtual environment (optional but recommended)

## Installation

1. Clone this repository:

```bash
git clone git@github.com:yumsha/AutoCommit-Git.git
cd AutoCommit-Git
```

2. (Optional) Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Open `app.py` and configure your settings if needed (commit message, interval, etc.).
2. Run the script:

```bash
python app.py
```

3. Your repository will now automatically commit changes based on the configured interval.

## Security

⚠️ Make sure **not to commit your personal secrets**, tokens, or passwords. Use `.env` files and `.gitignore` to keep them safe.

## Contributing

Pull requests are welcome! Feel free to add new features, improve documentation, or report bugs.

## License

This project is open source under the MIT License.

