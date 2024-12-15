import pandas as pd
import re
import argparse

def parse_fortigate_log(log_file):
    data = []

    log_pattern = re.compile(
    r'date\s*=\s*(?P<date>[\d\-]+)\s+'
    r'time\s*=\s*(?P<time>[\d\:]+)\s+'
    r'eventtime\s*=\s*(?P<eventtime>\d+)\s+'
    r'tz\s*=\s*"?(?P<tz>[\w\+\-]+)"?\s+'
    r'logid\s*=\s*"?(?P<logid>\d+)"?\s+'
    r'type\s*=\s*"?(?P<type>\w+)"?\s+'
    r'subtype\s*=\s*"?(?P<subtype>\w+)"?\s+'
    r'level\s*=\s*"?(?P<level>\w+)"?\s+'
    r'vd\s*=\s*"?(?P<vd>\w+)"?\s+'
    r'srcip\s*=\s*(?P<srcip>[\d\.]+)\s+'
    r'srcport\s*=\s*(?P<srcport>\d+)\s+'
    r'srcintf\s*=\s*"?(?P<srcintf>\w+)"?\s+'
    r'srcintfrole\s*=\s*"?(?P<srcintfrole>\w+)"?\s+'
    r'dstip\s*=\s*(?P<dstip>[\d\.]+)\s+'
    r'dstport\s*=\s*(?P<dstport>\d+)\s+'
    r'dstintf\s*=\s*"?(?P<dstintf>\w+)"?\s+'
    r'dstintfrole\s*=\s*"?(?P<dstintfrole>\w+)"?\s+'
    r'srccountry\s*=\s*"?(?P<srccountry>\w+)"?\s+'
    r'dstcountry\s*=\s*"?(?P<dstcountry>\w+)"?\s+'
    r'sessionid\s*=\s*(?P<sessionid>\d+)\s+'
    r'proto\s*=\s*(?P<proto>\d+)\s+'
    r'action\s*=\s*"?(?P<action>\w+)"?\s+'
    r'policyid\s*=\s*(?P<policyid>\d+)\s+'
    r'service\s*=\s*"?(?P<service>\w+)"?\s+'
    r'trandisp\s*=\s*"?(?P<trandisp>\w+)"?\s+'
    r'app\s*=\s*"?(?P<app>\w+)"?\s+'
    r'duration\s*=\s*(?P<duration>\d+)\s+'
    r'sentbyte\s*=\s*(?P<sentbyte>\d+)\s+'
    r'rcvdbyte\s*=\s*(?P<rcvdbyte>\d+)\s+'
    r'sentpkt\s*=\s*(?P<sentpkt>\d+)\s+'
    r'rcvdpkt\s*=\s*(?P<rcvdpkt>\d+)\s+'
    r'appcat\s*=\s*"?(?P<appcat>\w+)"?\s+'
    r'dsthwvendor\s*=\s*"?(?P<dsthwvendor>\w+)"?\s+'
    r'dstdevtype\s*=\s*"?(?P<dstdevtype>\w+)"?\s+'
    r'dstosname\s*=\s*"?(?P<dstosname>\w+)"?\s+'
    r'masterdstmac\s*=\s*"?(?P<masterdstmac>[0-9a-fA-F:]+)"?\s+'
    r'dstmac\s*=\s*"?(?P<dstmac>[0-9a-fA-F:]+)"?\s+'
    r'dstserver\s*=\s*(?P<dstserver>\w+)'
    )
    with open(log_file, 'r') as file:
        for line in file:
            match = log_pattern.search(line)
            if match:
                entry = {key: match.group(key) for key in match.groupdict()}
                data.append(entry)
            else:
                print("No match for line:", line.strip()) 

    return data

def save_to_excel(data, output_file):
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)

def main():
    parser = argparse.ArgumentParser(description="Parse FortiGate logs and export to Excel.")
    parser.add_argument('-i', '--input', required=True, help='Path to the input log file')
    parser.add_argument('-o', '--output', default='fortigate_output.xlsx', help='Output Excel file name')

    args = parser.parse_args()

    log_data = parse_fortigate_log(args.input)
    if log_data:
        save_to_excel(log_data, args.output)
        print(f"Data has been exported to {args.output}")
    else:
        print("No data extracted.")

if __name__ == "__main__":
    main()
