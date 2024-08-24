# Flow-Logs-Parser
This project is to parse the file containing flow log data and store the tag counts based on a lookup table. It also generates counts for each port/protocol combination.

## Assumptions:
- The program only supports the default AWS flow log format and version 2.
- The flow logs are in a text file.
- The lookup table must be a comma-seperated values file saved as text file.
- The first line of the lookup table file is assumed to be a header and is skipped
- The log entries must be in the default log format as specified in the AWS VPC Fow Logs Documentation.
- The mapping of protocol numbers to their corresponding protocol names is present in protocol_mapping_table.csv and the data was sourced from wikipidea

## File Structure:
```
project-root/
│
├── Solution.py                 # Main script to run the program
├── utils.py                    # Utility functions, including load_lookup_table and 
├── config.py                   # Configuration file, containing file paths
├── results/                    # Directory where output files are saved
  ├── tag_counts.csv              # File containing counts of matches for each tag
  └── port_protocol_counts.csv    # File containing counts of matches for each port/protocol combination 
├── lookup_table.txt            # Sample lookup table (provide your own)
├── flow_logs.txt               # Sample flow log file (provide your own)
├── protocol_mapping_table.csv  # File containing mapping of protocol numbers to their corresponding protocol names.
└── README.md                   # This readme file
```

## Installation
The program requires no additional packages or libraries and is designed to run on a standard Python installation.  

## Usage
1. Prepare the Lookup Table and FLow Log Files:
    Ensure that the lookup file is a txt file with comma-seperated values with the following format:
   ```
    dstport,protocol,tag
    25,tcp,sv_P1
    443,tcp,sv_P2
    110,tcp,email
   ```
   Prepare the flow log file in the default AWS flow log format version 2.
3. Define File Paths:
    Specify paths to lookup table and flow log file in the config.py file
4. Run the program
    Execute the main script to process the flow log file. The output files will be saved into `results` directory.
    ```python Solution.py```

