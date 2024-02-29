# Locust Performance Testing Project

This project is aimed at conducting performance testing for the JioSaavn iOS app using Locust, an open-source load testing tool written in Python. The purpose of this load testing project is to simulate real user behavior and evaluate the app's performance under various conditions.

## Prerequisites

Before running the performance tests, make sure you have the following software installed:

- Python 3.x
- Locust (install via `pip install locust`)
- Allure (optional, for generating a beautiful HTML report)

## Project Structure

The project has the following structure:

```
|-- locustfile.py
|-- results
|-- data
|-- output.html
|-- README.md
```

- `locustfile.py`: This file contains the performance test scenarios written in Python using Locust's API.
- `data`: This directory contains any test data or input files required for the test.
- `results`: This directory is used to store test results, such as logs and screenshots (if enabled).
- `reports`: This directory is used to store generated test reports (e.g., Allure report).
- `README.md`: This readme file with project information and instructions.

## Running the Performance Tests

To run the performance tests, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Execute the following command:

```
 locust -f locustfile.py -u 10 -r 10 --run-time 200s --host=https://staging.jiosaavn.com --csv=results --html=output.html            

```

4. Open a web browser and go to `http://localhost:8089` to access the Locust web interface.
5. Specify the number of total users and spawn rate in the Locust web interface and start the test.

## Generating the Test Report (Optional)

To generate a beautiful test report using Allure, follow these steps:

1. Install Allure command-line tool from [Allure official website](https://docs.qameta.io/allure/).
2. Open a terminal or command prompt.
3. Navigate to the project directory.
4. Execute the following command:

```
allure serve reports
```

This will generate and open the Allure HTML report in your default web browser.

## Additional Information

- The `locustfile.py` contains example test scenarios for different user actions like login, creating playlists, accessing podcast home, etc. Modify these scenarios to suit your specific testing requirements.
- You can add more test data or input files in the `data` directory if needed for data-driven testing.
- Customize the `User` class in `locustfile.py` to simulate more realistic user behavior and interactions.

## Contributing

Feel free to contribute to this performance testing project by creating pull requests or reporting issues.

Happy load testing!