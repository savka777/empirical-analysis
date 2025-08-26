from analyze_time import analyze_time, plot_results, pretty_time


if __name__ == "__main__":

    @analyze_time()
    def bubble_sort(arr : list): # Import! Type hints must be used, so reccomend python >3.5
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
    
    results = bubble_sort.analyze_complexity()

    for size, time in results:
        print("Input size: ", size, "Time Taken: ", pretty_time(time) , "MS")

    plot_results(results)   