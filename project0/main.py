import argparse
import project0
import PyPDF2

def main(url):
    incident_data = project0.fetchincidents(url)
    incidents = project0.extractincidents(incident_data)
    #print(incidents)
    db = project0.createdb()
    project0.populatedb(db,incidents)
    project0.status()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents",type=str,required=True,help="Incident summary url.")
    args = parser.parse_args()
    if args.incidents:
     main(args.incidents)
