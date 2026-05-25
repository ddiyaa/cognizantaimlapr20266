#create streaming inference
from time import sleep
import time
import random
def stream_inf(prompt):
    #stimulate ttft
    ttft=0.248

    response="""
    The Supreme Court, on Monday (May 25, 2026), 
    squarely blamed the National Testing 
    Agency (NTA) for the National Eligibility 
    cum Entrance Test Undergraduate (NEET-UG) 
    2026 paper leak, saying the exam body sadly 
    did not learn its lesson even two 
    years after the last security breach in 2024.
    
    """
    tokens=response.split()
    start_time=time.time()
    for token in tokens:
        print(token,end=" ",flush=True)
        delay=random.uniform(0.05,0.15) #simulate token generation time
        sleep(delay)
    end_time=time.time()
    print(f"\nTotal time: {end_time - start_time:.2f} seconds")

if __name__=="__main__":
    prompt="What is the latest news on NEET-UG 2026 paper leak?"
    stream_inf(prompt)
