from multiprocessing import Pool
from time import time
import requests
import argparse

def job(a):
    # Maybe our job does some network io. If the bottleneck is not in fact your CPU.
    r=requests.get("https://www.google.com/") 
    return r.status_code

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--processes', '-p', type=int, required=True,  help='number of concurrent processes')
    
    args = parser.parse_args()
    p = Pool(args.processes)

    start_time = time()
    # do the job with all the numbers from 1 to 100
    print(p.map(job, list(range(100))))

    end_time = time()
    print("That took %s seconds" % (end_time - start_time))

