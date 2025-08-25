# An empirical way to analyze time complexity
import time
import functools
import random
import matplotlib.pyplot as plt

def analyze_time(input_generator, sizes, runs=5):
    """
    Decorator for empirical time complexity analysis.
    
    Args:
        input_generator: Function that generates test input of given size
        sizes: List of input sizes to test
        runs: Number of runs per size (default 5)
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # If called normally, just run the function
            if args or kwargs:
                return func(*args, **kwargs)

            results = []  # the time it takes to run on different input sizes

            # iterate through the different input sizes and call our func
            for size in sizes:
                times = []
                # iterate each size multiple times, why? reduce noise and system interference, 
                # usually taken into account the minimum time it takes for the function to run 
                # on a given input size, this implies lower system interference, i.e CPU is in optimal state.
                # iterating once per time can cause inaccurate data as the state of the system 
                # may interfere with the analysis and give different results each time.

                # simple solution: run the analysis 5 iterations for each time. Take the minimum time 
                # it takes for the function to execute.
                for _ in range(runs):
                    test_input = input_generator(size)  # generate test data for input size
                    start_time = time.perf_counter() 
                    func(test_input)  # call function on input size
                    end_time = time.perf_counter()
                    times.append(end_time - start_time)
            
                results.append((size, min(times)))
            return results
        
        # add custom attribute to wrapper function, so that we can call it when we want 
        # to go into analysis mode - this gives the freedom of turning on and off analysis mode
        wrapper.analyze_complexity = lambda: wrapper()

        return wrapper
    
    return decorator

def pretty_time(time):
    return round(1_000 * time, 2)

def generate_list(size):
    """Generate a random list of given size for testing"""
    return [random.randint(1, 1000) for _ in range(size)]

def plot_results(results):
    """Plot the complexity analysis results"""        
    sizes = [r[0] for r in results]
    times = [r[1] for r in results]
    
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, 'bo-')
    plt.xlabel('Input Size')
    plt.ylabel('Time (seconds)')
    plt.title('Time Complexity Analysis')
    plt.grid(True)
    plt.show()