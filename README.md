# Cardiopy

A flexibile package for R-peak detection and heart rate variability analysis of single-lead EKG data. <br>

## How to use Cardiopy
Cardiopy can be used in two ways:<br>
   1. __As a preprocessing module for the import and cleaning of clinical EKG data in conjuction
		with HRV analyses by standard software packages.__ For this use, run through feature sets 1 and 2 (listed below). The exported '*_nn.txt*' file is compatible with all major HRV software packages <br>
   2. __As a stand-alone HRV analysis toolkit.__ For this use, continue through the workflow from feature set 1 through 4 (listed below). To ensure analytic reproducibilty, we highly recommend exporting cleaned nn detections at feature set 2.

## Features
__1. Data preprocessing and cleaning__<br>
   * Load single-lead EKG data<br>
   * Detect R-peaks with flexible thresholding parameters for adjustment to noisy data and varying amplitudes<br>
		- Option to filter especially noisy data prior to peak detection<br>
   * Built-in detection visualization methods<br>
   * Simple artifact removal methods for manual inspection of detected peaks<br>
  
__2. Export methods for cleaned peak detections__<br>
   * Compatible with commonly used software such as Kubios HRV and Artiifact<br>
   
__3. HRV analysis methods__<br>
   * Standard time-domain statistics<br>
   * Standard frequency domain statistics<br>
		- Option for Multitaper or Welch power spectral estimates<br>
    
__4. HRV statistics export__<br>
   * Single-file report exports in json format<br>
   * Multi-file exports into .csv spreadsheets for group statistics<br>

## Usage
Best when run with jupyter notebook. For detailed instructions see example in CardioPy/example_run/CardioPy_Example_2020.ipynb <br>
	*For optimal performance, close figure interactions ('off' button on the top right corner) when finished with each window.*

### Parameter Optimization & Cleaning Tips
* Remove false interbeat intervals LAST, after all cleaning (addition/removal of peaks) has been done.
* To maintain integrity of the artifact logs:
	- Only remove incorrectly added peaks with EKG.undo_add_peak NOT with EKG.rm_peak.
	- Only re-add incorrectly removed peaks with EKG.undo_rm_peak NOT with EKG.add_peak.

* If R peaks are not very pronounced, try: 
	1. reducing the moving window
	2. reducing the upshift percentage

        <b>For example:</b> <br>
    <p align=center>
	<b>50ms moving window + 1.7% upshift (Suboptimal)</b>
        <img src="https://github.com/CardioPy/CardioPy/blob/master/example_run/advice_images/example_bad_mw.PNG">
        <br><br>
        <b>20ms moving window + 1.7% upshift (Optimal)</b>
        <img src="https://github.com/CardioPy/CardioPy/blob/master/example_run/advice_images/example_good_mw.PNG">
    </p>

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install CardioPy.

```bash
pip install CardioPy
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
BSD 3-Clause

## Roadmap
The authors plan for the next version of CardioPy to include automatic parameter detection. This would include upshift, moving window and smoothing window suggestions for optimal peak detection. <br>
Future versions also aim to implement a graphical user interface, as well as support for additional commonly used data formats.
