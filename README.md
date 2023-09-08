# Fishing Resort Terminal Management System

A proprietary terminal management software for "Fishing Resort".
<p float="left">
  <img src="https://github.com/Miautawn/vu-system-quality-project/assets/24988290/d19b78e1-61a3-4274-a9e2-46160a3271eb" width="280" />
  <img src="https://github.com/Miautawn/vu-system-quality-project/assets/24988290/702bcfec-7c13-4c68-9f3a-ed6feeeb44c9" width="500" /> 
</p>

## 
* [Intro 📑](#intro)
* [Dependancies 📌](#dependencies)
* [Setup ⚙️](#setup)

## Intro
This **T**erminal **U**ser **I**nterface (TUI) provides a number of functions used to manage the establishment:
* View information about the guests
* View information about the rooms
* List available & occupied rooms
* Calculate the revenue for the current occupancy

For more info about the tool, please check the [documentation 📖](https://fishing-resort.atlassian.net/wiki/home)

## Dependencies
This tool is built with Python 🐍 and uses the [InquirerPy](https://inquirerpy.readthedocs.io/en/latest/) for user interface + [MongoDB](https://www.mongodb.com/) for local storage.  
Below you can find the data model currently used:
<p align="center">
  <img src="https://user-images.githubusercontent.com/24988290/197361836-3d10a1be-0fcb-4c90-a73a-32b837730849.png">
</p>

## Setup
> Make sure you use Python ^3.8!

1. Clone the repo `git clone https://github.com/Miautawn/vu-system-quality-project.git`
2. Install dependencies via Poetry `poetry install`
3. Setup local MongoDB instance on your machine -> [documentation](https://www.mongodb.com/docs/manual/installation/)
4. Run the program `poetry run python src/main.py`
