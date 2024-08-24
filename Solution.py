import config
from collections import defaultdict
from utils import load_lookup_table, load_protocol_mapping_table, save_port_protocol_counts_to_csv, save_tag_counts_to_csv, create_directory
 
def process_flow_logs(flow_log_file, lookup_table, protocol_map):
    '''
    Function to parse the flow logs and count the frequency of port/protocol combination and tags.
    It takes following arguments:
        flow_log_file - path to flow logs, 
        lookup_table  - the lookup table dictionary 
        protocol_map  - protocol mapping table dictionary 
    Returns two dictionaries, one each for tag_counts and port-protocol combination counts
    '''
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)
    untagged = 0

    try:
        with open(flow_log_file, 'r') as file:
            for data in file:

                #skip empty lines
                if not data.strip():
                    continue

                fields = data.split()

                #skip malformed lines
                if len(fields) < 13:
                    continue
                
                dstport = int(fields[6])
                protocol_num = int(fields[7])
                
                #protocol numbers 124-252 are Unassigned
                protocol = protocol_map.get(protocol_num, "Unassigned")
                
                key = (dstport,protocol)
                
                if key in lookup_table:
                    tag_counts[lookup_table[key]] += 1
                else:
                    untagged += 1
                port_protocol_counts[key] += 1
            
            if untagged:
                tag_counts["Untagged"] = untagged
    
    except FileNotFoundError:
        raise Exception(f"Flow Logs File missing : {filename} not found.")

    except Exception as e:
        raise Exception(f"Error while loading flow logs: {str(e)}")
    
    return tag_counts , port_protocol_counts

def main():
    #Load Lookup Table 
    lookup_table = load_lookup_table(config.LOOKUP_TABLE_FILE)
    
    #Load Protocol Mapping Table
    protocol_mapping_table = load_protocol_mapping_table(config.PROTOCOL_MAPPING_TABLE_FILE)
    
    #Process the flow logs and get counts
    tag_counts, port_protocol_counts = process_flow_logs(config.FLOW_LOGS_FILE , lookup_table, protocol_mapping_table)
    
    #Write the output to csv
    create_directory(config.RESULT_DIR)
    save_tag_counts_to_csv(tag_counts, config.TAG_COUNT_OUTPUT_FILE)
    save_port_protocol_counts_to_csv(port_protocol_counts, config.PORT_PROTOCOL_OUTPUT_FILE)

if __name__ == "__main__":
    main()
