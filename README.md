# Complexity Analyzer
                                                                                                                                                 
Turn algorithmic complexity from theory into empirical data with a simple decorator.

```python
@analyze_time()
def bubble_sort(arr):
    # Your sorting algorithm here
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

results = bubble_sort.analyze_complexity()
plot_results(results)  # Visualize the O(n²) curve
# [(100, 0.000343), (500, 0.006530), (1000, 0.028113)] → Quadratic growth confirmed
```

## What This Is

The 'drop a decorator' on your function and get:
- Empirical time complexity measurement across input sizes
- Noise reduction through multiple runs and minimum time selection
- Matplotlib visualization of scaling behavior  
- Evidence-based performance analysis for your algorithms

## Work in Progress

This project is in **early development**. The core measurement system works and can analyze algorithm scaling behavior, but we're building toward something much more powerful:

**Current State:**
- ✅ Solid measurement engine with noise reduction
- ✅ Manual input generator specification  
- ✅ Visualization with matplotlib
- ✅ Clean decorator API that works today

**Vision:**
- 🚧 **Smart input detection** (type hints, parameter names, patterns)
- 🚧 **Extensible generator registry** for any data structure  
- 🚧 **Automatic Big O classification** with curve fitting
- 🚧 **Community-driven ecosystem** of specialized generators

## Contributing

We're building this as a community driven tool. The foundation is solid, but there's tons of room to grow:

**Ways to help:**
- **Try it with your algorithms** - test the current decorator and share results
- **Suggest improvements** to the measurement methodology
- **Brainstorm input generators** for different data types (graphs, matrices, strings)
- **Share domain expertise** - what algorithms in your field need analysis tools?
- **Discuss the vision** - help shape where this tool should go

Start by opening an Issue with your thoughts, algorithms you'd like to test, or ideas for the roadmap.

## Current Status

- ✅ **Core measurement engine** - reliable timing with noise reduction
- ✅ **Manual input specification** - works with any data generator function  
- ✅ **Visualization tools** - matplotlib integration for curve analysis
- ✅ **Clean API** - simple decorator pattern that's ready to use
- 🚧 **Automatic input detection** - registry system for universal usage
- 🚧 **Big O classification** - curve fitting and complexity estimation  
- 🚧 **Enhanced developer tools** - CLI, CI/CD integration, better output

**Built for**: Engineers optimizing production code • Researchers developing algorithms • Students learning complexity • Teams making data driven decisions
---

⭐ **Star this repo** if you're tired of manual benchmarking and want empirical algorithmic analysis to be as easy as adding a decorator.
