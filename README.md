# Flow-Logs-Parser
This project is to parse the file containing flow log data and store the tag counts based on a lookup table. It also generates counts for each port/protocol combination.

## Assumptions:
- The flow log file must be a text file in the default AWS flow log format, version 2, as specified in the AWS VPC Fow Logs Documentation. 
- The lookup table must be a txt file having comma seperated values with a header with the following columns:
  - dstport - an integer representing destination port 
  - protocol - a string representing the protocol 
  - tag - a string representing the tag uniquely identified by dstport and protocol together 
- The first line of the lookup table file is assumed to be a header and is skipped
- The mapping of protocol numbers to their corresponding protocol names is present in protocol_mapping_table.csv (the data is sourced from [Wikipedia](https://en.wikipedia.org/wiki/List_of_IP_protocol_numbers))

## File Structure:
```
project-root/
│
├── Solution.py                 # Main script to run the program
├── utils.py                    # Utility functions, including load_lookup_table and other utility functions
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
- Prepare the Lookup Table and FLow Log Files:
  - Ensure that the lookup file is a txt file with comma-seperated values with the following format:
   ```
    dstport,protocol,tag
    25,tcp,sv_P1
    443,tcp,sv_P2
    110,tcp,email
   ```
  - Prepare the flow log file in the default AWS flow log format version 2.
- Define File Paths:
  - Specify paths to lookup table and flow log file in the config.py file
- Run the program
  - Execute the main script to process the flow log file. The output files will be saved into `results` directory.
    ```
    python Solution.py
    ```
## Test Scenarios
- Lookup Table was empty
- Flow logs were empty
- Both Lookup Table and Flow Logs were empty
- All tags are unique
- Some tags are not unique, i.e. they have multiple port and protocol pairs with the same tag

