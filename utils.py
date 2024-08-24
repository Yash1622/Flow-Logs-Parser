import csv
import os
from collections import defaultdict
import config

def load_lookup_table(filename):
    ''' 
    Function to Load the lookup table from the desired input file and return it as a dictionary
    The text file should be have data in the format dstport,protocol,tag
    The first line is skipped as it has headers.
    If there is data on line 0 then please comment line 18 in this code file
    '''
    lookup_table = {}
    try:
        with open(filename, mode='r') as lookup_file:
           
            file_reader = csv.reader(lookup_file)

            # skipping the first line as it has headers dstport,protocol,tag
            next(file_reader)

            for data in file_reader:

                #skip empty lines
                if not data:
                    continue

                dstport = data[0]
                protocol = data[1].strip()
                tag = data[2].strip()
                key = (int(dstport) , protocol.lower())

                lookup_table[key] = tag

    except FileNotFoundError:
        raise Exception(f"Lookup Table File missing : {filename} not found.")

    except Exception as e:
        raise Exception(f"Error while loading lookup table: {str(e)}")

    return lookup_table

def load_protocol_mapping_table(filename):
    '''
    Function to load the Protocol Mapping Table.
    The input file is a csv file of the format "protocol_number,keyword"
    It will return a dictionary mapping the protocol numbers to their corresponding protocols names. 
    '''
    protocol_mapping_table = {}
    try:
        with open(filename, mode='r') as csvfile:
    
            lookup_file = csv.DictReader(csvfile)
    
            for data in lookup_file:
                protocol_number = int(data['protocol_number'])
                protocol = data['keyword']
                protocol_mapping_table[protocol_number] = protocol

    except FileNotFoundError:
        raise Exception(f"Protocol Mapping Table File missing : {filename} not found.")

    except Exception as e:
        raise Exception(f"Error while loading Protocol Mapping table: {str(e)}")

    return protocol_mapping_table

def create_directory(dir_path):
    ''' 
    Function to create directory for a given path
    '''
    try:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
    
    except Exception as e:
        raise Exception(f"Error while creating directory {dir_path} : {str(e)}")

def save_tag_counts_to_csv(tag_counts, output_dir):
    '''
    Function to write the tag counts to a CSV file. The file is created if it does not exists.
    '''
    
    try:
        with open(output_dir, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Tag', 'Count'])
            for tag, count in tag_counts.items():
                writer.writerow([tag,count])
    
    except Exception as e:
        raise Exception(f"Error writing Tag Counts : {str(e)}")

def save_port_protocol_counts_to_csv(port_protocol_counts, output_dir):
    '''
    Function to write the port/protocol counts to a CSV file. The file is created if it does not exists.
    '''
    try:
        with open(output_dir, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Port', 'Protocol', 'Count'])
            for (port, protocol), count in port_protocol_counts.items():
                writer.writerow([port, protocol, count])

    except Exception as e:
        raise Exception(f"Error writing Port/Protocol combination Counts : {str(e)}")
