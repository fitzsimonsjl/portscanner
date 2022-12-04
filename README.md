# A basic port scanner with python

To learn more about networking with Python, it seemd like a good first project would be to write a simple port scanner that would check ports between 1-500, and say whether they were open or closed. This would be saved to a .csv file so that it could be analysed more later on.

In the future I would like to expand on it more by:

- Adding a proper terminal UI
- Accept host input from the terminal (could use argparse, as an example)
- Handle more cases so rather than just "open" or "closed", filtered or unfiltered could be determined
- To speed up scanning, threading would need to be implemented
- Add a comparison list of ports and determine which services are on which ports